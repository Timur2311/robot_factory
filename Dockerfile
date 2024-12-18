# Base image
FROM python:3.12

# Set the working directory
WORKDIR /app


# Copy the .env file into the Docker image
COPY .env /app/.env

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose the port for Django
EXPOSE 8000

# Default command to run the server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
