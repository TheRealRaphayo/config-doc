# Programme : salle de présentation

**Dernière révision de la section :** 2026-10-05

Cette section décrit le programme de contrôle, pas un équipement. Elle fournit deux parties du document : « Information du système » (au début) et « Configuration logiciel » (après les équipements).

## Information du système

Voici la fonctionnalité du modèle de salle de présentation. Le système est autonome et ne comporte pas de système de conférence intégré. Les sources locales et la plaque murale de la table sont acheminées vers le système de présentation Crestron HD-PS402, qui effectue la commutation automatique vers le projecteur et le moniteur. L'audio du programme est séparé par le HD-PS402 et acheminé vers l'amplificateur Crestron AMP-X300. Le contrôle de la salle est assuré par le clavier processeur Crestron MPC4-102-B. Lorsque le système retourne en mode veille, les ajustements de volume sont réinitialisés à la valeur par défaut. Le système s'allume automatiquement lorsqu'il détecte une source. Le système s'éteint automatiquement après 60 secondes lorsqu'aucune source n'est détectée.

Voici la liste du matériel couvert par ce document :

<!-- INSTRUCTION: ne garder que les lignes des équipements présents dans la liste. Pour un équipement de la liste absent de ce tableau, ajouter une ligne avec la description donnée dans la liste. -->

| Équipement | Description |
|---|---|
| Crestron CEN-SWPOE-10 | Commutateur réseau géré 10 ports, PoE+ sur 8 ports |
| Crestron MPC4-102-B | Processeur 4-Series et clavier de contrôle mural |
| Crestron HD-PS402 | Système de présentation 4x2 4K60 4:4:4 |
| Crestron HD-TX-4KZ-211-2G | Plaque murale émettrice DM Lite, HDMI et USB-C |
| Crestron AMP-X300 | Amplificateur quatre canaux, 300 W |
| Crestron HD-RXC-4KZ-101 | Récepteur DM Lite avec contrôle CEC, IR et RS-232 |
| Sharp XP-V731U-W | Projecteur laser WUXGA, raccordé par HDBaseT |
| LG 65PK640S0UB | Moniteur UHD 65 pouces |

### Interface de contrôle de salle

Le système est équipé d'un clavier Crestron MPC4-102-B qui intègre le processeur de contrôle 4-Series et l'interface usager dans un seul appareil. Les boutons capacitifs permettent la sélection des sources, la mise en marche et l'arrêt du système ainsi que l'ajustement du volume. Le détecteur de proximité réveille l'interface à l'approche de l'usager et la luminosité des boutons s'ajuste automatiquement selon l'éclairage de la salle.

Voici l'assignation des boutons du clavier :

<!-- INSTRUCTION: assignation par défaut du programme. Si l'utilisateur fournit une autre assignation, l'utiliser. -->

| Bouton | Fonction |
|---|---|
| 1 | Plaque murale HDMI & USB-C |
| 2 | Plaque murale HDMI |
| 3 | HDMI 3 (Non utilisé). |
| 4 | HDMI 4 (Non utilisé). |
| Marche / Arrêt | Mise en marche et arrêt du système |
| Volume et sourdine | Ajustement du niveau du programme et sourdine |

## Configuration logiciel

### Fichier de configuration

Lors du téléversement initial du système, le fichier de configuration sera automatiquement créé dans le dossier User du processeur.

### Commandes console usager

Aucune commande usager n'est accessible dans ce système.
