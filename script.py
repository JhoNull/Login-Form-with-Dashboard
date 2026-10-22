
import flet as cs
from flet import controls
from flet.controls import border_radius, control_event, page


username = "admin"
password = "admin123"


def main(page: cs.Page):
    page.title="Tracker"
    page.window.height = 400
    page.window.width = 300
    page.theme_mode = cs.ThemeMode.LIGHT



    # The Content of the login page
    def show_login():
        page.clean()

        page.window.height = 400
        page.window.width = 300
        page.window.resizable = False
        page.window.minimizable = False
        page.window.maximizable = False


        user = cs.TextField(
            label="Enter Your Username",
            prefix_icon=cs.Icons.PERSON,
            width=300,
            border_radius=20
        )
        passw = cs.TextField(
            label = "Enter Your Password",
            prefix_icon=cs.Icons.LOCK,
            width=300,
            border_radius=20,
            password=True,
            can_reveal_password = True
        )

        message = cs.Text()
        def buttonclick(e):
            if user.value == username and passw.value == password:
                show_dashboard()
            else:
                message.value = "Wrong Username or Password"
                message.color = "red"
                page.update()
        form = cs.Column (
            controls=[
                cs.Text("Welcome",weight=cs.FontWeight.BOLD, size=20),
                cs.Text("Login",weight=cs.FontWeight.BOLD, size=20),
                user,
                passw,
                cs.Button(content="Login", on_click=buttonclick,width=300),
                message,
            ],
            horizontal_alignment = cs.CrossAxisAlignment.CENTER,
            alignment = cs.MainAxisAlignment.CENTER,
            spacing=15,
            tight=True

        )
        alignment=cs.Alignment.CENTER,
        expand=True


        #dark mode
        def change_theme(e):
            if page.theme_mode == cs.ThemeMode.DARK:
                page.theme_mode = cs.ThemeMode.LIGHT
            else:
                page.theme_mode = cs.ThemeMode.DARK
                page.update()


        page.add(form)
        # This will add the page main content after login
        def show_dashboard():

            page.clean()

            page.window.width = 600
            page.window.height = 600
            page.window.resizable = False
            page.window.maximizable = False
            page.window.minimizable = False
            page.add(
                cs.Column(
                    controls=[
                      cs.Row(
                          controls=[
                              cs.Button(content="Logout", on_click=lambda e: show_login()),
                              cs.Button(content="🌙", on_click=change_theme),
                          ],
                          alignment=cs.MainAxisAlignment.END,
                      ),

                        cs.Container(content=cs.Text("Welcome tracker", size=30, weight=cs.FontWeight.BOLD,),
                        alignment=cs.Alignment(0,0),
                        expand=True,
                        )
                    ],
                ),

            )


    show_login()
cs.run(main=main)




