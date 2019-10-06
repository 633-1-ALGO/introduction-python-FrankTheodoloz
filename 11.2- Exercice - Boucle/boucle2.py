# Problème : Etant donné un tableau B de "n" nombres réels, on demande de trier le tableau B avec le tri par insertion
# Données : un tableau B de n nombre réels
# Résultat attendu : Le tableau B trié

B = [2, 6, 8, 5, 4, 12, 98, 34, 1]


def tri_insertion(_list: list) -> list:
    i = 1  # indice départ (0 considéré comme classé)
    while i < len(_list):
        valeur = _list[i]
        indice_test = i - 1  # indice précédent
        while valeur < _list[indice_test] and indice_test >= 0:
            _list[indice_test + 1] = _list[indice_test]  # déplace l'indice précédent vers la droite
            _list[indice_test] = valeur
            indice_test -= 1
        i += 1

    return _list


print(tri_insertion(B))
