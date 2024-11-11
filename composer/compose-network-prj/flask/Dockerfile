FROM python:3

RUN pip install Flask requests Flask-MySQLdb

WORKDIR /app

COPY . .

EXPOSE 5000

CMD ["python3", "./app.py"]