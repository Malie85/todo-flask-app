# To-Do List App

A simple task management (To-Do) web application built using Flask (Python) for the backend and Vanilla JavaScript for the frontend.

---

## Project Structure

```
TODOPROJECT/
├── backend/
│   └── app.py
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── scripts.js
├── instance/
├── README.md
└── LICENSE
```

---

## Technologies Used

- Python (Flask)
- SQLite (via SQLAlchemy)
- HTML & CSS
- JavaScript (Vanilla JS)
- Flask-CORS (for frontend-backend communication)

---

## How to Run

1. Navigate to the backend folder:
   ```bash
   cd backend
   ```

2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install flask flask_sqlalchemy flask_cors
   ```

4. Run the Flask server:
   ```bash
   python app.py
   ```

5. Open `frontend/index.html` in your browser to view the app.

---

## API Endpoints

- `GET /tasks` – Fetch all tasks
- `POST /tasks` – Add a new task (JSON: `{ "text": "task content" }`)
- `DELETE /tasks/<id>` – Delete a task by ID

---

## Author

**Mohammad Ali Eftekhari**  
This project was created as a portfolio piece and learning project for Python, Flask, and JavaScript.

---

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.
