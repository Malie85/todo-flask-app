from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


app = Flask(__name__)
CORS(app)  # allow access from the frontend

# database setting
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../backend/tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Task model for database
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200), nullable=False)
    done = db.Column(db.Boolean, default=False)

# creating tables
with app.app_context():
    db.create_all()

# APIs
@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([{"id": task.id, "text": task.text, "done": task.done} for task in tasks])

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.json
    new_task = Task(text=data['text'], done=False)
    db.session.add(new_task)
    db.session.commit()
    return jsonify({"message": "Task added!", "id": new_task.id}), 201

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get(task_id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Task deleted!"})

if __name__ == '__main__':
    app.run(debug=True)