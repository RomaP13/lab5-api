# Модель: Метод Ньютона (5 семестр)
# Автор: Помазан Роман, група АІ-233

FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .

EXPOSE 5000

CMD ["python", "main.py"]
