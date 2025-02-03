# Use a compatible Python version
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Upgrade pip before installing dependencies
RUN pip install --upgrade pip

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000
EXPOSE 8000

# Run Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
