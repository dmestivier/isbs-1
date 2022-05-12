#Compte-rendu TP : PyzoPlasmes

L'objectif est d'effectuer une recherche bibliographique sur le site pubmed du NCBI, obtenue à partir de la liste des publications concernant le Physarum polycephalum. 

##Méthode : 

###1 Obtention de la liste des publications

Sur le site du NCBI, dans la banque des données pubmed on recherche le mot-clé "Physarum polycephalum" et on obtient 1631 résultats publié entre 1945 et 2022. 
Afin d'affiner les recherches, on sélectionne le format pubmed on obtient donc un fichier texte que l'on sauvegarde.

###2 Obtention des mots-clés

A partir du fichier texte sauvegardé, on utilise le script "get-wordcounts-from-pubmed-output.ipynb" que l'on copie pour le coller dans un programme python qui nous a permis d'obtenir un fichier CSV contenant l'ensemble des mots-clés associés à la recherche.
Ainsi que leur nombre d'occurence.

###3 Obtention d'un wordcloud

