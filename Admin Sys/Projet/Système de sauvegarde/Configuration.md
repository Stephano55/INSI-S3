
- **Commande pour la synchronisation:**
```
rsync -av --delete  "{Dossier contenant les données critiques}" "{Dossier pour envoyer les fichiers à sauvegarder}"
```

- **Création du script pour faire la sauvegarde:**
```
#!/bin/bash

# Date pour les logs
DATE=$(date +%Y-%m-%d_%H-%M)

# Dossiers
SOURCE="{Dossier contenant les données critiques}"
DEST="{Dossier pour envoyer les fichiers à sauvegarder}"
LOGDIR="{Dossier contenant le projet}/Logs"
LOGFILE="$LOGDIR/backup_$DATE.log"

# Créer le dossier de logs s'il n'existe pas
mkdir -p "$LOGDIR"

# Lancer la sauvegarde
rsync -av --delete "$SOURCE" "$DEST" >> "$LOGFILE" 2>&1

```

Il faut rendre le fichier exécutable avec la commande `chmod +x` 

- **Automatisation avec `cron`**:
    - **ouvrir l'éditeur de crontab**: `crontab -e`
    - **Ajouter la ligne:** `*/10 * * * * {chemin vers le script backup}`
        cette ligne veut dire que la synchronisation se fait toutes les **10 minutes**

- **Tester la restauration:**
    Il faut que chaque sauvegarde aille dans un **nouveau dossier daté** à chaque exécution. On peut faire ça avec le script suivant:
```
    #!/bin/bash

# Date/Heure pour la version de sauvegarde
DATE=$(date +%Y-%m-%d_%H-%M)

# Dossiers
SOURCE="{Dossier contenant les données critiques}"
DEST_BASE="{Dossier pour envoyer les fichiers à sauvegarder}"
DEST="$DEST_BASE/$DATE"
LOGDIR="{Dossier contenant le projet}/Logs"
LOGFILE="$LOGDIR/backup_$DATE.log"

# Créer les dossiers si nécessaires
mkdir -p "$DEST"
mkdir -p "$LOGDIR"

# Sauvegarde versionnée
rsync -av "$SOURCE" "$DEST" >> "$LOGFILE" 2>&1

```

