import flet as ft
import buttonClick

instruction_text = ft.TextField(
    value = "Press on the microphone and speak into it so it can suggest icebreaker topics",
    disabled = True,
    bgcolor = "lightblue",
    border_color = "blue",
    color = "black",
    multiline = True,
    min_lines = 2,
    max_lines = 4,
    expand = False,
)

mic_button = ft.Container(
    content = ft.Image(
        src = "https://cdn-icons-png.flaticon.com/512/8863/8863272.png",
        width = 700,
        height = 700
    ),
    tooltip = "Speak",
    on_click = buttonClick.micButtonClick,
    width = 700,
    height = 700,
    border_radius = 50,  #circle hitbox
    alignment = ft.alignment.top_left,
    margin = ft.margin.only(top = 170, left = 50)
)


cancel_icon = ft.Container(
    content = ft.Image(
        src = "https://img.icons8.com/fluent-systems-regular/512/228BE6/cancel.png", 
        width = 100,
        height = 100
    ),
    tooltip = "Cancel",
    on_click = buttonClick.cancelButtonClick,
    width = 100,
    height = 100,
    border_radius = 50,  #circle hitbox
    clip_behavior = ft.ClipBehavior.HARD_EDGE,  # ensure it's clipped
    alignment = ft.alignment.top_right,
    margin = ft.margin.only(top = 20, left = 230) 
)

mic_cancel_group = ft.Stack([
    mic_button,
    cancel_icon
], width = 320, height = 320)  

left_column = ft.Column(
    controls = [mic_cancel_group],
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
