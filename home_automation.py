import time
from datetime import datetime
import piir

WAIT_TIME = 15
WAIT_TIME_LIGHT = 55

class HomeAutomation():
    def __init__(self, on_times=['6:29'], off_times=[]):
        self.on_times = on_times
        self.off_times = off_times
        self.__create_remote()

    def run(self):
        print('Start Home Automation...')
        while(1):
            try:
                time.sleep(WAIT_TIME)
                now = datetime.now()
                now_string = now.strftime("%H:%M")
                if now_string in self.on_times:
                    print('Turning Light ON!')
                    self.remote.send('on')
                    time.sleep(WAIT_TIME_LIGHT)
                elif now_string in self.off_times:
                    print('Turning Light OFF!')
                    self.remote.send('off')
                    time.sleep(WAIT_TIME_LIGHT)
                
            except KeyboardInterrupt:
                print('End of Program')
                break
    
    def __create_remote(self):
        self.remote = piir.Remote('light.json', 18)


if __name__ == "__main__":
    home_automation = HomeAutomation()
    home_automation.run()