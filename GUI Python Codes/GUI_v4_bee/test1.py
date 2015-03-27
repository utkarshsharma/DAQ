
import time
from gi.repository import Gtk
from gi.repository import GObject
from gi.repository import GLib
from gi.repository import Gdk
import serial

import threading

global text
global TPS1
global TPS2
global BPS
global STR

global cTPS1
global cTPS2
global cBPS
global cSTR

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
def update(str):

    if str[0] == "h":
        cTPS1 = str[1]
        cTPS2 = str[2] 
        cBPS = str[3]
        cSTR = str[4]

        TPS1 = ord(cTPS1)
        TPS2 = ord(cTPS2)
        BPS = ord(cBPS)
        STR = ord(cSTR)


        TPS1 = float(TPS1/255.00)
        TPS2 = float(TPS2/255.00)
        BPS = float(BPS/255.00)
        STR = float(STR/255.00)
        
        print(TPS1)
        print(TPS2)
        print(BPS)
        print(STR)

        app_gui.p1.set_fraction(TPS1)
        app_gui.p2.set_fraction(TPS2)  
        app_gui.p3.set_fraction(BPS)
        app_gui.p4.set_fraction(STR)
 
    pass

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
        self.window2.show_all() 
        self.window2.set_title("DAQ GUI IIT Bombay Racing");
        
        self.p1 = self.builder.get_object("p1")
        self.p2 = self.builder.get_object("p2")
        self.p3 = self.builder.get_object("p3")
        self.p4 = self.builder.get_object("p4")
        
        TPS1 = 0.5
        TPS2 = 0.5
        BPS = 0.5
        STR = 0.5

        self.p1.set_fraction(TPS1)
        self.p2.set_fraction(TPS2)
        self.p3.set_fraction(BPS)
        self.p4.set_fraction(STR)


        self.serial_port = mySerial("/dev/ttyUSB2")
        self.serial_port.start()


        #GObject.idle_add(update,text)


    def quit(self, widget):
        sys.exit(0)

'''
Serial port class. Runs on seperate thread.
'''

class mySerial(threading.Thread):

    def __init__(self,portname):
        #self.textview = textview
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
        '''
        while self.serial_port.isOpen():
            with self.state:
                if self.paused:
                    self.state.wait()
        '''
        while 1:
            text = self.serial_port.read(5)
            time.sleep(0.001)
            #print(text)
            GObject.idle_add(update,text)
        
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
    
    app_gui =   gui()
    GLib.threads_init()
    Gdk.threads_init()
    Gdk.threads_enter()

    Gtk.main()

    Gdk.threads_leave()

