CR1

I. Objectifs

Obtenir une vue des publications associées à Physarum polycephalum et en particulier de trouver des mots-clés associés à ces publications pour se donner une idée des domaines
de recherche qui utilisent cet organisme.

II. Méthode

1. récupération des références scientifiques:

• Allez sur le site du NCBI / Entrez
• Sélectionnez la banque de données pubmed
• Lancez une recherche large avec la requête suivante :
– Physarum polycephalum
• Explorez les résultats affichés
• questions :
– combien d’articles proposés ?
• Testez les options d’affichage Display options
• Sélectionnez l’option d’affichage qui permet d’obtenir les informations de mot-clés (tag: OT)
• Sauvegardez votre recherche :
– soit dans un fichier
– soit via un envoi e-mail
• Sauvegardez ce fichier
• Vérifiez avec votre éditeur de texte qu’il comporte l’information attendue.


2. extraction des mots-clés associés

• utiliser le site https://www.wordclouds.com/ pour générer un World cloud
• Utilisez :
– le Notebook Jupyter get-wordcounts-from-pubmed-output.ipynb
– ou le script python get-wordcounts-from-pubmed-output.py

pour extraire les mots-clés de votre interrogation Pubmed et produire un fichier de ces motsclés et de leurs occurences dans le format attendu par le site worldclouds.com.



3. import de ces mots-clés dans un site Web qui construit un “World cloud”

Allez sur le site https://www.worldclouds.com :
• Explorez un peu ce site et ce qu’il propose
• Importez votre fichier de mot-clés
• Explorez les options



• Produisez un Worldcloud des mots-clés associés aux domaines de recherche du Physarum.

III. Résultat

Obtention d'une figure circulaire contenant tous les mots-clés

Options choisies:

Min. word size: 5
Word margin: 2
Canvas padding (%): 5
Text shadow size (slow!): 0
Drawing method: Circles*
Text drawing mode: File
