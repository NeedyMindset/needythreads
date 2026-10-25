# Banque d'histoires (Story Bank)

La matière brute de tes posts Threads : ce que tu as réellement fait, en chiffres, avec des noms et des dates. Le Profil de voix contient *comment tu parles*. Celui-ci contient *ce que tu as à dire*.

Chaque skill d'écriture de ce bundle le lit avant de rédiger : il arrête de te demander « un chiffre précis ou un moment » à chaque demande et puise dans ce que tu lui as déjà dit une fois.

Sur Threads, les sections qui rapportent le plus sont les Tournants et les Histoires récurrentes : la plateforme vit de la conversation, et une histoire invite à répondre là où une affirmation invite à scroller. Les Positions comptent toujours, mais formulées comme les tiennes, pas comme une correction adressée au lecteur.

> **Garde ce fichier hors de git.** Il contient des détails de carrière, des chiffres, des échecs et des noms de personnes. Ceci est le gabarit vide du plugin. Ta version remplie est enregistrée dans `~/.needythreads/story-bank.md`, en dehors du plugin : une mise à jour ne l'efface pas et elle n'est jamais envoyée dans git. Rien ici n'est envoyé à un service.

Remplis-le en lançant `threads-humanizer --mode interview`, qui t'interroge et écrit ce fichier. Tu peux aussi le modifier à la main à tout moment ; le skill lit ce qui s'y trouve.

## Statut (Status)

- filled: no
- updated: (date)
- sessions: (nombre d'interviews qui y ont contribué)

---

## 1. Sur quoi tu travailles (What you are working on)

Le projet en cours, décrit comme tu le dirais à voix haute. Threads récompense l'inachevé et l'honnête : cette section n'a pas besoin d'une réponse polie pour être utile.

- (...)

## 2. Chiffres clés (Receipts)

Les chiffres que tu peux citer sans vérifier. C'est la section que les brouillons utilisent le plus, car un chiffre à la précision inhabituelle avec un référent nommé est le signal le plus fort qu'un humain a écrit le post.

Bien : « délai de déploiement passé de 22 à 9 minutes, équipe de quatre, T2 2025 ».
Inutile : « efficacité nettement améliorée ».

- (chiffre, ce qu'il mesure, quand, à qui ou à quoi il se rapporte)

## 3. Réalisations (Shipped)

Ce qui existe parce que tu y as travaillé. Produits, migrations, recrutements, articles, événements, sauvetages.

- (ce que c'était, ta part, ce que ça a coûté ou rapporté)

## 4. Tournants (Turning points)

Les moments où tu as changé d'avis ou où le plan a changé sous tes pieds. Ils portent mieux les posts que les réussites, et ce sont les plus difficiles à inventer.

- (ce qui s'est passé, ce que tu croyais avant, ce que tu crois maintenant)

## 5. Cicatrices (Scars)

Ce qui a mal tourné et ce que ça t'a appris. Séparé des tournants car la forme diffère : une cicatrice est un coût payé, pas un avis révisé.

- (ce qui a cassé, le coût réel, ce que tu fais autrement)

## 6. Positions (Positions)

Des opinions que tu défendrais devant une salle qui n'est pas d'accord. Une position qui ne coûte rien à tenir n'en est pas une ; note ce que la tenir te coûte.

- (l'affirmation, qui n'est pas d'accord, pourquoi tu la tiens quand même)

## 7. Histoires récurrentes (Recurring stories)

Les trois ou quatre que tu racontes déjà à voix haute, au dîner ou en entretien. Elles ont fait leurs preuves : tu sais qu'elles touchent. Écris-les ici avant qu'un brouillon ne les émousse.

- (l'histoire en deux lignes, et le point qu'elle illustre)

## 8. Noms que tu peux citer (Names you can use)

Personnes, entreprises, outils et lieux que tu peux nommer en public, et ceux que tu ne peux pas. Les brouillons restent vagues quand ils ne savent pas lesquels sont lesquels.

- Libre de nommer : (...)
- Ne jamais nommer : (...)
- Demander d'abord : (...)

## 9. Hors limites (Off limits)

Sujets qui restent hors des posts quelle que soit leur performance : affaires en cours, litiges, santé, affaires des autres, tout ce qui est sous NDA.

- (...)


---

## Comment les brouillons l'utilisent

- Un brouillon a besoin d'un détail concret : il le prend dans **Chiffres clés** ou **Réalisations** plutôt que de te le demander en pleine session.
- Une accroche a besoin d'un renversement ou d'un aveu : c'est dans **Tournants** et **Cicatrices** qu'ils se trouvent.
- Un post a besoin d'un argument : **Positions** fournit l'affirmation et l'opposition.
- Tout ce qu'un brouillon ne peut pas sourcer ici, il le demande ou l'omet. Il n'invente pas de chiffre. Si tu vois un chiffre inconnu dans un brouillon, c'est un bug à signaler.
