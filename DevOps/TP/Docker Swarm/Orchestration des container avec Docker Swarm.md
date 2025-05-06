Pour configurer un **Swarm**, il faut :
- **Demarer plusieurs hôtes Docker**
- **Désigner un hôte en tant que manager**:
	`docker swarm init --advertise-addr {addresse IP}`
- **Désigner les autres hôtes en tant que Worker:**
	`docker swarm join --token {token}`
- **Création d'un service**:
	On execute la commande `docker service` dans le **Manager**
	**exemple**: `docker service create --name foo alpine ping 8.8.8.8`
		- **create**: création du service
		- **--name**: pour spécifier le nom du service
		- **alpine**: image utiliser pour le container
		- **ping 8.8.8.8**: commande à exécuter quand le container est lancé