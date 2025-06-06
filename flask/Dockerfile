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

ENTRYPOINT flask db upgrade && python -m app.app
# CMD ["python", "-m", "app.app"]

# FROM builder AS dev-envs

# RUN <<EOF
# apk update
# apk add git
# EOF

# RUN <<EOF
# addgroup -S docker
# adduser -S --shell /bin/bash --ingroup docker vscode
# EOF

# # install Docker tools (cli, buildx, compose)
# COPY --from=gloursdocker/docker / /

# CMD ["python", "-m", "app.app"]
