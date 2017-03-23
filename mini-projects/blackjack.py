# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank),
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)

# define hand class
class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        hand = "Hand:"
        for c in self.cards:
            hand += " " + str(c)
        return hand

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        card_total = 0
        num_of_aces = 0
        for c in self.cards:
            card_rank = c.get_rank()
            card_total += VALUES.get(card_rank)
            if card_rank == 'A':
                num_of_aces += 1
        ace_as_ten_total = card_total + (10 * num_of_aces) - num_of_aces
        if ace_as_ten_total <= 21:
            return ace_as_ten_total
        else:
            return card_total

    def draw(self, canvas, pos):
        pass	# draw a hand on the canvas, use the draw method for cards


# define deck class
class Deck:
    def __init__(self):
        self.deck = []
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop()

    def __str__(self):
        deck = "Deck:"
        for c in self.deck:
            deck += " " + str(c)
        return deck


#define event handlers for buttons
def deal():
    global outcome, in_play, my_hand, my_deck, dealer_hand

    my_deck = Deck()
    my_hand = Hand()
    dealer_hand = Hand()

    my_deck.shuffle()
    my_hand.add_card(my_deck.deal_card())
    my_hand.add_card(my_deck.deal_card())
    print "My " + str(my_hand)
    dealer_hand.add_card(my_deck.deal_card())
    dealer_hand.add_card(my_deck.deal_card())
    print "Dealer " + str(dealer_hand)

    in_play = True

def hit():

    if in_play:
        if my_hand.get_value() <= 21:
            my_hand.add_card(my_deck.deal_card())
            print my_hand
            if my_hand.get_value() > 21:
                print "YOU BUSTED"

    # if the hand is in play, hit the player

    # if busted, assign a message to outcome, update in_play and score

def stand():
    if in_play:
        if my_hand.get_value() > 21:
            print "YOU BUSTED"
        else:
            while dealer_hand.get_value() < 17:
                dealer_hand.add_card(my_deck.deal_card())
        if dealer_hand.get_value() > 21:
            print "DEALER BUSTED"
        elif dealer_hand.get_value() == my_hand.get_value():
            print "DEALER WINS"
        elif my_hand.get_value() > dealer_hand.get_value():
            print "YOU WIN"
        else:
            print "DEALER WINS"

    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below

    card = Card("S", "A")
    card.draw(canvas, [300, 300])


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric
