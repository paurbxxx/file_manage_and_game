from time import sleep
from tkinter import *
from config import CANVAS_SIZE, BG_COLOR, EMPTY, RATIO, RECT_SIZE

# class Apple():
#     pass
class Board(Tk):
    def __init__(self):
        super().__init__()
        self.canvas = Canvas(width=CANVAS_SIZE, height=CANVAS_SIZE, bg=BG_COLOR)
        self.canvas.pack()
        self.rect_size = RECT_SIZE
        self.player_x = CANVAS_SIZE // 2 - RECT_SIZE
        self.player_y = CANVAS_SIZE // 2 - RECT_SIZE
        self.ratio = RATIO
        self.player_pos_row = self.ratio//2-1
        self.player_pos_col = self.ratio//2-1
        self.empty = EMPTY
        self.speed = 0.1
        self.canvas.bind_all('<KeyPress>', self.change_direction)
        self.pole = self.build_grid()
        self.player = self.render_player()
        self.player_direction = ''
    
    def build_grid(self):
        row = [self.empty] * self.ratio
        col = []
        for _ in range(self.ratio): 
            col.append(row[:])
        print(col)
        return col

    def render_player(self):
        r_size = self.rect_size
        field = self.pole
        field[self.player_pos_row][self.player_pos_col] = 'player'
        for r in range(self.ratio):
            for c in range(self.ratio):
                if field[r][c] == 'player':
                    player = self.canvas.create_rectangle(self.player_x, self.player_y, self.player_x + r_size, self.player_y + r_size, fill='white')
        return player

    def change_direction(self, event):
        '''Magic number: 6, its a gap between edges and figure
        Render player on field
        '''
        field = self.pole
        r_size = self.rect_size
        
        if (event.keysym == 'Up' or event.keysym == 'w') and self.player_direction != 'down':
            self.player_direction = 'up'

        if (event.keysym == 'Down' or event.keysym == 's') and self.player_direction != 'up':
            self.player_direction = 'down'

        if (event.keysym == 'Right' or event.keysym == 'd') and self.player_direction != 'left':
            self.player_direction = 'right'

        if (event.keysym == 'Left' or event.keysym == 'a') and self.player_direction != 'right':
            self.player_direction = 'left'
   
    def move(self):
        field = self.pole
        r_size = self.rect_size

        if self.player_direction == 'up':
            self.player_pos_col -= 1
            if field[self.player_pos_row][self.player_pos_col] != 'empty' or self.player_pos_col < 0:
                self.player_pos_col += 1
            elif field[self.player_pos_row][self.player_pos_col] == 'empty':
                field[self.player_pos_row][self.player_pos_col + 1] = 'empty'
                field[self.player_pos_row][self.player_pos_col] = 'player'
                self.canvas.move(self.player, 0, -r_size)

        if self.player_direction == 'down':
            self.player_pos_col += 1
            if field[self.player_pos_row][self.player_pos_col] != 'empty' or self.player_pos_col > self.ratio - 2:
                self.player_pos_col -= 1
            elif field[self.player_pos_row][self.player_pos_col] == 'empty':
                field[self.player_pos_row][self.player_pos_col - 1] = 'empty'
                field[self.player_pos_row][self.player_pos_col] = 'player'
                self.canvas.move(self.player, 0, r_size)

        if self.player_direction == 'right':
            self.player_pos_row += 1
            
            if field[self.player_pos_row][self.player_pos_col] != 'empty' or self.player_pos_row > self.ratio - 2:
                    self.player_pos_row -= 1
            elif field[self.player_pos_row][self.player_pos_col] == 'empty':
                field[self.player_pos_row - 1][self.player_pos_col] = 'empty'
                field[self.player_pos_row][self.player_pos_col] = 'player'
                self.canvas.move(self.player, r_size, 0)

        if self.player_direction == 'left':
            self.player_pos_row -= 1
            if field[self.player_pos_row][self.player_pos_col] != 'empty' or self.player_pos_row < 0:
                self.player_pos_row += 1
            elif field[self.player_pos_row][self.player_pos_col] == 'empty':
                field[self.player_pos_row + 1][self.player_pos_col] = 'empty'
                field[self.player_pos_row][self.player_pos_col] = 'player'
                self.canvas.move(self.player, -r_size, 0)
        sleep(self.speed)

def save():
    return {
        "level": 1,
        "obstacles": {
            "easy": 10,
            "medium": 15,
            "hard": 5,
        },
        "word": "orange"
}

def load(data):
    print(data)


board = Board()
while True:
    board.move()
    board.update()

# board.mainloop()