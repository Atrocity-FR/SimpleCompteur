def compter_lignes(nom_fichier):
    try:
        with open("exemple.txt", 'r') as fichier: # Mettre le nom du fichier
            nombre_lignes = sum(1 for ligne in fichier)
        return nombre_lignes
    except FileNotFoundError:
        print(f"Le fichier '{nom_fichier}' n'a pas été trouvé.")
        return None
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        return None

# Exemple d'utilisation
nom_du_fichier = 'exemple.txt'
resultat = compter_lignes(nom_du_fichier)

if resultat is not None:
    print(f"Le fichier '{nom_du_fichier}' contient {resultat} lignes.")
