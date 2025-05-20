# flask-postgresql-docker-local-dev
Local development setup for Flask and PostgreSQL running in Docker.

It should be used solely for local development, as it is not configured for production (the database has the authentication disabled, Flask is run with local development server etc.).

## 1. Prerequisites
### a) Linux distro / Mac OS with Docker and git installed.

### b) Clone repository and change dir to repository root directory:

``
git clone git@github.com:electro-spark/flask-postgresql-docker-local-dev.git
cd flask-postgresql-docker-local-dev
``

### c) Make sure all scripts are set as executable:

``
chmod u+x ./start.sh ./be_logs.sh ./be_shell.sh ./stop.sh ./clean.sh
``

## 2. Start application
``
./start.sh
``

or

``
sudo ./start.sh
``
(if Docker is not setup with non-root access).

## 3. Access website
Point the browser to `localhost`.

## 4. View application container logs
``
./be_logs.sh
``

or

``
sudo ./be_logs.sh
``
(if Docker is not setup with non-root access).

## 5. Access application container shell
``
./be_shell.sh
``

or

``
sudo ./be_shell.sh
``
(if Docker is not setup with non-root access).

## 6. Stop application
``
./stop.sh
``

or

``
sudo ./stop.sh
``
(if Docker is not setup with non-root access).

## 7. Remove all local Docker images and containers
``
./clean.sh
``

or

``
sudo ./clean.sh
``
(if Docker is not setup with non-root access).

