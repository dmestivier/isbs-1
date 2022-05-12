# lit un fichier au format PUBMED produit par une
# (nom de fichier a modifier 'data-test.txt')
# interrogation pubmed et extrait les mots-cles 
# (champs `OT`) et associe leur comptage.
# Export au format CSV ( ";"-separateur) dans un fichier
# 'wordcounts.csv'
#
# pour importer dans `www.worldclouds.com`
#
# Mestivier Denis - Mai 2022
#


###
### dictionnaire :
### - cle = key-word
### - val = nombre d'occurences
###

d = {}

###
### Parsing du fichier
###

# fichier a importer

fn = "data-test.txt"

# ouverture du fichier pour lecture
# on cree une variable file-identifier pour acceder a notre fichier

fid = open( fn, "rt" )

# go !

for lig in fid:
    # est-ce que la ligne commence par `OT` ???
    if lig[0:5] == "OT  -":
        # oui.
        # 1. j'ote le debut de la ligne
        kw = lig[6:-1]

        # 2. je vire d'eventuels "*"
        kw = kw.replace("*", "" )

        # 3. j'enregistre
        if kw not in d.keys():
            d[kw] = 0

        d[kw] = d[kw] + 1

# fermeture du fichier. On renseigne notre OS
# que l'on ne va plus s'en servir

fid.close()

# Export du dico dans un fichier "wordcounts.csv"

fout = open( "wordcounts.csv", "wt" )
fout.write( "weight;word;color;url\n" )

for kw in d.keys():
    fout.write( str(d[kw]) + ";" + kw + "\n" )

fout.close()

