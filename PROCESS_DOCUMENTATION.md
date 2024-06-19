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

## Research

I found a repository or another way to make the map. Using graph nodes instead of a grid. I might use OSMNX to import to python a real location graph. I'm hoping I can edit the exported graph as I want.

From what I've found I could technically manipulate the data I get and simulate live tracking too, also distance, and speed, traffic and other.

I will also have to research more about NetworkX and OSMNX.

Also from what I'm reading I should probably work on making a WMS and ERP.

I guess the research never stops.

Alan has been helping me figure out how it needs to work.

So the TMS should have a list of pending movements or deliveries, and from those be able to schedule the route and stuff.

I branched the repository, to try to catch some of the cases befoe calculating everything.

## Design and prototyping

I'm going to start working on making something out of the OSMNX (Jan 17 2024), since I think based on what Find I'll be able to decipher things like the database and stuff.

I also started wireframimg using Figma, I will clean it up later.

So I startes playing with the graph and osmnx, from what I figured out is that im going to need to follow something along this

```
Deside place in map -> get graph from osmnx -> save file ->
assign bussinesses based on node ids (probably more than x distance) -> show graph -> select origin and destination (by selecting businesses, which will select the nodes) -> get route -> place an item in the graph -> move that item to the next node following path (probably will have to move it along some coordinates between the nodes in the route over time)
```

I was able to get a LineString of an edge, that linestring contains the coordinates, so now I can make the route, and for each edge in the route get the linestring and just keep adding to the list of coordinates of all edges.

So, today is Jan/23/2024 I was working with D3 but I found that Leaflet has everything I need, as of right now I was able to drag a marker to origin and one to destination, make my api call and draw with a polyline on top of the map (a real world map).

I think what comes next is being able to get the closest edge and coordinate to the destination so it doesnt stop drawing at the edge, then comes making the moving icon.

The map has been going well, I finally finished pre origin logic. Next thing to do is do the same with the destination.

There is currently an error happening when the closest node is not part of the closest edge. For example closest node is A which connects to D, and closest edge is B to C. In this case I'm thinking that the closest edge should take priority. If this is the case I would have to change the closest node to be the closest node from the edge to the coordinate.

I'm redoing my logic, changing a lot of things. I might branch it just in case.

I now need to take into account that the algorithm that will avoid and decide the route based on pricing or time needs to have a different approach when it comes to assigning starting and finishing nodes.

I'm asking in stack overflow, now I need to extarct only the necessary code to explain my situation.
I think I'm going to create a file in my repository to help with it.

From asking online I came up with the idea that maybe I can create a node and edge for each coordinate in the interpolated edge. This could potentially solve the issue when deciding a starting edge considering the thing I'm going to base the route on. For example I wouldn't have to worry about changing directions or starting and finishing nodes. I would have to calculate estimated times and ignore the found edge. It could work.

I will have to calculate the speed, distance and other things about the road, I'm going to have to come up with a specific measurment for the interpolation, since im going to have to divide the street evenly within a certain distance.

I looked into OSRM but I want to be able to choose between shortest distance, fastest distance.

Okay, new approach. I'm going to divide everything into smaller sections. Clearing up the files into different tasks.
I'm also going to start with the logic of the database and after some parts are done, continue with the routing algorithms.

For routing algorithms node --> Dijktra, A search algorithm, euclian distance, graphHopper

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
I am now going to start with the login page, as well as the register, but the register can only be accesed by the admin so I will have to work on the auth section.
I'm finishing today with the login form from other places as to not spend too much time on it. What's next is to figure out form submition, add a
TODO for real-time validation, I don't think I should be spending too much time in that either.

June 2
The login form component should have validations for that form, the login page file should have log in handling.
The handle login should verify account, retrieve data for user and redirect to appropriate dashboard.

June 3
Changed some things that I had copied into what I understand better, I am working on setting up the API for loggin in.

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

I decided to have just one layout file, because of reusability of code and readibility in the rendering. It is also not that big of a file so there shouldn't be a need to separate them.

Okay so in order to improve how I handle all of this I'm going to modify auth.js into an context provider which will wrap my app.

Jun 9
I was able to both fix the auth.js with the context provider and to restrict access with a single component. Next steps are to go page by page creating a basic design and coding the important parts. I'm starting with the UserManagement page.

Jun 10
There was an issue with the timing of the auth.jsx states when refreshing due to the useEffect and how it works. The solution was adding a Loading state that would give time for the useEffect to set the states before attempting to use them. I also added a delay so the tranistions look smoother.

Jun 12
I have been working on making the app even more modular, thinking it was going to be pretty easy. But I stumbled accross an error with my JWT when trying to logout. The issue was resolved by setting up a secret key for JWT and an algorithm.
I think what I need to do next is learn how to do testing files, for cases so I dont have to manually do everything.

Jun 19
I modified the database and added a lot more stuff. So now I need to refactor my code to fix the new schema. Lesson for later -> **Set up the schema before developing the code, cannot use a test database with real code, but can use test code with real database**.
