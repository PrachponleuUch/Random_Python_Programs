from tkinter import *
from cell import Cell
import settings
import utils

root = Tk() #instantiate window instance
#Override settings of the window
root.configure(bg="black")
root.geometry(f'{settings.width}x{settings.height}') #Window Size
root.title("Minesweeper")
root.resizable(False,False)

#Frame(parent window, options...)
top_frame = Frame(
    root,
    bg='black', #Change later to black
    width=utils.width_prct(100),
    height=utils.height_prct(25)    
)

top_frame.place(
    x=0,
    y=0
)

game_title = Label(
    top_frame,
    bg='black',
    fg='white',
    text='Minesweeper Game',
    font=('',48)
)

game_title.place(
    x=utils.width_prct(25),
    y=utils.height_prct(0)
)

left_frame = Frame(
    root,
    bg='black',
    width=utils.width_prct(25),
    height=utils.height_prct(75)
)

left_frame.place(
    x=0,
    y=utils.height_prct(25)
)

center_frame = Frame(
    root,
    bg='black',
    width = utils.width_prct(75),
    height = utils.height_prct(75)
)

center_frame.place(
    x=utils.width_prct(25),
    y=utils.height_prct(25)
)

for x in range(settings.grid_size):
    for y in range(settings.grid_size):
        c = Cell(x,y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=x,
            row=y
        )


#Call the label from the Cell class
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(
    x=0,
    y=0
)

Cell.randomize_mines()



root.mainloop() #program will end