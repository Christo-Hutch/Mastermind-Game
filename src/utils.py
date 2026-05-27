from colorama import Style
from math import trunc

def get_colors_tooltip(colors: dict) -> str:
    tooltip_list = []
    for key, value in colors.items():
        tooltip_list.append(f"{key} = {value} {Style.RESET_ALL}")

    refined_tooltip_list = [' '.join(tooltip_list[i:i+3]) for i in range(0, len(tooltip_list), 3)]

    return "\n".join(refined_tooltip_list)