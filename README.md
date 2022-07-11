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
