# REST API Automation Framework (User Management) 🔌

## 📌 Project Overview
This project is a modular automation framework designed to validate **User Management APIs**. It uses **Python Requests** and **Pytest** to perform CRUD operations (Create, Read, Update, Delete), ensuring data accuracy and contract reliability through **JSON Schema Validation**.

## 🛠 Tech Stack
* **Language:** Python
* **Libraries:** `requests`, `pytest`, `jsonschema`
* **Architecture:** Modular framework with reusable `api_client` wrappers.
* **Validation:** Status codes, Response body assertions, and Schema compliance.

## 🧪 Test Scenarios Covered
| Operation | HTTP Method | Test Description | Assertion |
| :--- | :--- | :--- | :--- |
| **Create User** | POST | Verify user creation with valid payload. | Status 201 + ID generation |
| **Get User** | GET | Retrieve user details by ID. | Status 200 + Data Match |
| **Update User** | PUT/PATCH | Modify existing user data. | Status 200 + Field Update |
| **Delete User** | DELETE | Remove user from system. | Status 204 + 404 on retry |
| **Schema Check** | N/A | Validate response structure against JSON schema. | Schema Compliance |

## 🚀 How to Run
1. Clone the repository:
   ```bash
   git clone [https://github.com/ReemasFury/Rest-API-Testing-Framework.git](https://github.com/ReemasFury/Rest-API-Testing-Framework.git)

2. Install dependancies:
   ```
   pip install requests pytest jsonschema

3. Run the Test Suite:
   ```
   pytest tests/ -v
