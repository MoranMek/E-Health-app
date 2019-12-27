
prenom = "Quel est votre prenom ? : "
a= "Quel est votre age ? : "
b = "Quel est votre sexe ? h pour Homme et f pour femme : "
c = "Quel est votre poids en Kg ? : "
d = "Quel est votre sport pratique ? : "
sports_pratique = "sports de contact/combats=0 ,sports d'addresse=1,sports de fond/endurance=2 : "
t = "Utilisez vous un traitement particulier ? 'oui' ou 'non' : "
quelt = "Quel traitement prenez vous ? : "
allergie = "Avez vous des allergies connues ? 'oui' ou 'non' : "
allergi_util = "Quelles allergies ? : "
nature1 = "Douleur=0,Gonflement=1,Invalidite=2,antecedants comparable=3 : "
nature = "Pourquoi avez vous besoin de consulter ? : "
liste_nature = ['0', '1', '2', '3']
liste_sport = ['0', '1', '2']
douleur = "Ou avez vous mal ? : "
liste_endroit_douleur = ['cheville', 'genoux', 'hanche', 'bassin', 'coude', 'poignet', 'épaule', 'cou', 'ventre']
liste_endroit_douleur2 = ['Cheville','Genoux','Hanche','Bassin', 'Coude','Poignet','Epaule','Cou', 'Ventre', 'CHEVILLE',
                          'GENOUX', 'HANCHE','BASSIN','COUDE','POIGNET','EPAULE','COU','VENTRE','Cheville','Genoux',
                          'Hanche','Bassin', 'Coude','Poignet','Epaule','Cou', 'Ventre', 'CHEVILLE','GENOUX', 'HANCHE',
                          'BASSIN','COUDE','POIGNET','EPAULE','COU','VENTRE',]
liste_douleur = ['tendon', 'Tendon', 'TENDON', 'articulation', 'Articulation', 'ARTICULATION', 'articulaire',
                 'Articulaire', 'ARTICULAIRE', 'muscle', 'Muscle', 'MUSCLE', 'muscles', 'Muscles', 'MUSCLES',
                 'Autre', 'autre', 'AUTRES', ' Autres', ' autre', ' Autre', ' AUTRE', ' AUTRES']
liste_date_douleur = ['quelques semaines', 'quelques jours', 'plusieurs mois']
Kine_Ostheo = 0.0
Cardiologue = 0.0
Gynecologue = 0.0
Nutritionniste = 0.0


name = input(prenom)
print("Bonjour", name)

age = int(input(a))
while (age < 0 or age > 100):
    age = int(input(a))
if (age>50) :
    Cardiologue = Cardiologue +3
elif (age<50 and age>30 ):
    Cardiologue = 2 + Cardiologue
elif (age<30):
    Cardiologue = Cardiologue + 1


sexe = input(b)
while (sexe != "h" and sexe != "f"):
    sexe = input(b)

if sexe == "h":
    Gynecologue = Gynecologue - 500
elif sexe == "f":
    Gynecologue = Gynecologue + 2


taille = int(input("Quelle taille faites-vous ? (en cm)"))
                                                                #inclure blindage si taille n'est pas un int redemander
while (taille <0):
    taille = int(input("Quelle taille faites-vous ? (en cm)"))

poids = int(input(c))
while (poids < 0):
    poids = int(input(c))

IMC = poids/((taille/100)*(taille/100))
if (IMC < 18):
    Nutritionniste = Nutritionniste + 3
elif (IMC > 18 and IMC < 25):
    Nutritionniste = Nutritionniste
elif (IMC > 25 and IMC < 30):
    Nutritionniste = Nutritionniste + 3
    Cardiologue = Cardiologue + 2
    Kine_Ostheo = Kine_Ostheo + 1
elif (IMC > 30 and IMC < 35):
    Nutritionniste = Nutritionniste + 4
    Cardiologue = Cardiologue + 3
    Kine_Ostheo = Kine_Ostheo + 3
elif (IMC > 35):
    Nutritionniste = Nutritionniste + 4
    Cardiologue = Cardiologue + 4
    Kine_Ostheo = Kine_Ostheo + 4

Oui_ou_Non = input('Pratiquez vous un sport ? Oui ou Non ')
while(Oui_ou_Non != "Oui" and Oui_ou_Non !="Non" and Oui_ou_Non != "oui" and Oui_ou_Non != " Oui" and Oui_ou_Non != " Non" and Oui_ou_Non != " non"):
    Oui_ou_Non = input('Pratiquez vous un sport ? Oui ou Non')

if (Oui_ou_Non == "Oui" or Oui_ou_Non == "oui"):
    print(sports_pratique)
    sport = input(d)
    while (sport not in liste_sport):
        sport = input(d)
        break
 

traitement = input(t)
while (Oui_ou_Non != "Oui" and Oui_ou_Non !="Non" and Oui_ou_Non != "oui" and Oui_ou_Non != " Oui" and Oui_ou_Non != " Non" and Oui_ou_Non != " non"):
    traitement = input(t)

if (traitement == "oui"):
    quel_traitement = input(quelt)
else:
    print("Parfait !")

allergiesconnues = input(allergie)
while (Oui_ou_Non != "Oui" and Oui_ou_Non !="Non" and Oui_ou_Non != "oui" and Oui_ou_Non != " Oui" and Oui_ou_Non != " Non" and Oui_ou_Non != " non"):
    allergiesconnues = input(allergie)

if (allergiesconnues == "oui" or allergiesconnues == "Oui" or allergiesconnues == " oui" or allergiesconnues == " Oui" or allergiesconnues == "OUI" or allergiesconnues == " OUI"):
    allergieclient = input(allergi_util)

else:
    print("Ok")

print(nature1)
natureconsul = input(nature)
while (natureconsul not in liste_nature):
    natureconsul = input(nature)
print(liste_endroit_douleur)
oudouleur = input(douleur)
while (oudouleur not in liste_endroit_douleur):
    oudouleur = input(douleur)

endroitdouleur = input("Pensez vous que la douleur provient du : Articulation, Muscle ou Autre :")
while (endroitdouleur not in liste_douleur):
    endroitdouleur = input("Pensez vous que la douleur provient du : Articulation, Muscle ou Autre :")

if (endroitdouleur == 'Muscle' or endroitdouleur == 'Articulation' or endroitdouleur == ' Muscle' or
        endroitdouleur == ' Articulation' or endroitdouleur== 'muscle' or endroitdouleur == ' muscle'):
    Kine_Ostheo == Kine_Ostheo+2
    break

print(liste_date_douleur)
datedouleur = input("Depuis combien de temps avez vous mal ? :")
while (datedouleur not in liste_date_douleur):
    datedouleur = input("Depuis combien de temps avez vous mal ? :")



print("Kine_Osthéopath = ", Kine_Ostheo)
print("Cardiologue = ", Cardiologue)
print("Nutritionniste = ", Nutritionniste)
print("Gynécologue = ", Gynecologue)