FROM python:alpine
RUN pip install beautifulsoup4
RUN pip install colorama
WORKDIR /app
COPY . /app
ENTRYPOINT ["python3", "main.py"]
