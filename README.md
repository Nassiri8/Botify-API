# Botify-Test

Test technique Botify:

    Script:
        - Conversion CSV to Mysql: csvToDb.py
        - Installation des dépendance: install
        - Lancement de L'API: run

    API Flask-Restful:
        Town:
        - /towns: Liste de toutes les villes dans un json par ville
        - /town/<string:name>: Donne la ville selon la Name passer dans l'URL 
        - /town/delete/<string:name>: Delete la ville selon le name passer en URL
        - /town/region/<string:region>: Liste des villes selon la region
        - /town/<int:population>: Liste les ville ayant plus de population que le int passer en URL

         Simple Aggregation:

         - /aggs: liste le nombre de ville, moyenne d'age, minimun et maximun de population selon le code dept ou le code du district passer dans le body

        