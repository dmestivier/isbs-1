# Compte Rendu 1

## Objectif : 

L'objectif de notre TP était l'extraction des mots clés associés à l'organisme Physarum polycephalum (le blob) 
issus des articles trouvés sur Pubmed afin de construire un "Worldcloud" de ces mots clés.


## Méthode :

La procédure suivi pour construire notre Worldcloud était la suivante :
 
Pour commencer, nous avons effectué une recherche bibliographique sur le Site pubmed. 
Via la banque de données généraliste NCBI, nous avons recueilli les bioinformations sur Physarum polycephalum : 
tous les articles obtenus étaient au nombre de 1630

Au niveau de la barre de recherche, nous avons tapé : Physarum polycephalum puis nous avons sauvegardé (save) 
tous les résultats (all results) en format Pubmed (des informations sur les auteurs, les mots clés, les dates de publications, etc.)

Nous avons ensuite vérifié la présence du champ [OT] sur le fichier téléchargé avec le logiciel Notepad++ 
qui est un éditeur de texte (https://notepad-plus-plus.org/)

Après cette étape de sauvegarde, notre groupe a généré une paire de Clé SSH dans le but de pouvoir 
accéder au github de ISBS1, de l'utiliser et de le modifier. Pour cela nous avons télécharger git (https://git-scm.com/download/win)

A partir du fichier téléchargé au format pubmed, nous avons utilisé un Notebook Jupyter (get-wordcounts-from-pubmed-output.ipynb) 
pour générer un fichier au format csv comprenant les mots clés liés à physarum polycephalum ainsi que le nombre d'occurrences de ces mots clés. 
Pour cette étape de notre travail nous avons du utiliser le logiciel anaconda (https://www.anaconda.com/products/individual)


Notre fichier au format csv a été utilisé pour l'obtention d'une figure au format png sur le site worldcloud (https://www.worldclouds.com). 
Cette figure regroupe tous les mots clés de Physarum polycephalum sous forme de nuage de mots.
 
Nous avons choisi de représenter nos mots clés à l'aide du site du Worldcloud, sous la forme d'un nuage trouvé dans l'onglet "Shape" en direction horizontale. 
4 différents types de polices (fonts) ont été choisi également par nos soins. Il s'agit des polices Condiment, PT Serif Caption, Candal et Audiowide. 
Puis 4 couleurs (via Colors - word Colors) : le Fuschia, bleu, saumon et rose foncé avec un arrière plan noir (background & Mask Color) et enfin, 
la méthode de dessin (drawing method dans options) choisie était "circles" avec un word Margin à 6.


## Résultat :

Grâce à toutes les méthodes présentées précédemment, nous avons pu obtenir une figure regroupant nos différents mots clés.

On a pu constater sur notre figure qu'il ya une multitude de mots clés associés à "physarum polycephalum". 
De plus, tous les mots clés s'organisent autour de  notre sujet central qui est "physarum polycephalum. Pour finir, nous avons vu que 
plus le nombre d'occurrences du mot clé est important plus ce mot apparaît en grand dans notre nuage de mots. 
Les mots clés les plus représentés donc les plus lisibles sur l'image étant : fungi, myxomycetes, experimental lab study, metabolism, cell division, physarum