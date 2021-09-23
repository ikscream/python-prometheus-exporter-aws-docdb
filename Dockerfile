FROM python:3-alpine3.9

COPY . .
RUN pip install -r requriments.txt

ENV PORT=5000
ENV DOCDB_HOST=example.com
ENV DOCDB_PASSWORD=password

CMD ["python", "main.py"]