FROM python:3.8.10-slim as dock_challenge_api
WORKDIR /app
COPY . /app
RUN pip3 install -r requirements.txt
CMD sh -c "python3 -m api.app"
