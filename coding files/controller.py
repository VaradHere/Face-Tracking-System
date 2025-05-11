import pyfirmata

comport = 'COM11'

bord = pyfirmata.Arduino(comport)

led_1=bord.get_pin('d:13:o')
#led_2=bord.get_pin('d:3:o')

def abc(pos):
    if pos == 0:
        led_1.write(0)
        #led_2.write(0)


    elif pos == 1:
        led_1.write(1)
        #led_2.write(0)

    #elif pos == 2:
        #led_1.write(0)
        #ed_2.write(1)

