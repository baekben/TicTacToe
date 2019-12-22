from tkinter import *
import numpy as np

# Start screen


def main():
    global begin
    begin = Tk()
    begin.title('Tic-Tac-Toe')
    global ttt
    ttt = np.full([3, 3], 10)

    begin.configure(background='#345eeb')
    startScreen = Label(
        begin, text='Do you \n want to \n play Tic-Tac-Toe?', font=('Helvetica', 30), background='#345eeb')
    message = Label(begin, text='Two players\n needed',
                    font=('Helvetica', 15), foreground='#eb8934', background='#345eeb')

    yes = Button(begin, text='Yes', padx=30, pady=30,
                 font=('Helvetica', 20), command=game)
    no = Button(begin, text='No', padx=30, pady=30, font=(
        'Helvetica', 20), command=begin.destroy)

    startScreen.grid(row=0, column=1, columnspan=1)
    yes.grid(row=1, column=0)
    no.grid(row=1, column=2)
    message.grid(row=1, column=1)

    begin.mainloop()
# Gives the user an option for X or O to be inputed onto the board


def board(square, character):
    global ttt
    if (1 <= square) and (square <= 3):
        a = 0
        b = square-1
    elif (4 <= square) and (square <= 6):
        a = 1
        b = square-4
    else:
        a = 2
        b = square-7

    if character == 'X':
        ttt[a, b] = 1
    if character == 'O':
        ttt[a, b] = 0

    if ((ttt[0, 0] == 1 and ttt[0, 1] == 1 and ttt[0, 2] == 1) or
        (ttt[0, 0] == 1 and ttt[1, 0] == 1 and ttt[2, 0] == 1) or
        (ttt[0, 1] == 1 and ttt[1, 1] == 1 and ttt[2, 1] == 1) or
        (ttt[0, 2] == 1 and ttt[1, 2] == 1 and ttt[2, 2] == 1) or
        (ttt[0, 0] == 1 and ttt[1, 1] == 1 and ttt[2, 2] == 1) or
        (ttt[0, 2] == 1 and ttt[1, 0] == 1 and ttt[2, 0] == 1) or
        (ttt[1, 0] == 1 and ttt[1, 1] == 1 and ttt[1, 2] == 1) or
            (ttt[2, 0] == 1 and ttt[2, 1] == 1 and ttt[2, 2] == 1)):
        popup('X')
    if ((ttt[0, 0] == 0 and ttt[0, 1] == 0 and ttt[0, 2] == 0) or
        (ttt[0, 0] == 0 and ttt[1, 0] == 0 and ttt[2, 0] == 0) or
        (ttt[0, 1] == 0 and ttt[1, 1] == 0 and ttt[2, 1] == 0) or
        (ttt[0, 2] == 0 and ttt[1, 2] == 0 and ttt[2, 2] == 0) or
        (ttt[0, 0] == 0 and ttt[1, 1] == 0 and ttt[2, 2] == 0) or
        (ttt[0, 2] == 0 and ttt[1, 0] == 0 and ttt[2, 0] == 0) or
        (ttt[1, 0] == 0 and ttt[1, 1] == 0 and ttt[1, 2] == 0) or
            (ttt[2, 0] == 0 and ttt[2, 1] == 0 and ttt[2, 2] == 0)):
        popup('O')


def clicked(num):
    global answer
    answer = Tk()
    answer.title('X OR O?')
    answer.geometry('350x200')

    answer.configure(background='#808080')

    title = Label(answer, text='X OR O?', font=(
        'Helvetica', 20), background='#808080').grid(row=0, column=1)

    button_x = Button(answer, text='X', padx=40, pady=30,
                      font=(
                          'Helvetica', 20), command=lambda: btnX(num), background='#00D3FF')
    button_x.grid(row=1, column=0)

    button_o = Button(answer, text='O', padx=35, pady=30,
                      font=(
                          'Helvetica', 20), command=lambda: btnO(num), background='#6200FF')
    button_o.grid(row=1, column=2)

# This function holds the basic outline of the game


def game():
    begin.destroy()
    global root
    root = Tk()
    root.title('Tic-Tac-Toe')
    root.geometry('695x765')
    global square_1
    global square_2
    global square_3
    global square_4
    global square_5
    global square_6
    global square_7
    global square_8
    global square_9
    square_1 = Button(root, text='-', padx=100, pady=100,
                      font=(
                          'Helvetica', 20), command=lambda: clicked(1))
    square_1.grid(row=0, column=0)

    square_2 = Button(root, text='-', padx=100, pady=100,
                      font=(
                          'Helvetica', 20), command=lambda: clicked(2))
    square_2.grid(row=0, column=1)

    square_3 = Button(root, text='-', padx=100, pady=100,
                      font=(
                          'Helvetica', 20), command=lambda: clicked(3))
    square_3.grid(row=0, column=2)

    square_4 = Button(root, text='-', padx=100, pady=100,
                      font=(
                          'Helvetica', 20), command=lambda: clicked(4))
    square_4.grid(row=1, column=0)

    square_5 = Button(root, text='-', padx=100, pady=100,
                      font=(
                          'Helvetica', 20), command=lambda: clicked(5))
    square_5.grid(row=1, column=1)

    square_6 = Button(root, text='-', padx=100, pady=100,
                      font=(
                          'Helvetica', 20), command=lambda: clicked(6))
    square_6.grid(row=1, column=2)

    square_7 = Button(root, text='-', padx=100, pady=100,
                      font=(
                          'Helvetica', 20), command=lambda: clicked(7))
    square_7.grid(row=2, column=0)

    square_8 = Button(root, text='-', padx=100, pady=100,
                      font=(
                          'Helvetica', 20), command=lambda: clicked(8))
    square_8.grid(row=2, column=1)

    square_9 = Button(root, text='-', padx=100, pady=100,
                      font=(
                          'Helvetica', 20), command=lambda: clicked(9))
    square_9.grid(row=2, column=2)


# Inputs X into an empty box


def btnX(num):
    if num == 1:
        square_1['text'] = 'X'
        square_1['background'] = '#00D3FF'
        square_1.configure(state=DISABLED)
    if num == 2:
        square_2['text'] = 'X'
        square_2['background'] = '#00D3FF'
        square_2.configure(state=DISABLED)
    if num == 3:
        square_3['text'] = 'X'
        square_3['background'] = '#00D3FF'
        square_3.configure(state=DISABLED)
    if num == 4:
        square_4['text'] = 'X'
        square_4['background'] = '#00D3FF'
        square_4.configure(state=DISABLED)
    if num == 5:
        square_5['text'] = 'X'
        square_5['background'] = '#00D3FF'
        square_5.configure(state=DISABLED)
    if num == 6:
        square_6['text'] = 'X'
        square_6['background'] = '#00D3FF'
        square_6.configure(state=DISABLED)
    if num == 7:
        square_7['text'] = 'X'
        square_7['background'] = '#00D3FF'
        square_7.configure(state=DISABLED)
    if num == 8:
        square_8['text'] = 'X'
        square_8['background'] = '#00D3FF'
        square_8.configure(state=DISABLED)
    if num == 9:
        square_9['text'] = 'X'
        square_9['background'] = '#00D3FF'
        square_9.configure(state=DISABLED)
    board(num, 'X')
    answer.destroy()


def btnO(num):
    if num == 1:
        square_1['text'] = 'O'
        square_1['background'] = '#6200FF'
        square_1.configure(state=DISABLED)
    if num == 2:
        square_2['text'] = 'O'
        square_2['background'] = '#6200FF'
        square_2.configure(state=DISABLED)
    if num == 3:
        square_3['text'] = 'O'
        square_3['background'] = '#6200FF'
        square_3.configure(state=DISABLED)
    if num == 4:
        square_4['text'] = 'O'
        square_4['background'] = '#6200FF'
        square_4.configure(state=DISABLED)
    if num == 5:
        square_5['text'] = 'O'
        square_5['background'] = '#6200FF'
        square_5.configure(state=DISABLED)
    if num == 6:
        square_6['text'] = 'O'
        square_6['background'] = '#6200FF'
        square_6.configure(state=DISABLED)
    if num == 7:
        square_7['text'] = 'O'
        square_7['background'] = '#6200FF'
        square_7.configure(state=DISABLED)
    if num == 8:
        square_8['text'] = 'O'
        square_8['background'] = '#6200FF'
        square_8.configure(state=DISABLED)
    if num == 9:
        square_9['text'] = 'O'
        square_9['background'] = '#6200FF'
        square_9.configure(state=DISABLED)
    board(num, 'O')
    answer.destroy()


def play():
    popup.destroy()
    main()

# winner screen


def popup(winner):
    global root
    global popup
    popup = Tk()
    popup.title('WINNER!!!!')
    popup.geometry('1000x500')
    if winner == 'X':
        color = '#00D3FF'
    else:
        color = '#6200FF'
    popup.configure(bg=color)
    player = winner
    label = Label(
        popup, text='Tic-Tac-Toe \n three in a row! \n Player {} is the WINNER'.format(player), font=('Helvetica', 40), background=color)
    label.pack()
    close = Button(popup, text='close', padx=40, pady=40, font=(
        'Helvetica', 40), command=lambda: popup.destroy())
    close.pack()
    playAgain = Button(popup, text='Play Again?', padx=40,
                       pady=40, font=('Helvetica', 40), command=lambda: play())
    playAgain.pack()
    root.destroy()


main()
