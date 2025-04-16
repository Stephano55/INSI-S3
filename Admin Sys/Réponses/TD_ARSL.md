## Exo1
---
1. On a 192.16.5.133/29. Pour identifier la partie réseaux, on a besoin de **29 bits** et **3 bits** pour la partie hôtes.

2. /29 = 255.255.255.248
    256 - 248 = 8 (maka 8 bits par 8 bits zany)
    On a 192.168.186.227/29
    192.168.186.0 - 192.168.186.7  / 192.168.186.8 - 192.168.186.15 
    192.168.186.16 - 192.168.186.23  / 192.168.186.24 - 192.168.186.31
    ...
    192.168.186.224 - 192.168.186.231 (c'est là que .227 se trouve)
    la plage où se trouve 192.168.186.227 est donc : **192.168.186.225-192.168.186.230** car .224 pour l' **Ad réseaux** et .231 pour l' **Adresse de diffusion**

3. /23 = 255.255.254.0
    256 - 254 = 2 (maka 2 bits par 2 bits)
    On a 172.18.47.54
    172.18.46.0 - 172.18.47.255 (c'est là que se trouve 172.18.47.54)
    la plage où se trouve 172.18.47.54 est donc : **172.18.46.1-172.18.47.254**


## Exo 2
---
1. On a 172.16.5.10/28 . Le masque réseau en notation décimale est: **255.255.255.240**

2. l’adresse IP 222.1.1.20 avec le masque 255.255.255.192 en notation CIDR est :
    **222.1.1.20/26**

3. l’adresse IP 135.1.1.25 avec le masque 255.255. 248.0 en notation CIDR est :
    **135.1.1.25/21**

4. On a 192.168.1.0/28
    32 - 28 = 4
    2⁴ = 16    16 - 2 = 14
    Chaque sous-réseau peut donc contenir **14 hôtes**
5. On a 172.16.0.0/18 
    /18 = 255.255.192.0


## Exo3
---
On a 132.45.0.0/16

1. 2^n = 8    n = 3
    On a donc besoin de **3 bits** suplémentaires pour définir 8 sous-réseaux

2. Le masque de réseau qui permet de créer 8 sous-réseaux est 16+3 = **/19**

3. /19 = 255.255.224.0     256 - 224 = 32
    l'adresse réseau de chacun des huit sous-réseaux ainsi définis sont :
    - 132.45.0.0
    - 132.45.32.0
    - 132.45.64.0
    - 132.45.96.0
    - 132.45.128.0
    - 132.45.160.0
    - 132.45.192.0
    - 132.45.224.0

4. la plage des adresses utilisables du sous-réseau numéro 3
    réseaux n3 = 132.45.96.0
    plage : 132.45.96.1 - 132.45.127.254

5. l'adresse de diffusion du sous-réseau numéro 4
    réseau n4 : 132.45.128.0
    Ad Broadcast : 132.45.159.255


## Exo4
---
On attribue le réseau 200.35.1.0/24. Il faut définir un masque réseau étendu qui permette de placer 20 hôtes dans chaque sous-réseau

1. 2^h−2≥20
    si h = 5    32 - 2 ≥20
    Pour acceuillir au moins 20 hôtes sur la partie hôte de ce réseaux on doit ajouter **5 bits** suplémentaires.

2. le nombre maximum d'adresses d'hôte utilisables dans chaque sous-réseau est **30**

3. On a au départ /24, on y ajoute **3 bits** car **5its - 2** donc 
    2³ = 8
    le nombre maximum de sous-réseaux définis est **8**

4. /24 + 3 = /27
    /27 = 255.255.255.224
    256 - 224 = 32
    les adresses de tous les sous-réseaux définis sonts :
    - 200.35.1.0
    - 200.35.1.32
    - 200.35.1.64
    - 200.35.1.96
    - 200.35.1.128
    - 200.35.1.160
    - 200.35.1.192
    - 200.35.1.224

5. l'adresse de diffusion du sous-réseau numéro 2 est 
    Ad n2 : 200.35.1.64
    Ad Broadcast : 200.35.1.95