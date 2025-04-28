### Traduction de l'adresse IP en binaire :
---
La question qui se pose est comment calculer l'adresse IP du réseau qui contient l'adresse  **192.168.1.1/24**  

> [!/] Title
> /24 : annotation CIDR = 255.255.255.0

**1 octet = 8 bits**  ==Izay manome anazy no atao 1==

|                   | 2⁷  | 2⁶  | 2⁵  | 2⁴  | 2³  | 2²  | 2¹  | 2⁰  |
| ----------------- | --- | --- | --- | --- | --- | --- | --- | --- |
|                   | 128 | 64  | 32  | 16  | 8   | 4   | 2   | 1   |
| **192 en base 2** | 1   | 1   | 0   | 0   | 0   | 0   | 0   | 0   |
| **168 en base 2** | 1   | 0   | 1   | 0   | 1   | 0   | 0   | 0   |
| **1 en base 2**   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 1   |

```
192.168.1.1 = 11000000.10101000.00000001.00000001
```

```
255.255.255.0 = 11111111.11111111.11111111.00000000
```

0n additione les 2 adresse en **base 2** et ça donne :

```
11000000.10101000.00000001.00000000 = 192.168.1.0 (adresse reseaux)
```

- La question suivante qui se pose est que comment savoir combien d'autre machine est disponible sur ce réseau :

   2⁸ = 256                            256 - 2 = 254 machine disponible sur le reseaux


> [!Pourquoi -2] Pourquoi -2 ?
> -  adresse de diffusion
> - adresse du reseau


> [!NOTE] Pourquoi 2⁸ ?
> 8 ny isan'ny derniers "zéro" amle adresse ny masque en base 2




[^1]

[^1]: On a toujours besoin d'un masque de reseau pour determiner le nombre d'hôte disponible dans le réseau


---

### Gestion  réseau en ligne de commande sous linux

- Afficher toutes les interfaces réseaux et leurs informations. Cette commande est basée sur le paquet **iproute2**
```
ip a
```

- C'est un outil de configuration réseau positionné au dessus des gestionnaires de configuration réseaux **Systemd-network** et **network-manager**
```
netplan
```

**exemple**: `netplan status --all`   cette commande affiche la configuration détaillée de toute les interfaces, les adresses mac, et également les routes

- Pour afficher et modifier la table de routage sur linux et afficher l'itinéraire par défaut
```
ip route
```
**exemple** : `ip route show` affiche les routes en cours d'utilisation, notamment la passerelle par défaut et les itinéraires spécifique définie sur le système.
Pour définir une nouvelle passerelle par défaut sur l'adresse IP **192.168.1.2**, on utilise la commande : `sudo ip route add default via 192.168.1.2` 

==Ces trois premières commande permet donc d'afficher les configurations réseaux==

---

- Pour tester la connectivité réseau:
```
ping
```
La commande **ping** envoie une serie de *paquets* **ICMP**(Internet Control Message Protocol) à un hôte de destination pour vérifier s'il est joignable et mesurer le temps de réponse. Le `ping` sous linux est toujours continu contrairement au ping sous windows.

- Pour afficher le chemin emprunter par un paquet jusqu'à sa destination, en identifiant chaque routeur traversé.
```
traceroute
```
Si on arrive pas à joindre un hôte, on peut tenter d'identifier le point de blocage grâce à l'utilisation de la commande `traceroute`. En cas d'échec de connectivité réseau, cette commande peut aussi aider à comprendre où se situe la coupure sur le réseau.
Par défaut, l'outil **traceroute** utilise des paquets **UDP**(User Datagram Protocol) pour déterminer l'itinéraire. si un **parfeu** filtre ces paquets, on peut utiliser l'option `-I` pour basculer sur des paquets **ICMP** . Sinon, on peut aussi utiliser l'option `-T` pour basculer sur des paquets **TCP**(Transfer Control Protocol)

- Utiliser par l'outil nommé **My traceroute** qui présente l'avantage de combiner à la fois le `ping` et le `traceroute`
```
mtr  #My traceroute
```
Les données sont actualiser en temps réel et nous avons une visualisation plus dynamique du chemin réseau emprunter.

==Ce sont les commandes qui permettent de tester la connectivité réseau==

---

- Pour afficher les fichiers ouvert par les processus du système, y compris les connexions réseau actives
```
lsof   #List Open Files
```
**exemple:** `sudo lsof -i -Pn`
`-i` : afficher les connexions réseau ouvertes
`-P` : désactive la résolution d'un numéros des ports en nom de service
`-n` : empêche la résolution DNS

- Permet d'obtenir les info sur les connexions réseau 
```
ss    #Socket Statistics
```
c'est une version plus moderne et plus rapide de l'outil **netstat**
**exemple:** `sudo ss -tulnp`  cette commande nous fourni une vue détaillée des connexions réseau et des processus associés. Cette commande est très utile car elle permet d'obtenir la **liste des ports en écoute** sur la machine local grâce à la lecture de la colonne **Local Address:Port** 

- Pour capturer et analyser les paquets réseau en temps réel.
```
tcpdump
```
Il est souvent utiliser pour diagnostiquer les problèmes de communications réseau, examiner le trafique entrant et sortant, ou détecter d'éventuels flux malveillants. C'est donc un alternative de l'outil **WireShark** 


==Ce sont les commandes pour analyser la connexion et trafics réseau==

---

- Permet d'interroger un serveur DNS pour obtenir l'adresse IP associé à un nom de domaine (ou l'inverse)
```
nslooKup
```
**exemple**: `nslooKup google.com` ou `nslooKup 8.8.8.8`

- Pour diagnostiquer un problème DNS ou d'obtenir des infos sur un hôte, la commande `dig` est également intéressante. 
En comparaison de **nslooup**, `dig` fourniy des infos plus détaillées sur les **enregistrement DNS** d'un domaine.
**exemple**: une requête permettant d'afficher la **chaîne complète de la resolution DNS**:
`dig google.com +trace`  (ajout de l'option **+trace**)
Cette commande permet de suivre toutes les étapes de la résolution DNS. C-a-d, toutes les réponses depuis les serveurs racines jusqu'aux serveurs de noms final du domaine. La sortie affiche d'abord la requête envoyé au serveur racine puis le chemin suivi à travers les serveurs de noms successifs jusqu'à résolution complète du domaine 

```
dig (domain information groper)
```

==Ce sont les commandes pour diagnostiquer la résolution DNS==

---
- **netcat** ou **nc**:
    la commande `nc` permet de:
    - scanner des ports pour détecter ceux qui sont ouverts
    - tester l'ouverture d'un port sur une machine distante
    - écouter sur un port en mode serveur pour recevoir des connexions
    - établir une connexion **tcp/udp** vers un hôte distant
    **exemple**: `nc -zv nomDNS/IP 3389`  (3389 : RDP: Remote Desktop Protocol)
    `-z` : utiliser pour effectuer les scans des ports 
    `-v`: correspond au mode verbeux c-a-d, obtenir plus d'infos sur ce que fait la commande(comme des messages de réussite ou d'échec)
- **nmap**:
    c'est un outil très puissant pour efectuer 
    - des scans de ports
    - détecter les machines connectées à un réseau
    - éffectuer de la recherche des vulnérabilités  
    **exemple**: `nmap 192.168.1.202 -p 22,80,3389`

==Commandes pour scanner et tester les ports==

---

> [!NOTE] Wireshark
> analyse des trafics entrants et sortants sur le réseau

- **iperf**:
    Outil en ligne de commande permettant de mésurer la bande passante réseau entre deux machines. Il est très utiliser pour tester les performances d'un réseay **tcp** ou **udp** que ce soit en *LAN* ou en *WAN*
    Il y a 3 caractéristiques fondamentale qui détermine la qualité d'un lien réseau, que ce soit en **local** ou **distant**
    - **Bande passante**(bandwidth): c'est la quantité max de donnée qu'un lien peut transporter en un temps donnée, genéralement exprimé en **Mbps** ou **Gbps**
    - **Latence**(Latency): c'est le temps nécessaire pour qu'un paquet de données aille d'un point à un autre (en **ms**)
    - **la gigue**(jitter): c'est la variation de la latence d'un paquet à l'autre. Un réseau est dit stable si la **gigue** est **basse**
- **speedtest**:
    `speedtest-cli` est un outil en ligne commande qui permet de tester la vitesse de la connexion internet mais directement depuis un terminal

==commandes pour tester la bande passante==


---
## Protocole de messagerie: SMTP, POP, IMAP,MAPI

### SMTP (Simple Mail Transfert Protocol):
Le protocole SMTP a pour objectif d'acheminer les **e-mails** envoyés depuis un expéditeur, en s'appuyant sur le **serveur de messagerie**. Ce protocole fonctionne selon le mode **client-serveur** avec des connexions **tcp**. 
Les serveurs de messagerie, autrement dit **MTA**(Mail Transfert Agent) vont faire transiter les e-mails. Le mail est envoyé via **SMTP** à votre serveur de messagerie. Ensuite le serveur de messagerie va l'envoyer via **SMTP** au serveur de messagerie du destinataire. Pour trouver à quel serveur de messagerie l'e-mail doit être envoyer, le serveur SMTP va s'appuyer sur le **DNS** et consulter l'enregistrement **MX** associé à votre domaine: **cet enregistrement indique du serveur de messagerie à contacter**.
Le protocole **SMTP** s'appuie sur le **port 25** par défaut

> [!NOTE] SMTPS
> Protocole sécursé du SMTP qui utilise le port 587 également appelé SMTPoverSLL

#### Relais SMTP:
Un relais SMTP désigne généralement un serveur sur lequel on va s'appuyer pour faire transiter les e-mails dans le but qu'ils arrivent à destination  
**exemple:** serveur **NAS**(Network Atached Storage)

### POP: Post Office Protocol
Ce protocole utilise aujourd'hui sa **version 3** d'où le nom **POP3**. Il a pour objectif de permettre de télécharger les e-mails de votre boite aux lettres sur un serveur de messagerie à partir de votre client de messagerie(gmail , outlook, etc).
Notez bien que ce protocole télécharge les e-mails sur le client par exemple votre PC mais il n'y a pas de synchronisation client/serveur. C'est-à-dire lorsque le mail est télécharger sur votre PC par l'intermédiaire du protocole POP, **il n'est plus stocké sur le serveur** .
Ce mode de fonctionnement signifie que le protocole POP n'est pas adapté si vous utiliser votre **BAL**(Boite aux lettres) sur plusieurs appareils. 
**Exemple**: un e-mail télécharger sur votre PC ne sera pas accessible sur votre smartphone et vice-verse.

Le protocole POP utilise tcp avec comme port par défaut le **port 110**. Il y a aussi **POPS** ou **POPoverSSL** qui utilise le **port 995**.

### IMAP: Internet Message Access Protocol

IMAP a pour objectif de récupérer les mails de votre BAL sur un serveur de messagerie.
Ce protocole synchronise en permanence (sans effacer les e-mails sur le client à partir du serveur de messagerie). Autrement dit, il crée une copie du message sur votre PC ou smartphone grâce à la synchronisation. C-a-d que le message d'origine reste sur le serveur de messagerie ce qui va permettre de centraliser l'ensemble des boîtes aux lettres et de faciliter les sauvegardes. 
Cette synchronisation permet d'avoir une boîte aux lettres dans le même état sur l'ensemble de votre appareils.


> [!NOTE] Client de messagerie
> - client lourd : application installée sur le poste
> - client léger : via navigateur

**IMAP** utilise le port **143 ou 220**
**IMAPS** utilise le port **993**


### MAPI: Messaging Application Programming Interface

Le protocole **MAPI** est un protocole de messagerie propriétaire(contraire de **open source**) développé par **Microsoft**. Il sert à effectué la communication entre un client de messagerie et un serveur de messagerie appelé **Exchange**.
**MAPI** est compatible avec le client de messagerie **outlook** qui est intégré à la suite **Microsoft Office** .
L'avantage de **MAPI** par rapport à **IMAP** c'est qu'il intègre un aspect collaboratif, c-a-d en plus de synchroniser vos mails il synchronise également les **contacts** et le **calendrier**
Le protocle **MAPI** s'appuie sur des flux web en **https**, donc il utilise le port par défaut **443** pour ce type de connexion toujours avec des connexions **tcp** 