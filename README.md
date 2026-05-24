## What I've Built & Learned (So Far)

- **CRUD Operations:** Coded complete `GET`, `POST`, `PUT`, and `DELETE` routes to manage data dynamically without an external database (using isolated Python structures).
- **Data Validation (Pydantic):** Implemented strict data schemas using `BaseModel` to validate client requests.
- **Error Handling:** Integrated `HTTPException` and explicit status codes (`201 Created`, `204 No Content`, `404 Not Found`) to prevent server crashes on edge cases.

## Tech Stack
- **Language:** Python
- **Framework:** FastAPI
- **Server:** Uvicorn (ASGI)
- **Validation:** Pydantic

---

## How to Run This Locally

Follow these steps to set up and run the backend on your local machine.

---

### 1. Clone the Repository

```bash
git clone https://github.com/mihirkamat03/FastAPI-Backend.git
cd FastAPI-Backend
```

---

### 2. Create & Activate Virtual Environment

#### Windows
```bash
python -m venv venv
.\venv\Scripts\activate
```

#### macOS / Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install fastapi "uvicorn[standard]"
```

---

### 4. Run the Development Server

```bash
uvicorn main:app --reload
```
