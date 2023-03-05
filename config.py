# ---- Config Documentation ----
"""
This module save the constant for the configuration of the program.
Allows to make tests more efficiently.
"""
# ---- Config Documentation ----

# ---- Imports ----
import sys
# ---- End Imports ----

DATABASE_PATH = "clients.csv"
if "pytest" in sys.argv[0]:
    DATABASE_PATH = "tests/test_clients.csv"

