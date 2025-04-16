
## Scénario A: exécution du protocole RIPv1 sur des réseaux par classe

- **Etape 1: installation du réseau**

![[Pasted image 20250414102612.png]]

- **Etape2: Configuration de base**:
    - Configurez le nom d’hôte du routeur. 
    - Désactivez la recherche DNS. 
        `R1(config)#no ip domain-lookup`
    - Configurez un mot de passe pour le mode EXEC.
        `R1(config)#enable secret passR1`
    - Configurez une bannière du message du jour. 
        `R1(config)#banner motd #Acces interdit pour les personnes non autorise#`
    - Configurez un mot de passe pour les connexions console. 
        `R1(config)#line console 0`
        `R1(config-line)#password consolePass`
        `R1(config-line)#login`
        `R1(config-line)#exit`
    - Configurez un mot de passe pour les connexions VTY.
        `R1(config)#line vty 0 4`
        `R1(config)#password vtyPass`
        `R1(config)#login`
        `R1(config)#exit`

- **Etape3: Activation des intérfaces**:

| **Périphérique** | Interface |  Adresse IP  | Masque du réseau | Passerelle par défaut |
| :--------------: | :-------: | :----------: | :--------------: | :-------------------: |
|        R1        |   Fa0/0   | 192.168.3.1  |  255.255.255.0   |          N/D          |
|                  |   Se2/0   | 192.168.2.2  |  255.255.255.0   |          N/D          |
|                  |   Se3/0   | 192.168.4.2  |  255.255.255.0   |          N/D          |
|                  |           |              |                  |                       |
|        R2        |   Se2/0   | 192.168.2.1  |  255.255.255.0   |          N/D          |
|                  |   Fa0/0   | 192.168.1.1  |  255.255.255.0   |          N/D          |
|                  |           |              |                  |                       |
|        R3        |   Se2/0   | 192.168.4.1  |  255.255.255.0   |          N/D          |
|                  |   Fa0/0   | 192.168.5.1  |  255.255.255.0   |          N/D          |
|                  |           |              |                  |                       |
|       PC0        |    Fa0    | 192.168.1.10 |  255.255.255.0   |      192.168.1.1      |
|       PC1        |    Fa0    | 192.168.3.10 |  255.255.255.0   |      192.168.3.1      |
|       PC2        |    Fa0    | 192.168.5.10 |  255.255.255.0   |      192.168.5.1      |
- **Etape4: Configuration du routage dynamique**
    - **Activation du routage dynamique:**
        `R1(config)#router rip`
    - **Saisie des Ad IP:**
        On ajoute les adresses IP des réseaux connéctés directement au routeur:
        `R1(config-router)#network 192.168.2.0`
        `R1(config-router)#network 192.168.3.0`
        `R1(config-router)#network 192.168.4.0`
        `end`