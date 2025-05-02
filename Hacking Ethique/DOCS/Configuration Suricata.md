
## Installation
- **Installation des dépendances**:
    `sudo apt install -y software-properties-common`

- **Installation  de suricata**:
    `sudo apt install -y suricata`

- **Activer le mode promiscuous sur l’interface réseau**:
    `sudo ip link set <interface> promisc on`

## Configurer Suricata

- **Modifier le fichier /etc/suricata/suricata.yml**:
    Modifier la section :
```
    af-packet:
     - interface: ens33 
```

- **Activation de la détection IDS :
    - **Démarrer suricata en tant que IDS**:
        `sudo suricata -c /etc/suricata/suricata.yaml -i ens33`
    - **Démarrer suricata en tant que service**:
        `sudo systemctl enable suricata`
        `sudo systemctl start suricata`

## Télécharger les règles:
- **gérer les règles avec Suricata-Update**:
```
sudo apt install -y suricata-update
sudo suricata-update
```

- **Vérifier les logs**:
    Les logs sont dans `/var/log/suricata/`. Les fichiers importants à vérifier sont:
    - **fast.log**: alertes rapides
    - **eve.json**: format JSON structuré, utilisable avec ELK

