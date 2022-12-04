
import customtkinter

class App(customtkinter.CTk):

    customtkinter.set_appearance_mode("dark")

    def __init__(self):
        super().__init__()

        self.title("Quizlet to Anki")
        self.minsize(410,300)
        self.button = customtkinter.CTkButton(master=self,text = "To Search", command=self.button_callback)
        self.button.pack(padx=20, pady=200)

    def button_callback(self):
        dialog = customtkinter.CTkInputDialog(text="type subject to be searched for with \"-\" substituted for spaces",title="Quizlet Search")
        print(dialog)


if __name__ == "__main__":
    app = App()
    app.mainloop()











# needed to install tk package to actually run it
'''customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")

def login():
    print("t")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20,padx=60,fill="both",expand=True)

label = customtkinter.CTkLabel(master=frame, text="Login",font=("Roboto",24))
label.pack(pady=12,padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12,padx=10)


entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entry2.pack(pady=12,padx=10)

button = customtkinter.CTkButton(master=frame, text="login",command=login)
button.pack(pady=12,padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text = "REmember meee")
checkbox.pack(pady=12,padx=10)


root.mainloop()


'''

