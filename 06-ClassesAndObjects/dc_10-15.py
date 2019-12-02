class TV:
    def __init__(self, is_on=False, channel_on = 1, channels=None, vol=0) :
        self.is_on = is_on
        self.channel_on = channel_on
        self.channels = []
        self.vol = 0
    def show_status(self):
        if self.is_on == True:
            try:
                return f"TV is on, channel {self.channel_on}({self.channels[self.channel_on-1]}) volume:{self.vol}"
            except IndexError:
                return f"TV is on, please set channel list"
        else:
            return "Off" 
    
    def on(self):
        self.is_on = True
    
    def off(self):
        self.is_on = False

    def set_channel(self,new_channel_no):
        self.channel_on = new_channel_no

    def set_channels(self,channels_list):
        self.channels = channels_list

    def inc_vol(self):
        if self.vol == 10:
            print('Max vol')
        else:
            self.vol +=1 
    
    def dec_vol(self):
        if self.vol == 0:
            print("Min vol")
        else:
            self.vol -=1


samsung = TV()
print(samsung.show_status())
samsung.on()
print(samsung.show_status())
samsung.set_channels(["TVP1","TVP2", "Polsat", "TVN", "Filmbox", "Polsat2", "HBO", "Canal+"])
samsung.set_channel(4)
samsung.dec_vol()
print(samsung.show_status())
samsung.set_channel(7)
samsung.inc_vol()
print(samsung.show_status())
samsung.off()
print(samsung.show_status())
