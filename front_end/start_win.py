import tkinter as tk
from PIL import ImageTk , Image
import os

class game_window(tk.Frame):
    #starts the main window with the cards and the option to raise or fold
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self['bg']='black'
        self.grid_rowconfigure(0,weight=1)
        self.grid_columnconfigure(0,weight =1)
        controller.card_gen() #calls a function from the controller which generates new cards (and card paths)
        card1 = Image.open(os.path.join(controller.c_d,controller.card1_path)) #opens card1 image according to the path
        card2= Image.open(controller.c_d +"/"+controller.card2_path)#opens card2 image according to the path
        controller.position() #generates random position

        position= tk.Label(self,
                 text=controller.pos,
                 font=(controller.font, 60),
                 width=self.winfo_screenwidth(),
                 bg='black',
                 fg='white')
        position.grid(row=0 , column=0)



        canvas = tk.Canvas(self,
                           width=374,
                           height=271,
                           bg='black',
                           bd=0,
                           highlightthickness=0
                           )
        canvas.grid(row=1,column=0)
        canvas.image = ImageTk.PhotoImage(card1)




        canvas.create_image(0,
                            0,
                            image=canvas.image,
                            anchor=tk.NW
                            )

        canvas_in = tk.Canvas(canvas,
                           width=187,
                           height=271,
                           bg='black',
                           bd=0,
                           highlightthickness=0
                           )


        canvas.create_window(187,0,anchor='nw' , window=canvas_in)
        canvas_in.image = ImageTk.PhotoImage(card2)
        canvas_in.create_image(0,
                               0,
                               image=canvas_in.image,
                               anchor=tk.NW
                               )

        act=  tk.Label(self,
                               text="Score:"+ str(controller.score)+"/"+ str(controller.total),
                               font=(controller.font, 40),
                               width=self.winfo_screenwidth(),
                               bg='black',
                               fg='white')
        act.grid(row=2,column=0)

        controller.button_gen('green',
                              'white',
                              'RAISE',
                              controller.raises,
                              self.winfo_screenwidth(),
                              self,
                              row=3,
                              column=0
                              )
        self.label_incorrect_r= tk.Label(self,
                               text="Incorrect",
                               font=(controller.font, 30),
                               width=self.winfo_screenwidth(),
                               bg='black',
                               fg='red')
        self.label_incorrect_r.grid(row=3, column=0 , sticky='nsew')
        self.label_incorrect_r.lower()
        self.test_label= tk.Label(self,
                               text="Test",
                               font=(controller.font, 30),
                               width=self.winfo_screenwidth(),
                               bg='black',
                               fg='red'
                                  )
        self.label_correct_r = tk.Label(self,
                                     text="correct",
                                     font=(controller.font, 30),
                                     width=self.winfo_screenwidth(),
                                     bg='black',
                                     fg='green')
        self.label_correct_r.grid(row=3, column=0, sticky='nsew')
        self.label_correct_r.lower()




        controller.button_gen('red',
                              'white',
                              'FOLD',
                              controller.fold,
                              self.winfo_screenwidth(),
                              self,
                              row=4,
                              column=0
                              )
        self.label_incorrect_f = tk.Label(self,
                                     text="Incorrect",
                                     font=(controller.font, 30),
                                     width=self.winfo_screenwidth(),
                                     bg='black',
                                     fg='red')
        self.label_incorrect_f.grid(row=4, column=0, sticky='nsew')

        self.label_correct_f = tk.Label(self,
                                   text="correct",
                                   font=(controller.font, 30),
                                   width=self.winfo_screenwidth(),
                                   bg='black',
                                   fg='green')

        self.label_correct_f.grid(row=4, column=0, sticky='nsew')
        self.label_incorrect_f.lower()
        self.label_correct_f.lower()
        controller.button_gen('blue',
                              'white',
                              'BACK',
                              controller.back_home,
                              self.winfo_screenwidth(),
                              self,
                              row=6,
                              column=0
                              )


