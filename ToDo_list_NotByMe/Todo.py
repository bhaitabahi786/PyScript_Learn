
from js import document, localStorage, Object

Tasks = localStorage

new_Task = Element('new-Task')
add_Task_form = Element('add-Task-form')
Task_container = Element('Task-container')

update_Task = Element('update-Task')
edit_Task_form = Element('edit-Task-form')
edit_Task_container = Element('edit-Task-container')


def add_new_Task(e):
    e.preventDefault()
    localStorage.setItem(get_next_Task_id(), new_Task.element.value)
    new_Task.element.value = ""
    get_Tasks()

# Returns an integer that is the next Task id


def get_next_Task_id():
    # declares an empty python dictionary
    Task_dict = dict({})
    next_id = 0

    # function to loop through local storage and add all the key-value pairs to the python dictionary
    def Task_loop(Tasks_entries, _, __):
        Task_dict[Tasks_entries[0]] = Tasks_entries[1]
        print("Inside taskloop entry 0 : ",Tasks_entries[0])
        print("Inside taskloop entry 1 : ",Tasks_entries[1])
        print("Inside taskloop Task_dict : ",Task_dict)

    Object.entries(Tasks).map(Task_loop)

    # Check for the max id in the dictionary and assign the value to next_id
    for Task_key in Task_dict:
        if next_id < int(Task_key):
            next_id = int(Task_key)

    return next_id + 1

# Function to fetch and append all Tasks to the document


def get_Tasks():
    # Clean inside the Task container lelement
    Task_container.element.innerHTML = ""
    # loop through all Task to append them to the Task container
    Object.entries(Tasks).forEach(Task_entries_loop)


def Task_entries_loop(Task_list, _, __):
    key = str(Task_list[0])
    Task = Tasks.getItem(key)
    # Creates new list element and buttons for editing and deleting Task
    btn_wrapper = document.createElement("div")
    Task_elem = document.createElement('li')
    Task_edit_btn = document.createElement('button')
    Task_del_btn = document.createElement('button')

    # Set classes and id for element
    btn_wrapper.className = "flex"
    btn_wrapper.id = key
    Task_del_btn.className = "delete-btn"
    Task_edit_btn.className = "edit-btn"
    Task_elem.className = "Task-" + key

    Task_edit_btn.innerText = "Edit"
    Task_del_btn.innerText = "Delete"
    Task_elem.innerText = Task

    # Append buttons to list element
    btn_wrapper.appendChild(Task_edit_btn)
    btn_wrapper.appendChild(Task_del_btn)

    Task_elem.appendChild(btn_wrapper)
    # events
    Task_del_btn.onclick = delete_Task
    Task_edit_btn.onclick = open_edit_container

    # append the new Task to the container
    Task_container.element.appendChild(Task_elem)


# Function to delete a memu using the key passed to parent as id
def delete_Task(e):
    Task_id = e.target.parentNode.id
    Tasks.removeItem(Task_id)
    get_Tasks()

# Function to edit a memu using the key passed to parent as id


def edit_Task(e):
    e.preventDefault()
    Task_id = e.target.classList
    print("edit task Task_id : ",Task_id)
    Tasks.setItem(Task_id, update_Task.element.value)
    close_edit_container()
    get_Tasks()

# Function to toggle the edit container

def open_edit_container(e):
    Task_id = e.target.parentNode.id
    print("open edit container Task_id : ",Task_id)
    edit_Task_container.element.classList.add("open")
    edit_Task_form.element.className = Task_id
    update_Task.element.value = Tasks.getItem(Task_id)


def close_edit_container():
    edit_Task_form.element.className = ""
    update_Task.element.value = ""
    edit_Task_container.element.classList.remove("open")


get_Tasks()

# Events
add_Task_form.element.onsubmit = add_new_Task
edit_Task_form.element.onsubmit = edit_Task
