# Compte-rendu groupe XAEAXII : 

## Objectif : 

L'objectif de ce TP était d'extraire les mots-clés associés à l'organisme Physarum polycephalum sur le site PubMed afin de réaliser un wordcloud grâce au site https://www.wordclouds.com/


## Méthode : 

Pour ceci, nous avons tout d'abord extrait tous les résultats contenant Physarum polycephalum sur PubMed grâce à la fonction **save** en choisissant **all resulats** ainsi que le **format PubMed**.
Nous avons donc obtenu un fichier texte (.txt) nommé *pubmed-Physarumpo-set* contenant toutes les informations concernant les articles qui contenaient Physarum polycephalum. Chaque information commençait par 2,3 ou 4 lettres qui décrivaient la nature de l'information. 
Les mots-clés commençaient par exemple par *OT*, les titres par *TI* ou encore les dates de publication par *DP*.

Nous avons ensuite utilisé un script python qui nous était fourni dans la séance 4 du cours sur EPREL qui se nommait : *get-wordcounts-from-pubmed-output.ipynb*.
Ce script nous a tout d'abord pemis de trier les différents résultats en fonction des lettres les précedant pour ne garder que les mots-clés commençant par *OT -*.
Il nous a ensuite permis de créer un **fichier au format CSV** à deux colonnes nommé *wordcounts.csv*  comportant seulement les mots-clés ainsi que leurs nombre d'occurences.
Pour cela nous avons ouvert le script dans le notebook Jupyter, nous avons importé le fichier *pubmed-Physarumpo-set* dans le script, puis nous avons **executé les différentes commandes** jusqu'à obtenir le fichier CSV nommé :*wordcounts*.

Nous avons enfin importé ce fichier dans le site : https://www.wordclouds.com/ en cliquant sur **wordlist** puis **import CSV**.
Nous avons choisi une forme imagée/dessinée (non réaliste) de Blob (Physarum polycephalum) et personnalisé notre wordcloud à des couleurs nous rappelant la biologie (vert et jaune principalement), nous avons changé la police d'écriture et avons choisi *Pacifico*.
Enfin nous avons sélectionné l'option **mask** et augmenté l'**autofit** à 50 pour que notre figure soit pleine.
Nous avons ensuite extrait notre figure au format PNG et m'avons enregistré dans un dossier au nom de notre groupe de travail.


## Résultats : 

En regardant notre wordcloud, nous pouvons observer un nuage de mots correspondants aux différents mots-clés associés au sujet Physarum polycephalum sur PubMed.
Plus le mot-clé est récurrent sur PubMed, plus il apparait avec une grande taille de police. Cela nous permet d'avoir un aperçu rapide des mots les plus utlisés concernant Physarum polycephalum et donc des axes de recherche sur ce sujet.
Nous constatons par exemple que le mot **FUNGI** est très employé associé à **Physarum polycephalum**, ainsi que **METABOLISM**, **CELL DIVISION** ou encore **EXPERIMENTAL LAB STUDY**.

***Remarque*** : Il est à noté qu'en fonction de la longueur du mot et du fait qu'il soit écrit en minuscules ou en majuscules impacte la taille du mot sur le nuage de mots. Ainsi le mot le plus récurrent ne sera pas néccessairement le mot le plus gros.

## Sources utilisées :

1. https://pubmed.ncbi.nlm.nih.gov/
2. https://www.markdownguide.org/cheat-sheet
3. https://www.wordclouds.com/
