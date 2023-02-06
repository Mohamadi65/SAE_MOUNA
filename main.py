import pandas as pd


def Not_Null(fichier,nom_colonne):



        for i in range(len(fichier)):
            # print(format(row.id,'0.0f'), row.nom)
            valeur = fichier.loc[i, nom_colonne]

            if str(valeur) == 'nan' or str(valeur)=='null':
                #print("différent de null", format(valeur, '0.0f'))



                with open("fichier_log.txt", "a", encoding='utf-8') as f:

                        f.write("la colonne ")
                        f.write("'")
                        f.write(nom_colonne)
                        f.write("'")
                        f.write(" à la ligne ")
                        f.write(str(i + 2))
                        f.write(" est vide alors qu'il ne doit pas l'être \n")



def Unique(fichier,nom_colonne):
    # déclaration d'une liste pour enrégistrer les données uniques
    liste=[]  # au début la liste est vide
    for i in range(len(fichier)):
        valeur = fichier.loc[i, nom_colonne]
        liste.append(valeur)

    for i in range(len(fichier)):
        valeur = fichier.loc[i, nom_colonne]
        if (str(valeur) != 'nan' or str(valeur)!='null') and liste.count(valeur)>1:
            if type(valeur)=='int':

                valeur=format(valeur,'0.0f')


            with open("fichier_log.txt", "a", encoding='utf-8') as f:
                f.write("la valeur  : ")
                f.write(str(valeur))
                f.write(" qui est presente à la ligne ")
                f.write(str(i+2))
                f.write(" de la colonne ")
                f.write("'")
                f.write(nom_colonne)
                f.write("'")
                f.write(" n'est pas unique , ce qui contrarie la contrainte d'unicité de la colonne\n")



def primary_key(fichier,nomcolonne):
    with open("fichier_log.txt", "a", encoding='utf-8') as f:
        f.write("Vérification de la contrainte de la clé primaire  : ")

    Unique(fichier,nomcolonne)
    Not_Null(fichier,nomcolonne)

if __name__ == '__main__':
    fichier = pd.read_csv("C:/code/python/Mouna/Données-Etudiants.csv", header=0, sep=";")
    Not_Null(fichier,'id_dept')
    Unique(fichier,'nom')
    primary_key(fichier,'id')