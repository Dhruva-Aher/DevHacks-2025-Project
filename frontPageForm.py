import flet as ft
from flet import View, Page, AppBar, ElevatedButton, Text
from flet import RouteChangeEvent, ViewPopEvent, CrossAxisAlignment, MainAxisAlignment
import homeScreen

#List of users
# usernameList = ["enguyen", "daher", "psolomon"]
userNamePassword = {"enguyen": "ethan2007",
                "daher" : "dhruva2007",
                "psolomon" : "prince2007"}
# passwordList = ["ethan2007", "dhruva2007", "prince2007"]

#Keep this global to reference in the function
username_field = ft.TextField(
    label = "Username", 
    text_size = 16,
    border_radius = 14, 
    focused_border_color = 'black', 
    color = 'black',
    cursor_color = 'black',
    border_width = 0.6,
    border_color = 'black',
)

password_field = ft.TextField(
    label = "Password", 
    text_size = 16,
    border_radius = 14, 
    focused_border_color = 'black', 
    color = 'black',
    cursor_color = 'black',
    border_width = 0.6,
    border_color = 'black',
    password = True,
    can_reveal_password = True,
)

def main(page: Page) -> None:
    page.window.width = 800
    page.window.height = 700
    page.bgcolor='#87CEEB'
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'

    def form_submit_function(e):

        #Checking if the user input is in the username database
        if username_field.value in userNamePassword:
            if userNamePassword[username_field.value] == password_field.value:
                # Login successful
                print("Login Successful")
                print(f"Username: {username_field.value}")
                print(f"Password: {password_field.value}")
                page.go('/mainUI')
            else:
                print("Login Unsuccessful")  # Wrong password
        else:
            print("Login Unsuccessful")  # Username not found


    def route_change(e: RouteChangeEvent) -> None:
        page.views.clear()

        #Login View
        page.views.append(
            View(
                route='/',
                vertical_alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                bgcolor = '#87CEEB',
                controls = [
                    ft.Container(
                    ft.Column([
                        ft.Text("Welcome to our Icebreaker App", size = 24, color = 'black', weight = 'w600'),
                        username_field,
                        password_field,
                        ElevatedButton(text="Go to Main UI", 
                                        on_click=form_submit_function,
                                        color = 'white',
                                        width = 700,
                                        height = 40,
                                        style = ft.ButtonStyle(
                                        text_style = ft.TextStyle(size = 16, weight = 'w600'),
                                        bgcolor = '#87CEEB',
                                        )
                                      )
                    ], horizontal_alignment = 'center'),
                    width = 400, 
                    height = 400, 
                    bgcolor = 'white',
                    border_radius = 18,
                    padding = 20,
                    )
        ]))

        #Main UI
        if page.route == '/mainUI':
            page.views.append(
            View(
                route='/',
                vertical_alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                spacing=26,
                
                controls=[ ft.Column(
                    expand=True,   # fill available space
                    controls=[
                        homeScreen.instruction_text,
                        homeScreen.main_row,
                        ft.Container(expand=True),  # pushes the button down
                        ft.Row(
                            controls=[
                                ft.ElevatedButton(
                                    text="Go back",
                                    on_click=lambda _: page.go('/'),
                                    width=120,
                                )
                            ],
                            alignment=ft.MainAxisAlignment.START,  # left
                        )
                    ]
                )]
            ))
                
        page.update()

    def view_pop(e: ViewPopEvent) -> None:
        page.views.pop()
        if page.views:
            top_view: View = page.views[-1]
            page.go(top_view.route)
    
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

if __name__ == '__main__':
    ft.app(target=main)
