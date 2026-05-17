# 📝 Task Tracker App

A simple task management application with both **CLI** and **Web** interface. Containerized with Docker for easy deployment.

# Screenshot
![web-app](https://github.com/sohanakhan45566-sudo/task-tracker/blob/main/images/web-app.png.png?raw=true)

## 🚀 Features

- ✅ Add, list, complete, and delete tasks
- 🖥️ Terminal (CLI) interface
- 🌐 Web interface (Flask)
- 🐳 Docker containerization
- 💾 Persistent storage (tasks.json)

## 🛠️ Technologies

- Python 3.9
- Flask (Web version)
- Docker

## 📋 How to Run

### CLI Version (Terminal)

```bash
# Build image
docker build -t task-tracker .

# Run container
docker run -it task-tracker
