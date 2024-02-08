from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    password_input.delete(0, END)

    password_input.insert(END, password)
    pyperclip.copy(password)




# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website= website_input.get()
    password= password_input.get()
    email= email_input.get()

    if website=='' or password=='' :
      messagebox.showinfo(title="Password Manager",message="Please don't leave any field empty")

    else:
      is_ok = messagebox.askokcancel(title="Password Manager", message=f"These are the details entered: \nEmail: {email}\nPassword: {password}\nIs it ok to save?")
      if is_ok:
         with open("data.txt",mode="a") as file:
             file.write(f"{website} | {email} | {password}\n")

             website_input.delete(0,END)
             email_input.delete(0,END)
             password_input.delete(0,END)



# ---------------------------- UI SETUP ------------------------------- #

window= Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas( width=200,height=200)
image= PhotoImage(file="logo.png")
canvas.create_image(100,100,image=image)
canvas.grid(column=1,row=0)



website_input=Entry(width=54)
website_input.grid(column=1,row=1,columnspan=2)
website_input.focus()
website_label=Label(text="Website:")
website_label.grid(column=0,row=1)

email_input=Entry(width=54)
email_input.grid(column=1,row=2,columnspan=2)
email_input.insert(0,"Mustafa@gmail.com")
user_label=Label(text="Email/Username:")
user_label.grid(column=0,row=2)

password_input=Entry(width=34)
password_input.grid(column=1,row=3)

password_label=Label(text="Password:")
password_label.grid(column=0,row=3)

generate_password=Button(text="Generate Password",command=generate_password)
generate_password.grid(column=2,row=3)

add_button=Button(text="Add",width=47,command=save)
add_button.grid(column=1,row=4,columnspan=2)


window.mainloop()