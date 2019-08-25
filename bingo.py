''' A game of BINGO designed for the Hart High School Football Quarterback Club '''

from random import choice as draw
import graphics as g
import tile as t

''' Clean pool for new game '''
def start():
    new_win = g.GraphWin('BINGO!', 250, 909)        # Generate game board
    new_win.master.geometry('+%d+%d' % (800, 50))   # Set game board position
    new_pool = t.draw_game(new_win)                 # Generate initial BINGO! tile set
    play(new_pool,new_win)                          # Start drawing BINGO! tiles

def play(pool,win):
    picked = draw(pool)  # Show game board with current pool of "available" and "drawn" tiles
    ''' Wait for user interaction '''
    while (win.mouseX == None or win.mouseY == None) and win.lastKey == '': # No mouse clicks, no key press
        win.update()
        g.time.sleep(.1) # give up thread
    ''' Mouse events '''
    if win.mouseX != None and win.mouseY != None:   # Mouse click in location (win.mouseX, win.mouseY)
        if (win.mouseX >=0 and win.mouseX <= 250) and (win.mouseY >= 0 and win.mouseY <= 51): # Inside the 'DRAW' button
            if picked.select(win) == 'bingo':   # Choose a BINGO! tile from the remaining pool
                win.close()
                if t.winner(): start()          # Generate Winner! If 'Play Again!', restart game, otherwise quit
               #else:        
               #     win.close()
            else:
                pool.remove(picked)             # Take the tile out of the available pool and draw again
                play(pool, win)
        elif (win.mouseX >=0 and win.mouseX <= 250) and (win.mouseY >= 859 and win.mouseY <= 910): win.close()  # Inside the 'QUIT' button
    ''' Keyboard events '''
    elif win.lastKey.lower() == 'd':          # Key 'D' or 'd' pressed
        if picked.select(win) == 'bingo':   # Choose a BINGO! tile from the remaining pool until BINGO! is called
            if t.winner(win):               # Generate Winner! If 'Play Again!', restart game, otherwise quit
                start()
            win.close()
        pool.remove(picked)                 # Take the tile out of the available pool and draw again
        play(pool)
    elif win.lastKey.lower() == 'q': win.close()    # Key 'Q' or 'q' pressed
    else:
        play(pool)

start()                                     # Start the game!