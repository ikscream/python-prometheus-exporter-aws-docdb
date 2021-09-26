FROM python:3-alpine3.9

COPY requriments.txt requriments.txt
RUN pip install -r requriments.txt

COPY . .

ENV PORT=5000
ENV DOCDB_HOST=example.com
ENV DOCDB_PASSWORD=password
ENV DOCDB_TLS=1

CMD ["python", "main.py"]