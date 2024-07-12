import random
zelist=[

    "apple", "berry", "mango", "peach", "grape", "lemon", "basil", "chili", "olive", "onion",
    "bread", "cream", "steak", "toast", "jelly", "honey", "lemon", "minty", "sugar", "spice",
    "wheat", "yeast", "bacon", "beans", "chips", "fruit", "melon", "peach", "squid", "sushi",
    "sauce", "jammy", "toasty", "tangy", "zesty", "pasta", "pizza", "salad", "tacos", "quich",
    "fancy", "scone", "prawn", "fishy", "berry", "crust", "crumb", "apple", "berry", "mango",
    "peach", "grape", "lemon", "basil", "chili", "olive", "onion", "bread", "cream", "steak",
    "toast", "jelly", "honey", "lemon", "minty", "sugar", "spice", "wheat", "yeast", "bacon",
    "beans", "chips", "fruit", "melon", "peach", "squid", "sushi", "sauce", "jammy", "toasty",
    "tangy", "zesty", "pasta", "pizza", "salad", "tacos", "quich", "fancy", "scone", "prawn",
    "fishy", "berry", "crust", "crumb","sigma"
]
gameboard=[['_','_','_','_','_'],
          ['_','_','_','_','_'],
          ['_','_','_','_','_'],
          ['_','_','_','_','_'],
          ['_','_','_','_','_'],
          ['_','_','_','_','_']]

done=True
tries=0
y=random.choice(zelist)

while done==True:
     for i in range(0,len(gameboard)):
        for q in range(0, len(gameboard[i])):
               if q== len(gameboard[i])-1:
                    print(gameboard[i][q])
               else:
                    print(gameboard[i][q], end="")

     guess=input('Guess a word, and you can count how many letters.').lower()

     while len(guess)<5 or len(guess)>5:
           print("try AGAINNNNNNNNNN")
           guess=input('Guess a word, and you can count how many letters.').lower()




     if guess==y:
                    print("Congrats! You guessed the word!")
                    done=False
     else:
           for k,j in enumerate(guess):
                 gameboard[tries][k]=j
                 if j==y[k]:
                    gameboard[tries][k]=j.upper()
                 elif j!=y[k] and j in y:
                       gameboard[tries][k]=j+'*'
if len(input)<5 or len(input)>5:
     print('Try again.')

     tries+=1
     if tries==5:
           done=True