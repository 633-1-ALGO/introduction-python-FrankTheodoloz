# Problème : Etant donné un tableau A de "n" nombres réels, on demande la moyenne des nombres du tableau
# Données : un tableau A de n nombre réels
# Résultat attendu : Moyenne des nombres réels du tableau A
A = [1, 5, 15, 25, 10, 55, 50, 35]


def moyenne_tableau(_list: list) -> float:
    i = 0
    somme = 0

    while i < len(_list):
        somme += _list[i]
        i += 1

    return somme / i


print(moyenne_tableau(A))
