FROM python:3.11-slim

WORKDIR /app

COPY web/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
RUN python app/manage.py collectstatic --noinput

COPY . .

ENV PYTHONUNBUFFERED 1

CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:8000"]