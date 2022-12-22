import customtkinter
from winquizletsearch import wimsimpsel



class App(customtkinter.CTk):

    customtkinter.set_appearance_mode("dark")

    def __init__(self):
        super().__init__()

        self.title("Quizlet to Anki")
        self.minsize(410,300)
        self.button = customtkinter.CTkButton(master=self,text = "To Search", command=self.button_callback)
        self.button.pack(padx=20, pady=200)

    def button_callback(self):
        dialog = customtkinter.CTkInputDialog(text="Type subject to be searched for. Use dashes: \"-\" substituted for spaces",title="Quizlet Search")
        #simpsel.autodeck(dialog.get_input()) 
        simpsel.autodeck(dialog.get_input())


if __name__ == "__main__":
    app = App()
    app.mainloop()










