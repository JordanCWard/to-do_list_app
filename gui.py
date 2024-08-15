from modules import functions1
import FreeSimpleGUI as sg
import time

# more themes: https://docs.pysimplegui.com/en/latest/documentation/module/themes/
sg.theme("DarkTeal12")

clock = sg.Text('', key="clock_key")
label = sg.Text("Type in a to-do")

# allow the user to enter to do then add a key to the item to reference it in the future
input_box = sg.InputText(tooltip="Enter todo",
                         key="todo")

add_button = sg.Button("Add")

# list of all current todos
list_box = sg.Listbox(values=functions1.get_todos(), key='item_to_edit',
                      enable_events=True, size=[45, 10])

edit_button = sg.Button("Edit list")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")


window_layout = [[clock],
                 [label],
                 [input_box, add_button],
                 [list_box, edit_button, complete_button],
                 [exit_button]]

window = sg.Window("My To-Do App",
                   window_layout,
                   font=('Helvetica', 20))

# loop reoccurs every time the user does something
while True:

    # assign variables to the first two items in the tuple
    # added a timeout which reruns the loop every 200 milliseconds so that the clock updates
    event, values = window.read(timeout=200)
    window["clock_key"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

    # easy way to see what is happening, not needed in final code
    print(1, event)
    print(2, values)
    print(3, values['item_to_edit'])


    # if the app is closed by hitting the red x in the corner or the exit button
    if event == sg.WIN_CLOSED or event == "Exit":
        break


    """
    These if statements check to see if any buttons were selected
    or if an item from the list was selected.
    """

    # adds an item to the list from the input box
    if event == "Add":
        todos = functions1.get_todos()
        new_todo = values['todo'] + "\n"
        todos.append(new_todo)
        functions1.write_todos(todos)
        window['item_to_edit'].update(values=todos)


    # replaces an item in the list with the input in the text box
    elif event == "Edit list":

        # if the user selects edit list without selecting an item first, an index error will occur
        try:

            # added 0 to only get the item, remove the newline
            todo_to_edit = values['item_to_edit'][0]

            # get the new item from the text box
            new_todo = values['todo']

            # get the list from the text file
            todo_list = functions1.get_todos()

            # find the item to edit
            index = todo_list.index(todo_to_edit)

            # overwrite the item in the text file
            todo_list[index] = new_todo + '\n'

            # write the updated list to the text file
            functions1.write_todos(todo_list)

            # replace the old item in the app with the new item
            window['item_to_edit'].update(values=todo_list)

        # if the user selects edit list without selecting an item first, an index error will occur
        except IndexError:
            sg.popup("Please select an item first", font=("Helvetica", 20))


    # removes an item from the list
    elif event == "Complete":

        # if the user selects complete without selecting an item first, an index error will occur
        try:

            # store the item that was selected in a variable
            completed_todo = values['item_to_edit'][0]

            # create a list with the current todos
            todos_list_temp = functions1.get_todos()

            # remove the selected item from the list
            todos_list_temp.remove(completed_todo)

            # write the new list to the text file
            functions1.write_todos(todos_list_temp)

            # update the window with the new list
            window['item_to_edit'].update(values=todos_list_temp)

            # clear the input window
            window['todo'].update(value="")

        # if the user selects complete without selecting an item first, an index error will occur
        except IndexError:
            sg.popup("Please select an item first", font=("Helvetica", 20))


    # when an item in the list is selected, this updates the text box with that item
    elif event == 'item_to_edit':
        window['todo'].update(value=values['item_to_edit'][0].strip('\n'))


window.close()