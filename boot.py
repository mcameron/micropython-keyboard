# boot.py -- run on boot-up
# can run arbitrary Python, but best to keep it minimal

import pyb

col1 = pyb.Pin('X9', pyb.Pin.IN, pyb.Pin.PULL_UP)
row1 = pyb.Pin('X19', pyb.Pin.OUT_PP)
row1.low()
pyb.delay(2000)

if not col1.value():
    pyb.usb_mode('CDC+MSC')
    pyb.main('unloop.py')           # if Escape pressed on boot, enable programming mode
else:
    pyb.main('main.py')
    pyb.usb_mode('CDC+HID', hid=pyb.hid_keyboard)

# main script to run after this one
# pyb.usb_mode('CDC+MSC') # act as a serial and a storage device
# pyb.usb_mode('CDC+HID') # act as a serial device and a mouse

