FROM python:alpine
RUN pip install beautifulsoup4
RUN pip install colorama
RUN pip install openai 
WORKDIR /app
COPY . /app
ENTRYPOINT ["python3", "main.py"]
CMD ["Api_Key"]
