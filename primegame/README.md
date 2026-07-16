# Prime Game

## Description

Maria et Ben jouent à un jeu basé sur les nombres premiers. Étant donné un ensemble d'entiers consécutifs de `1` à `n` inclus, ils choisissent chacun leur tour un nombre premier présent dans l'ensemble et retirent ce nombre ainsi que tous ses multiples. Le joueur qui ne peut plus jouer perd la partie.

Ils jouent `x` parties, `n` pouvant être différent à chaque partie. Maria commence toujours en premier, et les deux joueurs jouent de façon optimale. Le programme détermine le gagnant de chaque partie et retourne le nom du joueur ayant remporté le plus de parties.

## Exemple

```
carrie@ubuntu:~/primegame$ cat main_0.py
#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner


print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))

carrie@ubuntu:~/primegame$ ./main_0.py
Winner: Ben
carrie@ubuntu:~/primegame$
```

### Déroulement d'une partie (n = 4)

* Maria choisit 2 et retire 2, 4 → il reste 1, 3
* Ben choisit 3 et retire 3 → il reste 1
* Maria ne peut plus jouer → **Ben gagne**

## Prototype

```python
def isWinner(x, nums)
```

* `x` : nombre de parties jouées
* `nums` : tableau contenant la valeur de `n` pour chaque partie
* Retourne le nom du joueur (`"Maria"` ou `"Ben"`) ayant gagné le plus de parties
* Retourne `None` si le gagnant ne peut pas être déterminé (égalité)

## Contraintes

* `n` et `x` ne dépassent pas `10000`
* Aucun import de package n'est autorisé

## Algorithme

Choisir un nombre premier `p` et retirer ses multiples revient simplement à "consommer" un nombre premier parmi ceux ≤ `n`, car tout nombre composé est multiple d'un nombre premier plus petit qui aura forcément déjà été retiré. Les nombres composés ne peuvent donc jamais être choisis directement.

Le nombre total de coups possibles dans une partie est donc égal au **nombre de nombres premiers ≤ n** :

* Si ce nombre est **impair**, Maria (qui joue en premier) joue le dernier coup → **Maria gagne**
* Si ce nombre est **pair**, Ben joue le dernier coup → **Ben gagne**

### Complexité

Un crible d'Ératosthène est calculé une seule fois jusqu'à `max(nums)`, puis un tableau cumulatif du nombre de premiers permet de répondre à chaque partie en `O(1)`.

* Construction du crible : `O(n log log n)`
* Traitement des `x` parties : `O(x)`

## Fichiers

| Fichier | Description |
|---|---|
| `0-prime_game.py` | Contient la fonction `isWinner(x, nums)` |

## Repository

* GitHub repository : `holbertonschool-interview`
* Directory : `primegame`

## Auteur

Soufiane Filali (Souf) — Holberton School Toulouse
