#include "Condizionatore.h"

String inputMessage;
Condizionatore *condi;

void setup(){
  Serial.begin(9600);
  condi = new Condizionatore();
  delay(1000);
}

void loop() {

  inputMessage = Serial.readStringUntil('\v');

  if( inputMessage == "COLD") {
    condi->setColdAir();
  }else if( inputMessage == "HOT") {
    condi->setHotAir();
  } else if(inputMessage == "DEUMIDIFY") {
    condi->setDeumidificatore();
  }else if ( inputMessage == "OFF") {
    condi->powerOff();
  }

  
}
