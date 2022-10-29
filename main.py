from tkinter import *
from tkinter import messagebox
from random import  random, randint, choice, shuffle
import pyperclip

# even though we imported everything from tkinter
# it will not import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]


    password_list = password_numbers + password_symbols +password_letters

    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    # it will already copy it to your clipboard
    pyperclip.copy(password)

    print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_to_file():
    website_name = website_entry.get()
    email_name = email_entry.get()
    password_enterd = password_entry.get()

    # create a message box to confirm entry


    if len(password_enterd) == 0 or len(website_name) == 0 :
        messagebox.showinfo(title = "Wrong!", message= "Please make sure you haven't left any fields empty.")


    else:
        # return a boolean
        is_ok = messagebox.askokcancel(title=website_name,
                                       message=f"these are the details entered: \nEmail: {email_name}"
                                               f"\nPassword: {password_enterd} \nIs it ok to save?")
        if is_ok:



            with open("save.txt", mode="a") as file:
                file.write(f"{website_name} | {email_name} | {password_enterd}\n")
                website_entry.delete(0, "end")
                password_entry.delete(0, "end")
                password_entry.delete(0, "end")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator")
window.config(padx= 50, pady= 50, bg= "white")


logo_img = PhotoImage(file="logo.png")
canvas = Canvas(height=200, width=200, bg= "white")
canvas.create_image(100, 100, image= logo_img)
canvas.grid(column=1, row= 0)

# create entries

website_text = Label(text="Website", bg= "white")
website_text.grid(column=0, row=1)

# email/ username:

email = Label(text="Email/Username", bg= "white")
email.grid(row=2, column=0)

# password

password = Label(text="Password", bg= "white")
password.grid(column=0, row=3)


# Entries
# sticky basically "sticks" the widget to the edges of the column
website_entry = Entry()
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
# this will focus the curser on the current selection
website_entry.focus()
email_entry = Entry()
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
#  this will populate the email at index 0, so we don't need to type it each time
email_entry.insert(0, "alalemsouhile@yahoo.com")
password_entry = Entry()
password_entry.grid(column=1, row=3, sticky="EW")
#Add some text to begin with
# entry_plate.insert(0, string="Enter plate ID")
#Gets text in entry_plate

generate_passwords = Button(text="Generate Password", bg= "white", command= generate_password)
generate_passwords.grid(column=2, row=3, sticky="EW")
add_button = Button(text="add", bg = "white", width= 35, command= save_to_file)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")















window.mainloop()
