#A game of BINGO designed for the Hart High School Football Quarterback Club

from random import choice as draw
import graphics as g
import tile as t

# Main window
def play():
    win = g.GraphWin('BINGO!', 250, 909)
    pool = t.draw_game(win)

    
    while win.getMouse():
        win.close()
        if win.getKey() == 'g':
            win.setBackground('green')






    '''while True: 
            if keyStr.lower() == 'q' or (click.getX() in range(0,251) and click.getY() in range(859,910)):
                win.close()
            elif keyStr.lower() != 'q' and not (click.getX() in range(0,251) and click.getY() in range(0,51)):
                picked = draw(pool)
                if picked.select(win) == 'bingo':
                    if t.winner(win):
                        play()
                pool.remove(picked)
                continue
            else:            win.setBackground('blue')
                play()
'''


'''
# Wait for user to initiate click event
    while win.getKey() == "":
        if win.getMouse():
            win.close()


        click = win.getMouse()
            if (click.getX() in range(0,251) and click.getY() in range(859,910)):
                
'''
play()
