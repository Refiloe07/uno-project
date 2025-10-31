import random

colours=["blue","red","green","yellow"]
ranks=[0,1,2,3,4,5,6,7,8,9]
action_cards=["skip","reverse","draw two"]
#all_colours=["black"]
wild_cards=["wild card","wild draw  four"]

# value_suits = [ str(num) for num in range(0, 10)] + ['Skip', 'Reverse', 'Draw 2']

def play_uno(): 
    deck= [] 
    for colour in colours: 
        for rank in ranks: 
            card=f"{colour} {rank}"
            deck.append(card)
            if rank != 0:
                deck.append(card)
    for action in action_cards:
       for colour in colours:
            card=f"{colour} {action}"
            deck.append(card)
            if rank !=0:
                deck.append(card)
    '''for i in range(8):
        deck.append(action_cards[0])
        deck.append(action_cards[1])
        deck.append(action_cards[2])'''
               
    for i in range(4): 
        deck.append(wild_cards[0])
        deck.append(wild_cards[1]) 
    

    random.shuffle(deck)
    return deck 

#print(len(play_uno()))

def play():
    deck= play_uno()
    player1=[]
    computer=[]
    pile=[]
    first_card = deck.pop()
    
    ''' while any(action in action_cards or action in wild_cards) or first_cards in wild_card
    deck.insert(0,first_card)
    random.shuffle(deck)
    if not deck:
        break'''
        
    #first_card = deck.pop()


    pile.append(first_card)
    for i in range(7):
        player1.append(deck.pop())
        computer.append(deck.pop())
    
    
    print("dicard pile:",pile[-1])   
    print("player1 here are your cards:",player1)
    #print("computer:", computer)
    #print ("draw pile:",len(deck))

    turn= 0

    while True:
        top_card= pile [-1]
        if turn == 0:
            print("your turn to play! The top card is," + top_card)
            
            playable_cards=None
            for card in player1:
                if card.split()[0]==top_card.split()[0] or card.split()[1]==top_card.split()[1] or"wild" in card:
                    if playable_cards is None:
                        playable=card
                        break
                    if playable:
                        print("you can play:",playable)
                        player1.remove(playable)
                        pile.append(playable)
                        break

                    if playable:
                        print("you play")





play()


    

    
print(play_uno())


