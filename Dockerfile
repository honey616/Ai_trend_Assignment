# Use official lightweight Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy all files from local project directory to /app in container
COPY . /app

# Run the Python app
CMD ["python", "app/main.py"]
