import gpiod

pinSbarra = 17
pinScorrevole = 27
pinPortone = 22

chip = gpiod.Chip('gpiochip0')

sbarra = chip.get_lines([17])
sbarra.request(consumer='foobar', type=gpiod.LINE_REQ_DIR_OUT, default_vals=[ 1 ])
scorrevole = chip.get_lines([27])
scorrevole.request(consumer='foobar', type=gpiod.LINE_REQ_DIR_OUT, default_vals=[ 1 ])
portone = chip.get_lines([22])
portone.request(consumer='foobar', type=gpiod.LINE_REQ_DIR_OUT, default_vals=[ 1 ])
i = 4
while i>0:
    sbarra.set_values([not sbarra.get_values()])
    scorrevole.set_values([not scorrevole.get_values()])
    portone.set_values([not portone.get_values()])
    --i

