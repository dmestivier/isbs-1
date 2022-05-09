														# Compte-rendu TP 
														
	L'objectif est d'obtenir l'ensemble des publications associées à Physarum polycephalum puis de trouver les mots-clés de ces différents articles. 
Ceux-ci sont ensuite utilisés afin de construire un wordcloud à l’aide d’un site dédié. 

## Méthode : 

**1) Obtention de l'ensemble des publications

Les différentes publications se trouvent sur le site NCBI. 
Il faut alors sélectionner la banque de données Pubmed et lancer la recherche avec "Physarum polycephalum". On obtient ainsi 1631 publications sur ce sujet.
En sélectionnant l'option d'affichage permettant d'obtenir les infos des mots-clés (c'est-à-dire en recherchant "Physarum polycephalum [OT]", nous obtenons que 50 résultats. Cela signifie qu'il n'y a que 50 articles qui contiennent les mots "Physarum polycephalum" parmi mots-clés.
 Pour obtenir les articles avec les mots-clés en fichier texte, on utilise le format PubMed. Il faut sélectionner l'onglet "Save" puis modifier la sélection "All results", le format "PubMed" puis créer le fichier. 


**2) Extraction des mots-clés des publications

Afin d'extraire les mots-clés, on utilise le script get-wordcounts-from-pubmed-output.ipynb fourni par l'enseignant. Le script permet de parcourir tout le fichier texte 
(toutes les publications complètes avec les mots-clés). Il garde les lignes commençant par OT : ce sont les mots-clés. Ils sont alors isolés
et présentés ligne par ligne. On obtient finalement un fichier CSV avec les mots-clés ainsi que leur nombre d'itérations. 

**3) Création d'un wordcloud

Ainsi, on utilise le site https://www.wordclouds.com. Une fois arrivé sur la page, il est possible d'importer la liste des mots-clés au format CSV.
Pour cela, il faut sélectionner l'onglet "List/ Liste de mots" puis importer depuis CSV. 
A l'issue de cette importation, l'ensemble des mots-clés associés à la recherche apparaissent. 
La taille de chaque mot-clé est associée à son nombre de recherches. On utilise les filtres suivants : 
Auto fit : activé (ajustement de l'ensemble du nuage de mots dans la forme choisie)
Repeat words : desactivé (les mots n'apparaissent qu'une seule fois)
Taille : 50
Shape (icons) : f471 (correspond à la forme choisie)
Fonts : Raleway (police des mots-clés)
Direction : random (orientation aléatoire des mots) 
Colors (gradient, RGBA) : from (0, 0, 255, 1) to (0, 255, 220, 1) 


## Résultat : En pièce-jointe 
On remarque que le terme le plus employé est donc Physarum polycephalum. 
Shape (icons) : correspond à l'ADN en hélice
Colors (gradient, RGBA) : le fond est gris clair, les mots sont écrits en bleu, du vert-bleu pour les mots peu présents au bleu marine pour les plus représentés. 
Au final, on obtient donc un nuage de mots colorés et de différents tailles dans une forme d'hélice ADN double brin. 