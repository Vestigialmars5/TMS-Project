from flask import Blueprint, jsonify, request
from server.services import route_service


tm_blueprint = Blueprint(
    "transportation_manager", __name__, url_prefix="/api/transportation_manager"
)

""" 
Manages transportation operations, including planning and scheduling routes, selecting carriers, 
tracking shipments, and optimizing transportation costs. 

- **Dashboard**:
  Overview of transportation operations, key metrics, and notifications.
- **Route Planning**:
  Plan and schedule transportation routes.
- **Carrier Management**:
  Select carriers, manage contracts, and evaluate performance.
- **Shipment Tracking**:
  Track all shipments in real-time.
- **Cost Optimization**:
  Analyze and optimize transportation costs.
- **Reports**:
  Generate reports on transportation performance and costs.
- **Dashboard Analytics**:
  Real-time analytics, KPI updates, trend analysis, and actionable recommendations.
"""


# Route Planning
"""
This needs to include the following features:
- Create new routes
- Edit existing routes
- Delete routes
- View route details

Each route should have the following attributes:
- Route ID
- Origin
- Destination
- Distance
- Estimated Time of Arrival (ETA)
- Assigned Carrier
- Status (Pending, In Progress, Completed)
- Cost
"""


# Create new route from origin to destination
@tm_blueprint.route("/routes", methods=["POST"])
def create_route():
    data = request.get_json()

    origin = data.get("origin")
    destination = data.get("destination")

    response, status = route_service.create_route(origin, destination)


# Get all previously created routes
@tm_blueprint.route("/routes", methods=["GET"])
def get_routes():
    data = request.get_json()

    response, status = route_service.get_routes()


# Update/optimize existing route based on current conditions
@tm_blueprint.route("/routes/<int:route_id>", methods=["PUT"])
def update_route(route_id):
    data = request.get_json()

    response, status = route_service.update_route(route_id, data)


# Delete specific route
@tm_blueprint.route("/routes/<int:route_id>", methods=["DELETE"])
def delete_route(route_id):
    response, status = route_service.delete_route(route_id)


# Get specific route details
@tm_blueprint.route("/routes/<int:route_id>", methods=["GET"])
def get_route(route_id):
    response, status = route_service.get_route(route_id)


# Carrier Management
"""
This needs to include the following features:
- Add new carriers
- Edit carrier details
- Delete carriers
- View carrier details

Each carrier should have the following attributes:
- Carrier ID
- Carrier Name
- Contact Information
- Contract Details
- Performance Metrics
- Rating
- Cost
- Status (Active, Inactive)
"""


# Shipment Tracking (Managed by simulation, triggered events will be sent to the TMS)
"""
This needs to include the following features:
- Track shipments in real-time (receive current step from helper)
- View shipment details
- Receive notifications on shipment status
- View shipment history
- Generate shipment reports

Each shipment should have the following attributes:
- Shipment ID
- Origin
- Destination
- Carrier
- Status (Pending, In Transit, Delivered)
- ETA
- Cost
- History
- Events
- Notifications
"""


# Cost Optimization
"""
This needs to include the following features:
- Analyze transportation costs
- Optimize transportation costs
- Compare costs with previous periods
- Generate cost reports

The cost optimization module should provide the following functionalities:
- Cost Analysis: Analyze transportation costs by route, carrier, and shipment.
- Cost Optimization: Optimize costs by selecting the most cost-effective routes and carriers.
- Cost Comparison: Compare costs with previous periods and identify cost-saving opportunities.
- Cost Reports: Generate reports on transportation costs, cost trends, and cost-saving measures.
"""


# Reports
"""
This needs to include the following features:
- Generate reports on transportation performance
- Generate reports on transportation costs
- View historical data
- Export reports in different formats

The reports module should provide the following functionalities:
- Performance Reports: Generate reports on transportation performance, including on-time delivery, carrier performance, and route efficiency.
- Cost Reports: Generate reports on transportation costs, including cost breakdown by route, carrier, and shipment.
- Historical Data: View historical data on transportation performance and costs.
- Export Reports: Export reports in different formats, such as PDF, Excel, and CSV.

"""


# Dashboard Analytics
