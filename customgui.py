import customtkinter
from quizletsearch import simpsel 
#google sign in pop up gets in the way(locate and click on the element)
#closing pop up makes it work 
''' raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.ElementClickInterceptedExceptio
n: Message: Element <span> is not clickable at point (540,
273) because another element <iframe src="https://accounts
.google.com/gsi/iframe/select?client_id=520305074949.apps.
googleusercontent.com&auto_select=true&ux_mode=popup&ui_mo
de=card&as=pg%2BBDStgEqqR4w1NXRaj9g&is_itp=true&channel_id
=d1e766d518ea29152e85e5bc4997bce91b588149b3461e79aa7f17d8c
4e50d78&origin=https%3A%2F%2Fquizlet.com"> obscures it
Stacktrace:
'''
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










