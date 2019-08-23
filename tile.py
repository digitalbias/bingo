'''A class representing a bingo tile for display onscreen and to be chosen at random.'''

import graphics as g

class Tile:
    '''A BINGO tile containing a box and a label.'''

    def __init__(self, number):#, corner = g.Point(50,50)):
        '''Initialize number and corner attributes'''
        self.number = number +1
        if self.number < 16:
            x = 0
            self.name = 'B-' + str(self.number)
        elif self.number < 31:
            x = 50
            self.name = 'I-' + str(self.number)
        elif self.number < 46:
            x = 100
            self.name = 'N-' + str(self.number)
        elif self.number < 61:
            x = 150
            self.name = 'G-' + str(self.number)
        else:
            x = 200
            self.name = 'O-' + str(self.number)
        y = 106 + (50 * (int(number)%15))
        self.corner = g.Point(x, y)
        self.w = 50
        self.h = 50
        self.font_size = 36
        self.selected = False
        self.update()

    def update(self):
        self.__box = g.Rectangle(self.corner, g.Point(self.corner.getX()+self.w, self.corner.getY()+self.h))
        self.__box.setWidth(3)
        self.__label = g.Text(g.Point(self.corner.getX()+(self.w/2), self.corner.getY()+(self.h/2)), self.number)
        self.__label.setFace('arial'), self.__label.setStyle('bold'), self.__label.setSize(30)
        if self.selected == True:
            self.__box.setOutline('gray'), self.__box.setFill('black')
            self.__label.setFill('red')
        else:
            self.__box.setOutline('white'), self.__box.setFill('gray')
            self.__label.setFill('black')            

    def show(self, __win):
        self.__box.undraw(), self.__label.undraw()
        self.__box.draw(__win), self.__label.draw(__win)

    def select(self, __win):
        # Update tile and redraw
        self.selected = True
        self.update(), self.show(__win)
        # Create display window for selected tile
        s_win = g.GraphWin('New Tile', 500, 500)
        s_win.setBackground('black')
        # Show name of selected tile
        s_text = g.Text(g.Point(250,250), self.name)
        s_text.setFace('arial'), s_text.setStyle('bold'), s_text.setFill('red'), s_text.setSize(36)
        # Generate "BINGO!" button and instructions
        b = g.Rectangle(g.Point(0,0), g.Point(500,100))
        b.setFill('red'), b.setOutline('white'), b.setWidth(3)
        b_text = g.Text(b.getCenter(),'BINGO!')
        b_text.setFace('arial'), b_text.setStyle('bold'), b_text.setFill('black'), b_text.setSize(36)
        alt_text = g.Text(b.getCenter(),'click anywhere to continue...')
        alt_text.setFace('arial'), alt_text.setStyle('bold'), alt_text.setFill('white'), alt_text.setSize(16), alt_text.move(0, 300)
        # Draw "BINGO!" button and instructions
        b.draw(s_win), b_text.draw(s_win), alt_text.draw(s_win)
        s_text.draw(s_win)
        # Wait for user to initiate click event
        while True:
            b_click = s_win.getMouse()

            if b_click.getX() in range(0,501) and b_click.getY() in range(0,101):
                s_win.close()
                return 'bingo'
            else:
                s_win.close()
                return True


def draw_game(board):
    '''Generates a BINGO board with controls'''

    #Show BINGO column labels
    title = ['B', 'I', 'N', 'G', 'O']
    for letter in title:

        x = 50 * title.index(letter)
        y = 56

        l = g.Rectangle(g.Point(x,y), g.Point(x + 50, y + 50))
        l.setOutline('white'), l.setWidth(3)
        l_text = g.Text(l.getCenter(),letter)
        l_text.setFace('arial'), l_text.setStyle('bold'), l_text.setSize(36), l_text.setFill('red')
        l.setFill('black')
        l.draw(board), l_text.draw(board)

    # Generate and draw tiles
    tiles = []
    for value in range(0,75):
        tiles.append(Tile(value))
    for tile in tiles:
        tile.show(board)

    # Generate and draw "Draw" and "Quit" buttons
    d = g.Rectangle(g.Point(0,3), g.Point(250,53))
    d.setFill('red'), d.setOutline('black'), d.setWidth(3)
    d_text = g.Text(d.getCenter(),'Draw')
    d_text.setFace('arial'), d_text.setStyle('bold'), d_text.setSize(36), d_text.setFill('black')
    d.draw(board), d_text.draw(board)

    q = g.Rectangle(g.Point(0,859), g.Point(250,909))
    q.setFill('red'), q.setOutline('black'), q.setWidth(3)
    q_text = g.Text(q.getCenter(),'Quit')
    q_text.setFace('arial'), q_text.setStyle('bold'), q_text.setSize(36), q_text.setFill('black')
    q.draw(board), q_text.draw(board)

    return tiles

def winner(view):
    # Generate WINNER window and background colors
    # Black outer
    b_win = g.GraphWin('WINNER: BIN"GO HART GO!!!"', 1000, 1000)
    b_win.setBackground('black')
    # Red middle
    r_r = g.Rectangle(g.Point(50,50), g.Point(950,950))
    r_r.setFill('red'), r_r.draw(b_win)
    # White inner
    w_r = g.Rectangle(g.Point(100,100), g.Point(900,900))
    w_r.setFill('white'), w_r.draw(b_win)
    # Black center
    b_r = g.Rectangle(g.Point(150,150), g.Point(850,850))
    b_r.setFill('black'), b_r.draw(b_win)
    # Center Text
    w_text = g.Text(b_r.getCenter(), "WINNER!")
    w_text.setFace('arial'), w_text.setStyle('bold'), w_text.setFill('red'), w_text.setSize(36), w_text.draw(b_win)
    # Window controls
    # "Play Again" box
    p_box = g.Rectangle(g.Point(250,700), g.Point(350, 750))
    p_box.setFill('white'), p_box.setOutline('red'), p_box.setWidth(3), p_box.draw(b_win)
    p_txt = g.Text(g.Point(300, 725), 'Play Again')
    p_txt.setFace('arial'), p_txt.setStyle('bold'), p_txt.setFill('black'), p_txt.setSize(12), p_txt.draw(b_win)
    # "Quit" box
    q_box = g.Rectangle(g.Point(650,700), g.Point(750, 750))
    q_box.setFill('white'), q_box.setOutline('red'), q_box.setWidth(3), q_box.draw(b_win)
    q_txt = g.Text(g.Point(700, 725), 'Quit')
    q_txt.setFace('arial'), q_txt.setStyle('bold'), q_txt.setTextColor('black'), q_txt.setSize(12), q_txt.draw(b_win)

    # Wait for user to initiate click event
    while True:
        b_click = b_win.getMouse()

        if b_click.getX() in range(650,751) and b_click.getY() in range(700,751):
            b_win.close()
        elif b_click.getX() in range(275,376) and b_click.getY() in range(700,751):
            view.close()
            b_win.close()
            return True
        else:
            b_win.getMouse()



