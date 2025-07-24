# Use a lightweight Python image
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=app:app
ENV CONFIG_MODULE=config.local
ENV FLASK_ENV=production

EXPOSE 5000

CMD sh -c 'gunicorn --bind 0.0.0.0:${PORT:-5000} --workers 4 --log-level info app:app'
