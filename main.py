from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
# Load the kv files
Builder.load_file('login.kv')
Builder.load_file('main.kv')

class LoginScreen(Screen):
    def login(self):
        username = self.ids.username_input.text
        password = self.ids.password_input.text

        if username == '1' and password == '1':
            #self.manager.get_screen('main').username = username
            app = App.get_running_app()
            app.un=username
            app.pw=password
            self.manager.current = 'main'          
        else:
            self.ids.error_label.text = 'Invalid username or password'

class MainScreen(Screen):
    #username=''
    
    def showmessage(self):
        app = App.get_running_app()
        self.manager.current = 'MoveIn'
        #app = App.get_running_app()
        #popup = Popup(title='Test popup', content=Label(text=app.un),
        #      auto_dismiss=True)
        #popup.open()
    def BulletinBoard(self):
        app = App.get_running_app()
        self.manager.current = 'bulletin_board'
        self.manager.current_screen.set_parameter(app.un +'_'+app.pw)

class BulletinBoardScreen(Screen):
    def set_parameter(self,new_parameter):
        pass

class ChangePasswordScreen(Screen):
    def update_password(self):
        old_password = self.ids.old_password_input.text
        new_password = self.ids.new_password_input.text

        # Update the password

        self.ids.update_label.text = 'Password updated successfully'

class MoveInScreen(Screen):
    pass
class MyApp(App):
    def build(self):
        # Create the screen manager
        sm = ScreenManager()

        # Add the screens
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(BulletinBoardScreen(name='bulletin_board'))
        sm.add_widget(ChangePasswordScreen(name='change_password'))
        sm.add_widget(MoveInScreen(name='MoveIn'))

        return sm

if __name__ == '__main__':
    MyApp().run()
