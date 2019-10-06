# Problème : Calculer le prix TTC d'une nombre d'articles ayant un prix unitaire donné. Avec une T.V.A à 7.7%.
# Données : Nombres d'articles et prix unitaire HT
# Résultat attendu : Un message "Le prix TTC est de XXX.XXX chf." Utilisez la fonction print().

nb_articles = 13
prix_ht = 42.75

print("Le prix TTC est de", nb_articles * prix_ht * 107.7 / 100, "chf")  # Le prix TTC est de 598.5427500000001 chf

print("Le prix TTC est de",
      "{:.2f}".format(round(nb_articles * prix_ht * 107.7 / 100 * 2, 1) / 2),
      "chf")  # Le prix TTC est de 598.55 chf
