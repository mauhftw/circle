FROM python:2.7
WORKDIR /app
COPY app /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
