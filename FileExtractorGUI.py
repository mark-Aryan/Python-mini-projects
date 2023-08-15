import PySimpleGUI as sg
import extractor

select_text1 = sg.Text("Select Zip Folder: ")
folder_input1 = sg.Input(key="Zip Folder")
btn1 = sg.FileBrowse(key="Browse")

select_text2 = sg.Text("Select Destination : ")
folder_input2 = sg.Input(key="Path")
btn2 = sg.FolderBrowse(key="Destination")

extract_btn = sg.Button("Extract", key="Extract")
output_lable = sg.Text(key="output", text_color="green")

layout = [[select_text1,folder_input1, btn1], [select_text2,folder_input2, btn2], [extract_btn,output_lable]]
window = sg.Window("File Extractor", layout=layout, font=("Courier", 15))

while True:
    event, values = window.read()
    try:
        zipFolder = values["Zip Folder"]
        path = values["Path"]
        extractor.extract(zipFolder=zipFolder, path=path)
        window["output"].update(value="Extract Completed!")
    except TypeError:
        sg.popup("Extraction Done!", title="Error")
    match event:
        case sg.WIN_CLOSED:
            break

window.close()