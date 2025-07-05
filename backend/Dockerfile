# Base image
FROM python:3.10-slim

# Install system dependencies for LaTeX and PDF generation
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       texlive-latex-base \
       build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /app

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/ ./app/

# Expose port
EXPOSE 8000

# Command to run
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]