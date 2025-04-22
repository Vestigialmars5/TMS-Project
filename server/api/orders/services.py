import logging
from server.extensions import db
from server.models.tms_models import Order, OrderDetails
from server.utils.exceptions import DatabaseQueryError
from server.utils.logging import create_audit_log
from server.utils.validations import order_exists, validate_order_products, user_exists
from sqlalchemy.exc import IntegrityError, SQLAlchemyError


logger = logging.getLogger(__name__)


def create_order(reference_id, customer_id, delivery_address, order_products, initiator_id):
    # TODO: Validation
    logger.info("Create Order Attempt: by %s", initiator_id)
    try:
        if order_exists(reference_id):
            logger.error("Create Order Attempt Failed: by %s | Order Already Exists", initiator_id)
            create_audit_log("Create Order", user_id=initiator_id, details="Order Already Exists")
            return {"success": False, "error": "Unique Constraint Violation", "description": "Order Already Exists"}
    

        # Validate the products exists (TODO: Probably add a call to the inventory here)
        is_valid, total = validate_order_products(order_products)
        if not is_valid:
            if total == "Product Does Not Exist":
                logger.error("Create Order Attempt Failed: by %s | %s", initiator_id, total)
                create_audit_log("Create Order", user_id=initiator_id, details=total)
                return {"success": False, "error": "Not Found", "description": total}
            else:
                logger.error("Create Order Attempt Failed: by %s | %s", initiator_id, total)
                create_audit_log("Create Order", user_id=initiator_id, details=total)
                return {"success": False, "error": "Invalid Data", "description":total}

        if not user_exists(customer_id):
            logger.error("Create Order Attempt Failed: by %s | Customer Does Not Exist", initiator_id)
            create_audit_log("Create Order", user_id=initiator_id, details="Customer Does Not Exist")
            return {"success": False, "error": "Not Found", "description": "Customer Does Not Exist"}
        
        # TODO: Add Address Checking

        try:
            order = insert_order(reference_id, customer_id, delivery_address, total)
            insert_order_details(order.order_id, order_products)
        except DatabaseQueryError as e:
            raise
        except IntegrityError as e:
            raise DatabaseQueryError("Something Already Exists")
        except Exception as e:
            raise DatabaseQueryError("Error Creating Order")
        
        logger.info("Create Order Attempt Successful: by %s | Created %s", initiator_id, order.order_id)
        create_audit_log("Create Order", user_id=initiator_id, details=f"Created {order.order_id}")
        return {"success": True}


    except DatabaseQueryError as e:
        logger.error("Create Order Attempt Failed: by %s | %s", initiator_id, e)
        create_audit_log("Create Order", user_id=initiator_id, details=e.message)
        raise

    except Exception as e:
        logger.error("Create Order Attempt Failed: by %s | %s", initiator_id, e)
        create_audit_log("Create Order", user_id=initiator_id, details=e.message)
        raise


def get_orders(search, sort_by, sort_order, page, limit, initiator_id):

    logger.info("Get Orders Attempt: by %s", initiator_id)

    try:
        try:
            orders = construct_query_orders(
                search, sort_by, sort_order, page, limit)

            logger.info("Get Orders Attempt Successful: by %s", initiator_id)
            create_audit_log("Get Orders", initiator_id, details="Success")
            return {"success": True, "orders": orders}

        except Exception as e:
            raise DatabaseQueryError(f"Error Fetching Orders {e}")

    except DatabaseQueryError as e:
        logger.error("Get Orders Attempt Failed: by %s | %s", initiator_id, e)
        create_audit_log("Get Orders", user_id=initiator_id, details=e.message)
        raise

    except Exception as e:
        logger.error("Get Orders Attempt Failed: by %s | %s", initiator_id, e)
        create_audit_log("Get Orders", user_id=initiator_id, details="Internal Server Error")
        raise


def get_order_details(order_id, initiator_id):

    logger.info("Get Order Details Attempt: by %s", initiator_id)

    try:
        try:
            details = db.session.query(OrderDetails).filter(OrderDetails.order_id == order_id).all()

            if len(details) <= 0:
                logger.error("Get Order Details Attempt Failed: by %s | No Order Details Found", initiator_id)
                create_audit_log("Get Order Details", user_id=initiator_id, details="No Order Details Found")
                return {"success": False, "error": "Not Found", "description": "No Order Details Found"}
            
            details_list = [detail.to_dict_js() for detail in details]

            logger.info("Get Order Details Attempt Successful: by %s", initiator_id)
            create_audit_log("Get Order Details", initiator_id, details="Success")
            return {"success": True, "details": details_list}

        except Exception as e:
            raise DatabaseQueryError(f"Error Fetching Order Details {e}")

    except DatabaseQueryError as e:
        logger.error("Get Order Details Attempt Failed: by %s | %s", initiator_id, e)
        create_audit_log("Get Order Details", user_id=initiator_id, details=e)
        raise

    except Exception as e:
        logger.error("Get Order Details Attempt Failed: by %s | %s", initiator_id, e)
        create_audit_log("Get Order Details", user_id=initiator_id, details="Internal Server Error")
        raise



def insert_order(reference_id, customer_id, delivery_address):
    order = Order(order_uuid=reference_id, customer_id=customer_id, status="Pending", delivery_address=delivery_address)
    db.session.add(order)
    db.session.commit()
    return order



def insert_order_details(order_id, products):
    try:
        order_details = [
            OrderDetails(
                order_id=order_id,
                product_id=product["product_id"],
                product_name=product["product_name"],
                quantity=product["quantity"],
                price=product["total_price"]
                ) 
                for product in products]
        
        db.session.bulk_save_objects(order_details)
        db.session.commit()

    
    except SQLAlchemyError as e:
        db.session.rollback()
        raise DatabaseQueryError("Error During Bulk Inserting")
    

def construct_query_orders(search, sort_by, sort_order, page, limit):
    """
    Construct the query for getting orders.

    @param search (str): The search query.
    @param sort (str): The sort order.
    @param page (int): The page number.
    @param limit (int): The number of items per page.
    @return (str, list): The query and params.
    """

    query = db.session.query(Order)

    if search:
        search_filter = f"%{search}%"
        query = query.filter(
            Order.status.like(search_filter)
        )

    if sort_by and sort_order:
        if sort_order == "asc":
            query.order_by(db.asc(sort_by))
        else:
            query.order_by(db.desc(sort_by))

    offset = (page - 1) * limit
    query = query.offset(offset).limit(limit)

    orders = query.all()

    order_list = [order.to_dict_js() for order in orders]

    return order_list
