import re

nc_file = open(r'F:\CNC DATA\Posted Code\620-040487 op1.NC', 'r')

big_code = nc_file.readlines()

g_code_parse_pattern = re.compile(r"(?P<code>[A-z])(?P<val>-?\d*\.?\d+\.?)")
pattern = re.compile(r"[A-z](?P<val>-?\d*\.?\d+\.?)")


def parse(line):
    first_char = line[0]
    skip_chars = ['(', 'O', '%']
    if first_char in skip_chars:
        return line.replace('\n', '')

    pattern = g_code_parse_pattern
    matches = pattern.finditer(line)
    codes = [x.group('code') for x in matches]
    return codes


for ln in big_code:
    print(parse(ln))

