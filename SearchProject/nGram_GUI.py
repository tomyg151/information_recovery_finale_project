import mainPage
from tkinter import *
from tkinter import *



# create a tkinter window
root1 = Tk()
root1.title('Welcome To Our Final Project! Denis Yerushchuck And Tom Groundland')
# Open window having dimension 100x100
root1.geometry('610x350')
root1['background'] = '#e4e7ed'
Copyright_label = Label(root1, bg='#e4e7ed', text="Ⓒ Copyright Tom and Denis")
# Copyright_label.grid(row=8, column=2)

Copyright_label.place(bordermode=OUTSIDE, height=660, width=630)


#check the existance of chosen word in the relevant file (GUI)
def wordExist():
    root2 = Tk()
    root2.title('if word exist in the data/docs')
    root2['background'] = '#e4e7ed'
    root2.geometry('600x600')

    def my_click2():
        txt = entry_txt.get()
        func = mainPage.wordExist(txt)

        myLabel = Label(root2, text=func, padx=50, pady=5)
        myLabel.grid(row=4, column=0)

    def clear_btn():
        entry_txt.delete(0, END)

    # Create Text Box Lables
    word_label = Label(root2, bg='#e4e7ed', text="enter a word: ")
    word_label.grid(row=0, column=0)

    # Create Text Box
    entry_txt = Entry(root2, width=25)
    entry_txt.grid(row=0, column=1, pady=10)

    #Clear and click buttons
    click_btn = Button(root2, text="submit", fg="BLACK", padx=40, pady=5, command=my_click2)
    click_btn.grid(row=1, column=0)

    clear_btn = Button(root2, text="clear", padx=40, pady=5, command=clear_btn)
    clear_btn.grid(row=1, column=1)





#count apperance of a word in the relevant file (GUI)
def apperance_of_word():
    root3 = Tk()
    root3.title('find word apperances in the data/docs')
    root3['background'] = '#e4e7ed'
    root3.geometry('600x600')

    def my_click2():
        txt = entry_txt.get()
        func = mainPage.apperance_of_word(txt)
        myLabel = Label(root3, text=func, padx=30, pady=5)
        myLabel.grid(row=4, column=0)

    def clear_btn():
        entry_txt.delete(0, END)

    # Create Text Box Lables
    word_label = Label(root3, bg='#e4e7ed', text="enter a word: ")
    word_label.grid(row=0, column=0)

    # Create Text Box
    entry_txt = Entry(root3, width=25)
    entry_txt.grid(row=0, column=1, pady=10)

    #Clear and click buttons
    click_btn = Button(root3, text="submit", fg="BLACK", padx=40, pady=5, command=my_click2)
    click_btn.grid(row=1, column=0)

    clear_btn = Button(root3, text="clear", padx=40, pady=5, command=clear_btn)
    clear_btn.grid(row=1, column=1)




def n_gram():
    root4 = Tk()
    root4.title('n-gram method')
    root4['background'] = '#e4e7ed'
    root4.geometry('600x600')

    def my_click2():
        txt = entry_txt.get()
        num = entry_txt2.get()
        func = mainPage.n_gram(txt, int(num))
        myLabel = Label(root4, text=func, padx=50, pady=5)
        myLabel.grid(row=5, column=0)



    def clear_btn():
        entry_txt.delete(0, END)
        entry_txt2.delete(0,END)

    # Create Text Box Lables
    word_label = Label(root4, bg='#e4e7ed', text="enter a word: ")
    word_label.grid(row=0, column=0)
    N_number = Label(root4, bg='#e4e7ed', text="enter a number(for N value): ")
    N_number.grid(row=1, column=0)

    # Create Text Box
    entry_txt = Entry(root4, width=25)
    entry_txt.grid(row=0, column=1, pady=10)
    entry_txt2 = Entry(root4, width=25)
    entry_txt2.grid(row=1, column=1, pady=10)

    #Clear and click buttons
    click_btn = Button(root4, text="submit", fg="BLACK", padx=40, pady=5, command=my_click2)
    click_btn.grid(row=2, column=0)

    clear_btn = Button(root4, text="clear", padx=40, pady=5, command=clear_btn)
    clear_btn.grid(row=2, column=1)




def count_apperance():
    root5 = Tk()
    root5.title('number of apperance of a word in each doc')
    root5['background'] = '#e4e7ed'
    root5.geometry('600x600')

    def my_click2():
        txt = entry_txt.get()
        func = mainPage.count_apperance_of_word_in_doc(txt)
        myLabel = Label(root5, text=func, padx=50, pady=5)
        myLabel.grid(row=5, column=0)

    def clear_btn():
        entry_txt.delete(0, END)

    # Create Text Box Lables
    word_label = Label(root5, bg='#e4e7ed', text="enter a word: ")
    word_label.grid(row=0, column=0)

    # Create Text Box
    entry_txt = Entry(root5, width=25)
    entry_txt.grid(row=0, column=1, pady=10)

    # Clear and click buttons
    click_btn = Button(root5, text="submit", fg="BLACK", padx=40, pady=5, command=my_click2)
    click_btn.grid(row=1, column=0)

    clear_btn = Button(root5, text="clear", padx=40, pady=5, command=clear_btn)
    clear_btn.grid(row=1, column=1)




# Create Buttons
"""wordExist function"""
Add_User_btn = Button(root1, text="wordExist", border=5, bg='#8ff86f', width=16, fg='black', bd='2', command=wordExist)
Add_User_btn.grid(row=3, column=1, columnspan=1, padx=15, pady=15)

"""apperance_of_word function"""
Add_Event_btn = Button(root1, text="apperance_of_word", border=5, bg='#8ff86f', width=16, fg='black', bd='2', command=apperance_of_word)
Add_Event_btn.grid(row=3, column=2, columnspan=1, padx=15, pady=15)

"""n_gram function"""
Add_Comment_btn = Button(root1, text="n_gram", border=5, bg='#8ff86f', width=16, fg='black', bd='2', command=n_gram)
Add_Comment_btn.grid(row=3, column=3, columnspan=1, padx=15, pady=15)

"""count_apperance_of_word_in_doc function"""
Add_Approve_Event_btn = Button(root1, text="count_apperance", border=5, bg='#8ff86f', width=16, fg='black', bd='2', command=count_apperance)
Add_Approve_Event_btn.grid(row=3, column=4, columnspan=1, padx=15, pady=15)













#use the looping mechanisim
root1.mainloop()