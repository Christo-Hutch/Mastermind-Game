from colorama import Style
from math import trunc
import re
import os
import subprocess

def get_colors_tooltip(colors: dict) -> str:
    tooltip_list = []
    for key, value in colors.items():
        tooltip_list.append(f"{key} = {value} {Style.RESET_ALL}")

    refined_tooltip_list = [' '.join(tooltip_list[i:i+3]) for i in range(0, len(tooltip_list), 3)]

    return "\n".join(refined_tooltip_list)

def clean_user_input(user_input: str, valid_colors: list) -> list:
    tokens = re.findall(r'[a-zA-Z]+', user_input)

    cleaned_colors = [token.upper() for token in tokens if token.upper() in valid_colors]

    return cleaned_colors

def clear_terminal():
    if os.name == 'nt':
        subprocess.run('cls', shell=True)
    else:
        subprocess.run('clear', shell=True)