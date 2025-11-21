 ## Projet d'Animations avec Pygame

Ce projet contient trois scripts Pygame démontrant différentes fonctionnalités : animation d'images, formes animées et texte avec effet machine à écrire.

# Prérequis

- Python 3.x

- Pygame installé

Installer Pygame :

pip install pygame
# Contenu du projet

1- `Animation d'images`/ (animation_images.py)

- Charge plusieurs images (arbre1.png à arbre4.png) pour créer une animation.

- Affiche les images à une position fixe et fait défiler l'animation en boucle.

- La vitesse de l'animation peut être ajustée avec la variable speed.

- Limite la boucle à 60 FPS pour un rendu fluide.

2- `Animation de formes`/ (animation_formes.py)

- Affiche un cercle bleu qui se déplace horizontalement et rebondit sur les bords de la fenêtre.

- Possibilité d'afficher un rectangle, un triangle ou une image en décommentant les sections correspondantes.

- La vitesse et la position des formes sont personnalisables avec les variables speed, x et y.

3- `Texte avec effet machine à écrire`/ (texte_machine_a_ecrire.py)

- Affiche un texte sur une image de fond (cyber.png) avec un effet "machine à écrire".

- Utilise Pygame pour afficher le texte caractère par caractère.

- Couleur, police et vitesse de frappe peuvent être modifiées (font, CYAN, typing_speed).

- Fenêtre de dimension 900x400 pour mieux mettre en valeur l'animation texte + image.

# Exécution

Lancer un script à la fois depuis le terminal :

python animation_images.py
python animation_formes.py
python texte_machine_a_ecrire.py
# Personnalisation

- `Images` : remplacer les fichiers .png par vos propres images.

- `Vitesse` : modifier les variables speed ou typing_speed.

- `Positions` : ajuster x, y ou les coordonnées du texte pour changer l’emplacement des éléments.

- `Formes` : décommenter ou ajouter des formes avec pygame.draw.

# Notes

- Assurez-vous que toutes les images utilisées sont dans le même dossier que les scripts.

- Chaque script est indépendant et peut être exécuté seul.

- Ce projet est idéal pour comprendre les bases de Pygame : animation, gestion des événements, affichage d’images et texte.