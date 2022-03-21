from itertools import count
import os
import sys
from unicodedata import numeric

number_of_tries = 0
print("""

Witaj w WISIELCU !!!

""")

print("1. Easy")
print("2. Medium")
print("3. Hard")

while True:
    print()
    level = input("Wybierz poziom trudności: ")
    if level.count(str(1)):
        number_of_tries = 7
        break
    elif level.count(str(2)):
        number_of_tries = 5
        break
    elif level.count(str(3)):
        number_of_tries = 3
        break  
    else:
        print("Podaj numer podany przy poziomie trudności.")


while True:
    print()
    word = input("Podaj słowo do odgadnięcia: ")
    if len(word) > 15 or len(word) < 3:
        print("Słowo nie może mieć więcej niż 15 liter i nie mniej niż 3.")
    elif word.islower() == False:
        print("Słowo musi być tylko z małych liter")
    elif word.isalpha() == False:
        print("Słowo nie może zawierać znaków specjalnych i liczb.")
    else:
        break

user_word = []
used_letters = []

def find_indexes(word, letter):
    indexes = []

    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)

    return indexes

def show_state_of_game():
    print(user_word)
    print("Pozostało prób:", number_of_tries)
    print("Użyte litery:", used_letters)
    print()

def restart_game():
    restart = sys.executable
    os.execl(restart, restart, * sys.argv)

###

for _ in word:
    user_word.append("_")
    
continue_loops = True
while True:
    while True:
        
        while True:
            letter = input("Podaj literę: ")          
            if letter.isalpha() == False:
                print("""
                Źle podana litera ! 

                Info:
                Nie używaj liczby ani żadnych znaków specjalnych !
                Musi być podana mała literka !
                """) 
            elif letter.islower() == False:
                print("""
                    Źle podana litera ! 

                    Info:
                    Nie używaj liczby ani żadnych znaków specjalnych !
                    Musi być podana mała literka !
                    """) 
            elif len(letter) > 1:
                    print("Podaj JEDNĄ literke !")
            else:
                break

                

        used_letters.append(letter)

        found_indexes = find_indexes(word, letter)
                    
        if len(found_indexes) == 0:
            print()
            print("Nie ma takiej litery.")
            number_of_tries -= 1

            if number_of_tries  == 4:

                print("""
                
                
                
                
                
                
                
                _______
                """)
            elif number_of_tries == 3:
                
                print("""
                
                |       
                |    
                |   
                |     
                |
                |
                |_______
                """)
            elif number_of_tries == 2:

                print("""
                ____
                |    |   
                |    
                |   
                |     
                |
                |
                |_______
                """)
            elif number_of_tries == 1:

                print("""
                ____
                |    |   
                |    O
                |     
                |
                |
                |_______
                """)
            else:

                print("""
                ____
                |    |   
                |    O
                |   /|\     Game Over !!!
                |   / \  
                |
                |
                |_______
                """)            
        
            if number_of_tries == 0:
                print("Game over")
                sys.exit(0)
        else: 
            for index in found_indexes:
                user_word[index] = letter

            if "".join(user_word) == word:
                print("""
                WINNER !!!
                """)
                while True:
                    user_choice = input("Czy chcesz zagrać jeszcze raz ? (Y/N) :")
                    if user_choice.count("Y"):
                        restart_game()
                    elif user_choice.count("N"):
                        sys.exit(0)
                    else:
                        print("Podaj tylko możliwe opcje")
        show_state_of_game()


            

                    
        