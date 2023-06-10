# Todo App API

This is an API for a Todo App built using Flask and SQLAlchemy (with a PostgreSQL database). The API provides a way to manage users and their todo items. The API uses token-based authentication. The API is dockerised and has database migration functionaliy.

## Getting Started

To start the app on a local machine first you must create docker images and containers. Navigate to the directory where the `app.py` is contained and use the command.

    docker-compose up

You must then navigate to the container whcih is running the appliaction in order to set up migrations:

    docker exec -it simple-todo-app-web-1 /bin/bash

To set up migrations use the following lines in the command line:

    flask db init
    flask fb migrate
    flask db upgrade

*You are now free to use the application locally. Note the next version of this app will be hosted online and these instructions wil be updated accordingly. Note, in addition, interactive OpenAPI documentation will be added in the next version.*

## API Endpoints

### User Routes

1. **Create a new user**
    - URL: `/api/users`
    - Method: `POST`
    - Data Params: 
      ```
      {
          "first_name": "[string]",  // Non-empty, max 50 chars, only alpha
          "last_name": "[string]",  // Non-empty, max 50 chars, only alpha  
          "email": "[unique string]",  // Valid email with '@'
          "password": "[string]"  // Contains at least 5 chars, 1 number and 1 special char
      }
      ```
    - Success Response: 
      - Code: `201 CREATED`
      - Content: `{ id: [integer], first_name: "[string]", last_name: "[string]", email: "[unique string]" }`
    - Error Response:
      - Code: `409 CONFLICT`

2. **Read current user**
    - URL: `/api/users`
    - Method: `GET`
    - Headers: `Authorization: Bearer <your_token>`
    - Success Response: 
      - Code: `200 OK`
      - Content: `{ id: [integer], first_name: "[string]", last_name: "[string]", email: "[unique string]", todos: [Array of todo items] }`
    - Error Response:
      - Code: `401 UNAUTHORIZED` or `404 NOT FOUND`

3. **Update the first name and/or last name of a user**
    - URL: `/api/users`
    - Method: `PATCH`
    - Headers: `Authorization: Bearer <your_token>`
    - Data Params: 
      ```
      {
          "first_name": "[string]",  // Max 50 chars, only alpha
          "last_name": "[string]"  // Max 50 chars, only alpha
      }
      ```
    - Success Response: 
      - Code: `200 OK`
      - Content: `{ id: [integer], first_name: "[string]", last_name: "[string]", email: "[unique string]", todos: [Array of todo items] }`
    - Error Response:
      - Code: `400 BAD REQUEST` or `401 UNAUTHORIZED` or `404 NOT FOUND`

4. **Deletes a user**
    - URL: `/api/users`
    - Method: `DELETE`
    - Headers: `Authorization: Bearer <your_token>`
    - Success Response: 
      - Code: `200 OK`
    - Error Response:
      - Code: `401 UNAUTHORIZED` or `404 NOT FOUND`

### Auth Routes

1. **Log in and get login token**
    - URL: `/api/login`
    - Method: `POST`
    - Data Params: 
      ```
      {
          "email": "[string]",  // Valid email with '@'
          "password": "[string]"  // Contains at least 5 chars, 1 number and 1 special char
      }
      ```
    - Success Response: 
      - Code: `200 OK`
      - Content: `{ token: "[string]" }`
    - Error Response:
      - Code: `400 BAD REQUEST`

### Todo Routes

1. **Create a new todo**
    - URL: `/api/todos`
    - Method: `POST`
    - Headers: `Authorization: Bearer <your_token>`
    - Data Params: 
      ```
      {
          "content": "[string]",  // Max 200 chars  
          "priority": "[integer]"  // From 0-5
      }
      ```
    - Success Response: 
      - Code: `201 CREATED`
      - Content: `{ id: [integer], content: "[string]", priority: [integer] }`
    - Error Response:
      - Code: `400 BAD REQUEST`

2. **Get todo selected by id**
    - URL: `/api/todos/<int:todo_id>`
    - Method: `GET`
    - Headers: `Authorization: Bearer <your_token>`
    - Success Response: 
      - Code: `200 OK`
      - Content: `{ id: [integer], content: "[string]", priority: [integer] }`
    - Error Response:
      - Code: `400 BAD REQUEST` or `401 UNAUTHORIZED`

3. **Read user todos and (optionally) filter by priority**
    - URL: `/api/todos`, `/api/todos/priority/<int:priority>`
    - Method: `GET`
    - Headers: `Authorization: Bearer <your_token>`
    - Success Response: 
      - Code: `200 OK`
      - Content: `[ { id: [integer], content: "[string]", priority: [integer] }, ... ]`
    - Error Response:
      - Code: `400 BAD REQUEST` or `401 UNAUTHORIZED` or `404 NOT FOUND`

4. **Update the content and/or priority of a todo**
    - URL: `/api/todos/<int:todo_id>`
    - Method: `PATCH`
    - Headers: `Authorization: Bearer <your_token>`
    - Data Params: 
      ```
      {
          "content": "[string]",  // Max 200 chars
          "priority": "[integer]"  // From 0-5
      }
      ```
    - Success Response: 
      - Code: `200 OK`
      - Content: `{ id: [integer], content: "[string]", priority: [integer] }`
    - Error Response:
      - Code: `400 BAD REQUEST` or `401 UNAUTHORIZED` or `404 NOT FOUND`

5. **Delete a todo**
    - URL: `/api/todos/<int:todo_id>`
    - Method: `DELETE`
    - Headers: `Authorization: Bearer <your_token>`
    - Success Response: 
      - Code: `200 OK`
    - Error Response:
      - Code: `401 UNAUTHORIZED` or `404 NOT FOUND`

## Built With

- [Flask](https://flask.palletsprojects.com/) - The web framework used
- [SQLAlchemy](https://www.sqlalchemy.org/) - SQL Toolkit and Object-Relational Mapping (ORM) system for Python
- [PostreSQL](https://www.postgresql.org/) - Open source relational database
- [Docker](https://www.docker.com/) - Container platform

## Authors

Fergus Miller Kerins

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

I would like to acknoweldge insperation from: [Real Python REST API Tutorial](https://realpython.com/flask-connexion-rest-api/)