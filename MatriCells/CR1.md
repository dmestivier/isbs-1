Compte rendu - groupe MatriCells

## Objectifs:

1- A partir du site Pubmed du NCBI, il faut enregistrer tous les articles correspondant à Physarum Polycepharum, puis faire une recherche des mots-clés. 
Sauvegarder le fichier dans l'éditeur de texte Notepad++.
2- Extraction de mots clés sur Word cloud après modification du fichier en fomat CSV.
3- Validation du nom de groupe Matricells sur le git ISBS-1, en clonant puis en poussant le fichier modifié du Github local sur le Github global 
de la classe.
4- Parcourir les résultats grace à un script python afin d'avoir le nombre d'occurences des mot-clés et construire un wordcloud.

## Méthode:

1- Validation de Matricells: on a télécharger le fichier readme contenu dans le Github Isbs-1, on a cloné ce dernier sur le Github local grâce à la 
commande git clone. Ensuite nous avons ouvert le fichier README git clone, on a ouvert le fichier README.md pour apporter la modification 
de validation OUI à coté du nom de notre groupe MATRICELLS, puis on a réinjecté dans le GIT général isbs1.

2- Sur Pubmed: On effectue une recherche physarum plycepharum, on obtient 1631 résultats. L'option save --> All results --> Pubmed, nous permets 
de télecharger un fichier texte contenant les informations relatives aux articles ainsi que tous les mots-clés à coté des tags OT. 
Le fichier obtenu a été sauvegardé sous format txt.

3- Grace à un code Python, on a pu créer un fichier .CSV contenant les mot-clés de la recherche PUBMED sur différentes étapes:
	* Importation et ouverture du fichier .txt obtenu à l'étape 1.
	* Balayage de toutes les lignes afin de grader uniquement celles qui commencent avec le tag OT ( qui font réference aux mots clés)
	* Suppresion des elements suplementaires ( débuts de lignes et * ) 
	* Enregistrement des modifications et fermeture du fichier.
	* Exportation sur un fichier .CSV afin d'apporter des modifications.
	
4- On a ensuite importé sur Wordclouds.com le fichier .CSV obtenu afin de créer notre figure( wordcloud.jpg) qui est un nuage de mots clés.

## Résultats:
Nous avons obtenu un fichier .jpg avec le nuage concernant les mots clés de la rechcerche Physarum Polycepharum et un fichier .CSV contenant
tous ces mots clés. 