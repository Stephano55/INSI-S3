
## Syntaxe Dockerfile

- **FROM**:
    Cette instruction définit l'image de base pour le processus de construction de notre image personnalisée. Cette image de base sera ensuite utiliser par touts les autres instructions.

- **COPY**:
    Permet de copier un fichier entre la machine hôte et le système de fichier de l'image docker. La syntaxe est la suivante:
    `COPY {source} {destination}`

- **ADD**:
    Cette instruction a le même comportement que **COPY** mais elle permet aussi de copier un fichier à partir d'une URL

- **RUN**:
    Elle permet d'exécuter n'importe quelle commande dans l'image. La commande fournie via **RUN** est exécuter pendant la construction de l'image. La syntaxe est la suivante:
    `RUN {commande}`
    Il est recommandé de regrouper toutes les commandes dans une seule instruction **RUN**:
```
     RUN apt-get update && \
         apt-get install -y wget && \
         apt-get clean
```

- **ENV**:
    Elle définit une nouvelle variable d'environnement dans l'image. Une variable d'environnement est une paire clé-valeur, accessible depuis n'importe quel script ou application. La syntaxe est la suivante:
    `ENV {clé} {valeur}`
    - `{clé}`: représente la variable d'environnement qui sera définie
    - `{valeur}`: représente la valeur qui sera attribuée à la variable d'environnement

- **VOLUME**:
    Permet de créer un répertoire dans le système de fichier de l'image. Il peut ensuite être utiliser pour monter des volumes à partir de l'hôte docker ou dans les autres containers.
    La syntaxe est la suivante: `VOLUME ["{point de montage}"]`

- **EXPOSE**:
    Permet d'ouvrir un port réseau de container pour la communication entre le container et le monde extérieur. La syntaxe est la suivante: `EXPOSE {port}`

- **CMD**:
    Fait la même chose que **RUN** mais à la différence de celle-ci, **CMD** exécute les commandes fournies que lorsque le container est lancé.