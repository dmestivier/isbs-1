# Compte-rendu 1 : 

## Objectifs : 
1. Extraire des résultats de recherche PubMed sur le Physarum Polycephalum afin de créer un Wordcloud. 
2. Valider notre nom de groupe sur Git 


## Méthode : 
1. Nous avons effectué une recherche sur PubMed afin de trouver toutes les publications associées au Physarum Polycepharum et de trouver des mots-clés associés pour connaitre les domaines de recherche utilisant cet organisme.
Ensuite, nous sommes allées sur le site du NCBI, puis nous nous sommes redirigées vers la banque de données PubMed. Nous avons recherché « Physarum Polycephalum » .
Cette requête nous a donné 1 631 résultats, soit 1 631 articles traitant de Physarum Polycephalum.
Afin d’obtenir les informations de mots-clés (tag OT), nous avons cherché dans les options d’affichage "Display Options" et nous avons choisi "PubMed".
Nous avons sauvegardé ce fichier, en cliquant sur "Save" ainsi que le format du fichier "PubMed". 
Ce fichier est dans le dossier.
Après vérification, nous avons bien le champ OT dans le fichier qui nous indique les mots-clés de la recherche.
A l'aide de l'éditeur de texte, nous avons pu compter 1659 occurences de "PMID".
Le fichier a un poids de 3 769 Ko ce qui est comparable à ce qu'on également les autres groupes.
Comment on a obtenu le cloud ?
Nous avions exporté les mots trouvés sous un format .docx
Nous avons ensuite:
	- utilisé le notebook Jupyter get-wordcounts-from-pubmed-output.ipynb pour extraire les mots clés nous intéréssant
	- enregistré ces mots sous le format txt
	- importé notre fichier txt sur le site https://www.worldclouds.com 
	- créé notre Worldcloud des mots-clés
	
Paramètres graphiques sélectionnés:
	- text drawing mode : fill
	- drawing method : circles (no shuffle)
	- text shadow : 0
	- word margin : 2
	- min. word size : 5
	- canvas padding: 5%
	- no repeat words
Le wordcloud est dans le dossier LesViperes avec la recherche PubMed et ce compte-rendu.

2. Afin de valider notre nom de groupe sur GitHub, nous avons commencé par cloner le GitHub du cours gràce à la commande "git clone" suivie de l'adresse du Git Hub isbs1.
Nous avons ensuite modifié le fichier en ajoutant "OUI" sur notre ligne puis nous l'avons ajouté grâce aux différentes commandes : "git add README.md", nous avons indiqué notre identité comme demandé puis nous avons réalisé les commandes "git pull" et "git push" afin de charger les modifications et d'envoyer les notres au GitHub.
Grâce à la commande "git commit", nous vaons pu indiqué la nature de la modification.



## Résultat : 
1. Description du wordcloud : La plupart des motes sont en rapport avec la biologie. Nous observons que 4 mots, les plus gros sur l'image, sont ceux qui reviennent le plus souvent : physarum, differenciation, computing, cell.

2. Après vérification, notre modification était bien présente sur le GitHub.
