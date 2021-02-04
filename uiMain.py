import tkinter as tk 
import tkinter.filedialog as fd
import tkinter.simpledialog as sd
import tweetScrap as scrapper
import gingerAPI as grammar
import mongo as mongo

root = tk.Tk()
root.title('Joke Gen Tools')
root.geometry('300x150')
menu = tk.Menu(root)
userHandle = ""

#scrapping tool
def askForHandle():
    userHandle = sd.askstring("Input","Please Enter Twitter Handle.")
    scrapper.scrap(userHandle)
    tk.messagebox.showinfo('Information','Tweet Scrapping Completed.')

#grammar tool
def gingerGrammar():
    files = fd.askopenfiles()
    grammar.gingerMain(files)
    tk.messagebox.showinfo('Information','Grammar Check Completed.')

#database storage tool
def storeToDB():
    files = fd.askopenfiles()
    mongo.mongoStorage(files)
    tk.messagebox.showinfo('Information','Storing to Database Completed.')

#action menu implementation
actionMenu = tk.Menu(menu, tearoff = 0)
actionMenu.add_command(label = 'Scrap Tweets', command = askForHandle)
actionMenu.add_command(label = 'Check Grammar',command = gingerGrammar)
actionMenu.add_command(label = 'Store Database',command = storeToDB)
actionMenu.add_separator()
actionMenu.add_command(label = 'Exit', command = root.quit)

menu.add_cascade(label = 'Actions', menu = actionMenu)

root.config(menu = menu)
root.mainloop()
