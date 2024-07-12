GB=[
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],    
]
done=False
Player='X'
col='column'
while done==False:
   
   
   
    for i in range(0,len(GB)):
        for q in range(0, len(GB[i])):
            if q== len(GB[i])-1:
                print(GB[i][q])
            else:
                print(GB[i][q], end="")




    goodinput=False
    X=int(input('Which column would you like to go to?(1-7)'))-1
    while goodinput==False:
        if X < 0 or X > len(GB):
                print("NAH")
        else:
            goodinput = True

    # Above is broken other than that good job
   
    for i in reversed(range(0,len(GB))):

        if GB[i][X]==0:
            GB[i][X]=Player
            break

    t=1
    for i in range(0,len(GB)-1):
        if t==1:
            for j in range(0,len(GB)):
                try:
                    if GB[i][j]==GB[i+1][j]==GB[i+2][j]==GB[i+3][j]!=0 or GB[i][j]== GB[i][j+1]==GB[i][j+2]==GB[i][j+2]==GB[i][j+3]!=0 or GB[i][j]==GB[i+1][j+1]==GB[i+2][j+2]==GB[i+3][j+3]!=0 or GB[i][j]==GB[i+1][j-1]==GB[i+2][j-2]==GB[i+3][j-3]!=0:
                            
                        print(Player,'has Lost!!')
                        t=2
                        done=True
                        break
                        
                        
                except(IndexError):
                    pass