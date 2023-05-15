<table align="center"><tr><td align="center" width="9999">
<h1>UniCrud</h1>
</td></tr></table>

<div align="center">

</div>

UniCrud is as a RESTful API that acts as a proxy for multiple CRUD API implementations. 
It provides a unified set of API endpoints for Create, Read, Update, and Delete operations, 
which are the core operations of a RESTful API. By using the FastAPI framework and the 
provided HTTP verbs (POST, GET, PUT, DELETE), this application adheres to the principles 
of REST architecture.

## Features
- Supports multiple services with custom implementations
- Unified CRUD (Create, Read, Update, Delete) operations for resources
- Retrieve service-specific information
- FastAPI powered for easy integration and extensibility
- Example implementation for time tracking services
- Dockerized setup with Nginx reverse proxy

## Getting Started
### Prerequisites
- Docker
- Docker Compose

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/generalized-crud-api-wrapper.git
 
2. Move to the project directory:
    ```bash
    cd generalized-crud-api-wrapper
    ```
3. Build and run the Docker containers:
    ```bash
    docker-compose up -d --build
    ```

The api should now be accessible at http://localhost:8000/api/v1

## Implementing Custom Services
To add support for a new service, create a new module inside the implementations folder and ensure 
your implementation is a child of the `CRUDApi` abstract class. Update the find_all_implementations 
function in the main application file to discover and load your custom service.

## Usage
The API provides a common interface for CRUD operations and service information retrieval. Example usage includes:

- **POST /api/v1/{service}/create/{resource_type}/**
- **GET /api/v1/{service}/read/{resource_type}/**
- **PUT /api/v1/{service}/update/{resource_type}/**
- **DELETE /api/v1/{service}/delete/{resource_type}/**

Refer to the API documentation, available at http://localhost:8000/docs, for more details on the available endpoints and their parameters.