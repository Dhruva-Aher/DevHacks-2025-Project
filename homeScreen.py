import flet as ft

instruction_text = ft.TextField(
    value = "Please press on the microphone and speak into it so it can suggest an icebreaker topic.",
    disabled = True,
    bgcolor = "lightblue",
    border_color = "blue",
    color = "black",
    multiline = True,
    min_lines = 2,
    max_lines = 4,
    expand = False
)

mic_button = ft.Container(
    content = ft.Image(
        src = "https://img.freepik.com/premium-vector/vector-microphone-icon-blue-microphone-button-flat-design-record-button-isolated_118339-1767.jpg",
        width = 700,
        height = 700
    ),
    tooltip = "Speak",
    on_click = lambda e: print("Mic clicked!"),
    alignment = ft.alignment.top_left,
    margin = ft.margin.only(top = 170, left = 50)
)


refresh_icon = ft.Container(
    content = ft.Image(
        src = "https://i.fbcd.co/products/original/27e1bd4903a0e30e8e1c9daaf21b780704be85f408a163876c439dd6459f6384.jpg", 
        width = 100,
        height = 100
    ),
    tooltip = "Refresh",
    on_click = lambda e: print("Refresh clicked!"),
    alignment = ft.alignment.top_right,
    margin = ft.margin.only(top = 20, left = 230) 
)

mic_refresh_group = ft.Stack([
    mic_button,
    refresh_icon
], width = 320, height = 320)  

left_column = ft.Column(
    controls = [mic_refresh_group],
    alignment = "start",
    horizontal_alignment = "start",
    expand = True
)

output_columns = []
for i in range(1, 6):  
    title = ft.Text(f"Output {i}", weight="bold", color="black")
    textbox = ft.TextField(
        value = "",
        disabled = True,
        color = "black",
        width = 400
    )
    output_columns.append(ft.Column([title, textbox], spacing=5, expand=False))

right_column = ft.Column(
    controls = output_columns,
    spacing = 15,
    alignment = "center",
    horizontal_alignment = "center",
    expand = False
)

main_row = ft.Row(
    controls = [left_column, right_column],
    alignment = ft.MainAxisAlignment.END,
    vertical_alignment = ft.CrossAxisAlignment.START,
    expand = True,
    spacing = 40
)
