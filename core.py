import receiver
import time
import os



class Node(object):
    def __init__(self,system=None,mac_address=None):
        pass



    
    def loop_start(self):
        self._looping_flag = 1
        self.rec = receiver.RadioHoundSensorV3()

        while self._looping_flag == 1:  
            self.rec.readAdcIq_n()
            time.sleep(.5)


    def loop_stop(self):
        self._looping_flag = 0
                
