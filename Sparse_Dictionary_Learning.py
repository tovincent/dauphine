import requests
import random
import re
from bs4 import BeautifulSoup

# Récupérer le texte à partir d'une URL
def get_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    paragraphs = soup.find_all('p')
    text = ''
    for p in paragraphs:
        text += p.get_text() + ' '
    return text

# Créer un dictionnaire des 5 lettres les plus fréquentes pour chaque lettre de l'alphabet
def create_letter_dict(text):
    unique_words = set(text.split())
    letter_dict = {}
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        letter_dict[letter] = {}
        for word in unique_words:
            if word.startswith(letter):
                for i in range(len(word)-1):
                    if word[i] == letter:
                        next_letter = word[i+1]
                        letter_dict[letter][next_letter] = letter_dict[letter].get(next_letter, 0) + 1
        top_letters = sorted(letter_dict[letter], key=letter_dict[letter].get, reverse=True)[:5]
        letter_dict[letter] = top_letters
    return letter_dict

# Calculer le nombre moyen de lettres par mot
def calculate_avg_word_length(text):
    words = text.split()
    total_letters = sum(len(word) for word in words)
    avg_word_length = total_letters / len(words)
    return round(avg_word_length)

# URL du livre à utiliser
url = 'https://www.gutenberg.org/cache/epub/17489/pg17489-images.html#Chapitre_VI'

# Obtenir le texte du livre
text = get_text(url)

# Créer le dictionnaire des 5 lettres les plus fréquentes pour chaque lettre de l'alphabet
letter_dict = create_letter_dict(text)

# Afficher le dictionnaire
print(letter_dict)

# Calculer le nombre moyen de lettres par mot
avg_word_length = calculate_avg_word_length(text)

# Afficher le résultat
print(f"Le nombre moyen de lettres par mot est : {avg_word_length}")

def generate_word(letter_dict, letter):
    # Obtenir les lettres les plus fréquentes pour cette lettre
    next_letters = letter_dict[letter]
    next_letter = random.choice(next_letters) if next_letters else ''

    # Générer le mot de 5 lettres
    word = letter + next_letter
    for i in range(3):
        if next_letter in letter_dict:
            next_letters = letter_dict[next_letter]
            if next_letters:
                sorted_counts, sorted_letters = zip(*sorted(zip([next_letters.count(letter) for letter in next_letters], next_letters), reverse=True))
                next_letter = sorted_letters[0]
                word += next_letter
            else:
                break
        else:
            break
    return word

# Générer un mot de 5 lettres pour chaque lettre de l'alphabet avec les lettres du dictionnaire
for letter in 'abcdefghijklmnopqrstuvwxyz':
    if letter in letter_dict:
        word = generate_word(letter_dict, letter)
        if word:
            print(f"Pour la lettre '{letter}', le mot généré est '{word}'")
    else:
        print(f"Aucun mot généré pour la lettre '{letter}' car elle n'existe pas dans le dictionnaire.")
