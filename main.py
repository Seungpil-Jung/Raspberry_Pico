import machine, time, ssd1306

#pin25 = machine.Pin(25, machine.Pin.OUT)
# LED on board is connected to pin25

i2c = machine.I2C(1, sda=machine.Pin(26), scl=machine.Pin(27))
display = ssd1306.SSD1306_I2C(128, 64, i2c)

start = 1
stop = 8
for index in range(start, stop+1):
    img_fname = r'/ys_cartoon/ys_cartoon_0%d.txt' % index
    with open(img_fname,'r') as fp:
        img01 = fp.read()

    img01 = img01.split('\r\n')
    img01 = img01[:-1]
    img01 = [[int(x) for x in txt.split(' ')] for txt in img01]

    display.fill(0)
    for row in range(64):
        for col in range(128):
            pixel_value = img01[row][col]
            if pixel_value:
                display.pixel(col, row, pixel_value)
    display.show()
    del(img01)
    time.sleep(1)
