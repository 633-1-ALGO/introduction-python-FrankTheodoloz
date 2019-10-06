# Consigne : Rechercher le nombre d'occurences du mot "exemple" et l'afficher. Remplacer le mot "est" par "représente".
# Bonus : Inverser le sens de lecture.
texte = "Ceci est un exemple exemplaire d'exemple exempté d'exemple."
liste_mots: list
liste_mots_recursif: list = []


def remplacer_mot(_texte: str, _mot_cherche, _nouveau_mot) -> str:
    print("Remplacement du mot \"" + _mot_cherche + "\" par \"" + _nouveau_mot + "\"")
    return _texte.replace(_mot_cherche, _nouveau_mot)


def texte_split(_texte: str) -> list:
    return _texte.split(" ")


def compter_occurence(_liste: list, _lookup: str) -> None:
    i = 0
    for word in _liste:
        if _lookup in word:
            i += 1
    print("Il y a", i, "fois le mot \"" + _lookup + "\" dans le texte")


def afficher_texte_inverse(_texte: str) -> None:
    i = len(texte) - 1
    j = 0
    texte_inverse = ""
    while i >= 0:
        i -= 1
        j += 1
        texte_inverse = texte_inverse + str(_texte[i])

    print("le texte à l'envers :")
    print(texte_inverse)


def lire_mots_recursif(_texte: str, _start_pos: int = 0, _list_index: int = 0) -> None:
    while _start_pos < len(_texte) - 1:

        i = _start_pos
        while (not _texte[i].isspace()) and i < len(_texte) - 1:
            i += 1
        liste_mots_recursif.append(_texte[_start_pos:i])
        _list_index += 1
        _start_pos = i + 1

        lire_mots_recursif(_texte, _start_pos, _list_index)
        break  # ne pas continuer après récursion terminée


def afficher_texte_mots_inverse(_liste: list) -> None:
    print("les mots du texte à l'envers : ")
    i = len(_liste) - 1
    texte_mots_inverse = ""
    while i >= 0:
        texte_mots_inverse = texte_mots_inverse + str(_liste[i]) + " "
        i -= 1
    print(texte_mots_inverse)


texte = remplacer_mot(texte, "est", "représente")
liste_mots = texte_split(texte)

compter_occurence(liste_mots, "exemple")
afficher_texte_inverse(texte)

lire_mots_recursif(texte)
afficher_texte_mots_inverse(liste_mots_recursif)
