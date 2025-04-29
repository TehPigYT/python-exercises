import tkinter as tk
from tkinter import ttk  # ttk = themed widgets
from tkinter.messagebox import showwarning


def add_task():
    task = entry_task.get()
    if task == "":
        showwarning(title="Σφάλμα!", message="Θα πρέπει να εισάγετε μια εργασία")
    elif task in tasks.get():
        showwarning(title="Σφάλμα!", message="H εργασία ήδη υπάρχει στη λίστα")
    else:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)


def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]  # επιλογή εργασίας
        listbox_tasks.delete(task_index)
    except:
        showwarning(title="Σφάλμα!", message="Θα πρέπει να επιλέξετε μια εργασία")


#  δημιουργία GUI
root = tk.Tk()  # δημιουργία παραθύρου
root.title("Λίστα εργασιών")
tasks = tk.Variable(value=[])

frame_tasks = ttk.Frame(root)  # δημιουργία frame για το listbox και το scrollbar
frame_tasks.pack()  # τοποθέτηση frame στο παράθυρο

listbox_tasks = tk.Listbox(
    frame_tasks, height=10, width=50, listvariable=tasks
)  # δημιουργία listbox
listbox_tasks.pack(side=tk.LEFT)  # τοποθέτηση listbox στο frame

scrollbar_tasks = ttk.Scrollbar(frame_tasks)  # δημιουργία scrollbar για το listbox
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)  # τοποθέτηση scrollbar στο frame

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)  # σύνδεση listbox με scrollbar
scrollbar_tasks.config(command=listbox_tasks.yview)  # σύνδεση scrollbar με listbox

entry_task = ttk.Entry(root)
entry_task.pack(
    fill="x", expand=True
)  # fill="x" για να γεμίζει το πλάτος του παραθύρου

button_add_task = ttk.Button(root, text="Νέα εργασία")
button_add_task["command"] = add_task  # ή button_add_task.config(command=add_task)
button_add_task.pack(fill="x", expand=True)

button_delete_task = ttk.Button(root, text="Διαγραφή εργασίας", command=delete_task)
button_delete_task.pack(fill="x", expand=True)

root.eval("tk::PlaceWindow . center")  # τοποθέτηση παραθύρου στο κέντρο της οθόνης
root.mainloop()  # έναρξη βρόχου επεξεργασίας γραφικών