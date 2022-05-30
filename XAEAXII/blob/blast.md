## Compte-rendu TP 2 blob 

# Objectifs : 

L'objectif de ce TP est de comparer certains scaffolds du blob séquencés à Henri Mondor avec un scaffold disponible sur le site du NCBI afin d'évaluer leur précision.
Un **scaffold** est une séquence nucléotidique plus ou moins longue obtenue après assemblage de **reads** (résultats de séquençage).
Nous allons pour cela comparer l'**identité** des différents scaffolds ainsi que leurs **mismatchs** et leurs **gaps** avec le scaffold du NCBI.

# Méthode :

Pour réaliser ce travail, nous avons tout d'abord cherché le scaffold query *KL561420.1* sur le site du NCBI et l'avons téléchargé.
Dans un second temps, nous avons réalisé un pull du repository isbs-1 dans la fenêtre de commande GIT pour télécharger tous les scaffolds de l'ISBS.
Nous avons ensuite blasté chacun des scaffolds du jeu 2 de l'ISBS avec celui du NCBI grâce à la fonction **BLAST** du site du NCBI.
Nous avons importé dans *Enter query sequence* chacun des scaffolds de l'ISBS, nous avons coché "*Align two or more sequences* et nous avons importé le scaffold **KL561420.1** dans *Enter subject sequence*.
Nous avons enfin cliqué sur *BLAST* puis téléchargé les données d'aligenement sous format **Text**(dans l'onglet *Alignments*)telles que le pourcentage d'identité des deux séquences (voir fichers texte associés à chaque blast dans le sous-répertoire "*blob*").
Après réalisation des blast pour tous les scaffolds de l'ISBS, les informations contenues dans tous les fichiers textes téléchargés nous ont permis de réaliser un schéma de chevaucehement entre la séquence KL561420.1 et tous les scaffolds du jeu 2 (8 scaffolds).
Pour cetains blast, plusieurs alignements étaient proposés de différentes longueurs et de différents pourcentages d'identité. Nous avons choisi les plus longs alignements et ceux avec le pourcentage d'identité le plus élevé.

# Résultats : 

Les données issues des différents blasts nous ont permis de réaliser le "*schéma des chevauchements*". Pour chacun des blast, les pourcentages d'identité sont compris entre 99 et 100% et nous avons un taux moyen de gap de 0,19%.


# Conclusion : 

Nous remarquons que les séquences du jeu 2 sont très similaires à la séquence du NCBI. Les scaffolds de l'ISBS mis bout à bout représentent presque la totalité du scaffold du NCBI. Nous pouvons imaginer que si les deux scaffolds manquants étaient aussi représentés sur le schéma, les parties de la séquence du scaffold du NCBI non alignés aux scaffolds de l'ISBS seraient peu nombreuses.