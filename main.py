import pandas as pd



def check_Not_Null(fichier,champ):

        retour=0

        for i in range(len(fichier)):

            valeur = fichier.loc[i, champ]

            if str(valeur) == 'nan' or str(valeur)=='null':




                with open("fichier_log.txt", "a", encoding='utf-8') as f:

                    retour = retour + 1
                    if retour == 1:
                        with open("fichier_log.txt", "a", encoding='utf-8') as f:
                            f.write("\nvérification de la contrainte Null sur la colonne : ")

                            f.write("'")
                            f.write(champ)

                            f.write("'")
                            f.write(" \n")
                            f.write("ligne ")
                            f.write(str(i + 2))
                            f.write(", ")
                            f.write("la valeur ")
                            f.write("'")
                            f.write(str(valeur))
                            f.write("'")
                            f.write("")
                            f.write(" est vide \n")
                    else:
                        with open("fichier_log.txt", "a", encoding='utf-8') as f:
                            f.write("ligne ")
                            f.write(str(i + 2))
                            f.write(", ")
                            f.write("la valeur ")
                            f.write("'")
                            f.write(str(valeur))
                            f.write("'")
                            f.write("")
                            f.write(" est vide \n")



def check_Unique(fichier,champ):
    retour=0
    # déclaration d'une liste pour enrégistrer les données uniques
    liste=[]  # au début la liste est vide
    for i in range(len(fichier)):
        valeur = fichier.loc[i, champ]
        liste.append(valeur)

    for i in range(len(fichier)):
        valeur = fichier.loc[i, champ]
        if (str(valeur) != 'nan' or str(valeur)!='null') and liste.count(valeur)>1:
            if type(valeur)=='int':

                valeur=format(valeur,'0.0f')


            with open("fichier_log.txt", "a", encoding='utf-8') as f:
                retour = retour + 1
                if retour == 1:
                    with open("fichier_log.txt", "a", encoding='utf-8') as f:
                        f.write("\nvérification de la contrainte clé étrangère sur la colonne : ")

                        f.write("'")
                        f.write(champ)

                        f.write("'")
                        f.write(" \n")
                        f.write("ligne ")
                        f.write(str(i + 2))
                        f.write(", ")
                        f.write("la valeur ")
                        f.write("'")
                        f.write(str(valeur))
                        f.write("'")
                        f.write("")
                        f.write(" n'est pas unique \n")
                else:
                    with open("fichier_log.txt", "a", encoding='utf-8') as f:
                        f.write("ligne ")
                        f.write(str(i + 2))
                        f.write(", ")
                        f.write("la valeur ")
                        f.write("'")
                        f.write(str(valeur))
                        f.write("'")
                        f.write("")
                        f.write(" n'est pas unique \n")



def check_primary_key(fichier,champ):
    if str(champ)=="id":
        check_Unique(fichier,champ)

        check_Not_Null(fichier,champ)


def check_foreign_key(etudiant,departement,col_etu,col_dept):
    retour=0
    liste_dept=[]
    #récuperons tous les numéros des département et mettons les dans une liste
    for i in range(len(departement)) :
        valeur = departement.loc[i, col_dept]
        liste_dept.append(str(valeur))

    #Ici notre liste contient la liste des département

    for i in range(len(etudiant)):
        valeur = etudiant.loc[i, col_etu]

        if valeur not in liste_dept:

            with open("fichier_log.txt", "a", encoding='utf-8') as f:
                retour = retour + 1
                if retour == 1:
                    with open("fichier_log.txt", "a", encoding='utf-8') as f:
                        f.write("\nvérification de la contrainte clé étrangère sur la colonne : ")

                        f.write("'")
                        f.write(col_etu)

                        f.write("'")
                        f.write(" \n")
                        f.write("ligne ")
                        f.write(str(i + 2))
                        f.write(", ")
                        f.write("la valeur ")
                        f.write("'")
                        f.write(str(valeur))
                        f.write("'")
                        f.write("")
                        f.write(" n'est pas une clé étrangère \n")
                else:
                    with open("fichier_log.txt", "a", encoding='utf-8') as f:
                        f.write("ligne ")
                        f.write(str(i + 2))
                        f.write(", ")
                        f.write("la valeur ")
                        f.write("'")
                        f.write(str(valeur))
                        f.write("'")
                        f.write("")

                        f.write(" n'est pas une clé étrangère \n")




def check_type(fichier,champ):
    retour=0

    if str(champ)=='id' or str(champ)=="id_dept":
        for i in range(len(fichier)):

                valeur = fichier.loc[i, champ]
                try:
                    valeur=float(valeur)
                    if not valeur.is_integer():

                        retour = retour + 1
                        if retour == 1:
                            with open("fichier_log.txt", "a", encoding='utf-8') as f:
                                f.write("\nvérification de la contrainte type sur la colonne : ")

                                f.write("'")
                                f.write(champ)

                                f.write("'")
                                f.write(" \n")
                                f.write("ligne ")
                                f.write(str(i + 2))
                                f.write(", ")
                                f.write("la valeur ")
                                f.write("'")
                                f.write(str(valeur))
                                f.write("'")
                                f.write("")
                                f.write(" n'est pas un entier \n")
                        else:
                            with open("fichier_log.txt", "a", encoding='utf-8') as f:
                                f.write("ligne ")
                                f.write(str(i + 2))
                                f.write(", ")
                                f.write("la valeur ")
                                f.write("'")
                                f.write(str(valeur))
                                f.write("'")
                                f.write("")
                                f.write(" n'est pas un entier \n")
                except:
                    retour = retour + 1
                    if retour == 1:
                        with open("fichier_log.txt", "a", encoding='utf-8') as f:
                            f.write("\nvérification de la contrainte check sur la colonne : ")

                            f.write("'")
                            f.write(champ)

                            f.write("'")
                            f.write(" \n")
                            f.write("ligne ")
                            f.write(str(i + 2))
                            f.write(", ")
                            f.write("la valeur ")
                            f.write("'")
                            f.write(str(valeur))
                            f.write("'")
                            f.write("")
                            f.write(" n'est pas un entier \n")
                    else:
                        with open("fichier_log.txt", "a", encoding='utf-8') as f:
                            f.write("ligne ")
                            f.write(str(i + 2))
                            f.write(", ")
                            f.write("la valeur ")
                            f.write("'")
                            f.write(str(valeur))
                            f.write("'")
                            f.write("")
                            f.write(" n'est pas un entier \n")







    else:
        if  str(champ)=="nom" or str(champ)=="prenom":
            for i in range(len(fichier)):

                valeur = fichier.loc[i, champ]
                try:
                    valeur = float(valeur)
                    if isinstance(valeur,float) or isinstance(valeur,int):
                        with open("fichier_log.txt", "a", encoding='utf-8') as f:
                            f.write("colonne ")
                            f.write("' ")
                            f.write(champ)
                            f.write("' ")
                            f.write("la valeur  : ")
                            f.write(str(valeur))
                            f.write(" ligne :")
                            f.write(str(i + 2))

                            f.write("'")
                            f.write(" n'est pas une chaîne de caractère \n")


                except:
                    print("")



def check_taille(fichier,champ):
    retour=0
    if str(champ) == "nom" or str(champ) == "prenom" or str(champ) == "mdp" or str(champ) == "login" :
        for i in range(len(fichier)):
            valeur = fichier.loc[i, champ]
            if len(str(valeur))>50:
                retour = retour + 1
                if retour == 1:
                    with open("fichier_log.txt", "a", encoding='utf-8') as f:
                        f.write("\nvérification de la taille sur la colonne : ")

                        f.write("'")
                        f.write(champ)

                        f.write("'")
                        f.write(" \n")
                        f.write("ligne ")
                        f.write(str(i + 2))
                        f.write(", ")
                        f.write("la valeur")
                        f.write("'")
                        f.write(str(valeur))
                        f.write("'")
                        f.write("")
                        f.write(" dépasse 50 caractère \n")
                else:
                    with open("fichier_log.txt", "a", encoding='utf-8') as f:
                        f.write("ligne ")
                        f.write(str(i + 2))
                        f.write(", ")
                        f.write("la valeur ")
                        f.write("'")
                        f.write(str(valeur))
                        f.write("'")
                        f.write("")
                        f.write(" dépasse 50 caractère \n")

def check_check(fichier,champ):
    retour=0
    if str(champ) == "mdp" :
        for i in range(len(fichier)):
            valeur = fichier.loc[i, champ]
            if len(valeur)<8:
                retour=retour+1
                if retour==1:
                    with open("fichier_log.txt", "a", encoding='utf-8') as f:
                        f.write("\nvérification de la contrainte check sur la colonne : ")

                        f.write("'")
                        f.write(champ)

                        f.write("'")
                        f.write(" \n")
                        f.write("ligne ")
                        f.write(str(i + 2))
                        f.write(", ")
                        f.write("la valeur ")
                        f.write("'")
                        f.write(str(valeur))
                        f.write("'")
                        f.write("")
                        f.write(" doit avoir une taille >=8 \n")
                else:
                    with open("fichier_log.txt", "a", encoding='utf-8') as f:
                        f.write("ligne ")
                        f.write(str(i + 2))
                        f.write(", ")
                        f.write("la valeur ")
                        f.write("'")
                        f.write(str(valeur))
                        f.write("'")
                        f.write("")
                        f.write(" doit avoir une taille >=8 \n")


if __name__ == '__main__':

    #importation des deux fichiers
    etudiant = pd.read_csv("Données-Etudiants.csv", header=0, sep=";",decimal=".")
    departement=pd.read_csv("Données-Departements.csv",header=0, sep=";")

    # Appel des fonctions
    check_Not_Null(etudiant,'id')
    check_Not_Null(etudiant,'nom')
    check_Not_Null(etudiant,'prenom')
    check_Not_Null(etudiant,'login')
    check_Not_Null(etudiant,'mdp')
    check_type(etudiant,"id")
    check_type(etudiant,"id_dept")
    check_type(etudiant,"nom")
    check_type(etudiant,"prenom")
    check_Unique(etudiant,'login')
    check_Unique(etudiant,'mdp')
    check_primary_key(etudiant,'id')
    check_taille(etudiant,'nom')
    check_taille(etudiant,'prenom')
    check_taille(etudiant,'login')
    check_taille(etudiant,'mdp')
    check_check(etudiant,'mdp')
    check_foreign_key(etudiant,departement,'id_dept','num_dept')







