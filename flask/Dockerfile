FROM python:3.13-alpine AS builder
# Create app directory
WORKDIR /src

# Install app dependencies
COPY Pipfile* ./src

# Bundle app source
COPY . /src

RUN pip install pipenv
RUN pipenv requirements > requirements.txt
RUN pip install -r requirements.txt

# start with flask migrate and then run the server
ENTRYPOINT flask db upgrade && python -m app.app
