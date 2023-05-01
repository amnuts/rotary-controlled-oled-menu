from RPi import GPIO


class Rotary:
    def __init__(self, clk, dt, btn=None, menu=None):
        self.clk = clk
        self.dt = dt
        self.btn = btn
        self.menu = None
        self.rotary_last_state = None
        self.btn_last_state = None
        self.clk_level = 0
        self.dt_level = 0
        self.rotary_thread = None
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        if self.btn is not None:
            GPIO.setup(self.btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            GPIO.add_event_detect(self.btn, GPIO.FALLING, callback=self.__button, bouncetime=200)
            self.btn_last_state = GPIO.input(self.btn)
        if menu is not None:
            self.menu = menu
            self.rotary_last_state = None
            self.clk_level = 0
            self.dt_level = 0
            GPIO.add_event_detect(self.clk, GPIO.BOTH, callback=self.__pulse)
            GPIO.add_event_detect(self.dt, GPIO.BOTH, callback=self.__pulse)

    def __pulse(self, channel):
        clk_state = GPIO.input(self.clk)
        dt_state = GPIO.input(self.dt)
        if clk_state != self.rotary_last_state:
            self.rotary_last_state = clk_state
            if dt_state != clk_state:
                self.menu.change_highlight(1)
            else:
                self.menu.change_highlight(-1)
            self.menu.render()

    def __button(self, channel):
        self.menu.perform_current_action()
