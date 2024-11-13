# URL Shortener Service

A lightweight URL shortener service built with Python and Aiohttp. This service provides endpoints for creating, retrieving, and managing shortened URLs, backed by a PostgreSQL database using SQLAlchemy.

## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Service](#running-the-service)
- [API Endpoints](#api-endpoints)
  - [Create Short URL](#create-short-url)
  - [Redirect to Original URL](#redirect-to-original-url)
  - [Get URL Statistics](#get-url-statistics)
  - [Delete Short URL](#delete-short-url)

## Requirements

- Python 3.8+
- PostgreSQL
- Aiohttp
- SQLAlchemy

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/url-shortener.git
   cd url-shortener
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up the database**:
   Create a PostgreSQL database and update the database settings in `misc/env.py`.

## Configuration

Make sure your database configuration in `misc/env.py` includes:
```python
DB_USER = "your_db_user"
DB_PASS = "your_db_password"
DB_HOST = "localhost"
DB_PORT = 5432
DB_NAME = "url_shortener"
```

## Running the Service

To start the web server, use:

```bash
python main.py
```

This will run the server on the configured host and port (e.g., `http://localhost:8082`).

## API Endpoints

### 1. Create Short URL

**Endpoint**: `/shorten`  
**Method**: `POST`

**Request Body**:
```json
{
  "original_url": "https://example.com"
}
```

**Response**:
```json
{
  "short_code": "abc123"
}
```

**Example**:
```bash
curl -X POST http://localhost:8082/shorten -H "Content-Type: application/json" -d '{"original_url": "https://example.com"}'
```

### 2. Redirect to Original URL

**Endpoint**: `/{short_code}`  
**Method**: `GET`

Redirects the user to the original URL.

**Example**:
```bash
curl -X GET http://localhost:8082/abc123
```

### 3. Get URL Statistics

**Endpoint**: `/stats/{short_code}`  
**Method**: `GET`

Provides statistics for a specific short code, including the number of clicks.

**Response**:
```json
{
  "original_url": "https://example.com",
  "clicks": 5,
  "created_at": "2023-01-01T12:00:00"
}
```

**Example**:
```bash
curl -X GET http://localhost:8082/stats/abc123
```

### 4. Delete Short URL

**Endpoint**: `/delete/{short_code}`  
**Method**: `GET`

Deletes the specified short URL.

**Example**:
```bash
curl -X GET http://localhost:8082/delete/abc123
```

## Testing and Development

You can test the API endpoints using `curl`, Postman, or any other HTTP client. Make sure the database is running and configured correctly.

## License

This project is licensed under the MIT License.

## Contributing

Feel free to submit issues, fork the repository, and open pull requests to contribute to the project.

---
