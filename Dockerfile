# # Use official Python image
# FROM python:3.10-slim

# # Set working directory
# WORKDIR /app

# # Copy requirement files
# COPY requirements.txt .

# # Install dependencies
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy project code
# COPY . .

# # Expose FastAPI port
# EXPOSE 8000

# # Start FastAPI server
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]



FROM python:3.10-slim

# Install dependencies needed for cryptography
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
