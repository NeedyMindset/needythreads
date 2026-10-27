# Profil de voix et de marque (Voice & Brand Profile)

Ta voix, ta niche et tes règles au même endroit. Remplis-le une fois (ou laisse `threads-humanizer --mode profile` le construire à partir de quelques-uns de tes vrais posts), et chaque skill d'écriture de ce bundle Threads le lit avant de rédiger : tu n'as plus à réexpliquer qui tu es à chaque demande.
Ceci est le gabarit vide du plugin. Ta version remplie est enregistrée dans `~/.needythreads/voice-profile.md`, en dehors du plugin, pour que les mises à jour ne l'effacent pas. Modifie-la librement. Rien n'est envoyé nulle part, il sert seulement à orienter les brouillons. Les skills ne le chargent que si `filled: yes` figure ci-dessous ; un gabarit vide est ignoré.

## Statut (Status)

- filled: no
- source: template
- updated: --

## Légende des statuts

Chaque ligne remplie porte un statut en fin de ligne :

- `[confirmé]` : tu l'as écrit toi-même, avec tes mots. Les skills l'utilisent sans en changer le sens.
- `[à confirmer]` : une déduction. Les skills te demandent avant de l'utiliser, et ne la présentent jamais comme un fait.
- `[interdit]` : à ne jamais utiliser.

Une ligne sans statut est traitée comme `[à confirmer]`. Une section vide reste vide : rien n'est deviné, ni le réseau d'où viennent tes exemples, ni ton genre, ni un lien, ni un chiffre.

Ce fichier dit **comment tu écris** : voix, audience, règles, appels à l'action. Les faits de ton parcours (chiffres, histoires, noms) vivent dans la Banque d'histoires, pas ici.

## 1. Empreinte de voix (Voice fingerprint)

- Rythme des phrases :
- Débuts de phrase habituels :
- Habitudes de ponctuation :
- Mots et expressions que tu utilises souvent :
- Mots et expressions que tu n'utilises JAMAIS :
- Emoji :
- Format (Threads) : 500 caractères maximum par post ; longueur cible pour un post seul : 350 à 500 caractères (change ce chiffre si tu préfères plus court) ; ton chaleureux et conversationnel ; un seul hashtag maximum
- Signature (une seule phrase de clôture ; si tu en as plusieurs, dis laquelle sert pour quel type de post) :

## 2. Qui tu es et pour qui tu écris (Who you are)

- Tu es :
- Ton audience (ICP) :
- Tes piliers de contenu :

## 3. Règles strictes : toujours / jamais (Hard rules)

- Toujours :
- Jamais :

## 4. Liens et appel à l'action (Links and CTA)

- Lien principal vers lequel tu envoies les gens : (laisse vide s'il n'existe pas encore : un lien n'est jamais inventé)
- Où il se place :
- Ton style d'appel à l'action :

## 5. Exemples signature (Signature examples)

Colle 2 à 4 de tes vraies lignes ou posts Threads qui te ressemblent le plus. Les skills d'écriture imitent le rythme et le choix des mots de ces exemples, pas une voix générique.

-
-
-

## 6. Éléments de marque, pour les illustrations (Brand assets)

Utilisés par l'étape d'illustration (`lib.illustrate`) pour garder chaque image fidèle à ta marque grâce à une incrustation au pixel près. Tout est facultatif ; laisse vide pour ne pas incruster.

- Pseudo à afficher sur les images : (ex. @tonpseudo)
- Couleur de marque (hex) : (ex. #0A66C2)
- Logo : (chemin ou `logo_id` Pixfaro, si tu en as un)
- Position de l'incrustation : (ex. en bas à droite)
- Style visuel par défaut : (ex. vectoriel plat minimal ; éditorial marqué ; photo douce)
