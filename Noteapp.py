import os
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import showinfo

class Notepad:

   _root = Tk()

   text = Text(_root)
   MenuBar = Menu(_root)
   FileMenu = Menu(MenuBar)
   EditMenu = Menu(MenuBar)
   HelpMenu = Menu(MenuBar)
   CommandMenu = Menu(MenuBar)
   ScrollBar = Scrollbar(text)
   file = None
   def __init__(self,**kwargs):
      try:
         self.Width = kwargs['width']
      except KeyError:
         pass
      try:
         self.Height = kwargs['height']
      except KeyError:
         pass

      self._root.title("Untitled - Notepad")

      screenWidth = self._root.winfo_screenwidth()
      screenHeight = self._root.winfo_screenheight()
      left = (screenWidth / 2) - (self.Width / 2)
      top = (screenHeight / 2) - (self.Height / 2)
      self._root.geometry('%dx%d+%d+%d' % (self.Width, self.Height, left, top))
      self._root.grid_rowconfigure(0, weight=1)
      self._root.grid_columnconfigure(0, weight=1)

      self.text.grid(sticky=N + E + S + W)
      self.FileMenu.add_command(label="New", command=lambda:self.new())
      self.FileMenu.add_command(label="Open", command=lambda:self.open())
      self.FileMenu.add_command(label="Save", command=lambda:self.save())
      self.FileMenu.add_separator()
      self.FileMenu.add_command(label="Exit", command=lambda:self.exit())

      self.MenuBar.add_cascade(label="File", menu=self.FileMenu)
      self.EditMenu.add_command(label="Cut", command=lambda:self.cut())
      self.EditMenu.add_command(label="Copy", command=lambda:self.copy())
      self.EditMenu.add_command(label="Paste", command=lambda:self.paste())

      self.MenuBar.add_cascade(label="Edit", menu=self.EditMenu)
      self.HelpMenu.add_command(label="About Notepad", command=lambda:self.about())

      self.MenuBar.add_cascade(label="Help", menu=self.HelpMenu)
      self._root.config(menu=self.MenuBar)

      self.ScrollBar.pack(side=RIGHT,fill=Y)
      self.ScrollBar.config(command=self.text.yview)
      self.text.config(yscrollcommand=self.ScrollBar.set)

   def exit(self):
       self._root.destroy()

   def about(self):
      showinfo("About Notepad","This is a prototype of a Notepad. \nFor any quarry email us:dasrajdip78754282@gmail.com")

   def open(self):
      self.file = askopenfilename(defaultextension=".txt", filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
      if self.file == "":
         self.file = None

      else:
         self._root.title(os.path.basename(self.file) + " - Notepad")
         self.text.delete(1.0,END)
         file = open(self.file,"r")
         self.text.insert(1.0,file.read())
         file.close()

   def new(self):
      self._root.title("Untitled - Notepad")
      self.file = None
      self.text.delete(1.0,END)

   def save(self):
      if self.file == None:
         self.file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt", filetypes=[("All Files","*.*"), ("Text Documents","*.txt")])

      if self.file == "":
         self.file = None

      else:
         file = open(self.file,"w")
         file.write(self.text.get(1.0,END))
         file.close()
         self._root.title(os.path.basename(self.file) + " - Notepad")

   def cut(self):
      self.text.event_generate("<<Cut>>")

   def copy(self):
      self.text.event_generate("<<Copy>>")

   def paste(self):
      self.text.event_generate("<<Paste>>")

   def run(self):
      self._root.mainloop()

Notepad = Notepad(width=800, height=600)

Notepad.run()
