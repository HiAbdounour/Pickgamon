# Pickgamon

Pickgamon est un jeu de cartes initialement conçu en tant que projet final de fin d'année de spé NSI lorsque j'étais en Terminale.

**NOTE : Le jeu n'a pas été modifié. Ce repo présente le jeu exactement comme il était au moment de sa programamtion en 2024.**

***Note supplémentaire : Le jeu fut conçu avec les dimensions d'un écran PC de bureau (1920x1080). Récemment testé sur un PC portable (donc de dimensions plus petites), le jeu passe correctemet. Cela dit, il se peut que la fenêtre puisse dépasser pour des dimensions spécifiques.***

## Règles du jeu :

Il y a 4 joueurs (vous et 3 bots). Chaque joueur commence la partie avec **quatre cartes chacun**.\
Chacun son tour, le joueur a le choix entre **piocher une carte (quotat limité)** et **échanger une de ses cartes avec celle d'un autre joueur**. Ce choix se fait quasiment à l'aveugle : vous devez cliquer sur la carte du joueur adverse que vous souhaitez (présentée face cachée), puis sur celle de votre deck que vous souhaitez échanger. Vous découvrez la carte que vous avez choisie UNE FOIS L'ÉCHANGE EFFECTUÉ.\
L'objectif est de **finir avec 4 cartes identiques** avant les autres joueurs.

Le quotat de pioche est **fixé à 4** sur l'ensemble d'une partie; ce nombre monte à **5 si vous activez la carte ``WIN``**.\
Mais attention ! Des cartes spéciales se cachent dans cette pioche et peuvent pimenter votre avancée vers la victoire !

## Les 8 cartes

Voici les 8 cartes normales différentes utilisées dans le jeu. Chacune de ces cartes est présente exactement 4 fois. Posséder 4 cartes identiques permet de gagner la partie.

<table>
  <tr>
    <td><img width="80" height="120" alt="arabic card" src="https://github.com/user-attachments/assets/4a830a9d-5ccd-4226-96d7-d9aa45bbbce0" /></td>
    <td><img width="80" height="120" alt="charabia card" src="https://github.com/user-attachments/assets/4a3514f3-1473-4dca-8fbe-6fdd528fd229" /></td>
    <td><img width="80" height="120" alt="chinese card" src="https://github.com/user-attachments/assets/97a80670-d9a0-4511-8d89-2d46599aa72e" /></td>
    <td><img width="80" height="120" alt="egyptian card" src="https://github.com/user-attachments/assets/9cfbaafc-1119-4e0b-8629-9c8ea30ce6d8" /></td>
    <td><img width="80" height="120" alt="greek card" src="https://github.com/user-attachments/assets/cce2ef6b-ed61-4165-a6e8-50187970f46b" /></td>
    <td><img width="80" height="120" alt="korean card" src="https://github.com/user-attachments/assets/d470e74d-0abc-4289-9f1b-4647da154a0b" /></td>
    <td><img width="80" height="120" alt="russian card" src="https://github.com/user-attachments/assets/1970b7e2-9470-4c4e-9a77-b6e6fbed7a28" /></td>
    <td><img width="80" height="120" alt="topsxi card" src="https://github.com/user-attachments/assets/26bff0e8-161f-4488-8c62-f4a1c41a11a2" /></td>
  </tr>
  <tr>
    <td>Carte "arabic"</td>
    <td>Carte "charabia"</td>
    <td>Carte "chinese"</td>
    <td>Carte "egyptian"</td>
    <td>Carte "greek"</td>
    <td>Carte "korean"</td>
    <td>Carte "russian"</td>
    <td>Carte "Topsxi"</td>
  </tr>
</table>

## Les cartes spéciales

Quelque soit la partie, 3 cartes spéciales figurent toujours dans la pioche :

<table>
  <tr>
    <td><img width="80" height="120" alt="pick card" src="https://github.com/user-attachments/assets/47060e95-aa52-4f71-a9b3-546ac10afb69" /></td>
    <td><img width="80" height="120" alt="don card" src="https://github.com/user-attachments/assets/b7e7b2e0-69ee-4464-805f-210ad677c110" /></td>
    <td><img width="80" height="120" alt="spick card" src="https://github.com/user-attachments/assets/8e2c5bf6-40b3-4997-8d09-5945d6a42e7b" /></td>
  </tr>
  <tr>
    <td>Carte Pick</td>
    <td>Carte Don</td>
    <td>Carte Spick</td>
  </tr>
  <tr>
    <td>Vous permet de voler une carte à un adversaire (donc sans perdre une de vos cartes)</td>
    <td>Vous oblige à donner une de vos cartes à un adversaire (choisi aléatoirement)</td>
    <td>Protège une de vos cartes (au choix) d'être volée ou échangée jusqu'à la fin de la partie</td>
  </tr>
</table>

Il est également possible d'activer la présence de la carte WIN **dans les paramètres** :

<table>
  <tr><td><img width="80" height="120" alt="win card" src="https://github.com/user-attachments/assets/5a98e0f4-1b3d-4e4f-ab0d-45f6730adcc1" /></td></tr>
  <tr><td>Carte WIN</td></tr>
  <tr><td>Vous gagnez instantanément la partie (même si vous n'avez pas 4 cartes identiques)</td></tr>
</table>

Cette carte se trouve obligatoirement dans la pioche.\
En activant la présence de cette carte, tous les joueurs obtiennent **un 5e coup de pioche autorisé**.

## Changelog

Actuellement, je ne prévois pas de faire de mises à jour mais je ne mets pas le repo en archive au cas où. Dans ce cas, ouvrez une Pull Request ou une Issue.

À noter (bug connu):
- les joueurs 2 (à gauche) et 3 (à droite) peuvent avoir leur dernière carte à moitié coupée (sort à moitié de la fenêtre). Ce bug ne gêne pas au jeu.

## Licences :
```
Les assets (cartes et fonds) sont réalisés par moi-même et sont fournis avec la licence CC0.

La musique et les sons : honnêtement, je ne sais plus d'où ils viennent mais me connaissant, ce sont sûrement
des extraits récupérés sur une vidéo YouTube statuant une autorisation (par exemple "LIBRE DE DROITS" ou "NO COPYRIGHT").
 
Le code dans le fichier `game.py` a été entièrement écrit par moi-même. Il est fourni sous la licence MIT.
Le code dans le fichier `libx.py` provient d'une librairie Python mise à disposition par les professeurs de la spécialité NSI du lycée Les Pierres Vives. Tous les droits leur restent affiliés.
```
