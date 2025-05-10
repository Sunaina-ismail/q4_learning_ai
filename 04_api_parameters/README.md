# 🚀 FastAPI Item Management API
# Author: Sunaina Ismail

This project is a simple demonstration of **FastAPI**, showcasing how to work with various parameter types including **Path**, **Query**, and **Body** parameters.

---

## 🌐 About FastAPI

**FastAPI** is a modern and high-performance web framework for building APIs with Python. It is built on top of Starlette (for web parts) and Pydantic (for data validation). FastAPI is known for:

- Fast execution and high performance
- Automatic generation of API docs (Swagger & ReDoc)
- Built-in validation using Python type hints
- Asynchronous support using `async/await`

---

## 📌 Purpose of This API

This API lets users perform actions like:

- Adding new items
- Updating existing items with query and body data
- Searching for items using filters

It is mainly designed to demonstrate how FastAPI handles different types of inputs and validations.

---

## 📥 Parameter Types in FastAPI

FastAPI provides several ways to declare and validate parameters in your API endpoints:

- **Path Parameters**  
  Parts of the URL path that are variable.  
  Example: `/items/{item_id}`

- **Query Parameters**  
  Parameters appended to the URL after a `?`.  
  Example: `/items?skip=0&limit=10`

- **Request Body**  
  Data sent in the body of the request, usually in JSON format. Used for structured data (e.g., with Pydantic models).

- **Headers**  
  Custom HTTP headers sent with the request.  
  Example: `X-Token: mytoken123`

- **Cookies**  
  Data sent in the `Cookie` header, often used for session tracking or user preferences.

- **Form Data**  
  Fields submitted via a web form using `application/x-www-form-urlencoded` or `multipart/form-data`.

- **File Uploads**  
  Used for uploading files via form submissions. FastAPI handles file parsing and provides access to file content.

---

## 📖 API Documentation

Once the FastAPI server is running, you can view the interactive API documentation:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

---

## ✅ Summary

This FastAPI project demonstrates:

- Use of `Path`, `Query`, and `Body` parameters
- Validation using Python type hints
- Interactive API testing through auto-generated docs

It serves as a great starting point for beginners learning how to build modern APIs using FastAPI.
