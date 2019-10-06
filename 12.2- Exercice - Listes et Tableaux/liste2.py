# Problème : Etant donné un tableau, afficher l'indice du tableau comportant la valeur la plus elevée.
# Résultat attendu : Un affichage comme ceci : "La valeur maximum est :  x  et elle se trouve à l'indice [ n ][ m ]

tab = [[4, 7, 3, 20, 42], [2, 4, 5, 7, 2], [23, 24, 15, 75, 23]]


def valeur_max(_tableau: list) -> None:
    val_max = 0
    max_x = 0
    max_y = 0
    x = 0
    y = 0

    for tab_y in _tableau:
        for val_x in tab_y:
            if val_x > val_max:
                val_max = val_x
                max_x = x
                max_y = y
                x += 1
        y += 1
    print(_tableau)
    print("La valeur maximum est :", val_max, "et elle se trouve à l'indice [", max_y, "][", max_x, "] ([ ligne ][ valeur ])")


valeur_max(tab)
