# online-store-api
A file in xml format is given - a feed (product catalog) of an online store.
Designations: product - model - sold goods, offer - trade offer of the product.
Necessary:
1. Think over and implement a data structure for storage and operation. Relational database preferred.
2. Write a parser for the feed. For parsing XML, you can use a ready-made library.
3. Create an API with two endpoints: POST /products - getting products by category, GET /product - getting a card for a specific product (including all offers).

Also done:
- connection swagger, autodocumentation;
- added endpoint for uploading the feed file to the server;
- the project is built in docker.
The format of the files sent by the server is JSON.

### Prerequisites

This project relies on the [Docker](https://www.docker.com/) and the [Docker Compose](https://github.com/docker/compose). You should install them to build and run the project.

The system uses [RabbitMQ](https://www.rabbitmq.com/) and [PostgreSQL](https://www.postgresql.org/) as message broker and RDBMS respectively. Docker containers forwards default ports for them, therefore you should make sure, that these services shutted down or you should map different ports in _docker-compose.yml_ file.

### Build

To build the project you need to run the build command:

``` sh
docker-compose build
```

### Run

To run the project simply execute the following command:

``` sh
docker-compose up
```
