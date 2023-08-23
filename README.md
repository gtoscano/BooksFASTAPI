# BooksFASTAPI

BooksFASTAPI is a simple API developed using FastAPI to demonstrate the basic CRUD operations for managing books. The project showcases the power and simplicity of FastAPI, using PostgreSQL for storage.

## Setting Up

### Prerequisites

This project depends on the following Python packages:

- **FastAPI**: A modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints. [More info](https://fastapi.tiangolo.com/)
- **Uvicorn**: An ASGI server implementation, using uvloop and httptools. It allows for serving of FastAPI applications. [More info](https://www.uvicorn.org/)
- **SQLAlchemy**: A SQL toolkit and Object-Relational Mapping (ORM) library for Python. It gives application developers the full power and flexibility of SQL. [More info](https://www.sqlalchemy.org/)
- **psycopg2**: PostgreSQL adapter for Python. It is used to connect and interact with PostgreSQL databases from Python applications. [More info](http://initd.org/psycopg/)

### Required Python Version
- Python 3.9

### Installation

To install the project dependencies, you will need `pipenv`. If you haven't installed it, you can do so using `pip`:

```bash
pip install pipenv
```

Once `pipenv` is installed, navigate to the project directory (where the `Pipfile` is located) and run:

```bash
pipenv install
```

This will install all the dependencies as listed in the `Pipfile`.


### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/gtoscano/BooksFASTAPI.git
   cd BooksFASTAPI
   ```

2. **Set Up a Virtual Environment** (Optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install fastapi[all] sqlalchemy psycopg2
   ```

4. **Set Up the Database**:

   - Start PostgreSQL and create a new database named `bookdb`.
   - Update the `DATABASE_URL` in `models.py` with your PostgreSQL credentials.

5. **Create the Tables**:
   ```bash
   python create_tables.py
   ```

## Running the Application

To run the application, use the following command:

```bash
uvicorn main:app --reload
```

The API will be accessible at [http://localhost:8000](http://localhost:8000).

## Usage

Here are some `curl` examples to interact with the API:

- **Create a Book**:
  ```bash
  curl -X POST "http://localhost:8000/books/" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"author\":\"J.K. Rowling\",\"title\":\"Harry Potter\",\"year\":2001}"
  ```

- **Get All Books**:
  ```bash
  curl -X GET "http://localhost:8000/books/" -H  "accept: application/json"
  ```

- **Get a Specific Book**:
  ```bash
  curl -X GET "http://localhost:8000/books/1" -H  "accept: application/json"
  ```

- **Update a Book**:
  ```bash
  curl -X PUT "http://localhost:8000/books/1" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"author\":\"J.K. Rowling\",\"title\":\"Harry Potter and the Chamber of Secrets\",\"year\":2002}"
  ```

- **Delete a Book**:
  ```bash
  curl -X DELETE "http://localhost:8000/books/1" -H  "accept: application/json"
  ```

## License

This project is licensed under the terms of the [Apache License 2.0](LICENSE).

