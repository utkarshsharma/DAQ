
import time
from gi.repository import Gtk
import serial
#ser = serial.Serial(port = "/dev/ttyUSB0",baudrate = 9600)



'''
Function name: fnGet_USB_Serial_Ports
Input : None
Output: List of usb-to-serial ports
Description: This function returns list of all available usb-to-serial ports
'''
def fnGet_USB_Serial_Ports():
    list_serial=list(serial.tools.list_ports.comports())
    list_usb = [x for x in list_serial if ('ttyUSB' in x[0] or 'ACM' in x[0])]
    return list_usb

# Update function to regularly update the values.

def update(str)
	
	


	return 


class gui:

    #wTree = None

    def __init__( self ):

        filename = "test1.glade"
        self.builder = Gtk.Builder()
        self.builder.add_from_file(filename)

        dic = { 
               "on_window2_destroy" : self.quit,
              }

    
	self.builder.connect_signals(dic)
	
	self.window2= self.builder.get_object("window2")
#	self.builder.get_object("hboxWarning").hide()

	self.window2.show_all()	
	self.window2.set_title("DAQ GUI IIT Bombay Racing");
	self.p1 = self.builder.get_object("p1")
	self.p2 = self.builder.get_object("p2")
	self.p3 = self.builder.get_object("p3")
	self.p4 = self.builder.get_object("p4")
	self.p5 = self.builder.get_object("p5")
	self.p6 = self.builder.get_object("p6")
	self.p7 = self.builder.get_object("p7")
	self.p8 = self.builder.get_object("p8")

	self.l1 = self.builder.get_object("l1")
	self.l2 = self.builder.get_object("l2")
	self.l3 = self.builder.get_object("l3")
	self.l4 = self.builder.get_object("l4")
	self.l5 = self.builder.get_object("l5")
	self.l6 = self.builder.get_object("l6")

	self.la1 = self.builder.get_object("la1")
	self.la2 = self.builder.get_object("la2")
	self.la3 = self.builder.get_object("la3")
	self.la4 = self.builder.get_object("la4")
	self.la5 = self.builder.get_object("la5")
	self.la6 = self.builder.get_object("la6")

	self.b1 = self.builder.get_object("b")
	self.b2 = self.builder.get_object("switch2")

	self.e1 = self.builder.get_object("e1")
	self.e2 = self.builder.get_object("e2")


	
	TPS1 = 0.90
	#time.sleep(5)
	TPS1 = 0.20
	TPS2 = 0.10
	BPS = 0.15
	STR = 0.20
	RPM_FL = 0.25
	RPM_FR = 0.30
	RPM_RL = 0.35
	RPM_RR = 0.40

	motor_l = 0.9
	motor_r = 0.8
	accX = 0.7
	accY = 0.6
	yaw = 0.5
	ang_acc = 0.4

	MC1 = 0
	MC2 = 1
	motor_temp = '39 Celcius'
	ediff_mode = 'Endurance'



#        gtk.main()
	
#   def click(self, widget):
	self.p1.set_fraction(TPS1)
	self.p2.set_fraction(TPS2)
	self.p3.set_fraction(BPS)
	self.p4.set_fraction(STR)
	self.p5.set_fraction(RPM_FL)
	self.p6.set_fraction(RPM_FR)
	self.p7.set_fraction(RPM_RL)
	self.p8.set_fraction(RPM_RR)

	self.l1.set_value(motor_l)
	self.l2.set_value(motor_r)
	self.l3.set_value(accX)
	self.l4.set_value(accY)
	self.l5.set_value(yaw)
	self.l6.set_value(ang_acc)

	lx1 = "%s Volts" %motor_l
	lx2 = "%s Volts" %motor_r
	lx3 = "%s Volts" %accX
	lx4 = "%s Volts" %accY
	lx5 = "%s Volts" %yaw
	lx6 = "%s Volts" %ang_acc

	self.la1.set_text(lx1)
	self.la2.set_text(lx2)
	self.la3.set_text(lx3)
	self.la4.set_text(lx4)
	self.la5.set_text(lx5)
	self.la6.set_text(lx6)


	self.b1.set_active(MC1)
	self.b2.set_active(MC2)

	self.e1.set_text(motor_temp)
	self.e2.set_text(ediff_mode)

    def quit(self, widget):
        sys.exit(0)

'''
Serial port class. Runs on seperate thread.
'''

class mySerial(threading.Thread):

    def __init__(self,portname,textview):
	self.textview = textview
        threading.Thread.__init__(self)
        self.daemon = True
        self.paused = True
        self.state = threading.Condition()
        self.started = False
	self.open_success = False	

	try:
	    self.serial_port = serial.Serial(portname,9600, timeout = 5)
	    self.open_success = True
	except:
	    print 'Unable to open port'

    def run(self):
        self.resume()
        self.started = True
        
        while self.serial_port.isOpen():
            with self.state:
                if self.paused:
                    self.state.wait()
#	    self.serial_port.write("iiiiiddddd")
#	    time.sleep(0.5)
	    text = self.serial_port.read()
#            print text
	    serial_q.put(text)
#	    self.textview.get_buffer().set_text("Hi")
#	    self.textview.get_buffer().insert(self.textview.get_buffer().get_end_iter(), text)
	    buffer_tv = self.textview.get_buffer()
	    buffer_tv.set_text('Hi')
	    self.textview.set_buffer(buffer_tv)
    def resume(self):
        with self.state:
            self.paused = False
            self.state.notify()

    def pause(self):
        with self.state:
            self.paused = True

    def stop(self):
        self.stopped = True
	self.paused = True
	self.serial_port.close() 






if __name__== "__main__":
    
    gui()
    Gtk.main()