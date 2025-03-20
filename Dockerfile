FROM node:20-alpine AS client

WORKDIR /app

COPY ./tracker/package.json ./tracker/yarn.lock \
  ./tracker/.browserslistrc \
  ./tracker/karma.conf.js \
  ./tracker/declarations.d.ts \
  ./tracker/postcss.config.js \
  ./tracker/prettier.config.js \
  ./tracker/tsconfig.json \
  ./tracker/.yarnrc.yml \
  ./tracker/webpack.config.js \
  ./
COPY ./tracker/bundles bundles
COPY ./tracker/design design
COPY ./tracker/tracker tracker
COPY ./tracker/.yarn .yarn

RUN corepack enable && \
    yarn install && \
    yarn build

FROM python:3.12

WORKDIR /app

RUN pip install django~=5.0
RUN django-admin startproject tracker_development

WORKDIR /app/tracker_development/donation-tracker

COPY \
  ./tracker/__init__.py \
  ./tracker/.flake8 \
  ./tracker/pyproject.toml \
  ./tracker/README.md \
  ./tracker/setup.py \
  ./tracker/.browserslistrc \
  ./tracker/karma.conf.js \
  ./tracker/declarations.d.ts \
  ./tracker/postcss.config.js \
  ./tracker/prettier.config.js \
  ./tracker/tsconfig.json \
  ./tracker/.yarnrc.yml \
  ./tracker/package.json \
  ./tracker/yarn.lock \
  ./tracker/webpack.config.js \
  ./
COPY ./tracker/bundles bundles
COPY ./tracker/design design
COPY ./tracker/.yarn .yarn

COPY --from=client /app/tracker/ tracker
COPY ./tracker/tracker tracker
COPY ./tracker/setup.py ./
RUN pip install daphne
# We need edit mode for some reason, or the templates don't get compiled in properly
# Likely something about this setup but at least it works
RUN pip install -e .

WORKDIR /app/tracker_development
COPY ./settings.py ./wsgi.py ./asgi.py ./local_statics.py ./routing.py ./urls.py /app/tracker_development/tracker_development/
COPY ./entrypoint.sh ./

RUN mkdir db && \
    apt update && \
    apt install -y locales && \
    echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen &&  \
    echo "en_GB.UTF-8 UTF-8" >> /etc/locale.gen && \
    echo "nl_NL.UTF-8 UTF-8" >> /etc/locale.gen && \
    locale-gen en_US.UTF-8 && \
    locale-gen en_GB.UTF-8 && \
    locale-gen nl_NL.UTF-8
#ENV LC_ALL en_US.UTF-8
ENV LC_ALL nl_NL.UTF-8

RUN mkdir -p /var/www/html/static && \
    python manage.py collectstatic --noinput

COPY ./fonts /var/www/html/fonts

#RUN ["python", "manage.py", "migrate"]
#RUN ["python", "manage.py", "loaddata", "blank.json"]

#ARG superusername=admin
#ARG superuserpassword=password

#RUN python manage.py createsuperuser --noinput --email nobody@example.com --username ${superusername}
#RUN yes ${superuserpassword} | python manage.py changepassword ${superusername}

ENTRYPOINT ./entrypoint.sh
