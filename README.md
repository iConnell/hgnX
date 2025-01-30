# Project Title

This project is a simple FastAPI application that provides student information through an API endpoint.

## Setup Instructions

1. **Clone the repository**:
    ```sh
    git clone https://github.com/iConnell/hgnX.git
    cd hgnX
    ```

2. **Create and activate a virtual environment**:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies**:
    ```sh
    pip install pipenv
    pipenv install
    ```

4. **Run the FastAPI application**:
    ```sh
    uvicorn main:app --reload
    ```

## API Documentation

### Endpoint URL

- **GET** `/api`

### Request/Response Format

- **Request**: No parameters required.
- **Response**:
    ```json
    {
        "data": {
            "email": "ik.ugwuanyi@gmail.com",
            "current_datetime": "2023-10-05T14:48:00Z",
            "github_url": "https://github.com/iConnell/hgnX"
        },
        "status_code": 200
    }
    ```

### Example Usage

To get the student information, send a GET request to the `/api` endpoint. You can use `curl` or any API client like Postman.

```sh
curl -X GET "http://127.0.0.1:8000/api"