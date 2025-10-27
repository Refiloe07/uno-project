def play_uno():
    deck=[]
    #defined a function that returns a list
    #we added deck so that we can append which means add to the end
    colours=["red","green","yellow","blue"]
    values=[0,1,2,3,4,5,6,7,8,"draw two","skip","reverse"]
    #w then made a list according to the instruction of the game, the colour or the cards and the numbers
    #in python strings can be in the same list as integers, it wont affect your code
    for colour in colours: #outer loop
        for value in values: #inner loop
            #we then create a for loop [a nested for loop, which is a for loop inside a for loop] so that we can generate our deck, for loop for colours and for values#
            #e.g the inner loop will run 2 times for each of the 3 times the outer loops runs
            #outer loop we go through each colour
            #inner loop, for each colour we go through each value
            card_val="{}{}".format(colour,value)
            #the curly brackets are two place holders that need to be filled in, the .format takes the values of colour and value and inserts them into a string. its like filling in the blanks with the actual values
            deck.append(card_val)
            #remember we created a deck that we were going to appened, thats what we do now
            if value !=0:
                deck.append(card_val)
                # now we use our if else statement to say if value is not equal to zero then append to the deck, which means we have 2 of everythig execpet for our zero, there is only one zero and two of everything
        print(deck)
        return deck 
    
    
play_uno()
#call your function
