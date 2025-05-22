# About
**Local development setup for Flask and PostgreSQL. It creates fully configured Flask, PostgreSQL and NGINX Docker containers for a seamless development experience.**

❗ It should be used solely for local development, as it is not configured for production (the database has the authentication disabled, Flask is run with local development server etc.).

# Features
**✓ Consistent development environment.**

**✓ Changes of the Flask project files on host machine, are automatically propagated into the cointainer.**

# Prerequisites

**Linux distro / Mac OS with Docker and git installed.**

**Clone repository and change dir to repository root directory:**

``
git clone https://github.com/electro-spark/flask-postgresql-docker-local-dev.git
``

``
cd flask-postgresql-docker-local-dev
``

**Make sure all scripts are set as executable:**

``
chmod u+x ./start.sh ./be_logs.sh ./be_shell.sh ./stop.sh ./clean.sh
``

# Usage

### 🔨 Start application
``
./start.sh
``

or

``
sudo ./start.sh
``
(if Docker is not setup with non-root access).

### 🔨 Access website
Point the browser to `localhost`.

### 🔨 View application container logs
``
./be_logs.sh
``

or

``
sudo ./be_logs.sh
``
(if Docker is not setup with non-root access).

### 🔨 Access application container shell
``
./be_shell.sh
``

or

``
sudo ./be_shell.sh
``
(if Docker is not setup with non-root access).

### 🔨 Stop application
``
./stop.sh
``

or

``
sudo ./stop.sh
``
(if Docker is not setup with non-root access).

### 🔨 Remove all local docker containers and images
``
./clean.sh
``

or

``
sudo ./clean.sh
``
(if Docker is not setup with non-root access).

