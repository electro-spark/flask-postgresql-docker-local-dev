#!/bin/bash
docker exec -it $(docker ps -q -f ancestor=flask-dbg-backend) sh
