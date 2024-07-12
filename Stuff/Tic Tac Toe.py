GB=[
    ['_', '_', '_' ],
    ['_', '_', '_' ],
    ['_', '_', '_' ]
]
done=False
Player='X'
col='column'
userinput=input
for  i in range(0,9):

    if Player=='X':
        Player="O"
    else:
        Player='X'
    for i in range(0,len(GB)):
        for z in range(0, len(GB[i])):
            if z== len (GB[i])-1:
                print(GB[i][z])
            else:
                print(GB[i][z], end="") 
    goodinput=False
    while (goodinput==False):
        Y=int(input('Which row would you like to go to?(0-2)'))
        X=int(input('Which column would you like to go to?(0-2)'))
        if X < 0 or X > len(GB) or Y < 0 or Y > len(GB) :
            print("NAH")
        else:
            if GB[X][Y] == Player:
                print('NAH (p2)')
            else:
                goodinput = True
    GB[Y][X] = Player

    


    if GB[0][0]==GB[0][1]==GB[0][2]==Player or GB[1][0]==GB[1][1]==GB[1][2]==Player or GB[2][0]==GB[2][1]==GB[2][2]==Player or GB[0][0]==GB[1][0]==GB[2][0]==Player or GB[0][1]==GB[1][1]==GB[2][1]==Player or GB[0][2]==GB[1][2]==GB[2][2]==Player or GB[0][0]==GB[1][1]==GB[2][2]==Player or GB[0][2]==GB[1][1]==GB[2][0]==Player:
        print (Player, 'Won!!') 
        break

    if i==8:
        print('Tie. Womp Womp.')
        break
        

