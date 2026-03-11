# Python-project_00

## API de gestion de collection de carte magic

**Besoins** : 
- un utilisateur se connecte = Auth jwt 
- L'utilisateur est capable de créer une collection et donner un type à cette collection (batch / deck etc.)
- L'utilisateur peut ajouter / supprimer / éditer le nombres de carte dans sa collection
- L'utilisateur peut voir le statut de l'api ('health check)
- L'utilisateur peut voir le compte rendu d'efficacité de l'appli (vitesse des requetes et toutes les métriques dont on a parlé)

## Archi ##
### Models ###
| Nom de la table  | Définition                                                                 | Attributs |
|------------------|----------------------------------------------------------------------------| ------|
| users            | L'utilisateur et toutes les info pertninentes                              | id / full name / email / hashed_password / created_at
| cartes           | Toutes les caractéristiques d'une carte                                    | id / name / edition / rareté / foil / langue / image / texte / force / endurance / created_at
| collections      | Une liste de carte                                                         | id / name / type (enum) / created_at / user_id
| audit_logs       | une table d'audit, de polymorphisme, pour savoir tout ce qu'il s'est passé | id / entity_type / entity_id / old_value / new_value / user_id / created_at
| collection_carte | Un collection peut avoir plusieurs cartes, et une carte peut avoir plusieurs collection | id / carte_id / collection_id / card_quantity

## Stack ##

- Python
- FastApi
- pyJwt
- sqlAlchemy
- alembic
- postgres
- Docker
- CI/CD en github action pour run les tests avant déploiement
- Déploiement sur VPS de la boite
- pytest + httpx

## Routes ##

| Méthode | routes                                              | Roles                                            |
|---------|-----------------------------------------------------|--------------------------------------------------|
| POST    | /login                                              | Connection et recupération du jwt                |
| POST    | /register                                           | Créer un compte                                  |
| POST    | /refresh                                            | Recréer un nouveau JWT                           |
| GET     | /collections                                        | Voir la liste de ses collections                 |
| POST    | /collections                                        | Créer une nouvelle collection                    |
| GET     | /collections/{id}                                   | Voir sa collections et toutes les cartes associées |
| PUT     | /collections/{id}                                   | Mettre à jour sa collections (type / nom)        |
| DELETE  | /collections/{id}                                   | Supprimer une collections                        |
| PUT     | /collections/{id}/cards/{id}                        | Modifier les cartes dans la collections          |
| GET     | /cards?name=card_name&strength>=3&edtion=tartanpion | Rechercher des cartes                            |
| GET     | /cards/{id}                                         | Obtenir les informations d'une carte             |
| GET     | /status                                             | Donne l'état de l'api                            |
| GET     | /logout                                             | Invalider le token                               |

