# coding=utf-8
# python
import get_key
import matrix

# Current delay is
# - 140 milliseconds for HID processing.
# -
# DEBOUNCE_MAX = 20

column1 = pyb.Pin('X9', pyb.Pin.IN, pyb.Pin.PULL_UP)
column2 = pyb.Pin('X10', pyb.Pin.IN, pyb.Pin.PULL_UP)
column3 = pyb.Pin('X11', pyb.Pin.IN, pyb.Pin.PULL_UP)
column4 = pyb.Pin('X12', pyb.Pin.IN, pyb.Pin.PULL_UP)
column7 = pyb.Pin('X8', pyb.Pin.IN, pyb.Pin.PULL_UP)
column6 = pyb.Pin('X7', pyb.Pin.IN, pyb.Pin.PULL_UP)
column5 = pyb.Pin('X6', pyb.Pin.IN, pyb.Pin.PULL_UP)
column8 = pyb.Pin('X5', pyb.Pin.IN, pyb.Pin.PULL_UP)
column9 = pyb.Pin('X4', pyb.Pin.IN, pyb.Pin.PULL_UP)
column10 = pyb.Pin('X3', pyb.Pin.IN, pyb.Pin.PULL_UP)
column11 = pyb.Pin('X2', pyb.Pin.IN, pyb.Pin.PULL_UP)
column12 = pyb.Pin('X1', pyb.Pin.IN, pyb.Pin.PULL_UP)

columns = [column1, column2, column3, column4, column5, column6, column7, column8, column9, column10, column11,
           column12]

row1 = pyb.Pin('X19', pyb.Pin.OUT_PP)
row1.low()
row2 = pyb.Pin('X20', pyb.Pin.OUT_PP)
row2.low()
row3 = pyb.Pin('X21', pyb.Pin.OUT_PP)
row3.low()
row4 = pyb.Pin('X22', pyb.Pin.OUT_PP)
row4.low()

rows = [row1, row2, row3, row4]

# HID Handling
hid = pyb.USB_HID()
buf = bytearray(8)
last_buf = bytearray(8)
last_buf[2] = 0
last_buf[0] = 0
something_pressed = False
shift_pressed = False
ctrl_pressed = False
alt_pressed = False
command_pressed = False
fn1_pressed = False
fn2_pressed = False
ROW_RANGE = range(4)
COLUMN_RANGE = range(12)

control_keys = ['Shift', 'Command', 'Alt', 'Ctrl', 'Fn1', 'Fn2']


while True:
    something_pressed = False
    ctrl_pressed = False
    shift_pressed = False
    alt_pressed = False
    command_pressed = False
    fn1_pressed = False
    fn2_pressed = False
    for y in ROW_RANGE:
        row = rows[y]
        row.low()
        for x in COLUMN_RANGE:
            column = columns[x]
            key_string = matrix.matrix[x][y]
            if not column.value():
                if key_string not in control_keys:
                    something_pressed = True
                    pressed_x = x
                    pressed_y = y
                else:
                    if key_string is 'Ctrl':
                        ctrl_pressed = True
                    if key_string is 'Shift':
                        shift_pressed = True
                    if key_string is 'Alt':
                        alt_pressed = True
                    if key_string is 'Command':
                        command_pressed = True
                    if key_string is 'Fn1':
                        fn1_pressed = True
                    if key_string is 'Fn2':
                        fn2_pressed = True
        row.high()
    # All keys evaluated
    control_modifier = 0
    if ctrl_pressed:
        control_modifier += 1
    if shift_pressed:
        control_modifier += 2
    if alt_pressed:
        control_modifier += 4
    if command_pressed:
        control_modifier += 8
    buf[0] = control_modifier
    if not something_pressed:
        buf[2] = 0
    else:
        if fn1_pressed:
            buf[2] = get_key.lookup[matrix.fn1_layer[pressed_x][pressed_y]]()
        if fn2_pressed:
            buf[2] = get_key.lookup[matrix.fn2_layer[pressed_x][pressed_y]]()
        if not fn1_pressed and not fn2_pressed:
            buf[2] = get_key.lookup[matrix.matrix[pressed_x][pressed_y]]()
    if buf[2] != last_buf[2] or buf[0] != last_buf[0]:
        hid.send(buf)
        pyb.delay(70)
        last_buf[0] = buf[0]
        last_buf[2] = buf[2]
