print('\n\nMake it through the maze\n\n')

#~~~This is the Game Board~~~#
GB=[
['XX', 'XX', '##', '##', '##', '##', '##', 'XX'],
['##', '##', '##', '  ', '  ', '  ', '##', 'XX'],
['##', 'UU', '  ', '**', '##', '  ', '##', 'XX'],
['##', '##', '##', '  ', '##', '  ', '##', 'XX'],
['##', 'EE', '##', '##', '  ', '**', '##', 'XX'],
['##', '  ', '##', '  ', '##', '  ', '##', '##'],
['##', '  ', '##', '**', '  ', '  ', '  ', '##'],
['##', '  ', '  ', '  ', '##', '  ', '  ', '##'],
['##', '##', '##', '##', '##', '##', '##', '##']
]
Coin=0
done=False
X=1
Y=2
while done==False:
    for i in range(0,len(GB)):
        for q in range(0, len(GB[i])):
            if q== len(GB[i])-1:
                print(GB[i][q])
            else:
                print(GB[i][q], end="")
    userinput=input("W,A,S, or D?")
#~~~These are inputs~~~#
    GB[Y][X] = '  '
    if userinput=='W' or userinput=='w':
        if GB[Y-1][X] == '##':
            print('You Stupid!')
        else:
            Y -= 1
    elif userinput=='A' or userinput=='a':
        if GB[Y][X-1] == '##':
            print('You Stupid!')
        else:
            X -= 1
    elif userinput=='S' or userinput=='s':
        if GB[Y+1][X] == '##':
            print('You Stupid!')
        else:
            Y += 1
    elif userinput=='D' or userinput=='d':
        if GB[Y][X+1] == '##':
            print('You Stupid!')
        else:
            X += 1
    if GB[Y][X]=='**':
        print('You got one coin!')
        Coin += 1
    if Coin==3:
        print('You can finish now! Yay')
    GB[Y][X] = 'UU'
    
    



    if GB[4][1]== 'UU':
        print("You aren't dumb! Congrats!")
        done=True