#include <DYIRDaikin.h>

//#define DYIRDAIKIN_SOFT_IR

DYIRDaikin irdaikin;

class Condizionatore{
  
  public:

    Condizionatore(){ // initializing the irdaikin driver
      #ifdef DYIRDAIKIN_SOFT_IR
        irdaikin.begin(3);
      #else
        irdaikin.begin();
      #endif
      irdaikin.on();
      irdaikin.setSwing_off();
      irdaikin.setMode(1);
      irdaikin.setFan(4);//FAN speed to MAX
      irdaikin.setTemp(25);
      //----everything is ok and to execute send command-----
      this->powerOff();
    }

    void powerOff(){
      irdaikin.off();
      irdaikin.sendCommand();
      powerStatus = 0;
    }

    void setHotAir(){
      irdaikin.on();
      irdaikin.setFan(4);
      irdaikin.setMode(3);
      irdaikin.setTemp(30);
      irdaikin.sendCommand();
      powerStatus = 1;
    }

    void setColdAir(){
      irdaikin.on();
      irdaikin.setFan(4);
      irdaikin.setMode(1);
      irdaikin.setTemp(18);
      irdaikin.sendCommand();
      powerStatus = 1;
    }

    void setVentilator(){
      irdaikin.on();
      irdaikin.setFan(4);
      irdaikin.setMode(0);
      irdaikin.setTemp(18);
      irdaikin.sendCommand();
      powerStatus = 1;
    }

    void setDeumidificatore(){
      irdaikin.on();
      irdaikin.setMode(3);
      irdaikin.sendCommand();
      powerStatus = 1;
    }

    int getPowerStatus(){
      return powerStatus;
    }
    
  private:
    int powerStatus;
};