import random
point=0
def choose():
    dict=['DIRECTORY','CONSOLE','AFFORDABLE','INTERSHIP','ENTERPRENEUR','BUSINESS','FATHER','AEROPLANE','GREEN','COMPUTER']
    word=random.choice(dict)
    return word
q=0
while(q<5):
    pick = choose()
    mix = ''.join(random.sample(pick, len(pick)))
    print("Arrange the letters to form a valid word:")
    print(mix,end="\n")
    guess=input("")
    if guess.lower()==pick.lower() or guess.lower()==pick.upper() :
        print()
        print("Correct")
        print()
        point=point+1
    else:
        print()
        print("Wrong")
        print()
        point=point-1
    q=q+1
print("Net Score is",point)
