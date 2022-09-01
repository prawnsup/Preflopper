import tkinter as tk
class ranges_win(tk.Frame):
    def __init__(self, parent, controller):
        #range window
        tk.Frame.__init__(self, parent)
        self['bg'] = 'black'
        self.grid_rowconfigure(12, weight=1)
        self.grid_columnconfigure(0, weight=1)
        descriptor = tk.Label(self, text='Welcome fellow poker aficionado :)\n \n Please select a position below',
                              font=(
                                  controller.font,
                                  40),
                              bg='black',
                              fg='white'
                              )
        descriptor.grid(row=0, column=0)
        controller.button_genv2('black',
                                'white',
                                'blue',
                                'LJ',
                                self.winfo_screenwidth(),
                                self,
                                1,
                                0,
                                10,
                                15,
                                )
        controller.button_genv2('black',
                                'white',
                                'blue',
                                'HJ',
                                self.winfo_screenwidth(),
                                self,
                                3,
                                0,
                                10,
                                15,
                                )
        controller.button_genv2('black',
                                'white',
                                'blue',
                                'CO',
                                self.winfo_screenwidth(),
                                self,
                                5,
                                0,
                                10,
                                15,
                                )
        controller.button_genv2('black',
                                'white',
                                'blue',
                                'BTN',
                                self.winfo_screenwidth(),
                                self,
                                7,
                                0,
                                10,
                                15,
                                )

        controller.button_gen('#FF4040',
                              'white',
                              'RESTORE TO DEFAULT',
                              controller.defaults,
                              self.winfo_screenwidth(),
                              self,
                              row=9,
                              column=0
                              )

        controller.button_gen('#FF4040',
                              'white',
                              'BACK',
                              controller.back_home,
                              self.winfo_screenwidth(),
                              self,
                              row=11,
                              column=0
                              )
        controller.button_gen('lightgreen',
                              'white',
                              'SAVE',
                              controller.save_ranges,
                              self.winfo_screenwidth(),
                              self,
                              row=13,
                              column=0
                              )
        controller.button_gen('lightgreen',
                              'white',
                              'SAVE',
                              controller.save_ranges,
                              self.winfo_screenwidth(),
                              self,
                              row=13,
                              column=0
        )
