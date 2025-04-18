
- **Création de l'utilisateur**:
    `CREATE USER gestionnaire WITH PASSWORD 'GesPass';`
- **Création de la base de données**:
    `CREATE DATABASE gestion OWNER gestionnaire;`

## Modélisation des tables:

| **Produits**                           | **Fournisseurs**           | **Client**                 |
| -------------------------------------- | -------------------------- | -------------------------- |
| - id (serial, primary key)             | - id (serial, primary key) | - id (serial, primary key) |
| - Nom (varchar)                        | - Nom (varchar)            | - Nom (varchar)            |
| - catégories (varchar)                 |                            | - tel (varchar)            |
| - quantité (int)                       |                            | - adress (varchar)         |
| - déscription (varchar)                |                            |                            |
| - Fournisseur_id (serial, foreign key) |                            |                            |
| - prix (int)                           |                            |                            |

| **Stocks**                         | **Commandes**                     | **Payements**                       |
| ---------------------------------- | --------------------------------- | ----------------------------------- |
| - produit_id (serial, foreign key) | - id (serial, primary key)        | - commande_id (serial, foreign key) |
| - emplacement (varchar)            | - client_id (serial, foriegn key) | - prix_paye (int)                   |
| - q_restants (int)                 | - date_com (date)                 | - date_paye (date)                  |
| - date_ajout (date)                | - q_com (int)                     | - paye_id (serial, primary key)     |
|                                    | - tot_prix (int)                  |                                     |

| **Commande_annuler**                | **Livraison**                       | **Livreurs**        |
| ----------------------------------- | ----------------------------------- | ------------------- |
| - commande_id (serial, foreign key) | - id (serial, primary key)          | - CIN (int, unique) |
| - raison (text)                     | - livreur_id (serial, foreign key)  | - Nom (varchar)     |
| - date_annulation (date)            | - commande_id (serial, foreign key) | - tel (varchar)     |
| - com_an_id (serial, primary key)   | - date_livraison (date)             | - age (int)         |
|                                     | - client_id (serial, foreign key)   |                     |
