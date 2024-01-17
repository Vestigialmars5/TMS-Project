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

## Project timeline

### Start Date (11/Jan/2024)
### Approximate End Date (21/Mar/2024)

Research (2 days)

Design and Prototyping (5 days)

- Investigate about wireframes
- Build a wire-frame

Development and Testing (9 weeks)

- Front-End (2 weeks)
  - Design user interface (FIGMA or other tool) (2-4 days)
  - Code the front end (2-4 days)
- Back-End (3-5 weeks)
  - Define databases needed (1 day)
  - Server side logic (2 weeks)
  - App functionality (2 weeks)
- Testing (1-2 weeks)
  - Security vulnerabilities
  - Performance issues
  - Bugs
  - Design optimizations

## Research

I found a repository or another way to make the map. Using graph nodes instead of a grid. I might use OSMNX to import to python a real location graph. I'm hoping I can edit the exported graph as I want.

From what I've found I could technically manipulate the data I get and simulate live tracking too, also distance, and speed, traffic and other.

I will also have to research more about NetworkX and OSMNX.

Also from what I'm reading I should probably work on making a WMS and ERP.

## Design and prototyping

I'm going to start working on making something out of the OSMNX (Jan 17 2024), since I think based on what Find I'll be able to decipher things like the database and stuff.

I also started wireframimg using Figma, I will clean it up later.