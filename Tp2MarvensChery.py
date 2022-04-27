'''
@Marvens Chery
@matricule e2162809
@version 1.1 06-12-2021
'''
prenom = str(input("Quel est le prénom du caissier(ère)? : "))
print("Bonjour",prenom,", bon courage en cette journée de travail ! ")

recu = []


                                              #Ajouter un article taxable ou non taxable
def choix1et2(recu):
 article = str(input("veuillez entrez le nom de votre article : "))
 recu.append(article)
 prixu = float(input("veuillez entrez le prix unitaire de l'article : "))
 recu.append(prixu)
 quantité = int(input("veuillez entrez la quantité de  l'article : "))
 recu.append(quantité)
 if choix == 2:
     total = prixu * quantité * 1.14975
     total = (round(total, 2))
 else:
     total = prixu * quantité
 recu.append(total)
 print("Parfait!,",article,"a été ajouté",quantité, "fois a votre recu")



 menu()
                                                      # Supprimer un article

def choix3():

    artsup = str(input("Quel est larticle que vous voulez retirer?: "))
    if recu.count(artsup) == 0:
     print("ERREUR! L'article",artsup," n'a pas été trouvé :(")

    else:
         del (recu[(recu.index(artsup)) + 3])
         del (recu[(recu.index(artsup)) + 2])
         del (recu[(recu.index(artsup)) + 1])
         del (recu[(recu.index(artsup))])
         print("Parfait!",artsup," a été retiré de votre recu ")
    return menu()
                                                           # Générer le recu et quitter
def choix4():

    print("Votre recu")
    print("#####################")
    print("Article   Prixunitaire   Quantité   Total")
    total = 0
    for i in range (0,len(recu),4):
        a = recu[i]

        print( a,"       ",recu[i + 1],"        " ,   recu[i + 2] ,"       ",   recu[i + 3])


    print("-" * 25)
    for m in range (3,len(recu),4):
         total = total  + (recu[m])

    print("le montant  total à payer est de:",total,"$")
    print("Vous avez été servi par",prenom)
    print("Bonne Journée!")
                                                           #Menu des 4 choix
def menu():
            print("Menu")
            print("########################")
            global choix
            print("1- Ajouter un article non-taxable")
            print("2- Ajouter un article taxable")
            print("3- Supprimer un article de la liste d'achat")
            print("4- Générer le recu et quitter")
            choix = int(input("Quel est votre choix? : "))
            if choix == 1 or choix == 2:
                choix1et2(recu)
            elif choix == 3:
                choix3()
            elif choix == 4:
                choix4()
            elif choix > 4 or choix < 4 :
                print("Votre choix doit être entre les chiffres 1 et 4")
                menu()


menu()















