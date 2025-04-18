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
        is_valid, error = validate_order_products(order_products)
        if not is_valid:
            if error == "Product Does Not Exist":
                logger.error("Create Order Attempt Failed: by %s | %s", initiator_id, error)
                create_audit_log("Create Order", user_id=initiator_id, details=error)
                return {"success": False, "error": "Not Found", "description": error}
            else:
                logger.error("Create Order Attempt Failed: by %s | %s", initiator_id, error)
                create_audit_log("Create Order", user_id=initiator_id, details=error)
                return {"success": False, "error": "Invalid Data", "description":error}

        if not user_exists(customer_id):
            logger.error("Create Order Attempt Failed: by %s | Customer Does Not Exist", initiator_id)
            create_audit_log("Create Order", user_id=initiator_id, details="Customer Does Not Exist")
            return {"success": False, "error": "Not Found", "description": "Customer Does Not Exist"}
        
        # TODO: Add Address Checking

        try:
            order = insert_order(reference_id, customer_id, delivery_address)
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