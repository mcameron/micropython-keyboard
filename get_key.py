# coding=utf-8


def shift_command():
    # return 225
    return 0


def command_command():
    # return 227
    return 0


def control_command():
    # return 224
    return 0


def alt_command():
    # return 226
    return 0


def escape_command():
    return 41


def function_command():
    return 0


def singlequote():
    return 52


def exclamation():
    return 30


def doublequote():
    return 52


def bang():
    return 32


def dollar():
    return 33


def percent():
    return 196


def ampersand():
    return 199


def left_bracket():
    return 47


def right_bracket():
    return 48


def plus():
    return 87


def comma():
    return 54


def minus():
    return 45


def underscore():
    return 45


def period():
    return 55


def forward_slash():
    return 56


def zero():
    return 39


def one():
    return 30


def two():
    return 31


def three():
    return 32


def four():
    return 33


def five():
    return 34


def six():
    return 35


def seven():
    return 36


def eight():
    return 37


def nine():
    return 38


def colon():
    return 203


def semicolon():
    return 51


def less_than():
    return 197


def equals_to():
    return 103


def more_than():
    return 198


def questionmark():
    return 56


def at_symbol():
    return 206


def open_square_bracket():
    return 47


def backward_slash():
    return 49


def close_square_bracket():
    return 48


def power_of():
    return 35


def backtick():
    return 53


def backspace():
    return 42


def letter_a():
    return 4


def letter_b():
    return 5


def letter_c():
    return 6


def letter_d():
    return 7


def delete_char():
    return 76


def down():
    return 81


def letter_e():
    return 8


def enter_char():
    return 40


def letter_f():
    return 9


def function_one():
    return 58


def function_ten():
    return 67


def function_eleven():
    return 68


def function_twelve():
    return 69


def function_two():
    return 59


def function_three():
    return 60


def function_four():
    return 61


def function_five():
    return 62


def function_six():
    return 63


def function_seven():
    return 64


def function_eight():
    return 65


def function_nine():
    return 66


def free_button():
    return 4


def letter_g():
    return 10


def letter_h():
    return 11


def letter_i():
    return 12


def letter_j():
    return 13


def letter_k():
    return 14


def letter_l():
    return 15


def left():
    return 80


def letter_m():
    return 16


def letter_n():
    return 17


def letter_o():
    return 18


def letter_p():
    return 19


def null_key():
    return 0


def letter_q():
    return 20


def letter_r():
    return 21


def right():
    return 79


def letter_s():
    return 22


def space_char():
    return 44


def letter_t():
    return 23


def tab_char():
    return 43


def letter_u():
    return 24


def up():
    return 82


def letter_v():
    return 25


def letter_w():
    return 26


def letter_x():
    return 27


def letter_y():
    return 28


def letter_z():
    return 29


def open_squigly_bracket():
    return 47


def bar():
    return 201


def close_squigly_bracket():
    return 48


def tilde():
    return 53


def pound():
    return 204


def euro():
    return 4


def home():
    return 74


def end():
    return 77


def pgup():
    return 75


def pgdown():
    return 78


def volup():
    return 128


def voldown():
    return 129


def mute():
    return 127


def power_button():
    return 161


def dim():
    return 102


def brighten():
    return 0


lookup = {
    '0': zero,
    '1': one,
    '2': two,
    '3': three,
    '4': four,
    '5': five,
    '6': six,
    '7': seven,
    '8': eight,
    '9': nine,
    'a': letter_a,
    'b': letter_b,
    'c': letter_c,
    'd': letter_d,
    'e': letter_e,
    'f': letter_f,
    'g': letter_g,
    'h': letter_h,
    'i': letter_i,
    'j': letter_j,
    'k': letter_k,
    'l': letter_l,
    'm': letter_m,
    'n': letter_n,
    'o': letter_o,
    'p': letter_p,
    'q': letter_q,
    'r': letter_r,
    's': letter_s,
    't': letter_t,
    'u': letter_u,
    'v': letter_v,
    'w': letter_w,
    'x': letter_x,
    'y': letter_y,
    'z': letter_z,
    'Alt': alt_command,
    'Backspace': backspace,
    'Command': command_command,
    'Ctrl': control_command,
    'Del': delete_char,
    'Down': down,
    'Enter': enter_char,
    'Esc': escape_command,
    'F1': function_one,
    'F10': function_ten,
    'F11': function_eleven,
    'F12': function_twelve,
    'F2': function_two,
    'F3': function_three,
    'F4': function_four,
    'F5': function_five,
    'F6': function_six,
    'F7': function_seven,
    'F8': function_eight,
    'F9': function_nine,
    'Fn': function_command,
    'Free1': free_button,
    'Left': left,
    'phantom': null_key,
    'Right': right,
    'Shift': shift_command,
    'Space': space_char,
    'Tab': tab_char,
    'Up': up,
    'Home': home,
    'End': end,
    'PgUp': pgup,
    'PgDown': pgdown,
    'VolUp': volup,
    'VolDown': voldown,
    'Mute': mute,
    'Power': power_button,
    'Dim': dim,
    'Brighten': brighten,
    '{': open_squigly_bracket,
    '|': bar,
    '}': close_squigly_bracket,
    '~': tilde,
    '£': pound,
    '€': euro,
    "'": singlequote,
    '!': exclamation,
    '"': doublequote,
    '#': bang,
    '$': dollar,
    '%': percent,
    '&': ampersand,
    '(': left_bracket,
    ')': right_bracket,
    '+': plus,
    ',': comma,
    '-': minus,
    '_': underscore,
    '.': period,
    '/': forward_slash,
    ':': colon,
    ';': semicolon,
    '<': less_than,
    'equals': equals_to,
    '>': more_than,
    '?': questionmark,
    '@': at_symbol,
    '[': open_square_bracket,
    'backslash': backward_slash,
    ']': close_square_bracket,
    '^': power_of,
    '`': backtick
}
