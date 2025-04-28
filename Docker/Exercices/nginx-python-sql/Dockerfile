FROM ubuntu:latest

#installation des dépendances nécessaires
RUN apt-get update && \
    apt-get install -y nginx && \
    apt-get install -y python3 && \
    apt-get install -y python3-pip && \
    apt-get install -y postgresql

#création de l'utilisateur data_scientist
RUN useradd -ms /bin/bash data_scientist  && \
    echo "data_scientist ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

#Installation des bibliothèques python
RUN python3 -m venv /env
RUN /env/bin/pip install pandas numpy scikit-learn matplotlib seaborn jupyter


#configuration de posgresql
USER postgres
RUN /etc/init.d/postgresql start && \
    psql --command "CREATE USER data_scientist WITH SUPERUSER PASSWORD 'password';" && \
    createdb datasci_db
USER root

#Ajout de la configuration du serveur
COPY nginx.conf /etc/nginx/nginx.conf

#script d'initialisation de base de donné
COPY int_db.sql /docker-entrypoint-initdb.d/int_db.sql

#Autoriser l'accée au dossier travail
RUN chown -R data_scientist:data_scientist /var/www/html

#script au démarage
COPY start.sh /start.sh
RUN chmod +x start.sh

EXPOSE 80 5432

CMD ["/start.sh"]