# Problème : Réaliser une table de multiplication de taile 10x10 en utilisant la liste fournie.
# Résultat attendu : un affichage comme ceci :   1  2  3  4  5  6  7  8  9  10
#                                             1  1  2  3  4  5  6  7  8  9  10
#                                             2  2  4  6  8  10 12 14 16 18 20
#                                             . .  .  .  .  .  .  .  .  .  .
# Indication :   L'alignement rectiligne n'est pas une contrainte, tant que la table est visible ligne par ligne c'est ok.
#               Si vous êtes perfectionnistes faites vous plaisir.
liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 32]


def valeur_max(_liste: list) -> int:
    return len(str(liste[-1] * liste[-1]))


def ajout_espace(_nombre: int) -> str:
    buffer = ""
    if _nombre == 0: _nombre = ""
    for e in range(0, espace - len(str(_nombre))):
        buffer += " "
    buffer += str(_nombre)
    return buffer


def table_multiplication(_list: list):
    ligne = ajout_espace(0)
    for item in _list:
        ligne += ajout_espace(item)
    print(ligne)

    for item_y in _list:
        ligne = ajout_espace(item_y)
        for item_x in _list:
            result = item_x * item_y
            ligne += ajout_espace(result)
        print(ligne)


espace = valeur_max(liste) + 1
table_multiplication(liste)
