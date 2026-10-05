# Index des sections

Le skill cherche ici le fichier de section de chaque équipement de la liste.
L'ordre des lignes est l'ordre des sections dans le document.

## Équipements

| Fabricant | Modèle | Autres noms acceptés | Fichier |
|---|---|---|---|
| Netgear | M4250-8G2XF-PoE+ | GSM4210PX, M4250, commutateur Netgear | netgear-m4250.md |
| Crestron | CEN-SWPOE-10 | commutateur Crestron | crestron-cen-swpoe-10.md |
| Crestron | RMC4 | | crestron-rmc4.md |
| Crestron | MPC4-102-B | MPC4-102, MPC4 | crestron-mpc4-102-b.md |
| Crestron | HD-CTL-101 | HDCTL101 | crestron-hd-ctl-101.md |
| Crestron | HD-PS402 | HDPS402 | crestron-hd-ps402.md |
| Crestron | HD-TX-4KZ-211-2G | HD-TX-211, plaque DM Lite | crestron-hd-tx-4kz-211-2g.md |
| Crestron | AMP-X300 | AMPX300 | crestron-amp-x300.md |
| Crestron | DM-NVX-E20-2G | NVX-E20-2G, E20-2G | crestron-dm-nvx-e20-2g.md |
| Crestron | DM-NVX-363 | NVX-363 | crestron-dm-nvx-363.md |
| Crestron | DM-NVX-D30 | NVX-D30 | crestron-dm-nvx-d30.md |
| Crestron | UC-ENGINE | UC-Engine, UCE | crestron-uc-engine.md |
| Crestron | I12, I20 | 1 Beyond i12, 1 Beyond i20, One Beyond | crestron-1beyond-i12-i20.md |
| QSC | Core 24f | Core, Q-SYS Core (autres modèles Core : confirmer avec l'utilisateur) | qsc-core.md |
| Sennheiser | TCCM | TCC M, TeamConnect Ceiling Medium | sennheiser-tccm.md |
| Sharp | XP-V731U-W | XP-V731U, projecteur Sharp | sharp-xp-v731u-w.md |
| LG | 65PK640S0UB | moniteur LG contrôlé par réseau | lg-65pk640s0ub.md |
| (tout fabricant) | Microphone sans-fil | micro sans-fil | microphone-sans-fil.md |
| (tout fabricant) | Moniteur | écran, afficheur (contrôle RS-232, sans section propre à son modèle) | moniteurs.md |

Équipements vus dans les documents d'origine mais sans section : Crestron DM-NVX-E30,
Crestron CEN-IO-COM-102, Crestron UC-CX100-T, Crestron HD-RXC-4KZ-101. Ils vont seulement dans l'annexe et
sont signalés comme « sans section ».

## Sections conditionnelles

| Condition | Fichier | Emplacement |
|---|---|---|
| Au moins un équipement DM-NVX dans la liste | crestron-dm-nvx-reinitialisation.md | après les sections DM-NVX |
| L'utilisateur indique un programme SIMPL Windows (.lpz/.sig) chargé par SFTP | crestron-chargement-sftp.md | après la section du processeur |

## Programmes (types de salle)

Demander à l'utilisateur quel programme est installé s'il ne l'a pas dit.

| Programme | Fichier |
|---|---|
| Salle de formation et multifonctionnelle | programme-salle-formation.md |
| Salle de présentation | programme-salle-presentation.md |
