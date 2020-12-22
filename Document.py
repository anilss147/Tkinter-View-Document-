
"""
@author: A-Bosh
"""
from tkinter import *
from tkinter import messagebox, Tk,  Button,LabelFrame
from tkdocviewer import *
class main:
    def __init__(self,master):
        self.master = master
        self.Border2=LabelFrame(master,text="View File",width=900,height=760)
        self.Border2.place(x=10,y=5)
        self.Border2.pack()
        self.complete_function()
              
    def Show_Pdf(self):
        self.v = DocViewer(self.Border2)
        self.v.fit_page(9.2,8)
        self.v.place(x=0,y=0)
        self.v.display_file("File_name.pdf")
        
    def complete_function(self):
        def window_close():
            MsgBox = messagebox.askquestion ('Exit','Are You Sure You Want To Exit',icon = 'warning',default='no')
            if MsgBox == 'yes':
                self.master.destroy()

        self.help_buttton=Button(self.master, text='View PDF ' , height="1", width="14", fg="Black",font=('Arial Black',11),command=self.Show_Pdf)
        self.help_buttton.place(x=400, y=780)
        self.master.protocol( 'WM_DELETE_WINDOW', window_close )

Homewindow = Tk()
main(Homewindow)
Homewindow.title("View PDF")
Homewindow.geometry('920x850')
Homewindow.mainloop()
