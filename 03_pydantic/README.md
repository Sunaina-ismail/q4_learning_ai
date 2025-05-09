# 📘 Pydantic Validation Project

## 🔍 What is Pydantic?

Pydantic is a powerful Python library used for **data validation and settings management** using Python type annotations. It helps ensure that the data you’re working with is structured correctly and meets specific requirements — without writing a lot of manual validation code.

---

## 💡 Why Use Pydantic?

Pydantic is widely used because:

- ✅ It automatically checks if the data matches the expected types (like strings, integers, emails, etc.).
- ⚙️ It supports complex data structures such as nested models and lists.
- 📧 It provides built-in validators for common data types like `EmailStr`.
- 📏 You can write custom validators to enforce specific rules (like name must be at least 2 characters).
- 🛡️ It improves code quality and prevents bugs caused by bad input.

---

## 🧠 What I Did in This Project

This project showcases my understanding of Pydantic through several examples:

- I created data models for users and students using `BaseModel`.
- I added email validation using `EmailStr`.
- I built nested models, such as a user with multiple addresses.
- I implemented custom validation to make sure names are not too short.
- I handled errors using `ValidationError` to catch and display validation issues.
- I used real-world data formats like common email domains to keep the examples realistic.
- I explored both required and optional fields to understand flexibility in data models.

---

## 🎯 Purpose of This Work

This work helped me:

- Learn how to validate structured data in Python.
- Understand the importance of clean and safe data for building applications.
- Practice writing user-friendly error messages.
- Prepare for real-world projects involving data input, APIs, or database interaction.

---

## 🙌 Author

**Sunaina Ismail**  
Completed as part of my Quarter 4 learning journey under the Governor’s Initiative in IT at the Governor House, Karachi.

