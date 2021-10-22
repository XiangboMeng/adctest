import os




class RadioHoundSensorV3(object):    
    def __init__(self, timeout=0.2):


        # default values
        self._N_samples = 1024

        self.count = 1
        try:
            print "opening device"
            self.dev = os.open("/dev/beaglelogic", os.O_RDONLY)
            self.fdev = os.fdopen(self.dev)
            #dev = open("/dev/beaglelogic", 'rb', buffering=0)
        except OSError:
            print "Device /dev/beaglelogic cannot be opened"
	print(self.fdev)





    def readAdcIq_n(self):
        
        # BeagleLogic
        if self.fdev.closed:
            print("dev is closed, reopening...")
            self.dev = os.open("/dev/beaglelogic",os.O_RDONLY)
            self.fdev = os.fdopen(self.dev)

        try:
            iqBytes = os.read(self.dev,self._N_samples*2)
            self.count = self.count + self._N_samples*2
            print("readAdcIq: " + str(type(iqBytes)) + " (" + str(len(iqBytes)) + "):" + str(iqBytes[1:10]) + "Number of samples captured: " + str(self.count))
            if np.sum(iqSamples)==0:
                return 1 # Opened device Successfully but returned zeros
            else:
                return 0 # Opened device Successfully and returned non-zero data
        except:
            return 2 # Opened device Successfully but couldn't read





