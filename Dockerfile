FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY youtube_api_script.py .

CMD ["python", "youtube_api_script.py"]