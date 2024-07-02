FROM python:latest

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY models /app/models
COPY house_pricing.py deploy.py ./

CMD ["python", "deploy.py"]