import FreeSimpleGUI as sg


def convert(feet: object, inches: object) -> object:
    """ Converts from imperial to metric (meters)."""
    meters = feet * 0.3048 + inches * 0.0254
    return meters


label1 = sg.Text("Enter feet:")
input1 = sg.Input(key="feet")

label2 = sg.Text("Enter inches:")
input2 = sg.Input(key="inches")

convert_button = sg.Button("Convert")
output_label = sg.Text(key="output", text_color="white")

exit_button = sg.Button("Exit")

window = sg.Window("File Compressor",
                   layout=[[label1, input1],
                           [label2, input2],
                           [convert_button, exit_button, output_label]])

while True:
    event, values = window.read()

    # if the app is closed by hitting the red x in the corner or the exit button
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    try:
        feet = float(values["feet"])
        inches = float(values["inches"])
        result = convert(feet, inches)
        window["output"].update(value=f"{result} m", text_color="white")
        output_label = convert(feet, inches)
        window["output"].update(f"{output_label} m")

    except ValueError:
        sg.popup("Please provide two numbers.", font=("Helvetica", 20))

window.close()
