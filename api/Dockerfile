FROM python:3.8.1
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD sh -c "python3 -m api.app"