from random import *                                    # importing random library to help us choose randomly
from random import choice                               # importing from random library choice to help us choose randomly
from tkinter import *                                   # importing tikinter library to help us run the gui


root = Tk()
root.title("Generate PassWord")                         # Titling the gui
root.geometry("1200x300")                               # Specefying the geometry
root.config(background = "lavender")                    # initializing the color of the main background

num_of_small_letters = Entry(root, width=15)            # initializing the entry
num_of_upper_letters = Entry(root, width=15)            # initializing the entry
num_of_nums = Entry(root, width=15)                     # initializing the entry
num_of_symbols = Entry(root, width=15)                  # initializing the entry

num_of_small_letters.grid(row=3, column=1)           # adding the entery to the gui
num_of_upper_letters.grid(row=4, column=1)           # adding the entery to the gui
num_of_nums.grid(row=5, column=1)                    # adding the entery to the gui
num_of_symbols.grid(row=6, column=1)                 # adding the entery to the gui






def checking_length():                                 # function that checks if the password is weak or strong
    global one_password                                # making the password global to use it later

    small_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                     "u", "v", "w", "y", "x", "z"]
    upper_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                     "U", "V", "W", "Y", "X", "Z"]
    symbols = [",", " !", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "?", ".", ">", "<", "/", ";",
               ":"]

    sum_upper = 0                                       # counter to sum the capital letters
    sum_lower = 0                                       # counter to sum the small letters
    sum_numbers = 0                                     # counter to sum the numbers
    sum_symbols = 0                                     # counter to sum the symbols

    for i in one_password:                              # for loop that sum
        if i in small_letters:                          # checking if the person added a small letter
            sum_lower +=1                               # summing the small letters

        if i in upper_letters:                          # checking if the person added a capital letter
            sum_upper +=1                               # summing the Capital letters


        if i in symbols:                                # checking if the person added a symbol
            sum_symbols +=1                             # summing the Symbols


        if i in range(0,10):                            # checking if the person added a number
            sum_numbers +=1                             # summing the Numbers


    if sum_lower < 2:                                   # checking if small letters < 2 then it is weak
        Error_Label = Label(root, text=" Please add more Small letters, the password is Weak ",background='lavender',fg = "red")
        Error_Label.grid(row=9, column=1)               # adding the label to the gui
       
    if sum_upper < 2:                                   # checking if capital letters < 2 then it is weak
        Error_Label = Label(root, text=" Please add more Capital letters, the password is Weak ",background='lavender',fg = "red")
        Error_Label.grid(row=9, column=1)               # adding the label to the gui
       
    if sum_numbers < 2:                                 # checking if numbers < 2 then it is weak
        Error_Label = Label(root, text=" Please add more Integers, the password is Weak ",background='lavender',fg = "red")
        Error_Label.grid(row=9, column=1)               # adding the label to the gui
       
    if sum_symbols < 2:                                 # checking if symbols < 2 then it is weak
        Error_Label = Label(root, text=" Please add more Symbols, the password is Weak ",background='lavender',fg = "red")
        Error_Label.grid(row=9, column=1)               # adding the label to the gui
       
    if sum_symbols >= 2 and  sum_numbers >= 2 and  sum_upper >= 2 and sum_lower >= 2:
                                                                                    # if password is strong
        last_password = "".join(map(str,one_password))  # map() method for converting elements in list to string
        The_password = Label(root, text=one_password, background='blue')# initializing the label
        The_password.grid(row=8, column=1)              # adding the label to the gui
        return last_password                            # returning the strong password
     
   

def generate_password():                                # function that generates the password
    small_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                     "u", "v", "w", "y", "x", "z"]
    symbols = [",", " !", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "?", ".", ">", "<", "/", ";",
               ":"]

    Error_Label = Label(root, text="", background='lavender', width=80)# initializing the label
    Error_Label.grid(row=9, column=1)                   # adding the label to the gui

    global one_password

    number_of_small_letters = num_of_small_letters.get() # getting the value added by the user
    number_of_upper_letters = num_of_upper_letters.get() # getting the value added by the user
    number_of_nums = num_of_nums.get()                   # getting the value added by the user
    number_of_symbols = num_of_symbols.get()             # getting the value added by the user


    randomsmallletter = [choice(small_letters) for s in range(0, int(number_of_small_letters))] # choosing from small letters as much as the entery says

    randomupperletter = [choice(small_letters).upper() for o in range(0, int(number_of_upper_letters))] # choosing from capital letters as much as the entery says

    randomintiger = [randint(0, 9) for p in range(0, int(number_of_nums))] # choosing from intigers as much as the entery says

    randomsymbols = [choice(symbols) for l in range(0, int(number_of_symbols))] # choosing from symbols as much as the entery says


    one_password = randomsmallletter + randomupperletter + randomintiger + randomsymbols # adding the small, capital, numbers and symbols together in one variable
    shuffle(one_password)                                # mixing the added elements in variable one_password to have a stronger password
    checking_length()                                    # calling the checking function to check if the password is strong enough or not



Welcome = Label(root, text="Welcome To Our Password Generator", bg="light blue", fg="white", height=2,
                    font=("Calbiri", "16"), width=120) # initializing the label
Welcome.grid(row=0, columnspan=3)                    # adding the label to the gui

Welcome2 = Label(root, text="Our Page will help you find a Strong Password", background='lavender') # initializing the label
Welcome2.grid(row=1, columnspan=3)                   # adding the label to the gui

Please = Label(root, text="Please ONLY Enter numbers", background='lavender') # initializing the label
Please.grid(row=2, column=1)                         # adding the label to the gui

label_small_letters = Label(root, text="How many small letters do you want in your password?",background='lavender') # initializing the label
label_small_letters.grid(row=3, column=0)            # adding the label to the gui


label_upper_letters = Label(root, text="How many capital letters do you want in your password?",
                                background='lavender') # initializing the label
label_upper_letters.grid(row=4, column=0)            # adding the label to the gui


label_nums = Label(root, text="How many numbers do you want in your password?", background='lavender') # initializing the label
label_nums.grid(row=5, column=0)                     # adding the label to the gui


label_symbols = Label(root, text="How many symbols do you want in your password?", background='lavender') # initializing the label
label_symbols.grid(row=6, column=0)                  # adding the label to the gui


The_password_L = Label(root, text="Your  STRONG  password is: ", background='lavender') # initializing the label
The_password_L.grid(row=8, column=0)                 # adding the label to the gui


   
search_for_password = Button(root, text="..SEARCH..", background='lavender', fg="red", command=generate_password) # initializing the button
search_for_password.grid(row=7, columnspan=3)        # adding the Button to the gui


root.mainloop()
