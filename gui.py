from modules import functions1

import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")


window = sg.Window("My To-Do App",
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 20))

# keep the app open after each item is added
while True:
    # assign variables to the first two items in the tuple
    event, values = window.read()
    print(event)
    print(values)
    match event:

        # basically the same function from cli file
        case "Add":
            todos = functions1.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions1.write_todos(todos)

        # if the app is closed by hitting the red x in the corner
        case sg.WIN_CLOSED:
            break

window.close()