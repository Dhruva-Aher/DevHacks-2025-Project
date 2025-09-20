import flet as ft

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

def form_submit_function(e):
    print("Form Submitted")
    
    #List of users
    usernameList = ["enguyen", "daher", "psolomon"]
    passwordList = ["ethan2007", "dhruva2007", "prince2007"]

    #Checking if the user input is in the username database
    if (username_field.value in usernameList):

        #Get the index
        index = usernameList.index(username_field.value)

        if (password_field.value in passwordList and 
            passwordList[index] == password_field.value):
            
            #Login successful
            print("Login Unsuccessful")
            print(f"Username: {username_field.value}")
            print(f"Password: {password_field.value}")
    else:
        print("Login Unsuccessful")

form_container = ft.Container(
    ft.Column([
        ft.Text("Welcome to our Icebreaker App", size = 24, color = 'black', weight = 'w600'),
        username_field,
        password_field,
        ft.Button(
            "Submit", 
            on_click = form_submit_function,
            color = 'white',
            width = 700,
            height = 40,
            style = ft.ButtonStyle(
                text_style = ft.TextStyle(size = 16, weight = 'w600'),
                bgcolor = '#87CEEB',
            )
        )
        

    ], horizontal_alignment= 'center'),
    width = 400, 
    height = 400, 
    bgcolor = 'white',
    border_radius = 18,
    padding = 20,
)

def main(page:ft.Page):
    
    page.window.width = 600
    page.window.height = 500
    page.bgcolor='#87CEEB'
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    page.add(
        form_container
    )

ft.app(main)
