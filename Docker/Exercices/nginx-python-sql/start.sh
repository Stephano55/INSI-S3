#!/bin/bash

# Démarrer PostgreSQL
service postgresql start

# Démarrer nginx
service nginx start

# Garder le conteneur vivant
tail -f /dev/null
