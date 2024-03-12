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

COPY ./tracker donation-tracker
COPY --from=client /app/tracker/ donation-tracker

RUN pip install ./donation-tracker

RUN pip install django~=5.0
#RUN pip install daphne

COPY ./settings.py ./wsgi.py ./asgi.py ./manage.py ./local_statics.py ./routing.py ./urls.py /app/
COPY ./entrypoint.sh ./

RUN mkdir -p /var/www/html/static
RUN python manage.py collectstatic --noinput

#RUN ["python", "manage.py", "migrate"]
#RUN ["python", "manage.py", "loaddata", "blank.json"]

#ARG superusername=admin
#ARG superuserpassword=password

#RUN python manage.py createsuperuser --noinput --email nobody@example.com --username ${superusername}
#RUN yes ${superuserpassword} | python manage.py changepassword ${superusername}

ENTRYPOINT ./entrypoint.sh

