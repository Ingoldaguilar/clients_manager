# ---- Run Documentation ----
"""
Main file of the program.
"""
# ---- Run Documentation ----

# ---- Imports ----
import menu
import sys
import ui
# ---- End Imports ----
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "-t":
        menu.init()
    else:
        app = ui.MainWindow()
        app.mainloop()