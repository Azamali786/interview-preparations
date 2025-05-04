# Use Ubuntu 20.04 as the base image
FROM ubuntu:20.04

# Set environment variables to prevent interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Set the working directory in the container
WORKDIR /app

# Install system dependencies and Python
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    python3-dev \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy the project files into the container
COPY . /app

# Ensure pip is up to date
RUN pip install --upgrade pip

# Install Python dependencies
RUN pip install -r requirements.txt

# Expose port 8000 for Django
EXPOSE 8000

# Copy the .env file
COPY .env /app/.env

# Apply migrations
RUN python3 manage.py makemigrations
RUN python3 manage.py migrate

# Collect static files (for production use)
# RUN python3 manage.py collectstatic --noinput

# Start the Django server
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
