from pywifi import PyWiFi, Profile

class Wifi:
    wifi = PyWiFi()

    def connect(self):
        profile = Profile()
        profile.ssid = 'BNUZ-Student'
        self.wifi.interfaces()[0].connect(profile)

    def disconnect(self):
        self.wifi.interfaces()[0].disconnect()
