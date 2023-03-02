# ---- Helpers Documentation ----
"""
Module for auxiliary functions.
"""
# ---- Helpers Documentation ----

# ---- Imports ----
import os
import platform
import re
# ---- End Imports ----

# ---- Functions ----
def clean_screen():
    """
    This function read the operative system that
    is running the program and choose a specific
    way of cleaning the screen depending on the
    platform. (windows, else => linux or mac)
    :return: None
    """
    os.system("cls") if platform.system() == "Windows" else os.system("clear")

def read_text(min_len=0, max_len=100, message=None):
    """
    This function receive a min and max length
    and a message, if the message is between the
    max and min length, it returns it.
    :param min_len: Minimum length of the message
    :param max_len: Maximum length of the message
    :param message: Message for print in the screen
    :return: message
    """
    print(message) if message else None
    while True:
        text = input("> ")
        if len(text) >= min_len and len(text) <= max_len:
            return text

def valid_ssn(ssn, l):
    """
    This function receive a ssn and a list
    of clients, and validate the introduced
    ssn; first validate if the ssn have the
    correct structure (two nums and 1 letter)
    and then validate if the ssn is not in
    use in any client of the list that is
    passed. If the ssn pass the two 'tests'
    it'll return True, if not, it'll return
    False.
    :param ssn: social security number, introduced by the user
    :param l: list of Client objects
    :return: False or True
    """
    # validate if the ssn is correctly structured.
    if not re.match('[0-9]{2}[A-Z]$', ssn):  # 2 numbers and 1 char
        print(f"Invalid ssn '{ssn}', must have two numbers and one letter.")
        return False

    # validate if the ssn is free to use
    for client in l:
        if client.ssn == ssn:
            print(f"Invalid ssn '{ssn}', already in use.")
            return False
    return True
# ---- End Functions ----
