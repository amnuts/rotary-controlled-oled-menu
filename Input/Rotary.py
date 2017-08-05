from RPi import GPIO


class Rotary:

    def __init__(self, clk, dt, btn, menu=None):
        self.clk = clk
        self.dt = dt
        self.btn = btn
        self.menu = None
        self.rotaryLastState = None
        self.btnLastState = None
        self.clkLevel = 0
        self.dtLevel = 0
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.clk, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.dt, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        if menu is not None:
            self.set_menu(menu)

    def set_menu(self, menu):
        self.menu = menu
        GPIO.add_event_detect(self.clk, GPIO.BOTH, callback=self.__pulse)
        GPIO.add_event_detect(self.dt, GPIO.BOTH, callback=self.__pulse)
        GPIO.add_event_detect(self.btn, GPIO.RISING, callback=self.__button, bouncetime=200)
        self.rotaryLastState = None
        self.btnLastState = GPIO.input(self.btn)
        self.clkLevel = 0
        self.dtLevel = 0

    def __pulse(self, channel):
        clk_state = GPIO.input(self.clk)
        dt_state = GPIO.input(self.dt)
        if clk_state != self.rotaryLastState:
            self.rotaryLastState = clk_state
            if dt_state != clk_state:
                self.menu.change_highlight(1)
            else:
                self.menu.change_highlight(-1)
            self.menu.render()

    def __button(self, channel):
        print('Button on pin {} pushed'.format(channel))
