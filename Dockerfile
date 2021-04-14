FROM python:3.7

WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 80

ENTRYPOINT [ "python" ]

CMD ["app.py", "run", "-h", "0.0.0.0", "-p", "80"]
