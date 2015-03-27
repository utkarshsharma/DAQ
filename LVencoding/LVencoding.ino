

#include <SoftwareSerial.h>

SoftwareSerial mySerial1(10, 11); // RX, TX

  int Shutdown_left ;
  int Shutdown_right ;
  int Shutdown_driver ;
  int BOTS ;
  int Inertia_switch ;
  int interlock_HV_ ;
  int Interlock_HV ;
  int Form_interlock ;
  int From_TSMS ;
  int TSAL_out ;
  int GFD ;
  int Precharge_signal ;
  int RTDS ;
  int Cplus ;
  int Ignition_switch ;
  int BMS_in ; 
  int HV_current_sensor ; 
  int MC_Voltage ;
  int HV_Battery_Voltage ;
  int s,a,w;
  char b,c,d;


void setup()  
{
  // Open serial communications and wait for port to open:
  mySerial1.begin(9600);
}

void loop() // run over and over
{

  Shutdown_left = 1;
  Shutdown_right = 1;
  Shutdown_driver = 1;
  BOTS = 1;
  Inertia_switch = 1;
  interlock_HV_ = 1;
  Interlock_HV = 1;
  Form_interlock = 1;
  From_TSMS = 0;
  TSAL_out = 1;
  GFD = 1;
  Precharge_signal = 1;
  RTDS = 0;
  Cplus = 1;
  Ignition_switch = 1;
  BMS_in = 0; 
  HV_current_sensor = 100; 
  MC_Voltage = 20;
  HV_Battery_Voltage = 150;

  
s = (Shutdown_right*64) + (Shutdown_driver*32) + (BOTS*16) + (Inertia_switch*8) + (interlock_HV_*4) + (Interlock_HV*2) + Form_interlock;
a = (TSAL_out*64) + (GFD*32)+ (Precharge_signal*16) + (RTDS*8) + (Cplus*4) + (Ignition_switch*2) + BMS_in; 
w = (Shutdown_left*2) + (From_TSMS);

b = char(s);
c = char(a);
d = char(w);

mySerial1.print('$');
delayMicroseconds(140);
mySerial1.print(b);
delayMicroseconds(140);
mySerial1.print(c);
delayMicroseconds(140);
mySerial1.print(d);
delayMicroseconds(140);
mySerial1.print(HV_current_sensor);
delayMicroseconds(140);
mySerial1.print(MC_Voltage);
delayMicroseconds(140);
mySerial1.print(HV_Battery_Voltage);
delayMicroseconds(140);

}
