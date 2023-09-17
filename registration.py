
import tkinter as tk
import json

def save_registration():
    name = entry_name.get()
    email = entry_email.get()
    contact = entry_contact.get()
    address = entry_address.get()

   
    registration_data = {
        "Name": name,
        "Email": email,
        "Contact": contact,
        "Address": address
    }

    
    with open("ankit.json", "w") as json_file:
        json.dump(registration_data, json_file, indent=4)

    
    entry_name.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_contact.delete(0, tk.END)
    entry_address.delete(0, tk.END)


root = tk.Tk()
root.title("Registration Form")


label_name = tk.Label(root, text="Name:", bg="lightgray", font=("Arial", 12))
entry_name = tk.Entry(root, width=40, font=("Arial", 12))

label_email = tk.Label(root, text="Email:", bg="lightgray", font=("Arial", 12))
entry_email = tk.Entry(root, width=40, font=("Arial", 12))

label_contact = tk.Label(root, text="Contact No:", bg="lightgray", font=("Arial", 12))
entry_contact = tk.Entry(root, width=40, font=("Arial", 12))

label_address = tk.Label(root, text="Address:", bg="lightgray", font=("Arial", 12))
entry_address = tk.Entry(root, width=40, font=("Arial", 12))

submit_button = tk.Button(root, text="Submit", command=save_registration, font=("Arial", 12))


label_name.grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_name.grid(row=0, column=1, padx=10, pady=5, columnspan=2)

label_email.grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_email.grid(row=1, column=1, padx=10, pady=5, columnspan=2)

label_contact.grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_contact.grid(row=2, column=1, padx=10, pady=5, columnspan=2)

label_address.grid(row=3, column=0, padx=10, pady=5, sticky="w")
entry_address.grid(row=3, column=1, padx=10, pady=5, columnspan=2)

submit_button.grid(row=4, columnspan=3, pady=10)

root.mainloop()