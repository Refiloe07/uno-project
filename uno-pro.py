import random

colours= ["blue","red","green","yellow"]
ranks= [0,1,2,3,4,5,6,7,8,9]
action_cards= ["skip","reverse","draw two"]
wild_cards= ["wild card","wild draw four"]

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
               
    for i in range(4): 
        deck.append(wild_cards[0])
        deck.append(wild_cards[1]) 
    

    #return deck 

def shuffle(deck):
    random.shuffle ()
    return deck

play_uno()

