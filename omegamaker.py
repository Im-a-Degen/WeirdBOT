try:
    from Tkinter import Tk
except ImportError:
    from tkinter import Tk


def omegalul_converter(input_string):
    letters = "abcdefghijklmnopqrstuvwxyz"
    regional_indicator_hash = {letter: f":regional_indicator_{letter}: " for letter in letters}
    regional_indicator_hash["o"] = "<:botOMEGALUL1:938653392153239633> "
    regional_indicator_hash["b"] = "<:b:938501626354884648> "
    regional_indicator_hash[" "] = "     "
    regional_indicator_hash["\n"] = "\n"
    regional_indicator_hash["0"] = "<:zero:938616895685406820> "
    regional_indicator_hash["1"] = "<:one:938616895685406820> "
    regional_indicator_hash["2"] = "<:two:938616895685406820> "
    regional_indicator_hash["3"] = "<:three:938616895685406820> "
    regional_indicator_hash["4"] = "<:four:938616895685406820> "
    regional_indicator_hash["5"] = "<:five:938616895685406820> "
    regional_indicator_hash["6"] = "<:six:938616895685406820> "
    regional_indicator_hash["7"] = "<:seven:938616895685406820> "
    regional_indicator_hash["8"] = "<:eight:938616895685406820> "
    regional_indicator_hash["9"] = "<:nine:938616895685406820> "

    output_string_prepro = []
    for letter in input_string:
        try:
            output_string_prepro.append(regional_indicator_hash[letter.lower()])
        except:
            output_string_prepro.append(letter)
    output_string = "".join(output_string_prepro)

    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(output_string)
    r.update()
    r.destroy()

    return output_string
