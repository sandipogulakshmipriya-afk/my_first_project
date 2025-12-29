from tkinter import *
from tkinter.messagebox import *
import random

# ---------------- Submit Function ----------------
def submit_form():
    name_val = name_entry.get()
    age_val = age_entry.get()
    email_val = email_entry.get()
    mobile_val = mobile_entry.get()
    state_val = state_var.get()

    # Gender
    if gender_var.get() == 1:
        gender_val = "Male"
    elif gender_var.get() == 2:
        gender_val = "Female"
    else:
        gender_val = "NA"

    # Skills
    selected_skills = [skills[i] for i in range(len(skills)) if skill_vars[i].get() == 1]
    skills_text = ", ".join(selected_skills)

    # Validation
    if not age_val.isdigit():
        showerror("Error", "Age must be a number")
        return

    if len(mobile_val) != 10 or not mobile_val.isdigit():
        showwarning("Warning", "Mobile number must be 10 digits")
        return

    # Generate Registration ID
    reg_id = "REG" + name_val[:2].upper() + age_val + str(random.randint(1000, 9999))

    # Set output variables
    regid_var.set(reg_id)
    name_var.set(name_val)
    age_var.set(age_val)
    email_var.set(email_val)
    mobile_var.set(mobile_val)
    state_out.set(state_val)
    gender_out.set(gender_val)
    skill_out.set(skills_text)

    showinfo("Success", "Form submitted successfully")

# ---------------- Main Window ----------------
root = Tk()
root.title("Student Form")
root.geometry("900x600")

# ---------------- Variables ----------------
regid_var = StringVar()
name_var = StringVar()
age_var = StringVar()
email_var = StringVar()
mobile_var = StringVar()
state_out = StringVar()
gender_out = StringVar()
skill_out = StringVar()

# ---------------- Input Fields ----------------
Label(root, text="Name").grid(row=0, column=0)
name_entry = Entry(root)
name_entry.grid(row=0, column=1)

Label(root, text="Age").grid(row=1, column=0)
age_entry = Entry(root)
age_entry.grid(row=1, column=1)

Label(root, text="Email").grid(row=2, column=0)
email_entry = Entry(root)
email_entry.grid(row=2, column=1)

Label(root, text="Mobile").grid(row=3, column=0)
mobile_entry = Entry(root)
mobile_entry.grid(row=3, column=1)

# ---------------- State ----------------
Label(root, text="State").grid(row=4, column=0)
state_var = StringVar()
state_var.set("Select State")
OptionMenu(root, state_var, "AP", "TS", "BR").grid(row=4, column=1)

# ---------------- Gender ----------------
Label(root, text="Gender").grid(row=5, column=0)
gender_var = IntVar()
Radiobutton(root, text="Male", variable=gender_var, value=1).grid(row=5, column=1)
Radiobutton(root, text="Female", variable=gender_var, value=2).grid(row=5, column=2)

# ---------------- Skills ----------------
Label(root, text="Skills").grid(row=6, column=0)
skills = ["Python", "Java", "HTML", "CSS", "JS"]
skill_vars = [IntVar() for _ in skills]

for i in range(len(skills)):
    Checkbutton(root, text=skills[i], variable=skill_vars[i]).grid(row=6, column=i+1)

# ---------------- Submit Button ----------------
Button(root, text="Submit", bg="green", command=submit_form).grid(row=7, column=1)

# ---------------- Output Section ----------------
Label(root, text="REG ID").grid(row=8, column=0)
Label(root, textvariable=regid_var, fg="green").grid(row=8, column=1)

Label(root, text="Name").grid(row=9, column=0)
Label(root, textvariable=name_var, fg="green").grid(row=9, column=1)

Label(root, text="Age").grid(row=10, column=0)
Label(root, textvariable=age_var, fg="green").grid(row=10, column=1)

Label(root, text="Email").grid(row=11, column=0)
Label(root, textvariable=email_var, fg="green").grid(row=11, column=1)

Label(root, text="Mobile").grid(row=12, column=0)
Label(root, textvariable=mobile_var, fg="green").grid(row=12, column=1)

Label(root, text="State").grid(row=13, column=0)
Label(root, textvariable=state_out, fg="green").grid(row=13, column=1)

Label(root, text="Gender").grid(row=14, column=0)
Label(root, textvariable=gender_out, fg="green").grid(row=14, column=1)

Label(root, text="Skills").grid(row=15, column=0)
Label(root, textvariable=skill_out, fg="green").grid(row=15, column=1)

root.mainloop()
