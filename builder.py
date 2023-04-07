from PIL import Image
from os import listdir, get_terminal_size


outname = input("Output Filename: ")
frame_delay = int(input("Frame delay (n*10ms): "))


basic_program = """
냥냥냥냥냥~"0"? "1"냥냥냥냥냥 냥? "2"냥냥냥냥냥 냥냥냥냥? "3"냥냥냥냥냥 냥냥냥냥? "4"냥냥냥냥냥 냥냥냥냥? "5"냥냥냥냥냥 냥냥냥냥냥 냥냥냥냥냥 냥냥냥냥냥 냥냥냥냥냥? "6"냥냥냥냥냥 냥냥냥냥냥 냥냥? "7"냥냥냥냥냥 냥냥냥냥냥 냥냥? "8"냥냥냥냥냥 냥냥냥냥냥 냥냥?
"9" 냥냥냥냥냥 냥냥? "10" 냥냥냥냥냥 냥냥냥? "11" 냥냥냥냥냥 냥냥? "12" 냥냥냥냥냥 냥냥? "13" 냥냥냥냥냥 냥냥냥냥냥 냥냥냥? "14" 냥냥!"13"!"12"!"11"!"10"!"9"!"8"!"7"!"6"!"5"!"4"!"3"!"2"!"1"!"0"냐-
? "1" 냥냥? "2" 냥? "3" 냐? "4"? "5" 냥? "6" 냐냐? "7" 냐? "8" 냥? "9" 냐냐? "10" 냥냥? "11"? "12" 냥? "13"냐
"""

mouse_program = """0->0: clear.nyan
1->0: time.sleep
"""

#   32 (루프 6 - 30) 1
# . 46 (루프 9 - 45) 2
# , 44 (루프 9 - 45) 3
# - 45 (루프 9 - 45) 4
# ~ 126 (루프 25 - 125) 5
# : 58 (루프 12 - 60) 6
# ; 59 (루프 12 - 60) 7
# = 61 (루프 12 - 60) 8
# ! 33 (루프 7 - 35) 9
# * 42 (루프 8 - 40) 10
# # 35 (루프 7 - 35) 11
# $ 36 (루프 7 - 35) 12
# @ 64 (루프 13 - 65) 13
# \n 10 (루프 2 - 10) 14

with open(outname+".nyan", "w", encoding="utf-8") as f:
    f.write(basic_program)
    
with open(outname+".mouse", "w", encoding="utf-8") as f:
    f.write(mouse_program)


def cursor_print(cursor: int, char: str, txt: str):
    addr = {" ": 1, ".": 2, ",": 3, "-": 4, "~": 5, ":": 6, ";": 7, "=": 8, "!": 9, "*": 10, "#": 11, "$": 12, "@": 13, "\n": 14}
    ncursor = cursor
    ntxt = txt
    while ncursor != addr[char]:
        if ncursor < addr[char]:
            ntxt += "?"
            ncursor += 1
        else:
            ntxt += "!"
            ncursor -= 1
    ntxt += "."
    return ncursor, ntxt


def order(files: list):
    return sorted(files, key=lambda x: int(x.split(".")[0]))


def build():
    print("Building an video...")
    cursor = 13
    tw, th = get_terminal_size().columns // 1.2, get_terminal_size().lines // 1.2
    l = order(listdir('source'))
    ll = len(l)
    
    for index, filename in enumerate(list(l)):
        frame_commands = ""
        im = Image.open("source/"+filename, "r")
        im.load()
        for h in range(0, im.height, im.height // int(th)):
            for w in range(0, im.width, im.width // int(tw)):
                r, g, b = im.getpixel((w, h))
                ave = (r+g+b)/3
                if ave == 0:
                    cursor, frame_commands = cursor_print(cursor, " ", frame_commands)
                elif ave < 22:
                    cursor, frame_commands = cursor_print(cursor, ".", frame_commands)
                elif ave < 44:
                    cursor, frame_commands = cursor_print(cursor, ",", frame_commands)
                elif ave < 66:
                    cursor, frame_commands = cursor_print(cursor, "-", frame_commands)
                elif ave < 88:
                    cursor, frame_commands = cursor_print(cursor, "~", frame_commands)
                elif ave < 110:
                    cursor, frame_commands = cursor_print(cursor, ":", frame_commands)
                elif ave < 132:
                    cursor, frame_commands = cursor_print(cursor, ";", frame_commands)
                elif ave < 154:
                    cursor, frame_commands = cursor_print(cursor, "=", frame_commands)
                elif ave < 176:
                    cursor, frame_commands = cursor_print(cursor, "!", frame_commands)
                elif ave < 198:
                    cursor, frame_commands = cursor_print(cursor, "*", frame_commands)
                elif ave < 220:
                    cursor, frame_commands = cursor_print(cursor, "#", frame_commands)
                elif ave < 242:
                    cursor, frame_commands = cursor_print(cursor, "$", frame_commands)
                else:
                    cursor, frame_commands = cursor_print(cursor, "@", frame_commands)
            cursor, frame_commands = cursor_print(cursor, "\n", frame_commands)
        frame_commands += ";먕" + ";"*frame_delay + "먀"
        with open(outname+".nyan", "a", encoding="utf-8") as f:
            f.write(frame_commands)
        print(f"Progress: {index}/{ll} \033[92m{index/ll*100}%\033[0m", end="\r")

build()
