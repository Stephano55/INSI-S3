
## exo1

- configuration de **R1**:
```
enable
configure terminal

! Configuration des interfaces
interface FastEthernet0/0
ip address 10.0.0.1 255.0.0.0
no shutdown
exit

interface GigabitEthernet0/0
ip address 140.140.0.1 255.255.0.0
no shutdown
exit

interface Serial0/0/0
ip address 20.0.0.1 255.0.0.0
no shutdown
exit

! Configuration du routage statique
ip route 192.168.1.0 255.255.255.0 140.140.0.2

end
write memory

```

- Cofiguration de **R2**

```
enable
configure terminal

! Configuration des interfaces
interface FastEthernet0/0
ip address 192.168.1.1 255.255.255.0
no shutdown
exit

interface GigabitEthernet0/0
ip address 140.140.0.2 255.255.0.0
no shutdown
exit

! Configuration du routage statique
ip route 10.0.0.0 255.0.0.0 140.140.0.1
ip route 20.0.0.0 255.0.0.0 140.140.0.1

end
write memory

```

- configuration **R3**

```
enable
configure terminal

! Configuration de l'interface
interface Serial0/0/0
ip address 20.0.0.2 255.0.0.0
no shutdown
exit

! Configuration du routage statique
ip route 10.0.0.0 255.0.0.0 20.0.0.1
ip route 192.168.1.0 255.255.255.0 20.0.0.1

end
write memory

```

- Configuration **PC1**

```
ip 10.0.0.10/8 10.0.0.1
```

- Configuration **PC2**

```
ip 192.168.1.10/24 192.168.1.1
```