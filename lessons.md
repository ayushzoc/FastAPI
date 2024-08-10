### Order Matters
* Always work with top-down approach.
* Structure matters.

### Why we need Schema
* It's a paint to get all the values from the body
* The client can send whatever data they want
* The data isn't getting validated
* We ultimately want to force the client to send data in a schema that we expect

### CRUD
* Create: Post
* Read: Get
* Update: Put/Patch
* Delete: Delete

### Path Parameter
* Every path parameter will have type 'str'.
* Have to change the type before implementing.
* Easiest way is to define the variable for path parameter in the function parameter itself.