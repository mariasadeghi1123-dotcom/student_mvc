import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from controller import StudentController

controller = StudentController()

root = tk.Tk()
root.title("Student Manager MVC")
root.geometry("900x520")
root.configure(bg="#2c3e50")

# -------- Input Frame --------
input_frame = tk.Frame(root, bg="#34495e", padx=10, pady=10)
input_frame.pack(fill="x")

fields = ["Student ID", "Name", "Age", "Score 1", "Score 2"]
entries = {}

for i, field in enumerate(fields):
    tk.Label(input_frame, text=field, bg="#34495e", fg="white").grid(row=0, column=i)
    e = tk.Entry(input_frame, width=12)
    e.grid(row=1, column=i, padx=5)
    entries[field] = e

# -------- Functions --------
def add_student():
    try:
        ok, msg = controller.add_student(
            int(entries["Student ID"].get()),
            entries["Name"].get(),
            int(entries["Age"].get()),
            float(entries["Score 1"].get()),
            float(entries["Score 2"].get())
        )
        messagebox.showinfo("Result", msg)
        show_all_students()
    except:
        messagebox.showerror("Error", "Invalid input")

def delete_student():
    try:
        ok, msg = controller.delete_student()
        messagebox.showinfo("Result", msg)
        show_all_students()
    except:
        messagebox.showerror("Error", "Invalid ID")

def update_student():
    # -------- 1) اول حتماً Student ID --------
    student_id_text = simpledialog.askstring(
        "Student ID",
        "Enter Student ID to update:",
        parent=root
    )

    if student_id_text is None:
        return

    try:
        student_id = int(student_id_text)
    except:
        messagebox.showerror("Error", "Invalid Student ID")
        return

    # -------- 2) انتخاب فیلد --------
    field_map = {
        "0": "name",
        "1": "age",
        "2": "score1",
        "3": "score2"
    }

    field_choice = simpledialog.askstring(
        "Update Field",
        "Which field do you want to update?\n"
        "0: Name\n"
        "1: Age\n"
        "2: Score1\n"
        "3: Score2",
        parent=root
    )

    if field_choice is None:
        return

    if field_choice not in field_map:
        messagebox.showerror("Error", "Please enter 0, 1, 2 or 3")
        return

    # -------- 3) مقدار جدید --------
    new_value = simpledialog.askstring(
        "New Value",
        "Enter new value:",
        parent=root
    )

    if new_value is None or new_value.strip() == "":
        messagebox.showerror("Error", "Value cannot be empty")
        return

    ok, msg = controller.update_student(
        student_id,
        field_map[field_choice],
        new_value
    )

    messagebox.showinfo("Result", msg)
    show_all_students()
# -------- SHOW ALL  --------
def show_all_students():
    for row in tree.get_children():
        tree.delete(row)

    students = controller.show_all_students()
    for s in students:
        tree.insert("", "end", values=s)

# -------- Buttons --------
btn_frame = tk.Frame(root, bg="#2c3e50")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add", bg="#27ae60", fg="white", width=12, command=add_student).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Update", bg="#f39c12", fg="white", width=12, command=update_student).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Delete", bg="#c0392b", fg="white", width=12, command=delete_student).grid(row=0, column=2, padx=5)
tk.Button(btn_frame, text="Show All", bg="#2980b9", fg="white", width=12, command=show_all_students).grid(row=0, column=3, padx=5)

# -------- TreeView --------
columns = ("ID", "Name", "Age", "Score1", "Score2", "Average")
tree = ttk.Treeview(root, columns=columns, show="headings", height=12)

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor="center")

tree.pack(fill="both", expand=True, padx=10, pady=10)

root.mainloop()