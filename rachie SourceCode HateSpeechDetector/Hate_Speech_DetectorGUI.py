# Color Schemes
#  Petal  #F98866
#  Poppy  #FF420E
#  Stem   #80BD9E
#  Spring Green  #89DA59

# Core Packages
import tkinter as tk
from tkinter import *
from tkinter import ttk, scrolledtext, Button
from tkinter.scrolledtext import ScrolledText

import hsd_helper as trans
import tweets_api

# Global Variable
tweets = ''
# Structure and Layout
window = Tk()
window.title("HateSpeechDetector")
window.geometry("1000x650")
window.config(background='black')

style = ttk.Style()
style.theme_use('winnative')
style.configure('lefttab.TNotebook', tabposition='wn', background="#89DA59")

# TAB LAYOUT
tab_control = ttk.Notebook(window, style='lefttab.TNotebook')

tab1 = Frame(tab_control, background="#80BD9E")
tab2 = Frame(tab_control, background="#80BD9E")
tab3 = Frame(tab_control, background="#80BD9E")

# ADD TABS TO NOTEBOOK
tab_control.add(tab1, text=f'{"Home ":^20s}')
tab_control.add(tab2, text=f'{"X":^20s}')
tab_control.add(tab3, text=f'{"About ":^20s}')

label2 = Label(tab2, text='Name', padx=5, pady=5, bg='#F98866', fg='#FFFFFF')
label2.grid(column=0, row=0, padx=10, pady=10, sticky='W')

raw_entry = StringVar()
name_entry = Entry(tab2, textvariable=raw_entry, width=50)
name_entry.grid(row=0, column=1, sticky='W', padx=10, pady=10)

label4 = Label(tab3, text='About', padx=5, pady=5, bg='#F98866', fg='#FFFFFF')
label4.grid(column=0, row=0, padx=10, pady=10, sticky='W')

tab_control.pack(expand=1, fill='both')


# Clear Text  with position 1.0
def clear_text_file():
    displayed_tweets.delete('1.0', END)


# Clear Result of Functions
def clear_text_result():
    tab2_display_text.delete('1.0', END)


# Functions for TAB 2 FILE PROCESSER
# Open File to Read and Process


def get_tweets_sentiment():
    # raw_text = displayed_tweets.get('1.0', tk.END)
    final_text = trans.text_sentiment(tweets)
    final_text = ' '.join([text + '\n\n' for text in final_text])
    result = '\nResult:{}'.format(final_text)
    tab2_display_text.insert(tk.END, result)


# Fetch Text From Url
def get_text():
    global tweets
    name = str(name_entry.get())
    number_of_tweets = number_entry.get()
    tweets = tweets_api.get_tweets(name, number_of_tweets)
    fetched_text = ' '.join([tweets + '\n\n' for tweets in tweets])
    displayed_tweets.insert(tk.END, fetched_text)


def clear_text():
    entry.delete('1.0', END)


def clear_display_result():
    tab1_display.delete('1.0', END)


def get_sentiment():
    raw_text = str(entry.get('1.0', tk.END))
    raw_text = raw_text.split('.')
    final_text = trans.text_sentiment(raw_text)
    final_text = ' '.join([text + '\n\n' for text in final_text])
    result = '\nResult:{}'.format(final_text)
    tab1_display.insert(tk.END, result)


# MAIN TAB
l1 = Label(tab1, text="Enter Text", bg='#F98866', fg='#FFFFFF')
l1.grid(row=0, column=0, padx=10, pady=10, sticky='W')

scrolW = 100
scrolH = 10

entry = scrolledtext.ScrolledText(tab1, width=scrolW, height=scrolH, wrap=tk.WORD)
entry.grid(column=0, columnspan=3, sticky='WE', padx=10, pady=10)

# BUTTONS

button1 = Button(tab1, text="Reset", command=clear_text, width=12, bg='#89DA59', fg='#fff')
button1.grid(row=4, column=0, padx=10, pady=10)

button2 = Button(tab1, text="Sentiment", command=get_sentiment, width=12, bg='#89DA59', fg='#fff')
button2.grid(row=4, column=1, padx=10, pady=10)

button3: Button = Button(tab1, text="Clear Result", command=clear_display_result, width=12, bg='#89DA59', fg='#fff')
button3.grid(row=4, column=2, padx=10, pady=10)

tab1_display: ScrolledText = scrolledtext.ScrolledText(tab1, width=scrolW, height=scrolH, wrap=tk.WORD)
tab1_display.grid(row=7, column=0, columnspan=3, sticky='WE', padx=10, pady=10)

# TWITTER TAB
l1 = Label(tab2, text="Number of Tweets", bg='#F98866', fg='#FFFFFF')
l1.grid(row=1, column=0, padx=10, pady=10, sticky='W')

number_entry = IntVar()
number_entry.set(5)
number_entry = Spinbox(tab2, from_=0, to=100, textvariable=number_entry, width=40)
number_entry.grid(row=1, column=1, sticky='W', padx=10, pady=10)

raw_entry = StringVar()
name_entry = Entry(tab2, textvariable=raw_entry, width=50)
name_entry.grid(row=0, column=1, sticky='W', padx=10, pady=10)

displayed_tweets = ScrolledText(tab2, width=scrolW, height=scrolH, wrap=tk.WORD)
displayed_tweets.grid(row=2, column=0, columnspan=3, sticky='WE', padx=10, pady=10)

# BUTTONS FOR SECOND TAB/FILE READING TAB
b0 = Button(tab2, text="Get Tweets", width=12, command=get_text, bg='#89DA59', fg='#fff')
b0.grid(row=3, column=0, padx=10, pady=10)

b1 = Button(tab2, text="Reset ", width=12, command=clear_text_file, bg='#89DA59', fg='#fff')
b1.grid(row=4, column=1, padx=10, pady=10)

b2 = Button(tab2, text="Sentiment", width=12, command=get_tweets_sentiment, bg='#89DA59', fg='#fff')
b2.grid(row=3, column=1, padx=10, pady=10)

b3 = Button(tab2, text="Clear Result", width=12, command=clear_text_result, bg='#89DA59', fg='#fff')
b3.grid(row=4, column=0, padx=10, pady=10)

# Display Screen
# tab2_display_text = Text(tab2)
tab2_display_text = ScrolledText(tab2, width=scrolW, height=scrolH, wrap=tk.WORD)
tab2_display_text.grid(row=7, column=0, columnspan=3, sticky='WE', padx=10, pady=10)

# Allows you to edit
tab2_display_text.config(state=NORMAL)


# Exit Gui clearly
def _quick():
    window.quit()
    window.destroy()
    exit()


# Creating a Menu bar
menuBar = Menu(window)
window.config(menu=menuBar)

# Add menu items
fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label="Exit", command=_quick)
menuBar.add_cascade(label="File", menu=fileMenu)

# Add another Menu to the Menu Bar and an Item

helpMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Help", menu=helpMenu)

# About TAB
about_label = Label(tab3, text="HateSpeechDetectorV1\n ", pady=10, padx=10, bg='#F98866', fg='#FFFFFF')
about_label.grid(column=0, row=1)
contact = Label(tab3, text="contact:r203565x@students.msu.ac.zw", pady=10, padx=10, bg='#F98866', fg='#FFFFFF')
contact.grid(column=0, row=2)
window.mainloop()
