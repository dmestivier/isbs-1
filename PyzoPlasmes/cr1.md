# Compte-rendu TP : PyzoPlasmes

L'objectif est de réaliser un Wordcloud à partir des mots-clés associés à la recherche "Physarum Polycephalum" sur le site NCBI.

## Méthode : 

### 1 Obtention de la liste des publications

Sur le site du NCBI, dans la banque de données pubmed on recherche le mot-clé "Physarum polycephalum" et on obtient 1631 résultats publiés entre 1945 et 2022. 
Afin d'affiner les recherches, on sélectionne le format pubmed, et on ne conserve que les mots-clés contenant le tag OT. On obtient donc un fichier texte que l'on sauvegarde.

### 2 Obtention des mots-clés
 
 On exécute le script "get-wordcounts-from-pubmed-output.ipynb" sur Spyder pour obtenir un fichier au format CSV nommé physarum-wordcloud.csv.
 Ce fichier contient les mots-clés et leurs occurences.

### 3 Obtention d'un wordcloud

On se connecte sur le site wordcloud. On sélectionne "wordlist" puis "import from csv". 
On sélectionne le fichier obtenu grâce au programme Python. 
On détermine les paramètres de couleur et forme, à l'aide des commandes "shape" et "colors". 
Nous avons choisi un cerveau en lien avec la recherche et les couleurs jaune et orange en lien avec la couleur du Blob. 
On enregistre cette image au format png. 

## Résultats 

On observe que sur l'image obtenue les mots les plus visibles sont ceux dont l'occurence est la plus grande. 
