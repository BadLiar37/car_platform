FROM python:3.10-slim

RUN pip install pipenv

WORKDIR /django

COPY . .

ENV PYTHONUNBUFFERED=1

RUN pipenv install --system --dev

CMD ["python3", "/django/src/manage.py", "runserver", "0.0.0.0:8000"]
