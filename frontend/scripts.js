// function for show tasks
async function loadTasks() {
    const response = await fetch('http://localhost:5000/tasks');
    const tasks = await response.json();
    const taskList = document.getElementById('taskList');
    taskList.innerHTML = tasks.map(task => 
       ` <li>
            <span>${task.text}</span>
            <button onclick="deleteTask(${task.id})">❌ Delete</button>
        </li> `
    ).join('');
}

// adding tasks function
async function addTask() {
    const input = document.getElementById('taskInput');
    const text = input.value.trim();
    
    if (text) {
        await fetch('http://localhost:5000/tasks', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ text })
        });
        input.value = '';
        loadTasks();
    }
}

// deleting tasks function
async function deleteTask(id) {
    await fetch(`http://localhost:5000/tasks/${id}`, { method: 'DELETE' });
    loadTasks();
}

// initial loading of tasks
loadTasks();