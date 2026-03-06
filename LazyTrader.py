import tkinter as tk
import webbrowser
import json

# --- LOAD CONFIG ---
with open("config.json") as f:
    config = json.load(f)

risk_percent = config["risk_percent"] / 100  # convert to decimal
checks = config["checklist_items"]
urls = config.get("urls", [])

# --- OPEN WEBSITES IN FIREFOX ---
firefox_path = r"C:\Program Files\Mozilla Firefox\firefox.exe"
webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(firefox_path))

for url in urls:
    webbrowser.get('firefox').open(url)

# --- GUI ---
root = tk.Tk()
root.title("NASDAQ Checklist + Risk Calculator")
root.geometry("300x400")
root.attributes("-topmost", True)

vars = []

def update_color():
    if all(v.get() for v in vars):
        root.configure(bg="green")
    else:
        root.configure(bg="SystemButtonFace")

tk.Label(root, text="Checklist:", font=("Arial", 12, "bold")).pack(pady=5)
frame = tk.Frame(root)
frame.pack(pady=5)

for item in checks:
    var = tk.IntVar()
    chk = tk.Checkbutton(frame, text=item, variable=var, command=update_color)
    chk.pack(anchor="w")
    vars.append(var)

def reset():
    for v in vars:
        v.set(0)
    update_color()
    balance_entry.delete(0, tk.END)
    risk_label.config(text="Risk Amount: $0.00")

tk.Button(root, text="Reset", command=reset).pack(pady=5)

def calculate_risk(event=None):
    try:
        balance = float(balance_entry.get())
        risk_amount = balance * risk_percent
        risk_label.config(text=f"Risk Amount: ${risk_amount:,.2f}")
    except:
        risk_label.config(text="Risk Amount: $0.00")

tk.Label(root, text="Account Balance:", font=("Arial", 12, "bold")).pack(pady=5)
balance_entry = tk.Entry(root)
balance_entry.pack()
balance_entry.bind("<KeyRelease>", calculate_risk)

risk_label = tk.Label(root, text="Risk Amount: $0.00", font=("Arial", 12, "bold"))
risk_label.pack(pady=5)

root.mainloop()