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
            print('function1')
        if fn2_pressed:
            buf[2] = get_key.lookup[matrix.fn2_layer[pressed_x][pressed_y]]()
            print('function2')
        if not fn1_pressed and not fn2_pressed:
            buf[2] = get_key.lookup[matrix.matrix[pressed_x][pressed_y]]()
    if buf[2] != last_buf[2] or buf[0] != last_buf[0]:
        print(buf[2])
        pyb.delay(70)
        last_buf[0] = buf[0]
        last_buf[2] = buf[2]
