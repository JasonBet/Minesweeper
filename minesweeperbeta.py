from Tkinter import *
import time
import tkMessageBox 
import random

class Game:
    

    def __init__(self, master):

        self.flags = 60
        self.createButtons(master)
        self.update_count

        self.bottomFrame = Frame(root)
        self.bottomFrame.grid(row=11, columnspan=10)

        self.flagRemainning = Label(self.bottomFrame, text='Flag Remaining : '+str(self.flags))
        self.flagRemainning.grid(row=12)

        self.quitBtn = Button(self.bottomFrame, text='Quit', command=root.destroy)
        self.quitBtn.grid(row=13, columnspan=2)

        self.total = 0
        self.count = 0
        for i in self.buttons:
            if self.buttons[i][4][0] == 1:
                self.total += 1
                
    def update_count(self):
        self.bttn_clicks += 1
        self.bttn['text'] = "Total Clicks: " + str(self.bttn_clicks)
        print self.bttn_clicks
        
    def savefileW(self):
        print "ROYDABOI"
        f.close()
        
    def openfileR(self):
        f= open("Readme.txt" , 'r')
        print "It works"

    def createButtons(self, parent):
        self.buttons = {}
        row = 0
        col = 0
        for x in range(0, 160):
            status = random.choice(['safe', 'danger'])
            self.buttons[x] = [
            Button(parent, bg='#8a8a8a'),
            status,
            row,
            col,
            [0 if status == 'danger' else 1] 
            ]

            self.buttons[x][0].bind('<Button-1>', self.leftClick_w(x))
            self.buttons[x][0].bind('<Button-3>', self.rightClick_w(x))
            col += 1
            if col == 20:
                col = 0
                row += 1
            for k in self.buttons:
                self.buttons[k][0].grid(row= self.buttons[k][2], column= self.buttons[k][3])

   
    def leftClick_w(self, x):
        return lambda Button: self.leftClick(x)

    def rightClick_w(self, x):
        return lambda Button: self.rightClick(x)

    def leftClick(self, btn):
        check = self.buttons[btn][1]
        if check == 'safe':

            self.buttons[btn][0].config(bg='green')
            self.buttons[btn][0].config(state='disabled', relief=SUNKEN)
            self.count += 1
            self.nearbyMines(btn)
            self.showNearby(btn)
            win = self.checkWin()
            if win:
                self.victory()

        if check == 'danger':
            self.buttons[btn][0].config(bg='red')
            self.buttons[btn][0].config(state='disabled', relief=SUNKEN)
            self.lost()

    def rightClick(self, btn):
        if self.flags > 0:
            self.buttons[btn][0].config(bg='blue')
            self.buttons[btn][0].config(state='disabled', relief=SUNKEN)
            self.flags -= 1
            self.flagRemainning.config(text= 'Flag Remaining : '+str(self.flags))
            if self.buttons[btn][1] == 'safe':
                self.count += 1

        else:
            showinfo('no flags', 'you run out of flags')

    def showNearby(self, btn):
        if btn > 20 and btn < 190:
            self.possible = [btn-21,btn+21, btn-20, btn+20,btn-19, btn+19,btn+1, btn-1]
            for i in self.possible:
                try:
                    if self.buttons[i][1] == 'safe':
                        if self.buttons[i][0]['bg'] == 'green':
                            continue
                        else:
                            self.buttons[i][0].config(bg='green')
                            self.buttons[i][0].config(state='disabled', relief=SUNKEN)
                            self.count += 1
                            self.buttons[i][4][0] == 0
                            self.nearbyMines(i)
                except KeyError:
                    pass

            if self.checkWin():
                self.victory()

    def nearbyMines(self, btn):
        self.near = 0
        if btn > 20 and btn < 190:
            self.pos = [btn-21,btn+21, btn-20, btn+20,btn-19, btn+19,btn+1, btn-1]
            for i in self.pos:
                try:
                    if self.buttons[i][1] == 'danger':
                        self.near += 1
                except KeyError:
                    pass
        if btn < 20:
            self.pos2 = [btn+21,btn+20, btn+19,btn+1]
            for i in self.pos:
                try:
                    if self.buttons[i][1] == 'danger':
                        self.near += 1
                except KeyError:
                    pass
        if btn > 190:
            self.pos3 = [btn-21,btn-20, btn-19,btn-1]
            for i in self.pos:
                try:
                    if self.buttons[i][1] == 'danger':
                        self.near += 1
                except KeyError:
                    pass
        self.buttons[btn][0].config(text=str(self.near), font=('Helvetica', 7))

    def lost(self):
        global root
        for i in self.buttons:
            if self.buttons[i][1] == 'danger':
                self.buttons[i][0].config(bg='red')
        time.sleep(.25)
        if tkMessageBox.askyesno("You Lose.", "You struck a mine and died...Play Again?"):
            root.destroy()
            main()
        else:
            root.destroy()

    def victory(self):
        global root
        if tkMessageBox.askyesno("You Win.", "congratulations you won ! do you want to play again?"):
            root.destroy()
            main()
        else:
            root.destroy()
            
    def openfileW():
        f= open("Readme.txt", 'w')
        names = listbox1.get(0, END)
        for i in names:
            f.write(i+"\n")
        f.close()

    def reset(self):
        self.createButtons
        self.flags = 50
        self.flagRemainning.config(text= 'Flag Remaining : '+str(self.flags))
        for i in self.buttons:
            self.buttons[i][0].config(bg='#8a8a8a', text='')
            self.buttons[i][0].config(state='normal', relief=RAISED)
            self.buttons[i][1] = random.choice(['safe', 'danger'])
        self.count = 0
        self.total = 0
        for i in self.buttons:
            if self.buttons[i][4][0] == 1:
                self.total += 1


    def checkWin(self):
        return self.count == self.total

    def quit(self):
        global root
        root.destroy()


def main():
    global root
    root = Tk()
    root.title('Minesweeper')
    game = Game(root)
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Open", command=game.openfileR)
    filemenu.add_command(label="Save", command=game.savefileW)
    filemenu.add_command(label="Exit", command=game.quit) 
    
    menubar.add_cascade(label="File", menu=filemenu)
    
    root.config(menu=menubar)
    root.mainloop()

if __name__ == '__main__':
    main()