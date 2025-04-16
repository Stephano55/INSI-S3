
- **UserName**: syncmachine
- **motDePasse**: `PassSync`

## configuration:

### Sur le serveur:

- **installation**:
```
sudo apt install bacula-director bacula-sd bacula-console bacula-common
```

- **Ajouter le section `client`**:
```
sudo nano /etc/bacula/bacula-dir.conf
```
```
Client {  
 Name = client-sync-machine  
 Address = 172.21.0.2  
 FDPort = 9102  
 Catalog = MyCatalog  
 Password = "BaculaPassInsI"          # password for FileDaemon  
 File Retention = 60 days            # 60 days  
 Job Retention = 6 months            # six months  
 AutoPrune = yes                     # Prune expired Jobs/Files  
}
```

- **Ajouter un `FileSet`**:
```
FileSet {  
 Name = "Sauvegarde Debian Client"  
 Include {  
   Options {  
     signature = MD5  
   }  
   File = /etc  
   File = /home  
 }  
}
```

- **Ajouter un `Job`**:
```
Job {  
 Name = "Sauvegarde-Client"  
 JobDefs = "DefaultJob"  
 Client = client-machine-fd  
 Level = Full  
 FileSet="Sauvegarde Debian Client"  
 Schedule = "WeeklyCycleAfterBackup"  
 Storage = File  
 Pool = Default  
 Messages = Standard  
 # This creates an ASCII copy of the catalog  
 # Arguments to make_catalog_backup.pl are:  
 #  make_catalog_backup.pl <catalog-name>  
 RunBeforeJob = "/etc/bacula/scripts/make_catalog_backup.pl MyCatalog"  
 # This deletes the copy of the catalog  
 RunAfterJob  = "/etc/bacula/scripts/delete_catalog_backup"  
 Write Bootstrap = "/var/lib/bacula/%n.bsr"  
 Priority = 10                   # run after main backup  
}
```

---

### Sur le client:

- **installation**:

```
apt update
apt install -y bacula-fd
```

- `bacula-fd.conf`:
```
Director {
  Name = bacula-dir
  Password = "BaculaPassInsI"
}

FileDaemon {
  Name = client-sync-machine
  FDAddress = 0.0.0.0
  FDPort = 9102
}

Messages {
  Name = Standard
  director = bacula-dir = all, !skipped, !restored
}

```

- **Redémarrer le service**:

```
bacula-fd &
```

- **vérifier qu'il écoute bien**
```
netstat -tnlp | grep 9102
```

![[Pasted image 20250413132003.png]]

