import re

# Définition des opérations de base

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    # Vérification pour éviter la division par zéro
    if y == 0:
        raise ValueError("Division par zéro impossible")
    return x / y

# Fonction principale de la calculatrice

def calculator():
    # Liste pour stocker l'historique des calculs
    history = []

    while True:
        print("\nCalculatrice9000")
        print("Opérateurs disponibles : +, -, *, /")
        print("Entrez 'exit' pour quitter")

        # Demande à l'utilisateur d'entrer une expression mathématique
        expression = input("Entrez une expression mathématique : ")

        # Vérification de l'option de sortie
        if expression.lower() == 'exit':
            break

        # Validation de l'expression pour éviter les entrées invalides
        if not re.match(r'^[-+*/.0-9\s]+$', expression):
            print("Erreur : Entrée invalide")
            continue

        try:
            # Découpage de l'expression en numéros et opérateur
            num1, operator, num2 = re.split(r'([-+*/])', expression)

            # Conversion des numéros en nombres flottants
            num1 = float(num1.strip())
            num2 = float(num2.strip())

            # Calcul en fonction de l'opérateur
            if operator == '+':
                result = add(num1, num2)
            elif operator == '-':
                result = subtract(num1, num2)
            elif operator == '*':
                result = multiply(num1, num2)
            elif operator == '/':
                result = divide(num1, num2)
            else:
                raise ValueError("Opération non supportée")

            # Affichage du résultat
            print("Résultat : {}".format(result))

            # Stockage de l'expression et du résultat dans l'historique
            history.append(expression + " = " + str(result))

        except ValueError as e:
            # Gestion des erreurs spécifiques
            print("Erreur :", str(e))
        except Exception as e:
            # Gestion des erreurs générales
            print("Erreur inattendue :", str(e))

    # Affichage de l'historique des calculs après la sortie de la boucle
    print("\nHistorique des calculs :")
    for entry in history:
        print(entry)

# Appel de la fonction principale pour exécuter la calculatrice
calculator()