FROM python:3.8-alpine
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN python -m smtpd -c DebuggingServer -n localhost:1025 &
CMD ["python", "run_tests.py"]

