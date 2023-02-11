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
        f.write("\n\n")
        unicite =Unique(fichier,nomcolonne)
        if unicite:
            f.write("cool")
        vide=Not_Null(fichier,nomcolonne)
        f.write("\n\n")

def foreign_key(etudiant,departement,col_etu,col_dept):
    liste_dept=[]
    #récuperons tous les numéros des département et mettons les dans une liste
    for i in range(len(departement)) :
        valeur = departement.loc[i, col_dept]
        liste_dept.append(str(valeur))

    #Ici notre liste contient la liste des département

    for i in range(len(etudiant)):
        valeur = fichier.loc[i, col_etu]
        print(type(valeur))
        if valeur not in liste_dept:
            print("not correspond",valeur)
    liste2=[]
    for i in liste_dept:
        liste2.append(int(i))

    for i in liste2:
        print(type(i))

# définition de la fonction type
def check_type(fichie,colname):
    for i in range(len(fichier)):
        valeur = fichier.loc[i, colname]
        print(type(valeur))

if __name__ == '__main__':

    # définition de la structure de données
    database_schema=[ {"nom_champ":"id","type":"integer","contrainte":['notnull','unique']},
               {"nom_champ":"nom","type":"character","taille":50,"contrainte": ['notnull']},
               {"nom_champ":"prenom","type":"character","taille":50,"contrainte": ['notnull',"unique"]},
               {"nom_champ": "login", "type": "character", "taille": 50, "contrainte": ['notnull', "unique"]},
               {"nom_champ": "mdp", "type": "character", "taille": 50, "contrainte": {'notnull':"true", "unique":"true","check":{"min":8}}},
               {"nom_champ": "id_dept", "type": "integer"}
               ]




    fichier = pd.read_csv("C:/code/python/Mouna/Données-Etudiants.csv", header=0, sep=";")
    departement=pd.read_csv("Données-Departements.csv",header=0, sep=";")
    """Not_Null(fichier,'id_dept')
    Unique(fichier,'nom')
    primary_key(fichier,'id')
    """

    check_type(fichier,'nom')
    #foreign_key(fichier,departement,'id_dept','num_dept')
