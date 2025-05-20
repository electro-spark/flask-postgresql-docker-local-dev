#!/bin/bash
docker logs $(docker ps -q -f ancestor=flask-dbg-backend)
