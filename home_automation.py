import time
from datetime import datetime
import piir


class HomeAutomation():
    def __init__(self, on_times=['6:30'], off_times=None):
        self.on_times = on_times
        self.__create_remote()

    def run(self):
        while(1):
            try:
                time.sleep(5)
                now = datetime.now()
                now_string = now.strftime("%H:%M")
                if now_string in self.on_times:
                    remote.send('on')
                    time.sleep(60)
            except KeyboardInterrupt:
                print('End of Program')
                break
    
    def __create_remote(self):
        self.remote = piir.Remote('light.json', 17)


if __name__ == "__main__":
    home_automation = HomeAutomation()
    home_automation.run()