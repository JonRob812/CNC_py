import math
import re

class UserVar:
    all_vars = []
    invalid_input_string = 'invalid input - Value Error - Please try again'

    @classmethod
    def reset(cls):
        for variable in cls.all_vars:
            variable.val = None

    def __init__(self, var_type, user_text):
        self.var_type = var_type
        self.val = None
        self.user_text = user_text
        self.all_vars.append(self)

    def value(self, one_shot=False):
        x = self.val
        if one_shot:
            x = None
        while x is None:
            try:
                incoming = input(self.user_text + ': ')
                x = self.var_type(incoming)
            except ValueError:
                print(UserVar.invalid_input_string)
                pass
        if not one_shot:
            self.val = x
        return x

    def set(self, value):
        self.val = self.var_type(value)


'''variables'''

diameter = UserVar(float, 'diameter')
drill_diameter = UserVar(float, 'drill diameter')
surface_feet_min = UserVar(float, 'surface feet per minute')
revolutions_min = UserVar(float, 'revolutions per minute')
inches_flute = UserVar(float, 'feed per flute')
flutes = UserVar(int, 'number of flutes')
step_over = UserVar(float, 'step over')
angle = UserVar(float, 'angle')
pitch = UserVar(float, 'pitch')
feed = UserVar(float, 'feed')
feed_rate = UserVar(float, 'feed rate')
inches = UserVar(float, 'Inches')
millimeters = UserVar(float, 'Millimeters')
radius = UserVar(float, 'radius')
step_down = UserVar(float, 'step down')
total_length = UserVar(float, 'overall length \n(part to riser distance)')
short_length = UserVar(float, 'distance from bolt to riser')
force = UserVar(float, 'force applied from bolt')
user_string = UserVar(str, "ex: 115\'16-7/8\" \nstring")


class Calculator:
    @staticmethod
    def rpm():
        sfpm = surface_feet_min.value()
        dia = diameter.value()
        revolutions_min.set((sfpm * 12) / (dia * math.pi))
        return revolutions_min.val

    @staticmethod
    def sfpm():
        revs = revolutions_min.value()
        dia = diameter.value()
        surface_feet_min.set((revs * (dia * math.pi)) / 12)
        return surface_feet_min.val

    @staticmethod
    def feed_rate():
        rpm = revolutions_min.value()
        ipt = inches_flute.value()
        num_flutes = flutes.value()
        feed_ = ipt * num_flutes
        feed.set(feed_)
        feed_rate.set(rpm * feed_)
        return feed_rate.val

    @staticmethod
    def rct_ipt():
        ipt = inches_flute.value()
        dia = diameter.value()
        step_o = step_over.value()
        v1 = (ipt * dia) / (2 * math.sqrt((dia * step_o) - (step_o * step_o)))
        v2 = (((dia / step_o)/2)/math.sqrt((dia/step_o)-1)) * ipt  # sandvik formula
        inches_flute.set(v2)
        return inches_flute.val

    @staticmethod
    def feed():
        ipt = inches_flute.value()
        num_flutes = flutes.value()
        feed.set(ipt * num_flutes)
        return feed.val

    @staticmethod
    def mrr():
        step_o = step_over.value()
        step_d = step_down.value()
        f = feed_rate.value()
        return step_o * step_d * f

    @staticmethod
    def drill_point():
        dia = diameter.value()
        a = angle.value()
        return (.5 * dia) / math.tan(.5 * math.radians(a))

    @staticmethod
    def mm():
        mm_ = millimeters.value(one_shot=True)
        return mm_ / 25.4

    @staticmethod
    def inch():
        inch_ = inches.value(one_shot=True)
        return inch_ * 25.4

    @staticmethod
    def drill_feed():
        dia = diameter.value()
        return dia * .013

    @staticmethod
    def serration_depth():
        rad = radius.value(one_shot=True)
        p = pitch.value(one_shot=True)
        try:
            return rad - math.sqrt(rad ** 2 - (p / 2) ** 2)
        except ValueError:
            return 'invalid inputs'

    @staticmethod
    def tap_drill():
        dia = diameter.value()
        p = pitch.value(one_shot=True)
        if p > 5:
            p = 1 / p
        drill_dia = dia - p
        diameter.set(drill_dia)
        return drill_dia

    @staticmethod
    def clamping_force():
        d1 = total_length.value(one_shot=True)
        d2 = short_length.value(one_shot=True)
        f = force.value(one_shot=True)
        return (f * d2) / d1

    @staticmethod
    def string_to_float():
        pattern = re.compile(r"(?P<feet>\d*')?(?P<inches>\d*?-?\d*?/?\d*?\")")
        string = user_string.value(one_shot=True)

        def decimal_feet(string_from_pattern):
            if not string_from_pattern:
                return 0
            return float(float(string_from_pattern.replace("'", "")) * 12)

        def decimal_inches(string_from_pattern):
            if not string_from_pattern:
                return 0
            inches_ = string_from_pattern.replace("\"", "")
            decimal = 0
            if "-" in string_from_pattern:
                inches_, fraction = string_from_pattern.split("-")
                fraction = fraction.replace("\"", "")
                num, den = fraction.split("/")
                decimal = int(num) / int(den)
            return int(inches_) + decimal

        match = re.search(pattern, string)
        return decimal_feet(match.group('feet')) + decimal_inches(match.group('inches'))


class Logos:
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



