import customtkinter
import os
from PIL import Image

# субклас, який відповідає за створення додатків 
class MyAppCTk(customtkinter.CTk):
    def __init__(self, title, fg_color):
        super().__init__(fg_color = fg_color)
        self.screen_ctk = customtkinter.CTk
        self.title = title
        self.app_width = 400
        self.app_height = 300
        self.screen_width = self.screen_ctk.winfo_screenwidth(self)
        self.screen_height = self.screen_ctk.winfo_screenheight(self)
        self.center_cor = f'{self.app_width}x{self.app_height}+{self.screen_width // 2 - self.app_width // 2}+{self.screen_height // 2 - self.app_height // 2}'
        self.choice_image = ''
        # якщо вказати шлях топ працює, але якщо через змінну "self.choice_image" то ні
        self.image = customtkinter.CTkImage(light_image = Image.open(self.choice_image),
                                            size = (self.app_width, self.app_height))
        self.label = customtkinter.CTkLabel(master = self.master, 
                                            text = "",
                                            image = self.image)
        self.label.place(x = self.app_width // 2, y = self.app_height // 2, anchor = customtkinter.CENTER)
    # шлях до зображення
    def path_to_img(self, name_img):
        path_to_img = __file__.split('\\')
        del path_to_img[-1]
        path_to_img = '\\'.join(path_to_img)
        path_to_img = os.path.join(path_to_img,name_img)
        self.choice_image += path_to_img
        return path_to_img
    # вивидення додатку
    def show_screen(self):
        self.screen_ctk.geometry(self, geometry_string = self.center_cor)
        self.screen_ctk.title(self,string = self.title)
        self.screen_ctk.mainloop(self)


my_app = MyAppCTk(title = "App", fg_color = "green")
my_app.path_to_img('img\\1.jpg')
my_app.show_screen()



