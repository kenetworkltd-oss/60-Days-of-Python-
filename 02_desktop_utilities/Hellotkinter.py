#Hello World using Tkinter


import tkinter as tk

# 1. Create the main application window
root = tk.Tk()
root.title("My First GUI")
root.geometry("300x200")  # Set window size to 300px wide, 200px tall

# 2. Create a "Label" widget (text on screen)
hello_label = tk.Label(root, text="Hello World", font=("Arial", 20))

# 3. Pack the label into the window (this places it on the screen)
hello_label.pack(pady=50)

# 4. Start the main event loop (keeps the window open)
root.mainloop()
