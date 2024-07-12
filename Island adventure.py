print("\n\nYou crashed on a random, uncharted location in the pacific, called the Island, a land full of dangerous animals.")
print("Be careful, for all the animals have figured out about your adventure to their island and are already planning to strike back.")
print("You must choose what you would do, or you die. A plane is coming to search tomorrow. Stay Alive.\n\n")

done=False

while done == False:
#~~~These are all of the choices~~~#
    print("A. Set camp.")
    print("B. Hunt for food.")
    print("C. Check your bag for supplies.")
    print("D. Sleep.")
    print("E. Quit.")
    userchoice=input("Select one of the previous: ")
   
#~~~This is choice A.~~~#  
    if userchoice== "A":
        print("you have found three suitable locations, Pick one: ")
        print("1. A shady area right next to a stream filled with fresh water.")
        print("2. A sunny area with a stream with fresh water half a mile away.")
        print("3. An area with sun and shade, with the nearest water source being 1 mile away.")

        userchoice=input("Select one: ")
        if userchoice=="1":
            print("You set up camp and are now ready to continue with your journey.")
        elif userchoice=="2":
            print("You have set down camp, but you start to get thirsty. You have to walk the half mile, and you barely make it there before you fainted. You woke up 20 minutes later and had fallen into the stream, but you managed to drink some and pull yourself out before journing back to camp.")
        elif userchoice =='3':
            print("you set up camp an take the mile long walk to get thirsty. your were too thirsty to make it back to your camp and died on the way back to camp. Mission failed.")
        
#~~~This is Choice B.~~~#
    elif userchoice=='B':
        print("You decided to go hunt for food.")
        userchoice=input("On the way to hunt, you realize you have no weapon. would you like to look around for weapons? Yes or No?")
        if userchoice== "No":
            userchoice=input("You continued on your way and came across a bear den. Do you go in? Yes or No? ")
            if userchoice=="Yes":
                print("You entered the den. A bear creeped up behind you and clawed you to death. You died. Womp Womp.")
            if userchoice== 'No':
                userchoice=input("You crept past the bear den and made it away safely. On the way past, you saw a large stick that could be fashioned into a spear. Do you take this?Yes or No?")
                if userchoice== 'Yes':
                    print("you grabbed the stick and a rock, then spent an hour working on sharpening it. You now have a spear.")
                    userchoice=input("It started getting dark, so you headed back to camp. On the way to camp, you encountered a deer. Will you kill the deer? Yes or No?")
                    if userchoice== 'Yes':
                        userchoice=input(" you threw your spear at the deer, and you killed it instantly.You drag the deer back to your camp. Do you cook it? Yes or No?")
                        if userchoice=='No':
                            print("You ate the raw meat and suffered from food poisoning. You died in your sleep. L Bozo.")
                        if userchoice=="Yes":
                            print("You made a campfire and then cooked the meet. You have a full belly and fall into a peaceful sleep.")
                if userchoice=='No':
                    print("you crawled pass the stick and kept on going.")
                    userchoice=input("It started getting dark, so you headed back to camp. On the way to camp, you encountered a deer. Will you kill the deer? Yes or No?")
                    if userchoice=='Yes':
                        print("You try to strangle the deer, as you have no weapon. However, the deer runs away, then charges back with its alpha deer and kills you. You lose.")
                    if userchoice== 'No':
                        print("Cry as you walk back to your camp, as you have no food. However, you are still alive when you wake up in the morning.")
        if userchoice=='Yes':
            userchoice=input("You walked around and found a medium sized stick. You can Turn it into either a sword or a spear. Which would you like to make? Sword or Spear?")
            if userchoice=='Sword':
                userchoice=input("You made a sword and continued on. you can either choose the right path or the left.Which would you like to choose? Left or Right?")
                if userchoice=='Left':
                    print("You verntured into a den of wild monkeys, and they started rushing you. You cannot run, as they are faster and more agile then you. You manage to kill five of the seven monkeys, but when you killed the fifth, the sword broke. the monkeys ripped you to pieces.You lose. Skill Issue. smh")
                if userchoice=='Right':
                    userchoice=input("you ventured into a bears den. Do you Fight or Run?")
                    if userchoice=='Fight': 
                        print('The bears launched an ambush on you, three on one. Your sword flashed out, wounding both the henchmen bears, leaving the Alpha. She rushed at you, and by some miracle, she slipped and could not get back up. You escaped.')
                        userchoice=input('You ran back to your camp, and saw a deer on the way back. Do you Kill It, or Leave It?')
                        if userchoice=="Kill It":
                            print("You somehow managed to kill it. Free food. You go to sleep and live another day")
                        if userchoice=='Leave It':
                            print('You starved in your sleep, clawing your throat, leaving a trail of blood into the woods, where your corpse lays. Womp Womp.')
                    if userchoice=='Run':
                        print('You ran away, however the bears heard you and chased you, and just when you were about to escape, you tripped and fell. They killed you, scraping out your throat and leaving you an indescibable pile of body.')
            if userchoice=='Spear':
                print('you slip and fall on you spear, impaling yourself from the beginning of your achilles tendon to the top of yuor throat, leaving yourself bleeding in the forest, dead. Be better.')
#~~~~~This is choice C~~~~#
    elif userchoice=='C':
        print('You have a bag with almost nothing in it, just a  water bottle with a hole in it, a moldy sandwitch, and a $50,000 gaming setup, perfectly intact. In a rage you grinded Fortnite for 100 hours straight, thn died of lack of G-Fuel.')

#~~~~This is choice D~~~#
    elif userchoice=='D':
        print('You curled down and went to sleep. when you were sleeping, a bunch of crabs grabbed you and pulled you into the ocean. Skill. Issue.')
#~~~~This is choice E~~~~#
    elif userchoice=='E':
        done=True