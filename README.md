# donation-tracker-toplevel

This is the top level of my fork of the GamesDoneQuick donation tracker.  

In order to deploy the tracker, some boilerplate code is neccessary for configuration and management. The goal of this repository is to make doing so as simple as possible for any given user to get started developing on the tracker.

## Getting a Working Copy of the Tracker

Docker images are available at [Docker Hub](https://hub.docker.com/esamarathon/tracker).
Any other method of running this software is heavily discouraged due to the insane rabbit hole python and django web-development is.
If you want to spend a couple hours getting the correct version of python, pip, django and gunicorn (or your wsgi server of choice) installed and setup in one of the several virtual environment solutions recommended by the community, go ahead. No support will be given for this, you are on your own.

## Getting a development version of the Tracker

1. [Install Git](http://www.git-scm.com/download). I'm assuming if you're here, you know enough about git and version control to get started. You can check if you have git with the command `which git`, and which version you have with `git --version`.
1. [Install Docker](https://www.docker.com/get-started). This version of the tracker requires Docker and Docker-compose.
1. Clone this repository, typically I put it in a folder called `donation-tracker-toplevel`, which is the path to which this repo will be referred for the remainder of these instructions:
    ```> git clone https://github.com/esamarathon/donation-tracker-toplevel.git``` or
    ```> git clone git@github.com:esamarathon/donation-tracker-toplevel.git``` if you prefer ssh.
1. Make a copy of `example_local.py` under `donations`, and call it `local.py`. This is where you will enter any deployment-specific settings for your instance of the website.
    ```> cp example_local.py local.py```
    1. (optional) Change the `NAME` field under the `DATABASES` variable to point at a different location if you wish.
    2. There are some other config variables related to timezone, e-mail, google docs, and giantbomb's API. None of these are neccessary to get started, and mostly can be ignored unless you are interested in that specific feature. Documentation on these fields is lacking, but it shouldn't be too diffficult to figure out how they work if you take a look at `settings.py`.
1. Clone the submodules.
    ```> git submodule update --init```
    1. This will clone `tracker` (the main backend and the classic frontend), `tracker_ui` (the fancy new experimental Javascript UI).
1. Build and start the docker containers.
```> docker-compose up --build```
This will first pull and build the necessary docker images, and then run them.
The "app" container is the actual tracker and will start by collecting static files, apply any missing migrations from the database and then launch the django built-in webserver as well as listening for updates to the static files to recollect them.
The code, including templates are all watched by the built-in server and will reload any updates made to the files.
1. Open a browser of your choice and go to [http://localhost:8080](http://localhost:8080) to see teh tracker.


## Server deployment

Use Docker. You can use the provided docker-compose.yml file as a template for your own setup.
Just change from the development image to any other to use a version built with a real wsgi server (Gunicorn) for better performance.
But you could probably get away with the development image if the load is small.


## Docker images

Typically there are three classes of images used in the project.

```
esamarathon/tracker:latest
esamarathon/tracker:production
```
Production builds. This is the recommended builds if you want to deploy a tracker instance for general use.
Build with `Dockerfile-production`.

```
esamarathon/tracker:development
```
are for development builds. It uses the regular `Dockerfile` for building and is recommended for developers working on the project.

```
esamarathon/tracker-statics:latest
```
Nginx webserver with the results of collectstatic stored in `/var/www/html/static/`
Useful for simple production setups to serve the tracker static files, such as stylesheets and images.
Build with `Dockerfile-statics`.
