FROM python:3.9-alpine

WORKDIR /app

COPY requirements.txt requirements.txt

# Atualizar pip
RUN pip install --upgrade pip

# Instalar dependências do sistema e do PostgreSQL
RUN apk add --no-cache build-base libpq postgresql-dev

# Instalar dependências do Python
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]
