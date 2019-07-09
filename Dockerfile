FROM python:3.7-alpine
WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY mythx_test.py ./
CMD ["python", "mythx_test.py"]
