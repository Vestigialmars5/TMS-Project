# Transportation Management System (TMS) Mock Project

#### Description: A TMS is a logistics system that manages things like shipments.

## Detailed Description

It helps with things like optimizing physical goods movement, plan, execute, both outgoing and incoming, documentation, etc.

#### Project idea

The idea I have is to create a TMS either of a simulated environment or see if I can tap in to a real shipment API or something.

I am now thinking of getting google map's api to get the world map, then simulate locations with some other program.

## Main Goal

My main goal is to create a large-scale project that will help me boost my real-life experience.

## Key Features

#### Shipment Planning:

- Allow users to plan and organize shipments efficiently.
- Schedule pickups and deliveries.

#### Route Optimization:

- Optimize routes to minimize transportation costs and time.
- Consider factors such as traffic, fuel efficiency, and delivery windows.

#### Real-Time Tracking:

- Provide real-time tracking of shipments in transit.
- Offer visibility into the current location and status of each shipment.

#### Inventory Management:

- Manage and track inventory levels throughout the transportation process.
- Integrate with warehouse management systems.

#### Document Management:

- Handle and store essential shipping documents electronically.
- Support document generation, storage, and retrieval.

#### Billing and Invoicing:

- Generate accurate invoices based on shipping activity.
- Support various billing models, such as per shipment or weight-based.

#### Integration with Other Systems (MAYBE WMS):

- Integrate with other business systems, such as Enterprise Resource Planning (ERP) or Warehouse Management Systems (WMS).

#### Alerts and Notifications:

- Provide alerts and notifications for critical events.
- Alert users about delays, exceptions, or changes in shipment status.

#### Exception Management:

- Handle exceptions and disruptions in the transportation process.
- Provide tools for resolving issues and implementing contingency plans.

#### Environmental Impact Tracking:

- Include features to track and report on the environmental impact of transportation activities.
- Support sustainable and eco-friendly transportation options.

## Initial Overall Design

So the main ideas and functioning of this app are:

#### User Interface

- Live tracking
- Order from other companies
- Deliver from inventory
- Choose routes

#### Shipment Planning

- Choose between routes
  - Use algorithms? (TODO: Investigate how)
  - Route optimization
- Schedule shipments

#### Route optimization

- Route calculating costs, time, traffic, fuel efficiency

#### Live Tracking

- Map with routes
- Current location of shipments
- Location of businesses

#### Virtual businesses

- Create shipments
  - Create deliveries
  - Create orders
- Manage inventory
  - Create inventory

#### Document management

- Store shipment documentation
- Retrieve shipment documentation

#### Billing

- Generate cost
- Generate profit
- Generate receipts

## Technology Stack

#### Backend:

- Programming Language: Python (Flask)
- Database: SQLite3 or PostgreSQL
- User Authentication: Third-party solution (to be decided later)

#### Frontend:

- Framework/Library: React
- Map Visualization: To be decided (Chart.js, D3.js, or other options)

#### Deployment:

- Cloud Provider: To be decided

## Initial Roadmap

#### Research

- TMS Requirements: Understand how a tms should work, get information about what to implement
- Technical Requirements: Define the technology stack, and data security requirements.
- Project Timeline: Develop a realistic timeline with milestones and deadlines.

#### Designing and Prototyping

- Wire-framing: Create wireframes to outline the layout and navigation of your web app.
- Prototyping: Build a prototype to test the user experience and gather feedback.

#### Development and Testing

- Front-End Development: Design the user interface and user experience.
- Back-End Development: Create the server-side logic, databases, and application functionality.
- Testing: Rigorously test the web app for bugs, security vulnerabilities, and performance issues.

# Naming Guidelines

## Filenames

- **Folders**: Use kebab-case.
  - Example: `/example-folder`
- **React Components**: Use PascalCase.
  - Example: `ExampleFile.jsx`
- **Python Files**: Use snake_case.
  - Example: `example_file.py`

## Components

- **React Components**: Use PascalCase.
  - Example: `ExampleComponent.jsx`

## Variables and Functions

- **JavaScript/React**:
  - Variables and functions: camelCase
    - Example: `exampleVariable`, `fetchData()`
- **Python**:
  - Variables and functions: snake_case
    - Example: `example_variable`, `fetch_data()`

## Constants

- **JavaScript/React**: Use UPPER_SNAKE_CASE for constants.
  - Example: `MAX_COUNT`
- **Python**: Use UPPER_SNAKE_CASE for constants.
  - Example: `MAX_COUNT`

## Classes

- **JavaScript/React**: Use PascalCase.
  - Example: `ExampleClass`
- **Python**: Use PascalCase.
  - Example: `ExampleClass`

## API Naming

- **Endpoint Names**: Use kebab-case for URL paths.
  - Example: `/api/login-user`
- **HTTP Methods**: Use appropriate HTTP methods (GET, POST, PUT, DELETE) with clear and descriptive names.
  - Example: `GET /api/get-user`, `POST /api/create-user`, `PUT /api/update-user`, `DELETE /api/delete-user`

## Database Tables

- **Table Names**: Use plural snake_case.
  - Example: `users`, `order_items`

## General Guidelines

- **Descriptive and Consistent**: Ensure names are descriptive and consistent throughout the project.
- **Avoid Abbreviations**: Avoid abbreviations unless they are widely accepted and understood.
- **Keep it Simple**: Names should be as simple and concise as possible while still conveying the necessary information.

## Example Structure

Here's an example directory and file structure following these guidelines:

- /my-project
- /api
- /v1
- users.py
- orders.py
- /frontend
- /src
- /components
- UserList.jsx
- UserProfile.jsx
- /pages
- HomePage.jsx
- LoginPage.jsx
- /migrations
- 001_initial_migration.py
- /models
- user.py
- order.py
- /services
- user_service.py
- order_service.py
- /static
- /css
- styles.css
- /templates
- base.html
- index.html
- app.py
- config.py
- requirements.txt

## Commits

- **INITIAL**: Commits that involve the initial project setup, including creating the project structure, adding essential configuration files, and initial dependencies.

  ```
  INITIAL: Set up initial project structure with basic configuration files

  - Created the initial folder structure
  - Added .gitignore, README.md, and LICENSE
  - Installed basic dependencies (React, Webpack, Babel)
  ```

- **ADD**: Commits that add new features, components, or substantial pieces of code to the project.

  ```
  ADD: Implemented user login functionality

  - Added Login component
  - Integrated authentication API
  - Included form validation logic
  ```

- **UPDATE**: Commits for small, incremental changes or improvements to existing code without introducing new features.

  ```
  UPDATE: Enhanced error handling in user profile component

  - Improved error messages for failed data fetches
  - Added additional checks for null values
  ```

- **REFACTOR**: Commits that involve restructuring existing code without changing its external behavior, typically for improving code readability, maintainability, or performance.

  ```
  REFACTOR: Simplified user service logic and improved readability

  - Extracted common functions into utils.js
  - Reorganized file structure for services
  - Removed redundant code
  ```

- **FIX**: Commits that fix bugs, typos, broken links, linter warnings, or other minor issues.

  ```
  FIX: Corrected typo in the registration form validation error message

  - Fixed typo in the validation message for email field
  - Updated unit tests to reflect the corrected message
  ```

- **TESTS**: Commits that add, update, or improve tests, including unit tests, integration tests, and end-to-end tests.

  ```
  TESTS: Added unit tests for the authentication service

  - Implemented tests for login and logout functions
  - Achieved 90% test coverage for the authentication module
  ```

- **STYLES**: Commits that involve changes to the styles, including CSS, SCSS, styled-components, or any other styling mechanisms.

  ```
  STYLES: Updated button styles to match the new design guidelines

  - Changed button colors and padding
  - Updated hover and active states
  - Ensured consistent styling across all button components
  ```

- **BUILD**: Commits related to the build process, including configuration files for build tools, scripts, and optimizations for the build process.

  ```
  BUILD: Optimized webpack configuration for production

  - Enabled code splitting
  - Configured tree shaking
  - Minified CSS and JS files
  ```

- **PRODUCTION**: Commits that are specific to deploying or preparing the application for production, including environment configurations and deployment scripts.

  ```
  PRODUCTION: Updated environment variables for production deployment

  - Added production API endpoint
  - Configured production-specific environment variables
  - Updated deployment scripts for the production environment
  ```

- **WIP**: Commits that represent work in progress, not yet ready for merging, but need to be committed to save progress.

  ```
  WIP: Started implementing the user dashboard component

  - Initial layout for the user dashboard
  - Placeholder data and basic structure in place
  - To be continued with data integration and styling
  ```

- **REMOVE**: Commits that remove unused files, obsolete code, or dependencies that are no longer needed.

  ```
  REMOVE: Deleted deprecated authentication module

  - Removed old authentication module no longer in use
  - Cleaned up related imports and dependencies
  - Updated documentation to reflect changes
  ```

# Status Codes Cheat Sheet

## Informational (1xx)

### Descriptions of provisional responses. The server has received the request headers, and the client should proceed to send the request body (if any).

- **100 Continue**
  - Example: The client should continue with its request.
- **101 Switching Protocols**
  - Example: The client has requested the server to switch protocols, and the server has agreed to do so.

## Successful (2xx)

### Indicates that the client's request was successfully received, understood, and accepted.

- **200 OK**
  - Example: The request has succeeded. Response to a successful GET, PUT, or DELETE.
- **201 Created**
  - Example: The request has been fulfilled, resulting in the creation of a new resource.
- **202 Accepted**
  - Example: The request has been accepted for processing, but the processing has not been completed.
- **204 No Content**
  - Example: The server has successfully processed the request, but is not returning any content.

## Redirection (3xx)

### Further action needs to be taken by the user agent to fulfill the request.

- **301 Moved Permanently**
  - Example: The requested resource has been permanently moved to a new URL.
- **302 Found**
  - Example: The requested resource has been temporarily moved to a different URL.
- **304 Not Modified**
  - Example: The resource has not been modified since the last request.

## Client Error (4xx)

### The request contains bad syntax or cannot be fulfilled.

- **400 Bad Request**
  - Example: The server cannot process the request due to a client error (e.g., malformed request syntax).
- **401 Unauthorized**
  - Example: The request requires user authentication. Response for missing or invalid JWT.
- **403 Forbidden**
  - Example: The server understands the request but refuses to authorize it.
- **404 Not Found**
  - Example: The server cannot find the requested resource.
- **405 Method Not Allowed**
  - Example: The request method is not supported for the requested resource.
- **409 Conflict**
  - Example: The request could not be processed due to a conflict with the current state of the resource.
- **429 Too Many Requests**
  - Example: The user has sent too many requests in a given amount of time.

## Server Error (5xx)

### The server failed to fulfill a valid request.

- **500 Internal Server Error**
  - Example: The server encountered an unexpected condition that prevented it from fulfilling the request.
- **501 Not Implemented**
  - Example: The server does not support the functionality required to fulfill the request.
- **502 Bad Gateway**
  - Example: The server, while acting as a gateway or proxy, received an invalid response from the upstream server.
- **503 Service Unavailable**
  - Example: The server is currently unable to handle the request due to maintenance or overload.
- **504 Gateway Timeout**
  - Example: The server, while acting as a gateway or proxy, did not receive a timely response from the upstream server.

## Project timeline

### Start Date (11/Jan/2024)

Research

Design and Prototyping

- Investigate about wireframes
- Build a wire-frame

Development and Testing

- Front-End
  - Design user interface (FIGMA or other tool)
  - Code the front end
- Back-End
  - Define databases needed
  - Server side logic
  - App functionality
- Testing
  - Security vulnerabilities
  - Performance issues
  - Bugs
  - Design optimizations

# Structure

## Admin

#### Oversees the entire system, manages user roles and permissions, and ensures smooth operation of the app.

- **Dashboard**:
  Overview of system performance, key metrics, and notifications.
- **User Management**:
  Add, edit, and remove users. Assign roles and permissions.
- **System Settings**:
  Configure system-wide settings and preferences.
- **Audit Log**:
  View system activity logs for security and compliance.
- **Reports**:
  Generate and view various system reports.
- **Simulation and Testing Environment**:
  Scenario Simulator for testing system resilience and performance.
- **Training and Support Resources**:
  Training Center with video tutorials, user manuals, FAQs, and helpdesk feature.

## Transportation Manager

#### Manages transportation operations, including planning and scheduling routes, selecting carriers, tracking shipments, and optimizing transportation costs.

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

## Carrier

#### Handles carrier-specific tasks such as accepting or rejecting shipments, updating shipment statuses, and providing freight quotes. Manages assigned shipments and communicates with the transportation manager.

- **Dashboard**:
  Overview of assigned shipments and key metrics.
- **Shipment Management**:
  Accept or reject shipments, update shipment statuses.
- **Freight Quotes**:
  Provide and manage freight quotes for new shipments.
- **Communication**:
  Interface for messaging with the transportation manager.
- **Reports**:
  View performance reports and shipment history.

## Customer/Shipper

#### Creates and tracks shipments, views shipment history, generates reports, manages billing and invoicing, initiates shipments, and tracks delivery progress.

- **Dashboard**:
  Overview of shipment status, key metrics, and notifications.
- **Create Shipment**:
  Initiate new shipments with necessary details.
- **Shipment Tracking**:
  Track the status of ongoing shipments.
- **Shipment History**:
  View history and details of past shipments.
- **Reports**:
  Generate various reports on shipments and billing.
- **Billing & Invoicing**:
  Manage billing information, view invoices, and make payments.
- **Messaging Hub**:
  Collaborative communication platform for seamless collaboration.

## Driver

#### Views assigned shipments, updates delivery statuses, and communicates with the transportation manager. Provides real-time location updates and confirms delivery completion.

- **Dashboard**:
  Overview of assigned shipments and key metrics.
- **Assigned Shipments**:
  View details of assigned shipments.
- **Update Status**:
  Update the status of shipments in transit.
- **Location Updates**:
  Provide real-time location updates.
- **Delivery Confirmation**:
  Confirm delivery completion with necessary details.
- **Messaging Hub**:
  Collaborative communication platform for coordination.

## Finance/Accounting

#### Manages billing, invoicing, payment processing, and financial reporting. Handles customer billing, carrier payments, invoice reconciliation, and financial compliance.

- **Dashboard**:
  Overview of financial performance, key metrics, and notifications.
- **Billing Management**:
  Handle customer billing processes.
- **Invoicing**:
  Generate and manage invoices for customers and carriers.
- **Payment Processing**:
  Process payments and manage payment records.
- **Financial Reports**:
  Generate financial reports and perform reconciliation.
- **Compliance**:
  Ensure financial operations comply with regulations.
- **Audit Trail & Compliance Center**:
  Track system activities and ensure compliance.

## Warehouse/Inventory Manager

#### Manages inventory within the TMS, including tracking inventory levels, stock replenishment, warehouse allocation, and order fulfillment. Coordinates with transportation for inbound and outbound shipments and ensures accurate stockkeeping.

- **Dashboard**:
  Overview of inventory levels and warehouse operations.
- **Inventory Management**:
  Track and manage inventory levels, perform stock replenishment.
- **Warehouse Allocation**:
  Allocate warehouse space for inbound and outbound shipments.
- **Order Fulfillment**:
  Manage order picking, packing, and shipping processes.
- **Shipment Coordination**:
  Coordinate with transportation for timely shipments.
- **Reports**:
  Generate inventory and warehouse performance reports.
- **Enterprise Integration Hub**:
  Integrate with ERP, CRM, or BI tools for seamless data flow.

### Performance Monitoring Suite (Check further along):

System-wide performance monitoring, caching mechanisms, load balancing, and scalability features.

## Simulation

I'm going to be using Discrete Event Simulation (DES). This is a prototype flow of what I want the simulation to do.

- **Start Simulation**
- **Initiation Sequences**

  - **Populate Databases**
    - tms_database
      - Users (multiple drivers, multiple warehouse managers), fill details
      - Warehouses (Fill with same info as simulation_database)
      - Inventory (Fill with same info as simulation_database)
    - simulation_database
      - Simulation control (clock?=0, speed_factor 1, status)
      - Simulaiton events (set events)
      - Probabilities (set probabilities)
      - Warehouses (fill with same info as tms_database)
      - Inventory (fill inventory, some warehouses ready to place orders)
      - Drivers (same info as tms_database)
      - Vehicles (set vehicle types)
  - **Create Objects and Environment**
    - Probably using simpy

- **Flow**

  1. Product needed, set up request for product (event)
  2. Plan route/driver/schedule (user action)

  - **Driver Events**

  1. Driver goes to pickup (event) (risks)
  2. Loading product (event)
  3. Start delivery route (event)
  4. End delivery route (event) (appointment time)
  5. Unload (event)
  6. Start return (event)
  7. End Return (event)

  - **Warehouses Events**

  1. Gradually reduce inventory (event)
  2. Request more product (event)

- **Risks**
  - **Road Blocks**
    - Small detour -> reroute (event)
    - Big detour -> action needed (event)
  - **Accident**
    - Small accident / low delay time (event)
    - Medium accident / mid delay time (event)
    - Big accident -> action needed (event)
  - **Traffic**
    - Small delay (event)
    - Mid delay (event)
    - Big delay -> action needed (event)
  - **Stops**
    - Sleep (event)
    - Eat (event)
    - Refuel (event)

## Research

I found a repository or another way to make the map. Using graph nodes instead of a grid. I might use OSMNX to import to python a real location graph. I'm hoping I can edit the exported graph as I want.

From what I've found I could technically manipulate the data I get and simulate live tracking too, also distance, and speed, traffic and other.

I will also have to research more about NetworkX and OSMNX.

Also from what I'm reading I should probably work on making a WMS and ERP.

I guess the research never stops.

Alan has been helping me figure out how it needs to work.

So the TMS should have a list of pending movements or deliveries, and from those be able to schedule the route and stuff.

I branched the repository, to try to catch some of the cases befoe calculating everything.

# Road

I'm going to start working on making something out of the OSMNX (Jan 17 2024), since I think based on what Find I'll be able to decipher things like the database and stuff.

I also started wireframimg using Figma, I will clean it up later.

So I started playing with the graph and osmnx, from what I figured out is that im going to need to follow something along this

```
Deside place in map -> get graph from osmnx -> save file ->
assign bussinesses based on node ids (probably more than x distance) -> show graph -> select origin and destination (by selecting businesses, which will select the nodes) -> get route -> place an item in the graph -> move that item to the next node following path (probably will have to move it along some coordinates between the nodes in the route over time)
```

I was able to get a LineString of an edge, that linestring contains the coordinates, so now I can make the route, and for each edge in the route get the linestring and just keep adding to the list of coordinates of all edges.

So, today is Jan/23/2024 I was working with D3 but I found that Leaflet has everything I need, as of right now I was able to drag a marker to origin and one to destination, make my api call and draw with a polyline on top of the map (a real world map).

I think what comes next is being able to get the closest edge and coordinate to the destination so it doesn't stop drawing at the edge, then comes making the moving icon.

The map has been going well, I finally finished pre origin logic. Next thing to do is do the same with the destination.

There is currently an error happening when the closest node is not part of the closest edge. For example closest node is A which connects to D, and closest edge is B to C. In this case I'm thinking that the closest edge should take priority. If this is the case I would have to change the closest node to be the closest node from the edge to the coordinate.

I'm redoing my logic, changing a lot of things. I might branch it just in case.

I now need to take into account that the algorithm that will avoid and decide the route based on pricing or time needs to have a different approach when it comes to assigning starting and finishing nodes.

I'm asking in stack overflow, now I need to extract only the necessary code to explain my situation.
I think I'm going to create a file in my repository to help with it.

From asking online I came up with the idea that maybe I can create a node and edge for each coordinate in the interpolated edge. This could potentially solve the issue when deciding a starting edge considering the thing I'm going to base the route on. For example I wouldn't have to worry about changing directions or starting and finishing nodes. I would have to calculate estimated times and ignore the found edge. It could work.

I will have to calculate the speed, distance and other things about the road, I'm going to have to come up with a specific measurements for the interpolation, since im going to have to divide the street evenly within a certain distance.

I looked into OSRM but I want to be able to choose between shortest distance, fastest distance.

Okay, new approach. I'm going to divide everything into smaller sections. Clearing up the files into different tasks.
I'm also going to start with the logic of the database and after some parts are done, continue with the routing algorithms.

For routing algorithms node --> Dijktra, A search algorithm, euclidean distance, graphHopper

Apr 17
I'm going to start marking dates for easier reference to my progress. Right now I'm going very slow and changing a lot of things, but learning for future projects.

Apr 22
Research about blueprints, I'm trying to figure out where to put what. For example my routing for thing like index, dashboard in routing, should I manage all routes in one file? Should I have separate files for different routes?

Apr 23
So blueprints can be used to have multiple routing files, then putting them together into the main app at the end. I'm going to divide the routing by role and a views.py, I'm going to have the teardown for closing db connections in app.py so it runs after each request (to be tested).

I'm also going to have an auth.py for login stuff, and forms.py

May 8
I have been concentrated on another thing, which has left this project stuck, so in order to keep it moving, even if I don't add code, I'll develop ideas to add, or just plan our my next steps.

June 1
I am finally free to start putting a lot of time to this project.
What I'm going to do is do all rendering with react, since react is a spa, I have to do something when building to handle joining both servers or something.
I am now going to start with the login page, as well as the register, but the register can only be accessed by the admin so I will have to work on the auth section.
I'm finishing today with the login form from other places as to not spend too much time on it. What's next is to figure out form submission, add a
TODO for real-time validation, I don't think I should be spending too much time in that either.

June 2
The login form component should have validations for that form, the login page file should have log in handling.
The handle login should verify account, retrieve data for user and redirect to appropriate dashboard.

June 3
Changed some things that I had copied into what I understand better, I am working on setting up the API for logging in.

June 4
I'm currently working on the logging in the user and saving the data in session. I need to clean up the handleLogin onSubmit for the Login.jsx and put all the api calls in it and get rid of unnecessary blocks.

June 5
I added a style guide to my project to avoid spending time trying to figure out how to name what.
I'm working on authorization, I'm taking a look at authorization tokens. As far as I understand this is how it will look. App.jsx handles routing, include PrivateRouting for things that require authorization, PrivateRouting will take care of the logic behind what to render.

June 6
I was able to implement the use of tokens in a very basic way to handle authentication and authorization. I was also able to figure out how to implement the PrivateRouting, by making it as a wall in order to access the nested Routes. I sill need to test if it works by redirecting to the AdminDashboard after login.

I think I finished checking for the access for admin, this should be the same for any other role. I also want to create a file for my TODO list so I keep track of what I leave for later.

June 8
Just finished adding TODOs into my TODO app, instead of keeping it as an .md file, I decided on using microsoft's TODO app and I now have them organized by priorities.

I'm thinking about how to set a layout for the different roles. Each layout needs to have the links to the respective pages. I could have 1 layout, and have the logic made in there. That sounds like the best choice. Another choice would be to have a layout for each role and make the app render each layout based on the role. I'm going to write some pros and cons.

I decided to have just one layout file, because of reusability of code and readability in the rendering. It is also not that big of a file so there shouldn't be a need to separate them.

Okay so in order to improve how I handle all of this I'm going to modify auth.js into an context provider which will wrap my app.

Jun 9
I was able to both fix the auth.js with the context provider and to restrict access with a single component. Next steps are to go page by page creating a basic design and coding the important parts. I'm starting with the UserManagement page.

Jun 10
There was an issue with the timing of the auth.jsx states when refreshing due to the useEffect and how it works. The solution was adding a Loading state that would give time for the useEffect to set the states before attempting to use them. I also added a delay so the transitions look smoother.

Jun 12
I have been working on making the app even more modular, thinking it was going to be pretty easy. But I stumbled across an error with my JWT when trying to logout. The issue was resolved by setting up a secret key for JWT and an algorithm.
I think what I need to do next is learn how to do testing files, for cases so I don't have to manually do everything.

Jun 19
I modified the database and added a lot more stuff. So now I need to refactor my code to fix the new schema. Lesson for later -> **Set up the schema before developing the code, cannot use a test database with real code, but can use test code with real database**.

Jun 23
~~I decided to declare how to pass data from and to the db. The rule will be to leave the data ready to use for the other. For example passing role_name: "Admin" to the frontend would be setting it as roleName in the backend.~~ The backend will handle changing it back and forth, in data cleanup.
I'm having trouble validating token, I'm researching and it turns out that the OPTIONS request in the preflight is having trouble with the jwt_required decorator. I think the solution is very simple since I've had this issue before but I just can't fix it.

Jun 24
Turns out the error was so simple, I had a typo in the endpoint. At the end I didn't even need that API. But the way I was able to find the error was through the devtools. I don't know how it didn't cross my mind that the preflight was failing because it couldn't find the endpoint. I was too focused, thinking the error was with how jwt_required was working. Anyways, I don't need that because of protected endpoints. What I do need to do is handle the unauthorized access status code and force logout when a jwt is invalid.
I also need to make a status code cheatsheet.

Jun 26
I'm thinking of how I should handle onboarding. I think I should include it in the response code.

Jul 1
I started designing how the simulation will interact with the app. I'm going to be developing it along side the remainding pages of the app so that the implementation is easier. As of right now I have the simulation folder on the same level as the server and client but I might move it inside the server folder because of how much it might use information from the users database.

Jul 4
I was able to get a prototype of the simulation working. So now I'm going to have to figure out how to implement it with real time, and how to set it up for it to work with the app.

Jul 5
Having some trouble implementing handling async functions inside the running simulation. I will use it to send the request but still lower the inventory and other stuff. I'm using asyncio but I cant seem to implement it correctly.

Jul 8
The warehouse manager needs to receive the info from the simulation. Then he places the information into the app.

Jul 9
The simulation with simpy might not be the best approach, simpy doesn't seem to work with async functions or threading. I was hoping on using it to trigger events outside the simulation but that doesn't seem to be possible. I'm going to take a look at other things like APS scheduler, or just try to create my own simulation engine.
I managed to make some progress using only threading, it doesn't seem like a good idea because of all the complexity of managing thread security and other things that come with threading. I'm trying to mix async and threading but it still feels off.

Jul 12
I think I have it sort of figured out, I'm going to have a simple WMS to handle **inventory management, reorder logic and request handling**. I'm going to probably use an event driven architecture.
I'm going to have it all inside the same flask app, but I need to make sure it is completely separate, this is because I want to implement a more robust WMS later on and I need it to be able to work independently from each other.

I think I can handle the risks and events for the driver still with simpy. The way this could work is to simulate the drive and save what events were triggered, then share the steps of what happened to the TMS or some other middleware.
I would need to add things like, original time, total time. Then I would also have to check if an action is needed, then I would also have to trigger the simulation maybe with an api. For example if a reschedule is needed send it to an api to run the simulation with the new data.
So to recap: WMS not using simpy, Driver events using simpy.

Jul 13
Maybe I leave the logic of a WMS for later, I should create a basic function like, create order. And just have it sent to the TMS.
Considering this the new flow, for creating a random order, would have to be something like: select a random vehicle > select random warehouse, select random product, select random supplier > select random quantity below vehicle constraints > ...

Jul 14
I decided on having it be more straight forward, I'm working on a TMS not the WMS. So for now I'm developing the connection between them. It will work like this:
Trigger an order creation, from order cases -> save in current wms db -> send to tms -> receive.
I'm going to be using event driven architecture. Probably using a post request, but look into including message brokers like Kafka, RabbitMQ.

Jul 16
Today I messed up bad! I tried to rename my server and client folders, but I decided against it and discarded all unstaged changes, this made the tracking for every file to go crazy, and then I tried just going back to the last commit, but ended up deleting all the untracked files (which were all of them since the folders still remained with their new names). I had to delete my local repo and clone it again. I, for some reason, stumbled across errors that weren't supposed to be there. For example: Wrongly named files. I have no idea since when it went back to that naming, but fixable.
I gotta take a course on git commands so that I know exactly what to do next time.
So apparently when renaming inside a repo, you should rename as commits for example git mv file other-file and then git commit. This is because Windows (where my git is) is case insensitive. And to rename a file from login to Login, you need to do something like git mv login tmp and then git mv tmp Login. Because of the same casing thing.

Jul 17
I'm going to try to rename them properly this time. I get permission denied. I wonder if it's because of OneDrive.
I'm also going to start implementing flask factory and logging.

Jul 19
I've been trying to set up my flask factory but I can't get anything to work.

Jul 26
I have been trying to refactor my whole app, I was able to make a flask factory pattern, but now I'm struggling refactoring to sqlalchemy.

Jul 28
Yesterday I was able to implement the multiple database initiation. Today I realized that there are some problems with migrations. For some reason it wants to delete all of my tables. I'm going to probably have to create a smaller example and ask online.

Aug 3
I have been busy refactoring to sqlalchemy, but I got that done. I am now asking online about my error handling questions, aborts, etc.

Aug 7
I've been stuck trying to decide on what to do with aborts and exceptions and logging.

Aug 8
The way I'm going to be handling request is as follows, endpoint receives check if data exists, abort if not, run service, if success return success response if error return appropriate error response. In service, try-catch block wrapping, raise custom exceptions, they are handled by errors_handler. Logging and audit happen before returning to the endpoint or before raising the error after catching it. Service only returns response.

Aug 13
I'm now done with adding the logging, audit, structuring how the app handles errors and setting up tests. Now I need to either keep moving forward with the app, or start adding validations and cleaning things up.
I think that I will start adding validations because it is going to take some time and I need to start so that when I have more things in my app, I already have a set structure and can just go through it.

Aug 19
Will probably have to look into flask-limiter. Moving forward to developing transportation manager, carrier, etc.

Aug 22
Did a diagram on how to approach cleaning things. Currently working on adding validations to update user. Got an idea of how to improve onboarding check: Add a status column to the user model, there will be 3 possible things "active", "inactive", "not_onboarded". This way I will only access first and last name if user is onboarded.

Aug 25
I had an idea on how to improve the onboarding check. By adding a status column to the user model. Having three cases "active, inactive or not_onboarded". This way I can keep everything bundled up and neat. But I have to consider how to correctly use it so it doesn't become more work than it was.

Aug 29
In order to improve the onboarding I need to do the following first: Update the database population (probably separating adding the roles from the users created), define the flow of the status in the auth token...

Sep 8
I was able to get a very good system design with the help of Claude. It is not refined but it has helped me clean some of my thoughts.
And now I think I want to do something drastic again. I want to change from having it based on role, to based on core modules, this way I can keep (Forgot what I was adding here).

Sep 17
I'm in the middle of refactoring, I have already done the backend. Refactoring the frontend has been harder since I'm having to implement Redux, Axios, and other things.

Sep 23
I'm currently working on fixing a race condition again. The PublicRoute checks if authenticated and redirects before the roleBasedNavigation can redirect. When commenting out the PublicRoute's check, the order of things still firstly goes to the PublicRoute and only after that is done it redirects based on the navigate in the roleBasedNavigation. I have some options, adding a loading state, adding a delay, checking why useNavigate doesn't immediately redirect.

Sep 25
I'm going to break down the problem into separate parts to be able to brainstorm solutions.
Problem: roleBasedNavigation code runs, PublicRoute then checks, PublicRoute redirects, roleBasedNavigation never redirects.
Details: roleBasedNavigation is a hook that uses useNavigate to redirect, PublicRoute is a component that checks if authenticated from the authState, it uses useNavigate to redirect.
The useAuth hook dispatches the setUser and other set functions for auth.
The authState changes to isAuthenticated therefore the PublicRoute's check is being triggered.
I don't understand why if I run the useNavigate in the roleBasedNavigation it doesn't redirect immediately. But instead if continues running the code until eventually the PublicRoute's useNavigate is triggered.
Ideas: So, what we don't want is the check to run. The check is running because the authState is being updated. I need to

Oct 12
Finished refactoring to centralize everything by core modules.
Moving on to implementing better access and refresh tokens. I haven't decided if my access token will always have user data of just the user id. Role checking for protected routes in the backend was done by checking the jwt token's data. But that means that when refreshing an access token I will have to create that data again.

April 15
Okay, I'm back from my long break, I have done more since Oct 12 but for some reason I didn't update this. Today I have reinstalled things and created files that got deleted because of factory resetting my computer.
FOR FUTURE REFERENCE DO THESE STEPS:
.env creation
create venv
install from requirements
flask --app server db-init
flask --app server populate-db
npm run dev (in the client folder)

Right now I need to add the Product table to the models, then create the validations for it. Add the insertion of the order to the database and check for errors.

Apr 23
I have decided to do the following with Spinners.
If in button:


```jsx
<Button
  variant="primary"
  type="submit"
  disabled={updateUserStatus === "pending"}
>
  {updateUserStatus !== "pending" ? (
    "Update"
  ) : (
    <Spinner animation="border" role="updateUserStatus" />
  )}
</Button>
```

If getting data for a component:

```jsx
{isLoading ? (
  <Spinner animation="border" role="dataStatus"/>
) : error ? (
  <p>Try Again...</p>
) : data && data.length > 0 ? (
  <DataComponent>
) : (
  <p>No data Found</p>
)}
```
