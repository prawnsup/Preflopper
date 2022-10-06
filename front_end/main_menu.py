import tkinter as tk
from PIL import ImageTk, Image
import os
class main_menu(tk.Frame):
    def __init__(self, parent, controller):
        controller.initialisation()
        tk.Frame.__init__(self, parent)
        self['bg'] = 'black'
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        image = Image.open(os.path.join(controller.c_d , 'images' , 'chips.png'))
        width, height = image.size
        canvas = tk.Canvas(self,
                           width=width,
                           height=height,
                           bg='black',
                           bd=0,
                           highlightthickness=0
                           )
        canvas.grid(row=0, column=0)
        canvas.image = ImageTk.PhotoImage(image)
        canvas.create_image(0,
                            0,
                            image=canvas.image,
                            anchor=tk.NW
                            )
        label_title = tk.Label(self,
                               text="PRELOPPER",
                               font=(controller.font, 60),
                               width=self.winfo_screenwidth(),
                               bg='lightyellow',
                               fg='black')
        label_title.grid(row=1, column=0, sticky='nsew')
        controller.button_gen('#00C040',
                              '#80FFC0',
                              'START',
                              controller.start_button_click,
                              self.winfo_screenwidth(),
                              self,
                              row=2,
                              column=0
                              )
        controller.button_gen('#FF4040',
                              '#FFC0C0',
                              'RANGES',
                              controller.range_button_click,
                              self.winfo_screenwidth(),
                              self,
                              row=3,
                              column=0
                              )

