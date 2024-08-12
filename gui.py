from modules import functions1

import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")

# allow the user to enter to do then add a key to the item to reference it in the future
input_box = sg.InputText(tooltip="Enter todo",
                         key="todo")

add_button = sg.Button("Add")

# list of all current todos
list_box = sg.Listbox(values=functions1.get_todos(), key='item_to_edit',
                      enable_events=True, size=[45, 10])

edit_button = sg.Button("Edit list")

window = sg.Window("My To-Do App",
                   layout=[[label],
                           [input_box, add_button],
                           [list_box, edit_button]],
                   font=('Helvetica', 20))

# keep the app open after each item is added
while True:
    # assign variables to the first two items in the tuple
    event, values = window.read()

    # easy way to see what is happening, not needed in final code
    print(1, event)
    print(2, values)
    print(3, values['item_to_edit'])

    match event:

        # the same function from cli file
        case "Add":
            todos = functions1.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions1.write_todos(todos)

            window['item_to_edit'].update(values=todos)

        # similar function from cli file
        case "Edit list":
            # added 0 to only get the item, remove the newline
            todo_to_edit = values['item_to_edit'][0]

            # get the new item from the text box
            new_todo = values['todo']

            # get the list from the text file
            todo_list = functions1.get_todos()

            # find the item to edit
            index = todo_list.index(todo_to_edit)

            # overwrite the item in the text file
            todo_list[index] = new_todo

            # write the updated list to the text file
            functions1.write_todos(todo_list)

            # replace the old item in the app with the new item
            window['item_to_edit'].update(values=todo_list)

        # when an item in the list is selected, this updates the text box with that item
        case 'item_to_edit':
            window['todo'].update(value=values['item_to_edit'][0])

        # if the app is closed by hitting the red x in the corner
        case sg.WIN_CLOSED:
            break

window.close()