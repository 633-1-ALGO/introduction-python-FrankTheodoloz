# Problème : Déterminer si une année est bissextile ou non. Pour cela, il faut avoir ces règles en tête :
#                   Si une année n'est pas multiple de 4, on s'arrête là, elle n'est pas bissextile.
#                   Si elle est multiple de 4, on regarde si elle est multiple de 100.
#                       Si c'est le cas, on regarde si elle est multiple de 400.
#                           Si c'est le cas, l'année est bissextile.
#                           Sinon, elle n'est pas bissextile.
#                       Sinon, elle est bissextile.
#
# Résultat attendu : Un message affichant "Année bissextile" ou "Année non bissextile"


def test_annee_bissextile(_annee: int) -> None:
    if _annee % 4 != 0:
        print(_annee, ": Année non bissextile")
    elif _annee % 100 == 0:
        if _annee % 400 == 0:
            print(_annee, ": Année bissextile")
        else:
            print(_annee, ": Année non bissextile")
    else:
        print(_annee, ": Année bissextile")


test_annee_bissextile(1900)

for annee in range(1980, 2020):
    test_annee_bissextile(annee)
