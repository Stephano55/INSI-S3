## C'est quoi Suricata?

C'est un outil de cyber-securité:
- **Intrusion Detection System (IDS**): collecter un max d'info pour détecter des comportements malveillants.
- **Intrusion Prevention System (IPS)**: bloquer les comportements potentielement malvaillants.
- **Network Security Monitoring (NSM)** 
- Created in 2009
- Opensource
- Developpé en C
- Maintenu par Open Information Security Foundation (**OISF**)
- OS: Linux, FreeBSD, OpenBSD, Windows 

### Fonctionalités:

- **Instance**: un outil suricata installé par serveur.
- **Multithread Infrastructure**: analyse des packets à très haute performance.
- **Rules**: instructions pour analyser et activer les alertes
- **Signature**: identification d'une attaque spécifique
- **Intégration des outils externes**: comme **wazuh** ou **opnsense**
- **Prevention**: action préventive pour bloquer les attaques
- **Trafic crypté**: isnpéction des packets **TLS/SSL**
- **NSM**: journal DNS et HTTP, extraction des fichiers, checksum (empreinte unique de hachage)
- **Port mirroring**: technique utilisée sur un switch pour **dupliquer** le trafic réseau d'un ou plusieurs ports vers un autre port. Cela permet d'analyser le trafic en temps réel sans perturber le réseau.


## Étapes:

1) **Capture de trafic**: avec des outils comme **pcap** ou **libcap**
2) **Analyse multi-thread**: divise le trafic par fil
3) Faire **Défrager** l'IP et **Assembler** les packets TCP pour avoir un trafic lisable
4) Interpretation des **Rules**
5) Analyse profonde pour aller dérière les **headers** et checker le corp du packet
6) Réponse et Action si besoin
7) Écriture des **Logs**
8) Collection des logs pour les envoyer vers des **Systèmes centralisé**

 