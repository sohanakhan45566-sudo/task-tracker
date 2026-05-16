FROM python:3.9-slim
WORKDIR /app
COPY task.py .
CMD ["python", "task.py"]