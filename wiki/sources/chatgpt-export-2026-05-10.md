---
title: Export de données ChatGPT (2026-05-10)
type: source
domain: perso
tags: [chatgpt, openai, export, donnees-personnelles]
created: 2026-06-02
updated: 2026-06-02
sources: []
links: ["[[sidy]]"]
---

# Export de données ChatGPT (2026-05-10)

## Référence
Export complet des données du compte ChatGPT de l'utilisateur, généré par OpenAI le **2026-05-10**.

## Accès
- Archive ZIP brute conservée **uniquement sur le serveur** dans `raw/` (non versionnée — voir `.gitignore`).
- Contenu : `conversations-000.json` + `conversations-001.json` (140 conversations), `user.json`, `user_settings.json`, `message_feedback.json`, `shared_conversations.json`, `export_manifest.json`, `chat.html`, et ~45 médias (images, générations DALL·E).

## Données extraites lors de l'INGEST du 2026-06-02
- Bloc `user_profile` (profil que ChatGPT affichait dans chaque conversation).
- Bloc `user_instructions` (préférences de réponse).
- `user.json` : année de naissance (les coordonnées sensibles — téléphone, e-mail — n'ont **pas** été reportées dans le wiki).

## Notes
- Les 140 conversations ne sont **pas** ingérées à ce stade (réserve pour de futurs INGEST thématiques).
- Provenance des faits de la page [[sidy]].
