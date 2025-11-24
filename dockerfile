FROM python:3.9.18-slim

# Set working directory
WORKDIR /app

# Install system dependencies (if needed for Pillow)
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Create a non-root user (optional but recommended)
RUN useradd -m -r botuser && chown -R botuser /app
USER botuser

# Start the bot
CMD ["python", "main.py"]
