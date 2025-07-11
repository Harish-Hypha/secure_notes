FROM python:3.10-slim-buster
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
ENV FLASK_APP=app/main.py
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080", debut=True]
