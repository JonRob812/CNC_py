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
                print(f'{var.user_text:>25} = {var.val:.4f}')


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
            user_function_name = menu[user_input][0]
            user_function = menu[user_input][1]
            result = user_function()
            if result is None:
                result_string = f'{user_function_name}: completed'
            else:
                result_string = f'{user_function_name}: {result:.4f}'
                pyperclip.copy(round(result, 4))
            show_values()
            print()
            print(result_string)
        except (ValueError, KeyError) as e:
            print(e)
            print('try again')


def kill():
    print(Logos.bye_bye)
    time.sleep(1)
    quit(0)


menu = {
    1: ('RPM', Calc.rpm),
    2: ('Feed rate', Calc.feed_rate),
    3: ('RCT IPT', Calc.rct_ipt),
    4: ('Feed', Calc.feed),
    5: ('Drill Point', Calc.drill_point),
    6: ('SFPM', Calc.sfpm),
    7: ('MRR - Material Removal Rate', Calc.mrr),
    8: ('MM to Inch', Calc.mm),
    9: ('Inch to MM', Calc.inch),
    10: ('Drill Feed', Calc.drill_feed),
    11: ('Serration Depth', Calc.serration_depth),
    12: ('Tap Drill Size', Calc.tap_drill),
    99: ('Reset Variables', UserVar.reset),
    100: ('List Functions', show_menu),
    101: ('Kill', kill),
}

if __name__ == "__main__":
    main()
