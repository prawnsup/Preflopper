import tkinter as tk
import tkinter.messagebox
import os.path
import re
import json
import pandas as pd
import random
import time
from PIL import ImageTk , Image
from front_end.start_win import game_window
from front_end.main_menu import main_menu
from front_end.range_win import ranges_win
from backend.ranges import ranges
from backend.card_gen import random_cards



class application(tk.Tk):
    # basically the controller
    def __init__(self, *args, **kwargs):
        self.score = 0 #correct answers
        self.total = 0 # total attempts
        self.pos='BTN'
        self.c_d = os.getcwd()  # to allow for access to images directory from any computer
        self.default_ranges = {
            "LJ": "AT++,KJ++,QJ++,T9s+,J9s+,Q9s-,K8s-,A3s-,66+",
            "HJ": "AT++,KT++,QT++,J9s+,76s+,55+,Q8s-,K6s-,A2s-",
            "CO": "A8++,KT++,QT++,JT++,76s+,97s+,33+,T7s+,J8s-,Q6s-,K3s-,A2s-",
            "BTN": "A4++,K8++,Q9++,J9++,T8++,98++,22+,54s+,53s+,85s+,T6s-,J4s-,Q3s-,K2s-,A2s-"
            }#default values
        self.valid = True#boolean variable that is used to confirm whether ranges have been entered in correct format
        self.current_ranges =  {
            "LJ": "AT++,KJ++,QJ++,T9s+,J9s+,Q9s-,K8s-,A3s-,66+",
            "HJ": "AT++,KT++,QT++,J9s+,76s+,55+,Q8s-,K6s-,A2s-",
            "CO": "A8++,KT++,QT++,JT++,76s+,97s+,33+,T7s+,J8s-,Q6s-,K3s-,A2s-",
            "BTN": "A4++,K8++,Q9++,J9++,T8++,98++,22+,54s+,53s+,85s+,T6s-,J4s-,Q3s-,K2s-,A2s-"
            } #a dictionary to hold ranges in string readable format.Its set to default ranges during start, i had issues with setting to be equal to self.default ranges
        self.dataframe=[] #going to store dataframe containing ranges,position and valid coordinates
        self.entries = {}  # dictionary to hold entries for all ranges.in tkinter var format
        self.font = 'Apple Braille' #font to be used
        tk.Tk.__init__(self, *args, **kwargs)
        self.state('zoomed')
        self.attributes("-fullscreen", True)
        def n_window(event):
            self.attributes('-fullscreen' , False)
        def f_window(event):
            self.attributes('-fullscreen' , True)
        self.bind('<Escape>' , n_window )
        self.bind('<F11>' , f_window)
        # container to be used to manage pages
        self.container = tk.Frame(self)  # basically parent- all widgets for all future pages will be placed here
        self.container.pack(side='top',
                       fill='both',
                       expand=True
                       )
        self.winfo_toplevel().title("Preflopper")
        self.container['bg'] = 'black'
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        # dictionary of frame instances in order to allow robust switching in the future
        main_win_f = main_menu(parent=self.container,
                               controller=self)
        self.frames['main_menu'] = main_win_f
        # creates a frame based on the class main_menu, with container as
        main_win_f.grid(row=0, column=0, sticky='nsew')

        # parent and start_win(self) as controller
        # creates an entry with the key being the class , the value being the object (frame) created from class
        # use print(self.frames) to get a better idea
        # without show_frame method all the frames will be packed into the container
        range_win_f = ranges_win(parent=self.container,
                                 controller=self)
        self.frames['ranges_win'] = range_win_f
        range_win_f.grid(row=0, column=0, sticky='nsew')
        game_window_f= game_window(parent=self.container,controller=self)
        game_window_f.grid(row=0,column=0,sticky='nsew')
        self.frames['game_window_f']=game_window_f
        main_win_f.tkraise()




    def button_gen(self, bg_color, fg_color, text, cmd, width, root, row, column):
        # issue with button background not changing for macos so decided to use labels as makeshift buttons :)
        label = tk.Label(root,
                         bg=bg_color,
                         fg=fg_color,
                         text=text,
                         width=width,
                         font=(self.font, 30),
                         bd=0
                         )

        def on_enter(event):
            label.config(background=fg_color)
            label.config(foreground=bg_color)

        def on_leave(event):
            label.config(background=bg_color)
            label.config(foreground=fg_color)
        def on_click(event):
            root.focus_set()
            cmd('x') #the x is just used as an useless input for the event parameter since a parameter is necessary

        label.bind('<Button-1>', on_click)
        label.bind('<Enter>', on_enter)
        label.bind('<Leave>', on_leave)
        label.grid(row=row, column=column, sticky='nsew', pady=(30, 30))

    def range_button_click(self, event):  # have to add the event parameter in order for tkinter to bind cmd normally
        self.frames['ranges_win'].tkraise()

    def start_button_click(self, event):
        self.frames['game_window_f'].tkraise()

    # function to process range values from user input into dataframe

    def data_proc(self, range_inputs):

        self.current_ranges = self.entries_convert(range_inputs)

    def range_validation(self, rnge):
        # not to self to optimise this later
        # checks if ranges are inputted correctly
        if ',' in rnge:
            for i in rnge.split(','):
                if len(i)==4:
                    x = re.search('[1-9AJQKT][1-9AJQKT][s][-+]', i)
                    if x==None:
                            x = re.search('[1-9AJQKT][1-9AJQKT][+][+]', i)
                            if x==None:
                                return False
                elif len(i) ==3:
                    x=re.search('[1-9AKQJT][1-9AKQJT][s+-]',i)
                    if x== None:
                        return False
                elif len(i)==2:
                    x=re.search('[1-9AKQJT][1-9AKQJT]',i)
                    if x==None:
                        return False
                else:
                    return False

        else:
            return False
        return True

    def range_saver(self, root, text, row, column): #text=position essentially
        #used to save ranges after user enters in values
        #produces text telling them whether the range is updated or if there's an issue
        label_s = tk.Label(root, text='Perfect :)', font=(self.font, 20), fg='green', bg='black')
        self.entries[text].set((self.entries[text].get()).upper())#makes all values inputted into uppercase
        x=''.join([i if i != 'S' else 's' for i in self.entries[text].get() ])
        self.entries[text].set(x)


        ranges = self.entries[text].get()
        self.valid = self.range_validation(ranges)
        self.current_ranges[text]= self.entries[text].get()
        if self.valid == False:
            label_s.configure(text='Please check that you have inputted your ranges correctly')
        label_s.grid(row=row, column=column)
        root.after(600, label_s.destroy)
        return

    def button_genv2(self, bg_color, fg_color, border_color, text, width, root, row, column, pady, thickness):
        #creates a button that when clicked changes into entry box
        self.entries[text] = tk.StringVar()  # adding to dictionary a tkinter variable essentially linked to the 'text' key
        self.entries[text].set(self.default_ranges[text])#default ranges will be text thats already stored here
        temp_f = tk.Frame(root, bg=border_color, width=width)
        temp_f.grid_rowconfigure(0, weight=1)
        temp_f.grid_columnconfigure(0, weight=1)
        temp_f.grid(row=row, column=column, pady=pady)
        label = tk.Label(temp_f,
                         bg=bg_color,
                         fg=fg_color,
                         text=text,
                         width=width,
                         font=(self.font, 30)
                         )

        label.grid(row=0,
                   column=0,
                   padx=(thickness, thickness),
                   pady=(thickness, thickness)
                   )
        entry1 = tk.Entry(temp_f, width=width, font=(self.font, 30), bg='black', fg='white',
                          textvariable=self.entries[text] , insertbackground = 'white')  # now we can access this entry from anywhere in the program.
        # entry1.grid(row=0, column=0, padx=(thickness, thickness), pady=(thickness, thickness))
        label.tkraise()

        def on_enter(event):
            label.configure(background=fg_color)
            label.configure(foreground=bg_color)

        def on_leave(event):
            label.configure(foreground=fg_color)
            label.configure(background=bg_color)

        def on_click(event):
            entry1.grid(row=0, column=0, padx=(thickness, thickness), pady=(thickness, thickness))
            entry1.tkraise()
            entry1.focus_set()

        def on_entry(event):
            entry1.grid_forget()
            label.focus_set()
            # label.tkraise()
            self.range_saver(root, text, row + 1, column)
            return

        def on_esc(event):
            entry1.grid_forget()
            self.entries[text].set(self.current_ranges[text])
            label.focus_set()
            label.tkraise()

        label.bind('<Enter>', on_enter)
        label.bind('<Leave>', on_leave)
        label.bind('<Button-1>', on_click)
        entry1.bind('<Return>', on_entry)
        entry1.bind('<Escape>', on_esc) #this is not working correctly note to self to fix

    # label.bind()

    #functions to return to the home page main_menu
    def back_home(self, event):
        self.frames['main_menu'].tkraise()

    def json_file_save(self,dic):
        #function to dump a dictionary into json file

       with open('ranges_dict.json', 'w') as outfile:
           json.dump(dic, outfile, indent=6)
    def valid_db(self):
        #function used to generate all valid combinations of cards for a particular position and range- which is then saved to dataframe
        self.dataframe=pd.read_json('ranges_dict.json', typ='series')

        for i in self.dataframe.index:
            range_processor=ranges(self.dataframe[i])
            range_processor.converter()
            self.dataframe[i+'-valid'] = set(range_processor.c_valid)


    def initialisation(self):
        #used to initialise the valid combinations of cards according to default ranges - which at the start= current ranges
        self.json_file_save(self.current_ranges)
        self.valid_db()




    def save_ranges(self, event):
        #function for the save button in range window, saves ranges to a json file
        if self.valid == False:
            tk.messagebox.showwarning(title='invalid input',
                                      message='one or more invalid inputs for ranges please check again')
        for position in self.entries:
            self.current_ranges[position] = self.entries[position].get()
        self.json_file_save(self.current_ranges)
        self.back_home('x')
        self.valid_db()


    def defaults(self,event):
        #sets starting range values for all the various position according to default_ranges variable
        self.valid=True
        for position in self.entries:
            self.entries[position].set(self.default_ranges[position])


    def card_gen(self):
        #used to generate the random cards- creates a file path to the images for the cards and saves the cards in the appropriate format. A3s,55 etc.
        numbers = ('A 2 3 4 5 6 7 8 9 T J Q K').split(' ')
        suits= ('Spades Clubs Heart Diamond').split(' ')
        rng= random_cards(numbers,suits)
        rng.card()
        self.card1_path= os.path.join('images',str(rng.card1[1]),str(rng.card1[0])+'.png') #generates paths to these cards
        self.card2_path=os.path.join('images',str(rng.card2[1]),str(rng.card2[0])+'.png')
        self.card1=rng.card1[0]
        self.card2=rng.card2[0]
        self.cards1= self.card1 + self.card2 # combines the two separate cards in two seperate combinations since, since cards can only be read as A2s , instead of 2As , higher value first
        self.cards2=self.card2+ self.card1 # I figured it will be less computationaly intensive compared creating an algorithm to just reorder the cards in the right way
        if rng.card1[1]==rng.card2[1]: #checks if the cards are suited
            self.cards1=self.cards1+"s" #if both are suited then an s is added to the end
            self.cards2=self.cards2+"s"
    def position(self): # randomly generates the position of the player
        self.pos=random.choice(['HJ','LJ','CO','BTN'])


    def reset(self,event): #reset the cards by regenerating the frame not sure if there is a better solution.
        self.card_gen
        tst = game_window(parent=self.container, controller=self)
        tst.grid(row=0, column=0, sticky='nsew')
        self.frames['game_window_f'] = tst
        self.frames['game_window_f'].tkraise()

    def checker(self, action):  # check whether the action to fold or raise is correct or not. True if correct otherwise false
        self.total = self.total + 1 #keeps count of total number of attempts
        if self.cards1 in self.dataframe[[self.pos+'-valid'][0]]: #if one of the combinations is within the set of accepted combinations then raise would result in a return of True

            if action=="raise":
                return True
            else:
                return False
        elif self.cards2 in self.dataframe[[self.pos+'-valid'][0]]:
            if action == "raise":
                return True
            else:
                return False

        else: #otherwise a fold would return True
            if action =="fold":
                return True
            else:
                return False

    def raises(self,event):
        #function for the raise button , increases score by 1 if correct action.Resets game with updated value with self.reset('x')
        x= self.checker('raise')
        if x== False:

            self.reset('x')
        else:
            self.score=self.score+1
            self.reset('x')
    def fold(self,event):
        #function for the raise button , increases score by 1 if correct action.Resets game with updated value with self.reset('x')
        x = self.checker('fold')
        if x == False:
            self.reset('x')
        else:
            self.score = self.score + 1
            self.reset('x')








