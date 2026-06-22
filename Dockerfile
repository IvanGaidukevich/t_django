FROM python:3.12-slim

WORKDIR /my_store

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["gunicorn", "my_store.my_store.wsgi:application", "--bind", "0.0.0.0:8000"]