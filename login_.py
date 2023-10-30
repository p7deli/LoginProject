import customtkinter as tk
from tkinter import Tk, Label, PhotoImage, messagebox
from PIL import ImageTk, Image
from database import Database


class Form_(Tk):
    def __init__(self):
        super().__init__()

        self.title("Login Form")
        self.geometry("850x550+220+70")
        self.resizable(False, False)
        self.config(bg="black")
        self.protocol("WM_DELETE_WINDOW", self.exit)

        self.image_background = Image.open(r"pictures/earth.jpg")
        self.image_background = self.image_background.resize((400, 250))
        self.photo_background = ImageTk.PhotoImage(self.image_background)
        self.lbl_background = Label(self, image=self.photo_background, bg="black")
        self.lbl_background.place(x=10, y=50)

        # ----------------------------------------------- Btn Menu
        self.image_open_menu = PhotoImage(file="pictures/open.png")
        self.btn_open_menu = tk.CTkButton(self, image=self.image_open_menu, text="", bg_color="black",
                                          width=50, fg_color="white", hover_color="#dae0db", command=self.open_menu)
        self.btn_open_menu.place(x=10, y=10)

        self.image_close_menu = PhotoImage(file="pictures/close.png")
        self.btn_close_menu = tk.CTkButton(self, image=self.image_close_menu, text="", bg_color="black",
                                           width=50, fg_color="white", hover_color="#dae0db", command=self.close_menu)
        self.btn_close_menu.place_forget()
        # ____________________________________________________________
        # ___________________________________________________ Frame Menu
        self.menu = tk.CTkFrame(self, width=100, height=65, fg_color="gray", border_width=2,
                                border_color="white")
        self.menu.place_forget()

        self.btn_signup = tk.CTkButton(self.menu, text="Sign Up", width=90, height=25,
                                       fg_color="white", border_width=2, border_color="black",
                                       text_color="black", font=("Arial", 12), command=self.open_sign_up)
        self.btn_signup.place(x=5, y=5)

        self.btn_signin = tk.CTkButton(self.menu, text="Sign In", width=90, height=25,
                                       fg_color="white", border_width=2, border_color="black",
                                       text_color="black", font=("Arial", 12), command=self.open_sign_in)
        self.btn_signin.place_forget()

        self.btn_exit = tk.CTkButton(self.menu, text="Exit", width=90, height=25,
                                     fg_color="white", border_width=2, border_color="black",
                                     text_color="black", font=("Arial", 12), command=self.exit)
        self.btn_exit.place(x=5, y=35)
        # ______________________________________________________________________
        # ________________________________________________________frame form log in
        self.form_log_in = tk.CTkFrame(self, width=405, height=540, fg_color="white",
                                       border_width=2, border_color="gray")
        self.form_log_in.place(x=440, y=5)

        self.img_login = Image.open("pictures/login1.png")
        self.img_login = self.img_login.resize((150, 150))
        self.photo_login = ImageTk.PhotoImage(self.img_login)
        self.lbl_img_login = Label(self.form_log_in, text="", image=self.photo_login,
                                   bg="white")
        self.lbl_img_login.place(x=120, y=5)

        self.photo_username_log_in = PhotoImage(file="pictures/username1.png")
        self.lbl_username_log_in = Label(self.form_log_in, text="", image=self.photo_username_log_in,
                                         bg="white")
        self.lbl_username_log_in.place(x=20, y=185)

        self.txt_username_log_in = tk.CTkEntry(self.form_log_in, width=300, height=50, placeholder_text="Username ...",
                                               font=("Arial", 18), fg_color="white", bg_color="white",
                                               border_color="white", text_color="#449657")
        self.txt_username_log_in.place(x=80, y=190)
        self.f_username_log_in = tk.CTkFrame(self.form_log_in, width=360, height=2, fg_color="black", bg_color="white")
        self.f_username_log_in.place(x=20, y=240)

        self.photo_pass_log_in = PhotoImage(file="pictures/password1.png")
        self.lbl_pass_log_in = Label(self.form_log_in, text="", image=self.photo_pass_log_in,
                                     bg="white")
        self.lbl_pass_log_in.place(x=20, y=250)

        self.txt_pass_log_in = tk.CTkEntry(self.form_log_in, width=300, height=50, placeholder_text="Password ...",
                                           font=("Arial", 18), fg_color="white", bg_color="white",
                                           border_color="white", show="*", text_color="#449657")
        self.txt_pass_log_in.place(x=80, y=250)
        self.f_pass_log_in = tk.CTkFrame(self.form_log_in, width=360, height=2, fg_color="black", bg_color="white")
        self.f_pass_log_in.place(x=20, y=300)

        self.show_hide_pass_log_in = tk.CTkCheckBox(self.form_log_in, text="Show Pass",
                                                    border_width=2, border_color="black", font=("Arial", 15),
                                                    command=self.show_pass)
        self.show_hide_pass_log_in.place(x=150, y=320)

        self.btn_sign = tk.CTkButton(self.form_log_in, text="Sign In", width=385, height=50,
                                     font=("Arial", 20, "bold"), fg_color="white", border_width=4,
                                     border_color="black", text_color="black", hover_color="#d1d0cd",
                                     command=self.login_)
        self.btn_sign.place(x=10, y=360)

        # ______________________________________________________________________
        # ________________________________________________________frame form sign up
        self.form_sign_up = tk.CTkFrame(self, width=405, height=540, fg_color="white",
                                        border_width=2, border_color="gray")
        self.form_sign_up.place_forget()

        self.img_sign_up = Image.open("pictures/login.png")
        self.img_sign_up = self.img_sign_up.resize((150, 150))
        self.photo_sign_up = ImageTk.PhotoImage(self.img_sign_up)
        self.lbl_img_sign_up = Label(self.form_sign_up, text="", image=self.photo_sign_up,
                                     bg="white")
        self.lbl_img_sign_up.place(x=120, y=5)

        self.txt_name_sign_up = tk.CTkEntry(self.form_sign_up, width=150, height=50, placeholder_text="Name ...",
                                            font=("Arial", 18), fg_color="white", bg_color="white",
                                            border_color="white", text_color="#449657")
        self.txt_name_sign_up.place(x=20, y=180)

        self.f_name_sign_up = tk.CTkFrame(self.form_sign_up, width=150, height=2, fg_color="black", bg_color="white")
        self.f_name_sign_up.place(x=20, y=230)

        self.txt_family_sign_up = tk.CTkEntry(self.form_sign_up, width=200, height=50, placeholder_text="Family ...",
                                              font=("Arial", 18), fg_color="white", bg_color="white",
                                              border_color="white", text_color="#449657")
        self.txt_family_sign_up.place(x=180, y=180)

        self.f_family_sign_up = tk.CTkFrame(self.form_sign_up, width=200, height=2, fg_color="black", bg_color="white")
        self.f_family_sign_up.place(x=180, y=230)

        self.photo_username_sign_up = PhotoImage(file="pictures/username.png")
        self.lbl_username_sign_up = Label(self.form_sign_up, text="", image=self.photo_username_sign_up,
                                          bg="white")
        self.lbl_username_sign_up.place(x=20, y=250)

        self.txt_username_sign_up = tk.CTkEntry(self.form_sign_up, width=300, height=50,
                                                placeholder_text="Username ...",
                                                font=("Arial", 18), fg_color="white", bg_color="white",
                                                border_color="white", text_color="#449657")
        self.txt_username_sign_up.place(x=80, y=255)
        self.f_username_sign_up = tk.CTkFrame(self.form_sign_up, width=360, height=2, fg_color="black",
                                              bg_color="white")
        self.f_username_sign_up.place(x=20, y=305)

        self.photo_pass_sign_up = PhotoImage(file="pictures/password.png")
        self.lbl_pass_sign_up = Label(self.form_sign_up, text="", image=self.photo_pass_sign_up,
                                      bg="white")
        self.lbl_pass_sign_up.place(x=20, y=330)

        self.txt_pass_sign_up = tk.CTkEntry(self.form_sign_up, width=300, height=50, placeholder_text="Password ...",
                                            font=("Arial", 18), fg_color="white", bg_color="white",
                                            border_color="white", show="*", text_color="#449657")
        self.txt_pass_sign_up.place(x=80, y=325)
        self.f_pass_sign_up = tk.CTkFrame(self.form_sign_up, width=360, height=2, fg_color="black", bg_color="white")
        self.f_pass_sign_up.place(x=20, y=380)

        self.show_hide_pass_sign_up = tk.CTkCheckBox(self.form_sign_up, text="Show Pass",
                                                     border_width=2, border_color="black", font=("Arial", 15),
                                                     command=self.show_pass)
        self.show_hide_pass_sign_up.place(x=150, y=405)

        self.btn_sign_up = tk.CTkButton(self.form_sign_up, text="Sign Un", width=385, height=50,
                                        font=("Arial", 20, "bold"), fg_color="white", border_width=4,
                                        border_color="black", text_color="black", hover_color="#d1d0cd",
                                        command=self.sign_up_)
        self.btn_sign_up.place(x=10, y=450)

    def open_menu(self):
        self.btn_open_menu.place_forget()
        self.btn_close_menu.place(x=10, y=10)
        self.menu.place(x=10, y=55)

    def close_menu(self):
        self.btn_open_menu.place(x=10, y=10)
        self.btn_close_menu.place_forget()
        self.menu.place_forget()

    def open_sign_up(self):
        self.txt_name_sign_up.focus_set()
        self.btn_signin.place(x=5, y=5)
        self.btn_signup.place_forget()
        self.form_log_in.place_forget()
        self.form_sign_up.place(x=440, y=5)

    def open_sign_in(self):
        self.txt_username_log_in.focus_set()
        self.btn_signin.place_forget()
        self.btn_signup.place(x=5, y=5)
        self.form_log_in.place(x=440, y=5)
        self.form_sign_up.place_forget()

    def show_pass(self):
        if self.show_hide_pass_sign_up.get():
            self.txt_pass_sign_up.configure(show="")
            self.show_hide_pass_sign_up.configure(text="Hide Pass")
        else:
            self.txt_pass_sign_up.configure(show="*")
            self.show_hide_pass_sign_up.configure(text="Show Pass")

        if self.show_hide_pass_log_in.get():
            self.txt_pass_log_in.configure(show="")
            self.show_hide_pass_log_in.configure(text="Hide Pass")
        else:
            self.txt_pass_log_in.configure(show="*")
            self.show_hide_pass_log_in.configure(text="Show Pass")

    def exit(self):
        ques = messagebox.askyesno("Exit", "DO You Want TO Exit?")
        if ques:
            self.destroy()

    def login_(self):
        username = self.txt_username_log_in.get()
        password = self.txt_pass_log_in.get()

        dt = Database("db_user.db")
        dt.is_connect()
        result = dt.check_user(username, password)
        if result:
            self.txt_username_log_in.delete(0, tk.END)
            self.txt_pass_log_in.delete(0, tk.END)
            dt.close_db()
            messagebox.showinfo("Sign In", f"Welcome {username}")
        else:
            dt.close_db()
            messagebox.showerror("Error", "username and password not correct")

    def sign_up_(self):
        name = self.txt_name_sign_up.get()
        family = self.txt_family_sign_up.get()
        username = self.txt_username_sign_up.get()
        password = self.txt_pass_sign_up.get()

        dt = Database("db_user.db")
        dt.is_connect()
        result = dt.creat_user(name, family, username, password)
        if result:
            dt.close_db()
            self.txt_name_sign_up.delete(0, tk.END)
            self.txt_family_sign_up.delete(0, tk.END)
            self.txt_username_sign_up.delete(0, tk.END)
            self.txt_pass_sign_up.delete(0, tk.END)
            messagebox.showinfo("Sign Up", "Profile registration was done successfully\n"
                                           "Please log in again")
            self.open_sign_in()
        else:
            dt.close_db()
            messagebox.showerror("Error", "This user has already been used\n"
                                          "Please enter another user")


def main():
    App = Form_()
    App.mainloop()


if __name__ == "__main__":
    main()
