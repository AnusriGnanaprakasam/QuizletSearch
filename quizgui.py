import customtkinter
import makedeck

class App(customtkinter.CTk):
    customtkinter.set_appearance_mode("dark")

    def __init__(self):
        super().__init__()

        self.title("Quizlet to Anki")
        self.minsize(410, 300)
        self.button = customtkinter.CTkButton(master=self, text="To Search", command=self.button_callback)
        self.button.pack(padx=20, pady=200)

    def button_callback(self):
        dialog_text = """Type subject to be searched for. Use dashes: \"-\" substituted for spaces.\n If you want to choose a specific deck, type the name of that deck
        (with dashes still replacing spaces) and use a comma to separate the author from the name. If you cannot find your deck, try to reduce the search down to important words. """
        dialog = customtkinter.CTkInputDialog(text=dialog_text, title="Quizlet Search")
        query = dialog.get_input()
        if ',' in query:
            query, authorname = query.split(",")
            makedeck.main(query, authorname)
        else:
            makedeck.main(query)


if __name__ == "__main__":
    app = App()
    app.mainloop()
