# University Paris Dauphine - PSL

### Ce code permet de prédire la prochaine lettre d'un mot en utilisant un dictionnaire de fréquences pour chaque lettre suivante de chaque lettre de l'alphabet, en se basant sur un texte obtenu à partir d'une URL donnée.
### La fonction get_text récupère le texte à partir d'une URL en utilisant la bibliothèque requests pour récupérer la réponse HTTP et BeautifulSoup pour extraire le texte HTML.
### La fonction create_letter_dict crée le dictionnaire de fréquences pour chaque lettre suivante en utilisant la méthode update du dictionnaire pour incrémenter les occurrences de la lettre suivante pour chaque lettre.
### La fonction predict_next_letter prédit la lettre suivante en se basant sur le dictionnaire de fréquences et en choisissant aléatoirement la lettre la plus fréquente parmi les lettres suivantes.
### Enfin, le code génère 10 mots de 5 lettres à partir des prédictions.
