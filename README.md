# Botify-Test

                                           Pré-requis: Python3, Flask, Flask-restful

Test technique Botify:

Script:
        - Conversion CSV to Mysql: csvToDb.py,
        - Installation des dépendance: install,
        - Lancement de L'API: run

    API Flask-Restful:
    GET:
        Town:
        - /towns: Liste de toutes les villes dans un json par ville
        - /town/<string:name>: Donne la ville selon la Name passer dans l'URL 
        - /town/delete/<string:name>: Delete la ville selon le name passer en URL
        - /town/region/<string:region>: Liste des villes selon la region
        - /town/<int:population>: Liste les ville ayant plus de population que le int passer en URL

         Simple Aggregation:

        GET:
         - /aggs: liste le nombre de ville, moyenne d'age, minimun et maximun de population selon le code dept ou le code du district passer dans le body

        Implement DSL: 

        POST:
        - /query: Traite un Json pour le transformer en SQL
            type: 
            -> SELECT [fields] FROM towns
            -> SELECT [fields] FROM towns WHERE [field] = [value]
            -> SELECT [fields] FROM towns WHERE [field] [predicate] [value]
            -> SELECT [fields] FROM towns WHERE [field] [predicate] [value] AND/OR [field] [predicate] [value]