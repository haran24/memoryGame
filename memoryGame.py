import random
       
def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck    
    '''
    l=[None]*len(deck)
    
    s = len(deck)
    for i in range(s):
       rnum = random.randint(0,s-1)

       while rnum  in l:
          rnum = random.randint(0,s-1)
       l[i]=(rnum)
       
    rDeck = [None]*s

    for c in range(s):
       rDeck[c] = deck[l[c]]
       
    for i in range(s):
       deck[i] = rDeck[i]

def create_board(size):
    '''int->list of str
       Precondition: size is even positive integer between 2 and 52
       Returns a rigorous deck (i.e. board) of a given size.
    '''
    
    board = [None]*size 

    letter='A'
    for i in range(len(board)//2):
          board[i]=letter
          board[i+len(board)//2 ]=board[i]
          letter=chr(ord(letter)+1)
    return board

def print_board(a):
    '''(list of str)->None
       Prints the current board in a nicely formated way
    '''
    for i in range(len(a)):
        print('{0:4}'.format(a[i]), end=' ')
    print()
    for i in range(len(a)):
        print('{0:4}'.format(str(i+1)), end=' ')


def wait_for_player():
    '''()->None
    Pauses the program/game until the player presses enter
    '''
    input("\nPress enter to continue. ")
    print()
    
def revealed(discovered, position1, position2, original_board):
   '''(list of str, int, int, list of str)->list of str
    Preconditions: position1 & position2 must be integers ranging from 1 to the length of the board
    '''
   discovered[position1-1] = original_board[position1-1]
   discovered[position2-1] = original_board[position2-1]
   return discovered
   
def print_revealed(discovered, position1, position2, original_board):
    '''(list of str, int, int, list of str)->None
    Prints the current board with the two new positions (position1 & position2) revealed from the original board
    Preconditions: position1 & position2 must be integers ranging from 1 to the length of the board
    '''
  
    discovered[position1-1] = original_board[position1-1]
    discovered[position2-1] = original_board[position2-1]
    print_board(discovered)
    
def print_stardeck(a):
   '''(list of str)->None
      Prints the board will all elements as * or face down
   '''
   for i in range(len(a)):
        print('{0:4}'.format('*'), end=' ')
   print()
   for i in range(len(a)):
        print('{0:4}'.format(str(i+1)), end=' ')


##

def read_raw_board(file):
    '''str->list of str
    Returns a list of strings represeniting a deck of cards that was stored in a file. 
    The deck may not necessarifly be playable
    '''
    raw_board = open(file).read().splitlines()
    for i in range(len(raw_board)):
        raw_board[i]=raw_board[i].strip()
    return raw_board


def clean_up_board(l):
    '''list of str->list of str

    The functions takes as input a list of strings representing a deck of cards. 
    It returns a new list containing the same cards as l except that
    one of each cards that appears odd number of times in l is removed
    and all the cards with a * on their face sides are removed
    '''
    print("\nRemoving one of each cards that appears odd number of times and removing all stars ...\n")
    playable_board=[]

    c = 0
    
    playable_board = l
    
    for i in range(len(l)):

       if l.count(l[i])%2!=0:
          playable_board[i] = '*'      

    while '*' in playable_board:
            playable_board.remove('*') 

    return playable_board


def is_rigorous(l):
    '''list of str->bool
    Returns True if every element in the list appears exactlly 2 times or the list is empty.
    Otherwise, it returns False.

    Precondition: Every element in the list appears even number of times
    '''

    
    k = True
    for i in range(len(l)):
       if l.count(l[i])<2 or l.count(l[i])>2:
          return False
        



def play_game(board):
    '''(list of str)->None
    Plays a concentration game using the given board
    Precondition: board a list representing a playable deck
    '''

    print("Ready to play ...\n")

    # this is the funciton that plays the game
 

    print_stardeck(board)
    b = ["*"]*(len(board))
    print()
    n = ["*"]*(len(board))
    count = len(board)
    g = 0
    while count!=0:
       print()
       print("Enter two distinct positions on the board that you want revealed.")
       print("i.e. two integers in the range: [1,",len(board),"]")
       position1 = int(input("Enter Position 1: "))
       position2 = int(input("Enter Position 2: "))
       print()
       while n[position1-1]!='*' or n[position2-1]!='*':
          print("One or both of your chosen positions has already been paired.")
          print("Please try again. This guess did not count. Your current number of guesses is",guess)
          print("Enter two distinct positions on the board that you want revealed.")
          print("i.e. two integers in the range: [1,",len(board),"]")
          position1 = int(input("Enter Position 1: "))
          position2 = int(input("Enter Position 2: "))
       while position1==position2:
          print("You chose the same positions.")
          print("Please try again. This guess did not count. Your current number of guesses is",guess)
          print("Enter two distinct positions on the board that you want revealed.")
          print("i.e. two integers in the range: [1,",len(board),"]")
          position1 = int(input("Enter Position 1: "))
          position2 = int(input("Enter Position 2: "))   
       print_revealed(b,position1,position2,board)
       if board[position1-1] == board[position2-1]:
          n = revealed(new,position1,position2,board)
          count = count - 2
       for i in range(len(n)):
          b[i] = n[i]
       g += 1
       wait_for_player()
       print("\n"*60)
       print_board(n)
       
    print("\n\nCongratulations! You completed the game with",g,"guesses.")

#main

print("Would you like (enter 1 or 2 to indicate your choice):")
print("(1) me to generate a rigorous deck of cards for you")
print("(2) or, would you like me to read a deck from a file?")
choice = int(input())
while choice!=1 and choice!=2:
   print(choice,"is not an existing option. Please try again. Enter 1 or 2 to indicate your choice")
   choice = int(input())   

if choice==1:
   print("You chose to have a rigorous deck generated for you")
   print("How many cards do you want to play with?")
   size = int(input("Enter an even number between 0 and 52: "))
   while size<0 or size>52:
      print("")
      size = int(input("Enter an even number between 0 and 52: "))
   while size%2 != 0:
      print("")
      size = int(input("Enter an even number between 0 and 52: "))
   board=create_board(size)
   print("Shuffling deck...")
   shuffle_deck(board)
   wait_for_player()
   play_game(board)   

elif choice==2:
   print("You chose to load a deck of cards from a file")
   file=input("Enter the name of the file: ")
   file=file.strip()
   board=read_raw_board(file)
   board=clean_up_board(board)
   print()
   if is_rigorous(board)==True:
      print("********************************************************************\n*                                                                  *")
      print("*__This deck is now playable and rigorous and it has,",len(board),"cards.__ *")
      print("*                                                                  *\n********************************************************************")
   else:
      print("************************************************************************\n*                                                                      *")
      print("*__This deck is now playable and not rigorous and it has,",len(board),"cards.__ *")
      print("*                                                                      *\n************************************************************************")
   
   wait_for_player()
   print("\n"*60)
   print("Shuffling deck...")
   shuffle_deck(board)
   wait_for_player()
   play_game(board)
