# Botify-Test

#Pré-requis: 
    - machine noyau Unix, ubuntu de préférence
    - Avoir une base de donnée nommer botify

Test technique Botify:

#Script:

        - Conversion CSV to Mysql: csvToDb.py

        - Installation des dépendances: install

        - Lancement de L'API: run

#API Flask-Restful:
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

#Fonctionnement: 
    bash /script/install.sh
        /script/run.sh

#Note: 

    Si le script run ne fonctionne pas, lancer la commande suivante "python3 Flask-Restful/api.py" 
    Le script pour convertir le csv crée une table et insert sur une base de donnée local
    Je n'ai pas utilser Docker par manque de temps :(, mon step5 ne fonctionne pas
    Les Champs de la table sont les même que le csv avec des underscore ajouter:

    Region_Code	
	Region_Name	
	Code_Department	
	Code_District	
	Code_town	
	Town_Name	
	Population	
	Average_Age