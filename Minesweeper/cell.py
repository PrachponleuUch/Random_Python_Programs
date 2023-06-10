from tkinter import Button, Label
import random
import settings
import ctypes
import sys

class Cell:
    all = []
    cell_count = settings.cell_count
    cell_count_label_object = None
    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.is_opened = False
        self.is_mine_candidate = False
        self.cell_btn_object = None
        self.x = x
        self.y = y
        
        #Append the obj to the Cell.all list
        Cell.all.append(self)
    def create_btn_object(self, location):
        btn = Button(
            location,
            width=12,
            height=4,
            #text = f"({self.x},{self.y})"
        )
        btn.bind('<Button-1>', self.left_click_actions) #left click
        btn.bind('<Button-3>', self.right_click_actions) #right click
        self.cell_btn_object = btn
        
    @staticmethod #one time method, no need 'self' as its not an instance method
    def create_cell_count_label(location):
        lbl = Label(
            location,
            text=f"Cells Left: {Cell.cell_count}",
            bg='black',
            fg='white',
            font=("", 30)
        )
        Cell.cell_count_label_object = lbl
        
    def left_click_actions(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mines_length == 0:
                for cell_obj in self.surround_cells:
                    cell_obj.show_cell()
            self.show_cell()
        #if cells count is equal to mines count, player won
        if Cell.cell_count == settings.mines_count:
            ctypes.windll.user32.MessageBoxW(0, 'Congratulation! You won the game!', 'Game over', 0)
        #Cancel left and right click events if cell is already opened
        self.cell_btn_object.unbind('<Button-1>')
        self.cell_btn_object.unbind('<Button-3>')
            
    def get_cell_by_axis(self, x, y):
        #return cell object based on value of x ,y
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell       
    @property #property decorator: read only
    def surround_cells(self):
        cells = [
            self.get_cell_by_axis(self.x-1,self.y-1),
            self.get_cell_by_axis
            (self.x-1, self.y),
            self.get_cell_by_axis(self.x-1,self.y+1),
            self.get_cell_by_axis(self.x,self.y-1),
            self.get_cell_by_axis(self.x+1,self.y-1),
            self.get_cell_by_axis(self.x+1, self.y),
            self.get_cell_by_axis(self.x+1,self.y+1),
            self.get_cell_by_axis(self.x,self.y+1)
        ]
        cells = [cell for cell in cells if cell is not None]
        return cells
        
    @property
    def surrounded_cells_mines_length(self):
        counter = 0
        for cell in self.surround_cells:
            if cell.is_mine:
                counter += 1
            
        return counter
            
    def show_cell(self):
        if not self.is_opened:
            Cell.cell_count -= 1
            self.cell_btn_object.configure(
                text=self.surrounded_cells_mines_length
            )
            #Replace the text of cell count label with the newer count
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(
                    text=f'Cells Left: {Cell.cell_count}'
                )
            # If this is a mine candidate, for safety we should configure the background color to SystemButtonFace
            self.cell_btn_object.configure(
                bg='SystemButtonFace'
            )
        #Mark cell as opened use it as the last line of this method)
        self.is_opened = True
            
    def show_mine(self):
        #A logic to interrupt the game and display a message that the player lost
        self.cell_btn_object.config(
            bg='red'
        )
        ctypes.windll.user32.MessageBoxW(0, 'You clicked on a mine', 'Game Over', 0)
        sys.exit(1)

    def right_click_actions(self, event):
        if not self.is_mine_candidate:
            self.cell_btn_object.configure(
                bg='orange'
            )
            self.is_mine_candidate = True
        else:
            self.cell_btn_object.configure(
                bg='SystemButtonFace'
            )
            self.is_mine_candidate = False
    
    @staticmethod #Belong globally to the class, not any instance
    def randomize_mines():
        picked_cells = random.sample(
            Cell.all, settings.mines_count
        )
        for picked_cell in picked_cells:
            picked_cell.is_mine = True
    
    def __repr__(self):
        return f"Cell({self.x},{self.y})"