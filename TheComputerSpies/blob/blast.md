#CR1


# Méthodologie :

Pour réaliser le TP Blast, nous avions à notre disposition des séquences Mondor/ISBS
représentant des scaffolds de physarum polycephalum. De plus, nous disposions du code
du scaffold de la base de de données NCBI : KL561420.1.

Nous avons choisi un jeu de scaffolds ISBS que nous avons blaster sur le scaffold NCBI indiqué.
Pour ce jeu 2, nous avions 8 scaffolds au lieu de 10 comme indiqué dans le document du TP.

Pour blaster, nous nous sommes rendus sur le site NCBI. Dans la barre de recherche, nous avons
entré le code du scaffold NCBI de physarum polycephalum et nous avons effectué la recherche.
Nous avons obtenu un lien vers la séquence nucléotidique de ce scaffold que nous avons téléchargé au format FASTA puis nous avons modifié l'extension pour passer en fichier .csv. Après avoir téléchargé le document, nous sommes enfin passés au blast à proprement parlé.

Au niveau du même lien vers la séquence du scaffold NCBI, nous cliquons sur BLAST. Pour blaster un scaffold avec la séquence NCBI, nous commençons par cocher la case "align two or more sequences" puis nous chargeons dans la fenêtre query, notre scaffold et enfin, nous chargeons dans la fenêtre subject, le scaffold NCBI que nous avons préalablement téléchargé.

Après avoir chargé nos deux scaffolds à blaster, nous cliquons sur la commande BLAST et nous observons nos résultats. Nous effectuonss cette manipulation pour les 8 scaffolds à notre disposition.

Les résultats étaient composés de différents éléments comme :
- Le pourcentage d'identité qui doit être compris entre 99 et 100%
- Le taux de recouvrement qui dans notre cas était inférieur à 10% dans tous nos Blast
- La longueur de nos scaffold qui variait entre 240 et 3291.


Les différentes tailles étaient les suivantes :
Scaffold 1306 : 3291
Scaffold 33289 : 1033
Scaffold 45598 : 842
Scaffold 75705 : 561
Scaffold 91931 : 457
Scaffold 119867 : 331
Scaffold 120397 : 329
Scaffold 155695 : 240

Une fois les blasts de nos 8 scaffolds l'un après l'autre avec le scaffold ISBS obtenu, nous avons réalisé une figure représentant le chevauchement de nos 8 BLAST.



## Description de notre Figure :

Notre figure présente le chevauchement de 8 scaffolds ISBS sur les séquences de scaffold NCBI KL561420.1.

Nous remarquons que le scaffold 1306 est le plus long et 155695 est le plus court.

Entre chaque 2 scaffolds, on trouve un vide dû au manque de la totalité des scaffolds.
On aurait pu combler deux vides si on avait NODE 71209 et le NODE 77023

### Conclusion :

Nous avons grâce à cette méthode pu observer la qualité du séquençage de ISBS. Malgré le fait que nous ne disposions pas des deux scaffolds manquant, nous pouvons dire que cette reconstruction de Novo a été mené à bien.
