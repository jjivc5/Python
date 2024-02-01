import tkinter as tk

root = tk.Tk()
# Marcos
marco = tk.Frame()

marco1 = tk.Frame()

#configuración

marco.config(width=400,
             height=300,
             bg="purple"
             )


marco1.config(width=400,
              height=300,
              bg="purple4"
              )


marco.pack()

marco1.pack()

root.mainloop()