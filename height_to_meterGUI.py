import PySimpleGUI as sg


def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters


layout = [[sg.Text("Feet:"), sg.Input(tooltip="Enter Feet", key="feet")],
          [sg.Text("Inches:"), sg.Input(tooltip="Enter Inches", key="inches")],
          [sg.Button("Convert"), sg.Button("Exit"), sg.Text(key="output")]]

window = sg.Window("Height to Meter Convertor", layout=layout)

while True:
    event, values = window.read()
    match event:
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break
    try:
        feet = float(values["feet"])
        inches = float(values["inches"])
        result = convert(feet,inches)
        window["output"].update(value=f"{result}m", text_color="WHITE")

    except ValueError:
        sg.popup("Please provide 2 number!", title="Error")


window.close()
