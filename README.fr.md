<p align="center">
  <img src="assets/hero.png" alt="Skills de marketing Threads pour Claude Code et Codex, open source sous licence MIT" width="900" />
</p>

[English](README.md) | **Français**

# Skills de marketing Threads pour Claude Code et Codex

<p align="center">
  <img src="https://img.shields.io/github/v/release/NeedyMindset/needythreads?color=111827&label=release" alt="Dernière release">
  <img src="https://img.shields.io/badge/Claude_Code-Compatible-D97757?logo=anthropic&logoColor=white" alt="Compatible Claude Code">
  <img src="https://img.shields.io/badge/Codex-Compatible-111827" alt="Compatible Codex">
  <img src="https://img.shields.io/badge/Claude-Skills-8A63D2" alt="Claude Skills">
  <img src="https://img.shields.io/badge/License-MIT-22C55E.svg" alt="Licence MIT">
  <img src="https://img.shields.io/github/stars/NeedyMindset/needythreads?style=social" alt="Étoiles GitHub">
  <img src="https://img.shields.io/badge/PRs-welcome-F59E0B.svg" alt="PRs bienvenues">
</p>

**8 skills qui transforment Claude Code et Codex en équipe de contenu pour Threads.** Ils écrivent des posts et des threads avec ta voix et des hooks validés sur un corpus, rédigent des réponses, lisent ta niche à partir de données réelles et planifient une semaine de contenu. Chaque brouillon est débarrassé des tics d'IA et attend ta validation avant toute publication. Aucun code requis.

Une fois installé, demande simplement à Claude Code ou à Codex, par exemple :

- "Écris un post Threads sur [sujet]"
- "Transforme ces notes en thread"
- "Qu'est-ce qui marche sur Threads dans ma niche ? (lit de vraies données via Apify)"
- "Réécris ça pour que ça sonne humain"

Le bon skill s'active automatiquement. Tu relis et tu valides ensuite.

## Installation

Choisis la méthode qui correspond à ton outil, Claude Code ou Codex :

### Codex CLI

```bash
codex plugin marketplace add NeedyMindset/needythreads
codex plugin add needythreads@needythreads
```

Pour tester un clone local avant de publier des modifications :

```bash
git clone https://github.com/NeedyMindset/needythreads.git
cd needythreads
codex plugin marketplace add .
codex plugin add needythreads@needythreads
```

### claude.ai (web)

1. Ouvre https://claude.ai/code
2. Va dans **Skills** dans la barre latérale
3. Clique sur **Add from GitHub**
4. Colle : `NeedyMindset/needythreads`
5. C'est fait. Les skills s'activent automatiquement quand tu parles de Threads.

### Claude Desktop (Mac / Windows)

1. Ouvre Claude Desktop
2. Ouvre **Settings** (l'icône d'engrenage)
3. Va dans **Skills**
4. Clique sur **Add from GitHub**
5. Colle : `NeedyMindset/needythreads`
6. C'est fait. Lance une nouvelle conversation et demande à Claude d'écrire un post Threads.

### Claude Code (CLI / VS Code / JetBrains)

```
/plugin marketplace add NeedyMindset/needythreads
/plugin install needythreads@needythreads
```

Ou clone le dépôt et ouvre-le comme dossier de travail :

```bash
git clone https://github.com/NeedyMindset/needythreads.git
cd needythreads
```

### OpenClaw

1. Ouvre ton dossier de travail OpenClaw
2. Clone les skills dedans :
   ```bash
   git clone https://github.com/NeedyMindset/needythreads.git
   ```
3. Dans les réglages d'OpenClaw, ajoute ceci au prompt système :
   ```
   You have Threads marketing skills in ./needythreads/.
   For any Threads task, read the relevant skills/*/SKILL.md first.
   Use lib/url_parser.py for URL parsing and lib/publora_client.py for publishing.
   ```
4. C'est fait. Demande à OpenClaw d'écrire un post Threads.

### Hermes Agent

Hermes Agent (Nous Research) suit le standard ouvert agentskills.io et charge directement `skills/*/SKILL.md`. Clone le bundle dans ton dossier de skills Hermes :

```bash
git clone https://github.com/NeedyMindset/needythreads.git ~/.hermes/skills/needythreads
```

Tu viens d'OpenClaw ? `hermes claw migrate` importe ces skills automatiquement. Appelle ensuite `/<nom-du-skill>` depuis n'importe quelle interface de chat Hermes.

### N'importe quel agent (CLI skills)

Une seule commande qui fonctionne avec Claude Code, Codex, Cursor et tout autre agent qui lit des fichiers SKILL.md :

```bash
npx skills add NeedyMindset/needythreads
```

> **Ce projet t'est utile ? [Mets une étoile au dépôt](https://github.com/NeedyMindset/needythreads).** Les annuaires de Claude Code et de Codex classent et filtrent selon le nombre d'étoiles, donc une étoile est ce qui rend ces skills trouvables pour la personne suivante. C'est la seule chose demandée. Sans inscription, sans email.

## Ce que tu peux faire

Une fois installé, demande simplement de l'aide sur Threads à Claude Code ou à Codex. Le bon skill s'active automatiquement.

**Écrire un post :**
> "Écris-moi un post Threads sur la raison pour laquelle la plupart des agents IA échouent sur les relances, pas sur le raisonnement. Ton chaleureux."

**Transformer une idée en thread :**
> "Transforme mes notes en thread Threads sur la façon dont on a réduit la latence de notre agent de 9 s à 2,1 s."

**Vérifier un brouillon avant de publier :**
> "Audite ce post Threads : tics d'IA et limite de 500 caractères : [colle ton texte]"

**Décortiquer un post viral :**
> "Quel hook utilise ce thread ? https://www.threads.net/@demo/post/abc (je te colle le texte)"

**Répondre à un créateur :**
> "Rédige une réponse à ce post Threads, je veux apporter de la valeur sans polémiquer : https://www.threads.net/@demo/post/abc"

**Planifier ta semaine :**
> "Planifie une semaine de contenu Threads. Je construis un agent IA en public pour des développeurs indépendants."

Chaque skill te montre d'abord un brouillon et attend ton accord. Rien n'est publié sans ta validation.

## Les 8 skills

| Skill | Ce qu'il fait |
|---|---|
| **Post Writer** | Rédige un post Threads unique ou un thread de plusieurs posts avec une formule de hook Threads 2026 choisie selon l'objectif : réponses, reposts, likes ou citations. Respecte la limite de 500 caractères (10 000 avec une pièce jointe texte) et le plafond d'un seul hashtag |
| **Humanizer** | Retire les tics d'IA auxquels les lecteurs réagissent : vocabulaire d'IA 2026 noté par densité dans chaque post, ponts de révélation, piles de fragments saccadés, triades empilées, sincérité jouée. Plafonne les tirets longs à un par post au lieu de les interdire, et ne force jamais le rythme (un rythme uniforme gagne sur Threads, quelle que soit la longueur). Ne promet pas de battre les détecteurs (aucune retouche n'y arrive de façon fiable). Inclut un contrôle avant publication `--mode audit` (longueur de 500 caractères, hook, plafond d'un hashtag, placement du lien, ton chaleureux) |
| **Hook Extractor** | Décortique le hook de n'importe quel post ou thread viral sur Threads. Le rattache à l'une des 13 formules Threads et renvoie un gabarit vierge à remplir |
| **Reply Drafter** | Rédige une réponse ou un post de citation à valeur ajoutée pour l'URL de n'importe quel post Threads. Décide entre réponse et citation. Une réponse à un autre utilisateur est un post séparé, donc le brouillon revient sous forme de bloc à copier-coller |
| **Repurposer** | Transforme du contenu d'une autre plateforme (post LinkedIn, thread X, article de blog, script YouTube, newsletter) en post ou thread Threads natif : réchauffe le ton, enlève le style corporate, redimensionne en post court ou thread léger, reconstruit le hook pour passer le "soft fold", retire les artefacts propres à l'autre plateforme et passe le tout dans l'Humanizer |
| **Content Planner** | Crée un plan hebdomadaire avec un mélange posts uniques et threads, des hooks par jour, des horaires de publication, des cibles de réponses quotidiennes et un contrôle de l'équilibre des objectifs |
| **Profile Optimizer** | Audite et réécrit un profil Threads de bout en bout : photo, nom avec un mot-clé recherchable, @handle, bio (150 caractères, chaleureuse et précise), lien, post épinglé, et le lien avec Instagram connecté qui alimente la découverte sur Threads. Renvoie une grille de notation, des correctifs prioritaires et des réécritures avant/après |
| **Audience Insights** | Lit ton audience et ta niche à partir de données réelles (via Apify, sans connexion) : scanne une requête ou un hashtag pour trouver les meilleurs posts du moment avec likes, réponses, reposts et citations, et récupère un profil (le tien ou celui d'un concurrent) avec nombre d'abonnés, bio, statut vérifié et posts récents avec leur engagement. Threads verrouille la liste des personnes qui interagissent, donc il s'agit de découverte et de statistiques de profil, pas d'une liste de likers |

## Comment fonctionnent les threads sur Threads

Threads plafonne un post à **500 caractères** (10 000 si tu joins le texte long). Pour tout contenu plus long, tu construis un thread de plusieurs posts. Avec l'API native de Threads, cela signifie créer un conteneur pour le post 1, le publier, puis créer chaque post suivant avec un `reply_to_id` qui pointe vers le précédent, et gérer les échecs partiels.

Ce bundle confie toute la chaîne à [Publora](https://publora.com). Tu écris le thread en un seul bloc (ou tu le découpes avec `---`), et Publora le découpe automatiquement en thread connecté aux frontières de paragraphe puis de phrase, et le publie en un seul appel. Contrairement à X, Threads n'ajoute pas de marqueurs `(1/N)` par défaut. Le skill Post Writer utilise cela après ta validation.

## Optionnel : publier automatiquement avec Publora

Par défaut, les skills rédigent le contenu pour que tu le copies-colles dans Threads. Si tu veux que Claude Code ou Codex publie directement les posts et les threads, connecte Publora. Cela prend environ 2 minutes.

### Qu'est-ce que Publora ?

[Publora](https://publora.com) est une API de publication qui transforme un seul appel `create-post` en thread Threads complet (et peut aussi publier le même contenu sur X, LinkedIn, Instagram et d'autres plateformes).

Publora propose aussi des [skills MCP officiels](https://github.com/publora/skills) (`npx skills add publora/skills`) : un skill par plateforme, qui ne couvrent que la publication. Ce bundle est la couche au-dessus, qui ajoute la lecture, le savoir-faire d'écriture et le processus de validation.

### Configuration (2 minutes)

**Étape 1.** Inscris-toi sur https://app.publora.com/signup (gratuit)

**Étape 2.** Connecte Threads : clique sur **Channels** dans la barre latérale gauche, puis **Add Channel**, choisis **Threads** et autorise.

**Étape 3.** Trouve ton Platform ID : va dans **Channels** et clique sur ton compte Threads. L'ID ressemble à `threads-17841412345678`. Copie-le en entier, préfixe `threads-` compris.

**Étape 4.** Récupère ta clé API : clique sur **Settings** (l'engrenage en bas à gauche), puis **API**, puis **Create Key**. Copie la chaîne `sk_...`.

**Étape 5.** Crée un fichier nommé `.env` dans le dossier needythreads :

```
PUBLORA_API_KEY=sk_paste_your_key_here
THREADS_PLATFORM_ID=threads-paste_your_id_here
```

Si tu as cloné le dépôt, copie plutôt le gabarit :

```bash
cp .env.example .env
```

Ouvre ensuite `.env` et remplace les valeurs d'exemple par tes vraies valeurs.

**Étape 6.** Installe deux petits paquets Python :

```bash
pip install requests python-dotenv
```

**Étape 7.** Teste. Demande à Claude Code ou à Codex :

> "Programme un post Threads de test via Publora dans 24 heures : 'test de la connexion API, je l'annulerai dans le dashboard'."

Si Publora renvoie un `postGroupId`, c'est bon. Annule le post dans le dashboard Publora avant l'heure programmée. Si tu obtiens une erreur HTTP 401, ta clé API est incorrecte. Si tu obtiens l'erreur `Invalid platform ID format`, ton `THREADS_PLATFORM_ID` est incorrect. Voir [Dépannage](#dépannage).

> **À propos des réponses :** une réponse au post d'un autre utilisateur est un post séparé que le `create-post` de Publora ne peut pas cibler, donc le Reply Drafter renvoie toujours son brouillon sous forme de bloc à copier-coller que tu publies toi-même. Les posts uniques et tes propres threads sont publiés automatiquement.

## Optionnel : générer des illustrations avec Pixfaro

Un visuel donne un coup de pouce à un post Threads. Le Post Writer peut générer une illustration ou une quote-card de ton hook et la joindre automatiquement à la publication. Sans clé, il rédige le prompt d'image et te demande de la générer toi-même, donc rien ne casse.

[Pixfaro](https://pixfaro.com) est une API d'images unique qui couvre plusieurs modèles (de `flux-schnell` à 0,004 $ jusqu'à `gpt-5-image`). Elle superpose ton handle, ta couleur de marque ou ton logo à l'image avec une **incrustation au pixel près**, donc même un modèle de base bon marché produit un texte net sur une quote-card. Récupère ces champs de marque dans ton [profil de voix et de marque](references/voice-profile.md) (section 6) et chaque visuel reste cohérent avec ta marque.

Configuration : ajoute `PIXFARO_TOKEN=pf_live_...` dans ton `.env`. Le client léger `lib/pixfaro_client.py` et les fonctions `lib.illustrate(prompt, kind="square")` et `lib.refine(image_id, instruction)` renvoient une URL hébergée qui alimente directement `lib.publish(..., media_urls=[url])`. `refine` modifie une image précédente à partir de son id (moins cher que de la régénérer) ; les résultats contiennent `cost`, `balance_after` et un indicateur `premium`, pour que les skills ne dépensent jamais discrètement sur un modèle coûteux.

## Optionnel : lire de vraies données Threads avec Apify

`threads-audience-insights` scanne une requête ou un hashtag pour trouver les posts qui circulent en ce moment (texte, likes, réponses, reposts, citations) et récupère le nombre d'abonnés, la bio et les derniers posts d'un profil. Sans identifiant de lecture, il te demande de coller ce que tu vois, donc rien ne casse.

**Avec un shell**, ajoute un token gratuit dans ton `.env` :

```
APIFY_TOKEN=apify_api_...
```

**Sur claude.ai**, où un skill n'a pas d'environnement pour stocker un token, ajoute plutôt le serveur MCP d'Apify comme connecteur personnalisé :

```
https://mcp.apify.com?actors=igview-owner/threads-search-scraper,apify/threads-profile-api-scraper
```

Connecte-toi avec OAuth à la première utilisation, aucune clé n'est stockée sur disque. **Garde le filtre `?actors=`** : le serveur sans filtre `https://mcp.apify.com` donne aussi à l'agent `search-actors` et `call-actor`, qui exécutent n'importe quel actor du Store Apify au prix que cet actor facture.

Deux choses à savoir dans les deux cas : l'actor de recherche facture un minimum de 20 posts par exécution, donc en demander 5 coûte quand même 20, et Threads verrouille entièrement la liste des likers, donc il s'agit de découverte et de statistiques de profil, jamais d'une liste de personnes qui interagissent. Détails et correspondance des champs : [`references/mcp-read-layer.md`](references/mcp-read-layer.md).

## Règles de voix

Chaque skill suit automatiquement ces règles :

1. Tirets longs plafonnés à un par post. Ce caractère a cessé d'être un indice en 2026 ; c'est la densité qui en est un.
2. Mets des majuscules aux noms. Toujours. Écrire une marque en minuscules fait négligé.
3. Pas de grappes de vocabulaire d'IA. Un marqueur 2026 ("leverage", "significant", "streamline", "foster") dans un post est de l'anglais ; trois dans un même post ressemble à de l'IA et le post est réécrit. (Ces mots concernent l'anglais ; les skills appliquent le même principe en français.)
4. Les chiffres précis valent mieux que les adjectifs. "2,4x" vaut mieux que "bien meilleur".
5. Une idée par post. La première ligne porte tout (le fil tronque avec "plus").
6. 500 caractères par post. 0 à 1 hashtag (Threads n'en autorise qu'un), 0 à 2 emojis.
7. Chaleureux et conversationnel, pas un clash importé de X.

## Dépannage

| Problème | Solution |
|---|---|
| Les skills ne s'activent pas quand je parle de Threads | Vérifie que tu as installé via le panneau Skills, `/plugin install` ou `codex plugin add`. Essaie une nouvelle conversation. |
| "PUBLORA_API_KEY not set" | Ton fichier `.env` est absent ou au mauvais endroit. Il doit être à la racine du dossier `needythreads/`. |
| "401 Invalid API key" de Publora | Ta clé API est incorrecte ou révoquée. Va dans Publora, Settings, API, et crée une nouvelle clé. |
| "Invalid platform ID format" | Ton `THREADS_PLATFORM_ID` est incorrect. Va dans Channels sur Publora et copie la chaîne `threads-...` complète. |
| Mon deuxième hashtag a disparu | Threads n'autorise qu'un hashtag par post. La plateforme supprime les suivants. Utilise-en un, à la fin. |
| Mon thread ne s'est pas publié en posts connectés | Le chaînage de plusieurs posts peut être temporairement suspendu pendant que Meta traite la reconnexion de l'application Threads. Publie le premier post, puis ajoute les autres en réponse à la main. |
| Ma réponse ne s'est pas publiée automatiquement | Une réponse à un autre utilisateur est un post séparé que Publora ne peut pas cibler. Le Reply Drafter renvoie un bloc à copier-coller. Publie-le toi-même. |
| `pip install` échoue | Utilise un environnement virtuel : `python -m venv venv && source venv/bin/activate && pip install requests python-dotenv` |

## Références transversales

- [`references/hook-formulas.md`](references/hook-formulas.md) - les 13 formules de hook Threads avec leurs squelettes et leurs étiquettes d'objectif
- [`references/algorithm-heuristics.md`](references/algorithm-heuristics.md) - signaux de classement Threads 2026, horaires et limites
- [`references/voice-rules.md`](references/voice-rules.md) - les règles de voix de référence dont chaque skill hérite

---

<details>
<summary><b>Pour les développeurs : compatibilité d'exécution, analyse d'URL et fonctionnement interne</b></summary>

## Compatibilité d'exécution

```
needythreads/
  skills/             frontmatter SKILL.md ; natif pour Claude Code et Codex, lu comme du markdown ailleurs
  .codex-marketplace/ paquet Codex imbriqué généré (lance scripts/sync_codex_marketplace.py)
  lib/                Python pur, fonctionne dans n'importe quel environnement d'agent
  references/         markdown pur, fonctionne partout
  scripts/            CLI Python pur, fonctionne partout
```

| Environnement | Découverte automatique des skills ? | Configuration |
|---|---|---|
| **Claude Code** (CLI, Desktop, Web, IDE) | Oui | Installe via le plugin ou clone. Les skills s'activent sur les prompts correspondants. |
| **Codex CLI** | Oui | `codex plugin marketplace add NeedyMindset/needythreads` puis `codex plugin add needythreads@needythreads`. |
| **Anthropic Managed Agents** (`/v1/agents`) | Oui | Passe les fichiers de skills dans le contexte de l'agent. |
| **Cursor / Cline / Aider** | Manuelle | Lis les fichiers `SKILL.md` comme contexte de prompt ; importe `lib/` en Python. |
| **LangChain / AutoGen** | Non | Utilise `lib/` comme paquet ; fournis `references/` comme contexte de prompt. |

## Démarrage rapide pour un agent Python générique

```python
import sys; sys.path.insert(0, "path/to/needythreads")
from lib import parse_threads_url, PubloraClient, publish

parsed = parse_threads_url("https://www.threads.net/@needymindsetshop/post/C8H9abcDEf_")
print(parsed["handle"], parsed["post_id"])  # needymindsetshop C8H9abcDEf_

# Côté écriture (Publora) - un post unique ou un thread (le contenu long est découpé automatiquement)
client = PubloraClient()  # lit PUBLORA_API_KEY dans l'environnement
client.create_post(
    content="First post of the thread\n\n---\n\nSecond post\n\n---\n\nThird post",
    platforms=["threads-17841412345678"],
)

# Ou utilise l'enveloppe de haut niveau qui gère l'aiguillage manuel / Publora / diy
publish("thread", draft_text="...", target_url="https://www.threads.com/",
        platforms=["threads-17841412345678"])
```

## Gestion des URL

`lib/url_parser.py` analyse les URL de posts et de profils Threads sur les deux domaines :

| Fragment d'URL | Résultat |
|---|---|
| `threads.net/@HANDLE/post/CODE` | `{handle, post_id, url_type: "post"}` |
| `threads.com/@HANDLE/post/CODE` | identique (normalisé en threads.com) |
| `threads.com/@HANDLE` | `{handle, url_type: "profile"}` |

```bash
python lib/url_parser.py "https://www.threads.net/@needymindsetshop/post/C8H9abcDEf_"
```

## Pourquoi une réponse est un post séparé

LinkedIn aplatit les fils de réponses sur 2 niveaux et exige l'URN du commentaire de premier niveau comme parent. Threads non : les réponses s'imbriquent naturellement et il n'y a aucun URN de commentaire parent à résoudre. Le Reply Drafter se contente donc de rédiger le texte. Le `create-post` de Publora ne peut pas cibler le post d'un autre utilisateur, donc la publication d'une réponse est une étape de copier-coller par conception.

</details>

## Références

- [Documentation de l'API Publora](https://docs.publora.com) - référence des endpoints de la couche de publication
- [API Threads (Meta for Developers)](https://developers.facebook.com/docs/threads/) - l'API Graph officielle de Threads derrière les heuristiques 2026

## Qui construit ce projet

NeedyThreads est construit par NeedyMindset, une agence de marketing web spécialisée dans l'automatisation NoCode, les tunnels de vente, les chatbots IA et la génération de leads. Nous construisons les systèmes qui transforment une voix publique en conversations et en clients : qualification de prospects, relances automatisées, workflows de contenu et infrastructure de publication.

Ce dépôt est la couche supérieure open source de cet ensemble. L'automatisation en dessous, c'est ce que nous construisons pour nos clients.

## Licence

MIT. Propulsé par [Publora](https://publora.com).

Voir aussi : le [dépôt Anthropic Skills](https://github.com/anthropics/skills) et l'annuaire `awesome-claude-skills`.
