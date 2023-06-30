FROM python:3.11
RUN apt-get update && apt-get install -y \
		gcc \
		gettext \
		default-mysql-client \
		default-libmysqlclient-dev \
		postgresql-client libpq-dev \
		sqlite3 \
		locales-all \
	--no-install-recommends && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /usr/src/app/tracker /usr/src/app/db
# COPY tracker/requirements.txt /usr/src/app/tracker/

COPY entrypoint.sh /usr/src/app/
COPY *.py *.json /usr/src/app/
COPY tracker/ /usr/src/app/tracker/
#RUN (cd /usr/src/app && pip install --no-cache-dir -e ./tracker)

#RUN python -m pip install watchdog[watchmedo]

WORKDIR /usr/src/app

RUN pip install --no-cache-dir -e ./tracker

#RUN ["python", "manage.py", "migrate"]
#RUN ["python", "manage.py", "loaddata", "blank.json"]

#ARG superusername=admin
#ARG superuserpassword=password

#RUN python manage.py createsuperuser --noinput --email nobody@example.com --username ${superusername}
#RUN yes ${superuserpassword} | python manage.py changepassword ${superusername}

EXPOSE 8000
CMD ./entrypoint.sh
