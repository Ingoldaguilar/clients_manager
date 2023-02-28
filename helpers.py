# ---- Helpers Documentation ----
"""
Module for auxiliary functions.
"""
# ---- Helpers Documentation ----

# ---- Imports ----
import os
import platform
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
# ---- End Functions ----
