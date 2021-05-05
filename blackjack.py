import random

def game_result(player_name, player_pts, rival_name, rival_pts):
    if player_pts == rival_pts:
        msg = "Draw Game"
    elif player_pts > rival_pts:
        msg = f'{player_name} Wins'
    else:
        msg = f'{rival_name} Wins'
    return msg

def gen_cards(player_name):
    global hand, cardNumber, sumCards, diferenceValue
    hand = []
    cardNumber = sumCards = 0
    
    while True:
        cardNumber = random.randrange(1,14)
        sumCards += cardNumber
        if sumCards <= 21:
            hand.append(cardNumber)
        else:
            break
    
    sumCards = 0
    for i in range(len(hand)):
        sumCards += hand[i]
    diferenceValue = sumCards - 21
    
    return player_name, hand, sumCards, diferenceValue

def the_game(player_name, rival_name):
    global playerHand, rivalHand
    playerHand = gen_cards(player_name)
    rivalHand = gen_cards(rival_name)
    winner_msg = game_result(playerHand[0],playerHand[3],rivalHand[0],rivalHand[3])
    final_msg = f'\nPlayerHand:> {playerHand}\nRivalHand:> {rivalHand}\nResult:> {winner_msg}\n'
    return final_msg

print(the_game("Fulano","Beltrano"))