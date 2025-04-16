- Creer un projet
- Création d'un conteneur dans le dossier du projet :

```
nano Dockerfile
FROM ubuntu
```

- Mettre à jour et installer les dépendances nécessaires dans le docker file (toujours avec **nano**)

```
RUN apt-get update && apt-get install -y \
    nginx \
    python3 python3-pip python3-venv \
    postgresql postgresql-contrib \
    && rm -rf /var/lib/apt/lists/*
```

**nginx**: Un serveur web très performant qui peut servir de:
- Serveur HTTP pour exposer vos applications data science
- Proxy inverse pour rediriger les requêtes vers différentes applications
- Équilibreur de charge si vous déployez plusieurs instances
**python3, python3-pip, python3-venv**: L'écosystème Python essentiel pour la data science
- Python 3: Le langage de programmation
- pip: Gestionnaire de packages Python
- venv: Outil pour créer des environnements virtuels isolés
**postgresql, postgresql-contrib**: Un système de base de données relationnelle puissant
- PostgreSQL: Pour stocker, requêter et analyser vos données structurées
- Les modules contrib: Extensions utiles pour des fonctionnalités avancées


- Créer un user **data-scientist** et un dossier pour les projets:
```
RUN useradd -m -s /bin/bash data_scientist \ && mkdir -p /home/data_scientist/projects \ && chown -R data_scientist:data_scientist /home/data_scientist/projects
```

- Installer les bibliothèques python énoncer dans le sujet:
```
RUN pip3 install --no-cache-dir pandas numpy scikit-learn
```

- Configuration de postgreSQL
```
COPY setup-postgres.sh /usr/local/bin/ 
RUN chmod +x /usr/local/bin/setup-postgres.sh
```

**$COPY setup-postgres.sh /usr/local/bin/**
 - Cette commande copie un fichier nommé `setup-postgres.sh` depuis votre contexte de build (le répertoire où se trouve votre Dockerfile sur votre machine hôte) vers le répertoire `/usr/local/bin/` dans l'image Docker
- `/usr/local/bin/` est un emplacement standard pour les scripts exécutables personnalisés dans les systèmes Linux

**$RUN chmod +x /usr/local/bin/setup-postgres.sh**
- Cette commande modifie les permissions du fichier pour le rendre exécutable
- `chmod +x` ajoute le droit d'exécution au fichier
- Sans cette étape, le script ne pourrait pas être exécuté directement comme une commande