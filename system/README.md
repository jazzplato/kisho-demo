# Kisho Cinema
Kisho Cinema is a demo system for this independent study. It is a simple web app where users can submit and search for movie ratings.

## System Goals
There are 3 main goals for this Kisho Cinema movie rating system:
- Availability
  - The system should always be available
  - This goal is from both the users' and the system owners' perspsectives
- Up-to-date
  - The ratings should be as up-to-date as possible
  - This goal is from the users' perspective
- Inexpensive
  - The system should only incur minimal costs
  - This goal is from the system owners' perspective

The system should always bare these 3 goals in mind

### Conflicting Goals

## System Architecture
### Components
In this demo system, there are 2 main components
- Web tier: a Django app
  - To allow users to query and submit ratings for the movies.
- Database tier: a MySQL database
  - To persist the data for users and movies.

### Connectors
In this demo system, there are a number of connector options for and between the components mentioned above.
- Reverse proxy
  - Nginx/Openresty
- Message queue
  - Redis
- Data cache
  - Redis

### C&C Views
Since there can be a number of connector choices of the given components (assuming the components are compatible with all the connector options in both architectural design and technical implmentation), the C&C architecture view of the Kisho Cinema system can have a number of variations, as below