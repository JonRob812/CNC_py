import pyperclip
import time
import os
from cnc_resources import Logos, Calculator as Calc, UserVar


def show_menu():
    for item in menu:
        print(f'{item:>3}  |  {menu[item][0]}')


def show_values():
    if any(x.val is not None for x in UserVar.all_vars):
        print()
        print('- current set variables - Reset: 99 -')
        print()
        for var in UserVar.all_vars:
            if var.val is not None:
                print(f'{var.user_text:>25} = {var.val}')


def main():
    run_once()
    run_forever()


def run_once():
    os.system('cls')
    print(Logos.logo)
    print(Logos.sign_2)
    show_menu()


def run_forever():
    while True:
        try:
            user_input = int(input(chr(955) + ' '))
            if not any(x == user_input for x in menu):
                print('not a valid choice - try again')
                continue
            result = menu[user_input][1]()
            if result is None:
                result = 'complete'
            show_values()
            print()
            print(f'{menu[user_input][0]}: {result}')
            pyperclip.copy(result)
        except (ValueError, KeyError) as e:
            print(e)
            print('try again')


def kill():
    print(Logos.bye_bye)
    time.sleep(1)
    quit(0)


menu = {
    1: ('RPM', Calc.rpm),
    2: ('Feedrate', Calc.feedrate),
    3: ('RCT IPT', Calc.rct_ipt),
    4: ('Feed', Calc.feed),
    5: ('Drill Point', Calc.drill_point),
    6: ('SFPM', Calc.sfpm),
    7: ('MM to Inch', Calc.mm),
    8: ('Inch to MM', Calc.inch),
    9: ('Drill Feed', Calc.drill_feed),
    10: ('Serration Depth', Calc.serration_depth),
    11: ('Tap Drill Size', Calc.tap_drill),
    99: ('Reset Variables', UserVar.reset),
    100: ('List Functions', show_menu),
    101: ('Kill', kill),
}

if __name__ == "__main__":
    main()
