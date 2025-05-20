# flask-postgresql-docker-local-dev
Local development setup for Flask and PostgreSQL running in Docker.

It should be used solely for local development, as it is not configured for production (the database has the authentication disabled, Flask is run with local development server etc.).

### 1. PREREQUISITES

**Linux distro / Mac OS with Docker and git installed.**

**Clone repository and change dir to repository root directory:**

``
git clone git@github.com:electro-spark/flask-postgresql-docker-local-dev.git
``

``
cd flask-postgresql-docker-local-dev
``

**Make sure all scripts are set as executable:**

``
chmod u+x ./start.sh ./be_logs.sh ./be_shell.sh ./stop.sh ./clean.sh
``

### 2. START APPLICATION
``
./start.sh
``

or

``
sudo ./start.sh
``
(if Docker is not setup with non-root access).

### 3. ACCESS WEBSITE
Point the browser to `localhost`.

### 4. VIEW APPLICATION CONTAINER LOGS
``
./be_logs.sh
``

or

``
sudo ./be_logs.sh
``
(if Docker is not setup with non-root access).

### 5. ACCESS APPLICATION CONTAINER SHELL
``
./be_shell.sh
``

or

``
sudo ./be_shell.sh
``
(if Docker is not setup with non-root access).

### 6. STOP APPLICATION
``
./stop.sh
``

or

``
sudo ./stop.sh
``
(if Docker is not setup with non-root access).

### 7. REMOVE ALL LOCAL DOCKER CONTAINERS AND IMAGES
``
./clean.sh
``

or

``
sudo ./clean.sh
``
(if Docker is not setup with non-root access).

