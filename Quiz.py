Points=0

def ask(question,answer):
    if input(question) == answer:
        print("Correct!")
        return 1
    else:
        print("Incorrect")
        return 0
Points += ask("What is 1+1? ", "2")
Points += ask("What is Skibiti's surname? ", "Toilet")
Points += ask("What is a cure for deppresion? ", "Fortnite")
Points += ask("What is the best state in the U.S.A.? ", "Ohio")
Points += ask("Who is the most skibiti Ohio Town Rizzard of Oz thing out there in Fortnite? ", "Renegade Raider")
print("You got", Points * 20, "percent.")
x