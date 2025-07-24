# Use a lightweight Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy the dependency file
COPY requirements.txt .

# Install dependencies including gunicorn
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code
COPY . .

# Set environment variables
ENV FLASK_APP=app:app
ENV CONFIG_MODULE=config.local
ENV FLASK_ENV=production

# Expose port
EXPOSE 5000

# Run production server
CMD sh -c 'gunicorn --bind 0.0.0.0:${PORT:-5000} --workers 4 --log-level info app:app'

