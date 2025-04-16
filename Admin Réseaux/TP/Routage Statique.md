
![[Pasted image 20250410211437.png]]

Le principe du routage statique est le suivant: Pour chaque routeur, identifier tous les réseaux qui ne sont pas voisins (En d'autres termes, qui ne sont pas directement raccordés) à celui-ci. Ensuite il faut définir une route (à l'aide d'une passerelle) pour atteindre chacun de ces réseaux.

**commandes pour le routage statique**:
```
 ip route {le réseau non connecté directement} {masque du réseau} {la passerelle}
 do wr 
```
- **Routeur 5**:
    Les réseaux qui ne sont pas connectés directement à ce routeur sont le réseau **192.168.1.0/24**, et le réseau **192.168.3.0/24**. Pour atteindre **192.168.1.0/24** on doit mettre comme **passerelle** l'IP **10.10.10.1**(c'est l'IP de l'interface directement opposée au routeur concerné dans le sens de ces Réseaux en question). Et pour atteindre le réseau **192.168.3.0/24**, on doit mettre comme **passerelle** l'IP **10.10.10.6**

- **Routeur 6**:
    Les réseaux qui ne sont pas connectés directement à ce routeur sont le réseau **10.10.10.4/30**, et le réseau **192.168.3.0/24**. Pour atteindre ces deux réseaux on doit mettre comme **passerelle** l'IP **10.10.10.2**

- **Routeur 7**:
    Les réseaux qui ne sont pas connectés directement à ce routeur sont le réseau **10.10.10.0/30**, et le réseau **192.168.1.0/24**. Pour atteindre ces deux réseaux on doit mettre comme **passerelle** l'IP **10.10.10.5**