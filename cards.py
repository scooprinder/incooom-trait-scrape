from web3.auto.infura import w3
import json
from enum import Enum

with open("incooom.abi") as f:
    info_json = json.load(f)
abi = info_json['result']

contract_addr = w3.toChecksumAddress('0x906642380fd9b7aa726bce9c6abee7378396061b')

contract = w3.eth.contract(address=contract_addr, abi=abi)

#    struct CardInfo {
#        string suit;     0
#        string value;    1
#        bool joker;      2
#        uint deck;       3
#        uint cardNumber; 4
#        TIER tier;       5
#    }

class TIER(Enum):
    BASIC = 0
    GOLD = 1
    PSYCHEDELIC = 2

class CardInfo():
    def __init__(self, id, suit, value, joker, deck, cardNumber, tier):
        self.id = id
        self.suit = suit
        self.value = value
        self.joker = joker
        self.deck = deck
        self.cardNumber = cardNumber
        self.tier = tier
    
    def __str__(self):
        return f'Token ID: {self.id}\n\nSuit: {self.suit}\nValue: {self.value}\nIs Joker? {self.joker}\nDeck Number: {self.deck}\nCard Number: {self.cardNumber}\nTier: {self.tier.name}\n\n'


f = open("incoomTraits.sql", "a")

# This takes time to run 2916 times
# Crude AF 
for i in range(0,2917):
    print(f'Card number: {i}')
    card = contract.functions.getCardInfo(i).call()
    cardInfo = CardInfo(i, card[0],card[1],card[2],card[3],card[4],TIER(card[5]))
    if (i == 0):
        f.write(f'select {cardInfo.id} as "ID", \'{cardInfo.value}\' as "Value", \'{cardInfo.suit}\' as "Suit", \'{cardInfo.tier.name}\' as "Tier", \'{cardInfo.deck}\' as "Deck Number", \'{cardInfo.cardNumber}\' as "Card Number" union all\n')
    else:
        f.write(f'select {cardInfo.id}, \'{cardInfo.value}\', \'{cardInfo.suit}\', \'{cardInfo.tier.name}\', \'{cardInfo.deck}\', \'{cardInfo.cardNumber}\' union all\n')

f.close()
