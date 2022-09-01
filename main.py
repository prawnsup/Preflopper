from backend.main_window import *
def initialisation():
    numbers=['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    suits=['s','d','c','h']
    h_cards= cards(numbers,suits)
    return h_cards
#print(str(h_cards.card1))
#print(str(h_cards.card2))
#print(str(h_cards.card1))
#print(str(h_cards.card2))
#position= input("please enter position you wish to play")
#range_in= input("please enter the ranges seperated by commas in terms of with largest number first: 22+ --> 22,33,44,55 ; 43s --> 54s,65s ; A2s- --> A3s,A4s ; A2 --> A2 ")
app=application()

app.mainloop()
print("hello")
