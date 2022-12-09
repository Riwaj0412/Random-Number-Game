from tkinter import *
from tkinter import messagebox
import random

root = Tk()
root.title("Login")
root.geometry("1280x720")
root.configure(bg="white")
root.resizable(False, False)

def signin():
    user_name = username.get()
    user_password = password.get()

    if user_name == 'admin' and user_password=='1234':
        root.destroy()
        #MAIN WORKING FUNCTION
        def check():
            if (a == v1 + v2 or a == abs(v1 - v2)) and (b == v3 + v4 or b == abs(v3 - v4)) and (
                    c == v1 + v3 or c == abs(v1 - v3)) and (d == v2 + v4 or d == abs(v2 - v4)):
                return True
            else:
                return False

        def reset():
            screen1.destroy()
            main_gui()

        def submit():
            global play_again, msg_box, count
            global a, b, c, d
            count = 0
            user_entry1 = int(e1.get())
            a = abs(user_entry1)
            user_entry2 = int(e2.get())
            b = abs(user_entry2)
            user_entry3 = int(e3.get())
            c = abs(user_entry3)
            user_entry4 = int(e4.get())
            d = abs(user_entry4)

            if check() == True:
                playing = False
                count = count + 1

                messagebox.showinfo("Congratulation", f'Yeah all the answers are correct\n Your score is {count}')
                msg_box = messagebox.askquestion("Play Again", 'Come, play again')
                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                play_again = True

                if msg_box == 'yes':
                    reset()
                    print("Its a yes")
                elif msg_box == 'no':
                    screen1.destroy()
                    print("Its a no")
                else:
                    print("No Response")


            elif check() == False:
                messagebox.showinfo("OOPS! ", 'Not all the answers are correct ! ')
            else:
                print("Something went wrong ! ")
            return count

        def start():
            global screen1
            root.destroy()
            screen1 = Tk()
            screen1.title("GAME STARTS")
            screen1.geometry("1600x900")

            global number1, number2, number3, number4, playing, not_playing
            global e1, e2, e3, e4, v1, v2, v3, v4
            global sign1, sign2, sign3, sign4
            global math_operation
            math_operation = ["+", "-"]

            number1 = random.randint(0, 100)
            number2 = random.randint(0, 100)
            number3 = random.randint(0, 100)
            number4 = random.randint(0, 100)
            sign1 = random.choice(math_operation)
            sign2 = random.choice(math_operation)
            sign3 = random.choice(math_operation)
            sign4 = random.choice(math_operation)

            v1 = StringVar()
            v1 = number1
            v2 = StringVar()
            v2 = number2
            v3 = StringVar()
            v3 = number3
            v4 = StringVar()
            v4 = number4

            playing = True

            while playing:

                num_1 = Label(screen1, text=v1, font=("Helvetica, 25"), height=2, width=6, bg='SystemButtonFace',
                              border=4,
                              borderwidth=4, relief="solid")
                num_1.grid(row=1, column=1, pady=5, padx=5)
                sign_1 = Label(screen1, text=sign1, font=("Helvetica, 25"), height=2, width=6, bg='SystemButtonFace',
                               border=4,
                               borderwidth=4, relief="solid")
                sign_1.grid(row=1, column=2, pady=5, padx=5)
                num_2 = Label(screen1, text=v2, font=("Helvetica, 25"), height=2, width=6, bg='SystemButtonFace',
                              border=4,
                              borderwidth=4, relief="solid")
                num_2.grid(row=1, column=3, pady=5, padx=5)
                equal_label1 = Label(screen1, text="=", font=("Helvetica, 25"), height=2, width=6,
                                     bg='SystemButtonFace',
                                     border=4, borderwidth=4, relief="sunken")
                equal_label1.grid(row=1, column=4, pady=5, padx=5)
                e1 = Entry(screen1, width=3, borderwidth=5, font=("Helvetica, 50"), relief="solid")
                e1.grid(row=1, column=5, pady=5, padx=5)
                sign_2 = Label(screen1, text=sign2, font=("Helvetica, 25"), height=2, width=6, bg='SystemButtonFace',
                               border=4,
                               borderwidth=4, relief="solid")
                sign_2.grid(row=2, column=1, pady=5, padx=5)
                sign_3 = Label(screen1, text=sign3, font=("Helvetica, 25"), height=2, width=6, bg='SystemButtonFace',
                               border=4,
                               borderwidth=4, relief="solid")
                sign_3.grid(row=2, column=3, pady=5, padx=5)
                num_3 = Label(screen1, text=v3, font=("Helvetica, 25"), height=2, width=6, bg='SystemButtonFace',
                              border=4,
                              borderwidth=4, relief="solid")
                num_3.grid(row=3, column=1, pady=5, padx=5)
                sign_4 = Label(screen1, text=sign4, font=("Helvetica, 25"), height=2, width=6, bg='SystemButtonFace',
                               border=4,
                               borderwidth=4, relief="solid")
                sign_4.grid(row=3, column=2, pady=5, padx=5)
                num_4 = Label(screen1, text=v4, font=("Helvetica, 25"), height=2, width=6, bg='SystemButtonFace',
                              border=4,
                              borderwidth=4, relief="solid")
                num_4.grid(row=3, column=3, pady=5, padx=5)
                equal_label2 = Label(screen1, text="=", font=("Helvetica, 25"), height=2, width=6,
                                     bg='SystemButtonFace',
                                     border=4, borderwidth=4, relief="sunken")
                equal_label2.grid(row=3, column=4, pady=5, padx=5)
                e2 = Entry(screen1, width=3, borderwidth=5, font=("Helvetica, 50"), relief="solid")
                e2.grid(row=3, column=5, pady=5, padx=5)
                equal_label3 = Label(screen1, text="=", font=("Helvetica, 25"), height=2, width=6,
                                     bg='SystemButtonFace',
                                     border=4, borderwidth=4, relief="sunken")
                equal_label3.grid(row=4, column=1, pady=5, padx=5)
                equal_label4 = Label(screen1, text="=", font=("Helvetica, 25"), height=2, width=6,
                                     bg='SystemButtonFace',
                                     border=4, borderwidth=4, relief="sunken")
                equal_label4.grid(row=4, column=3, pady=5, padx=5)
                e3 = Entry(screen1, width=3, borderwidth=5, font=("Helvetica, 50"), relief="solid")
                e3.grid(row=5, column=1, pady=5, padx=5)
                e4 = Entry(screen1, width=3, borderwidth=5, font=("Helvetica, 50"), relief="solid")
                e4.grid(row=5, column=3, pady=5, padx=5)

                e1.insert(3, "?")
                e2.insert(3, "?")
                e3.insert(3, "?")
                e4.insert(3, "?")

                submit_buttom = Button(screen1, text="SUBMIT", font=("Helvetica, 25"), height=2, width=8,
                                       bg='SystemButtonFace',
                                       border=4, borderwidth=8, command=submit)
                submit_buttom.grid(row=7, column=2, padx=5, pady=5)
                score_button = Button(screen1, text="SEE SCORE", font=("Helvetica, 25"), height=2, width=10,
                                      bg='SystemButtonFace',
                                      border=4, borderwidth=8, command=see_score)
                score_button.grid(row=7, column=4, padx=5, pady=5)

                user_entry1 = int(e1.get())
                a = abs(user_entry1)
                user_entry2 = int(e2.get())
                b = abs(user_entry2)
                user_entry3 = int(e3.get())
                c = abs(user_entry3)
                user_entry4 = int(e4.get())
                d = abs(user_entry4)

                if (a == v1 + v2 or a == abs(v1 - v2)) and (b == v3 + v4 or b == abs(v3 - v4)) and (
                        c == v1 + v3 or c == abs(v1 - v3)) and (d == v2 + v4 or d == abs(v2 - v4)):
                    playing = False
                    count = count + 1
                    messagebox.showinfo("Congratulation", f'Yeah all the answers are correct\n Your score is {count}')
                    messagebox.askquestion("Play Again ?", 'Going now ? Bye bye')
                    e1.delete(0, END)
                    e2.delete(0, END)
                    e3.delete(0, END)
                    e4.delete(0, END)
                    play_again = True

                else:
                    messagebox.showinfo("OOPS! ", 'Not all the answers are correct ! ')

                while play_again:
                    pass

            screen1.mainloop()

        def main_gui():
            global root, score

            root = Tk()
            root.title("Guess the number game")
            root.geometry("1600x900")

            start_btn = Button(root, text="START", font=("Helvetica, 50"), fg='magenta', borderwidth=4, command=start)
            start_btn.pack(anchor='center', pady=350)

            root.mainloop()

        main_gui()
        #MAIN WORKING FUNCTION
        screen.mainloop()
    elif username!='admin' and password!='1234':
        messagebox.showerror("Invalid", "Invalid credentials")

img = PhotoImage(file='1.png')
Label(root,image=img,bg='white',height=500,width=500).place(x=50,y=50)

frame = Frame(root,width=500,height=500, bg="white")
frame.place(x=600,y=70)

heading = Label(frame, text='Sign in', fg="#57a1f8", bg='white', font=("Microsoft YaHei UI Light", 23, 'bold'))
heading.place(x=190, y=5)
# ---------------------------------------------------------------------------------------------------------------
def on_enter(e):
    username.delete(0,'end')
def on_leave(e):
    name = username.get()
    if name == '':
        username.insert(0, 'Username')

username = Entry(frame, width=25, fg='black', border=0, bg='white', font=("Microsoft YaHei UI Light", 11))
username.place(x=120, y=80)
username.insert(0,'Username')
username.bind('<FocusIn>', on_enter)
username.bind('<FocusOut>', on_leave)

Frame(frame,width=295, height=2, bg='black').place(x=100,y=107)
# ---------------------------------------------------------------------------------------------------------------
def on_enter(e):
    password.delete(0,'end')
def on_leave(e):
    name = password.get()
    if name == '':
        password.insert(0, 'Password')

password = Entry(frame, width=25, fg='black', border=0, bg='white', font=("Microsoft YaHei UI Light", 11))
password.place(x=120, y=150)
password.insert(0,'Password')
password.bind('<FocusIn>', on_enter)
password.bind('<FocusOut>', on_leave)

Frame(frame,width=295, height=2, bg='black').place(x=100,y=177)
# ---------------------------------------------------------------------------------------------------------------
Button(frame, width=39,pady=7, text='Sign in', bg="#57a1f8", fg='white', border=0,command=signin).place(x=107, y=204)
label= Label(frame, text="Don't have an account ? ", fg='black', bg='white', font=("Microsoft YaHei UI Light", 9))
label.place(x=95, y=270)

sign_up = Button(frame, width=6, text = 'Sign up', border=0, bg='white', cursor='hand2', fg="#57a1f8")
sign_up.place(x=240, y=270)

root.mainloop()