import math
import pyperclip
import time
import os


# Adding stuff instructions
''' 
to add function, 
- add to fun_list variable
- add variable getter if needed
    - add support in get()
- add calc that returns function

'''


menu_items = {
    1: 'RPM',
    2: 'Feedrate',
    3: 'RCT Feedrate',
    4: 'Feed',
    5: 'Drill Point',
    6: 'SFPM',
    7: 'MM to Inch',
    8: 'Inch to MM',
    9: 'Drill Feed',
    10: 'Serration Depth',
    11: 'Tap Drill Size',
    12: 'Fractional Feet',
    100: 'List Functions',
    101: 'Kill',
    102: 'Logos',
}


def main():
    run_once()
    forever()


# keep asking for input
def forever():
    while True:
        user_input = input(chr(955) + ' ')

        if user_input == '1':
            do(user_input, get_rpm())
        elif user_input == '2':
            do(user_input, feedrate())
        elif user_input == '3':
            do(user_input, rct_feedrate())
        elif user_input == '4':
            do(user_input, feed())
        elif user_input == '5':
            do(user_input, drill_point())
        elif user_input == '6':
            do(user_input, sfpm_find())
        elif user_input == '7':
            do_convert(user_input, mm_in())
        elif user_input == '8':
            do_convert(user_input, in_mm())
        elif user_input == '9':
            do(user_input, drill_feed())
        elif user_input == '10':
            do(user_input, serration_depth())
        elif user_input == '11':
            do(user_input, tap_drill())
        elif user_input == '12':
            do(user_input, fraction_feet())
        elif user_input == '100':
            show_list()
        elif user_input == '101':
            kill()
        elif user_input == '102':
            run_once()


# simple get input sect.
''' 
example: dia() calls -> get('dia') calls -> 
get_input(type, name) type is float or int, name is for user
'''


# diameter getter
def dia():
    return get('dia')


# surface foot getter
def sfpm():
    return get('sfpm')


# ipt getter
def ipt():
    return get('ipt')


# flutes getter
def flutes():
    return get('flutes')


# angle getter
def angle():
    return get('angle')


# step over getter
def step_o():
    return get('step_o')


# RPM getter
def rpm():
    return get('rpm')


# Millimeter getter
def mm():
    return get('mm')


# Inch getter
def inch():
    return get('inch')


# Radius getter
def radius():
    return get('radius')


# Pitch getter
def pitch():
    return get('pitch')


# get based on variable name -> get input()
def get(name):
    x = None
    if name == 'dia':
        x = get_input('float', 'Diameter')
    elif name == 'sfpm':
        x = get_input('float', 'SFPM')
    elif name == 'ipt':
        x = get_input('float', 'Inches per flute')
    elif name == 'flutes':
        x = get_input('int', 'Number of flutes')
    # return radians
    elif name == 'angle':
        x = get_input('float', 'Angle')
        x = x * math.pi / 180
    elif name == 'step_o':
        x = get_input('float', 'Step over')
    elif name == 'rpm':
        x = get_input('int', 'RPM')
    elif name == 'mm':
        x = get_input('float', 'Millimeters')
    elif name == 'inch':
        x = get_input('float', 'Inches')
    elif name == 'radius':
        x = get_input('float', 'Radius')
    elif name == 'pitch':
        x = get_input('float', 'Pitch')
    else:
        return x
    return x


# get float or int from user
def get_input(typ, name):
    while True:
        x = None
        try:
            if typ == 'float':
                x = float(input(name + ": "))
            else:
                x = int(input(name + ": "))
        except ValueError:
            print("Input Invalid")
            continue
        else:
            break
    return x


# start calc section


# RPM finder
def get_rpm():
    diam = dia()
    return int((sfpm() * 12) / (diam * math.pi))


# surface feet finder
def sfpm_find():
    rev = rpm()
    diameter = dia()
    return int((rev * (diameter * math.pi)) / 12)


# feed rate finder
def feedrate():
    return round(get_rpm() * (ipt() * flutes()), 2)


# RCT feed rate finder
def rct_feedrate():
    d = dia()
    rp = rpm()
    f = ipt()
    flts = flutes()
    step = step_o()
    rct_ipt = (f * d) / (2 * math.sqrt((d * step) - (step * step)))
    return round(int(rp) * (rct_ipt * flts), 1)


# feed finder
def feed():
    return round(ipt() * flutes(), 5)


# drill point length
def drill_point():
    return round((.5 * dia()) / math.tan(.5 * angle()), 4)


# mm to inch
def mm_in():
    mm_ = mm()
    in_ = round(mm_ / 25.4, 4)
    return in_, mm_


# mm to inch
def in_mm():
    in_ = inch()
    mm_ = round(in_ * 25.4, 4)
    return mm_, in_


# drill feed
def drill_feed():
    d = dia()
    return round(d * .013, 4)


# serration depth
def serration_depth():
    while True:
        try:
            tool_radius = radius()
            p = pitch()
            x = round(tool_radius - math.sqrt(tool_radius**2 - (p / 2)**2), 4)
        except ValueError:
            print('That will never work - Please try again')
            continue
        else:
            break
    return x


# Tap drill size
def tap_drill():
    d = dia()
    p = 1 / pitch()
    return round(d - p, 4)


def do(user_input, value):  # value here is the function
    pyperclip.copy(value)  # this drives the functions
    print('')
    print(menu_items[int(user_input)] + ": " + str(value))  # shows the result
    print('')


def do_convert(user_input, value_out):
    pyperclip.copy(value_out[0])  # this drives the functions
    print('')
    print(str(value_out[1]), menu_items[int(user_input)] + ": " + str((value_out[0])))  # shows the result
    print('')


# list of calc functions
def show_list():
    for each in menu_items:
        print(each, menu_items[each])
    print('')


#  start
def run_once():
    os.system('cls')
    print(logo)
    print(sign_2)
    show_list()


#  end
def kill():
    print(bye_bye)
    time.sleep(2)
    quit(0)


#  logos
logo = """
               ▄████▄      ███▄    █     ▄████▄
              ▒██▀ ▀█      ██ ▀█   █    ▒██▀ ▀█
              ▒▓█    ▄    ▓██  ▀█ ██▒   ▒▓█    ▄
              ▒▓▓▄ ▄██▒   ▓██▒  ▐▌██▒   ▒▓▓▄ ▄██▒
              ▒ ▓███▀ ░   ▒██░   ▓██░   ▒ ▓███▀ ░
              ░ ░▒ ▒  ░   ░ ▒░   ▒ ▒    ░ ░▒ ▒  ░
                ░  ▒      ░ ░░   ░ ▒░     ░  ▒
              ░              ░   ░ ░    ░
              ░ ░                  ░    ░ ░
              ░                         ░
 """
logo_2 = """
  ██████╗    ███╗   ██╗     ██████╗
 ██╔════╝    ████╗  ██║    ██╔════╝
 ██║         ██╔██╗ ██║    ██║     
 ██║         ██║╚██╗██║    ██║     
 ╚██████╗    ██║ ╚████║    ╚██████╗
  ╚═════╝    ╚═╝  ╚═══╝     ╚═════╝ 
 """
sign = """
 ______  __   __      _____  _____  __   _  ______  _____  ______ 
 |_____]   \\_/          |   |     | | \\  | |_____/ |     | |_____]
 |_____]    |         __|   |_____| |  \\_| |    \\_ |_____| |_____]

"""
sign_2 = """
            ___  _ _      _ ____ __ _ ____ ____ ___ 
            |==]  Y    ___| [__] | \\| |--< [__] |==]
"""
bye_bye = """
                 ██▀███        ██▓      ██▓███  
                ▓██ ▒ ██▒     ▓██▒     ▓██░  ██▒
                ▓██ ░▄█ ▒     ▒██▒     ▓██░ ██▓▒
                ▒██▀▀█▄       ░██░     ▒██▄█▓▒ ▒
                ░██▓ ▒██▒ ██▓ ░██░ ██▓ ▒██▒ ░  ░
                ░ ▒▓ ░▒▓░ ▒▓▒ ░▓   ▒▓▒ ▒▓▒░ ░  ░
                  ░▒ ░ ▒░ ░▒   ▒ ░ ░▒  ░▒ ░     
                  ░░   ░  ░    ▒ ░ ░   ░░       
                   ░       ░   ░    ░           
                           ░        ░           
"""
#


if __name__ == '__main__':

    main()
