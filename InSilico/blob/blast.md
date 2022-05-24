# Blast-blob 2 : Scaffolding chez Physarum 

## Objectif : 

Effectuer plusieurs alignements de séquences entre des scaffolds obtenus à Mondor/ISBS et ceux publiés sur le site du NCBI. 

## Obtention des séquences : 

Pour effectuer un alignement de séquences entre la séquence NCBI et les séquences Mondor, il faut commencer par les obtenir.
On trouve la séquence NCBI en la cherchant sur le site du NCBI (copier le nom de la séquence :  KL561189.1) puis on la télécharge.
Ensuite, pour obtenir les séquences Mondor, on clone le dossier ISBS-1 accessible via git.
Maintenant, nous disposons de toutes les séquences pour travailler dessus.

## Alignement des séquences : 

Pour blaster, on utilise l’option "Align two or more sequences" sur la page BLAST du NCBI.
On choisit le scaffold Mondor en Query et NCBI en Subject.
On obtient l'alignement, avec la position des bases aux extrémités (start et end).

Nous avons choisi le jeu 1. Par exemple, la comparaison avec le scaffold Mondor 3085 donne une correspondance à 99%. Start : 39 End : 2664. 
On fait de même avec les 8 autres séquences Mondor à comparer.

A partir de ces informations placées sur un schéma, il suffit de les réarranger afin d'avoir la position des séquences Mondor par rapport à celle du NCBI.

## Résultat : 

On donne dans le dossier le schéma avec la position des séquences comparées, ainsi que les fichiers des 9 alignements de séquence. 

Une fois les blasts obtenus, nous avons réalisé une figure représentant le chevauchement de nos 8 BLAST.


## Description de notre Figure :

On constate que les 9 scaffolds recouvrent quasiment la totalité de la séquence NCBI. Il n'y a aucun chevauchement, mais il y a des gaps.
La plus grande est le scaffold 3085, avec 2625 nucléotides, et la plus courte est la 160809, avec 219 nucléotides. 

## Conclusion :

Nous avons grâce à cette méthode pu observer la qualité du séquençage de Mondor-ISBS, car on obtient des scores de correspondance de l'ordre de 99%. Malgré le fait que nous ne disposions pas d'un scaffold manquant, nous pouvons dire que cette reconstruction permet de recouvrir une grande partie de la séquence NCBI.




