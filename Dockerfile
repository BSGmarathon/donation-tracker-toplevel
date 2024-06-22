FROM node:18 AS client

WORKDIR /app

COPY ./tracker/package.json ./tracker/yarn.lock ./
RUN yarn

COPY \
  ./tracker/.browserslistrc \
  ./tracker/karma.conf.js \
  ./tracker/declarations.d.ts \
  ./tracker/postcss.config.js \
  ./tracker/webpack.config.js \
  ./
COPY ./tracker/bundles bundles
COPY ./tracker/design design
COPY ./tracker/tracker tracker

RUN yarn build

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
  ./

COPY --from=client /app/tracker/ tracker
COPY ./tracker/tracker tracker
COPY ./tracker/setup.py ./
RUN pip install -e .
RUN pip install daphne
#RUN pip install gunicorn

WORKDIR /app/tracker_development
COPY ./settings.py ./wsgi.py ./asgi.py ./local_statics.py ./routing.py ./urls.py /app/tracker_development/tracker_development/
COPY ./entrypoint.sh ./
RUN mkdir db

#RUN pip install ../donation-tracker

RUN apt update
RUN apt install -y locales
RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen
RUN echo "en_GB.UTF-8 UTF-8" >> /etc/locale.gen
RUN echo "nl_NL.UTF-8 UTF-8" >> /etc/locale.gen
RUN locale-gen en_US.UTF-8
RUN locale-gen en_GB.UTF-8
RUN locale-gen nl_NL.UTF-8
#ENV LC_ALL en_US.UTF-8
ENV LC_ALL nl_NL.UTF-8

RUN mkdir -p /var/www/html/static
RUN python manage.py collectstatic --noinput

#RUN ["python", "manage.py", "migrate"]
#RUN ["python", "manage.py", "loaddata", "blank.json"]

#ARG superusername=admin
#ARG superuserpassword=password

#RUN python manage.py createsuperuser --noinput --email nobody@example.com --username ${superusername}
#RUN yes ${superuserpassword} | python manage.py changepassword ${superusername}

ENTRYPOINT ./entrypoint.sh
