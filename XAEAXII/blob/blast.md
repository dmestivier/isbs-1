## Compte-rendu TP 2 blob 

# Objectifs : 

L'objectif de ce TP est de comparer certains scaffolds du blob séquencés à Henri Mondor avec un scaffold disponible sur le site du NCBI afin d'évaluer leur précision.
Un **scaffold** est une séquence nucléotidique plus ou moins longue obtenue après assemblage de **reads** (résultats de séquençage).
Nous allons pour cela comparer l'**identité** des différents scaffolds ainsi que leurs **mismatchs** et leurs **gaps** avec le scaffold du NCBI.

# Méthode :

Pour réaliser ce travail, nous avons tout d'abord cherché le scaffold query *KL561420.1* sur le site du NCBI et l'avons téléchargé.
Dans un second temps, nous avons réalisé un pull du repository isbs-1 dans la fenêtre de commande GIT pour télécharger tous les scaffolds de l'ISBS.
Nous avons ensuite blasté chacun des scaffolds de l'ISBS avec celui du NCBI grâce à la fonction **BLAST** du site du NCBI.
Nous avons importé dans *Enter query sequence* chacun des scaffolds de l'ISBS, nous avons coché "*Align two or more sequences* et nous avons importé le scaffold **KL561420.1** dans *Enter subject sequence*.


# Résultats : 

# Conclusion : 