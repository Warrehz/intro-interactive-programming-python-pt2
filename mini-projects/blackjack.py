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
outcome = "Hit or Stand?"
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        self.show = True
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
        if self.show:
            card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank),
                        CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
            canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        else:
            canvas.draw_image(card_back, (CARD_CENTER[0], CARD_CENTER[1]), CARD_SIZE, [100 + CARD_CENTER[0], 75 + CARD_CENTER[1]], CARD_SIZE)



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
        ace_as_ten_total = card_total + (10 * num_of_aces)
        if ace_as_ten_total <= 21:
            card_total = ace_as_ten_total
        return card_total

    def draw(self, canvas, pos):
        i = 0
        for c in self.cards:
            c.draw(canvas, [pos[0] + i, pos[1]])
            i += 72


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
    global outcome, in_play, my_hand, my_deck, dealer_hand, score

    if in_play:
        score -= 1

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

    dealer_hand.cards[0].show = False
    in_play = True
    outcome = "Hit or Stand?"

def hit():
    global outcome, score, in_play
    if in_play:
        my_hand.add_card(my_deck.deal_card())

        if my_hand.get_value() > 21:
            outcome = "YOU LOSE, YOU BUSTED! NEW DEAL?"
            score -= 1
            in_play = False
            dealer_hand.cards[0].show = True

    # if the hand is in play, hit the player

    # if busted, assign a message to outcome, update in_play and score

def stand():
    global outcome, score, in_play

    if not in_play:
        return

    dealer_hand.cards[0].show = True

    while dealer_hand.get_value() < 17:
        dealer_hand.add_card(my_deck.deal_card())

    if my_hand.get_value() > 21:
        outcome = "YOU LOSE, YOU BUSTED! NEW DEAL?"
        score -= 1
    elif dealer_hand.get_value() > 21:
        outcome = "YOU WIN, DEALER BUSTED! NEW DEAL?"
        score += 1
    elif dealer_hand.get_value() == my_hand.get_value():
        outcome = "TIE, DEALER WINS! NEW DEAL?"
        score -= 1
    elif my_hand.get_value() > dealer_hand.get_value():
        outcome = "YOU WIN! NEW DEAL?"
        score += 1
    else:
        outcome = "DEALER WINS! NEW DEAL?"
        score -= 1
    in_play = False

    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler
def draw(canvas):
    global outcome
    canvas.draw_text("Blackjack", (10, 25), 24, "Black")
    canvas.draw_text(outcome, (50, 300), 40, "Red")
    canvas.draw_text(("Score: " + str(score)), (400, 25), 24, "Black")
    my_hand.draw(canvas, [100, 400])

    if in_play:
        dealer_hand.draw(canvas, [100, 75])
    else:
        dealer_hand.draw(canvas, [100, 75])


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
