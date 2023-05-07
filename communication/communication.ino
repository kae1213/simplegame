#define BUTTON1_LEFT 2
#define BUTTON1_RIGHT 3

int x;
bool input_flag;

void setup() {
 Serial.begin(115200);
 Serial.setTimeout(1);

 pinMode(BUTTON1_LEFT, INPUT_PULLUP);
 pinMode(BUTTON1_RIGHT, INPUT_PULLUP);
 
 attachInterrupt(digitalPinToInterrupt(BUTTON1_LEFT), service_input1, LOW);
 attachInterrupt(digitalPinToInterrupt(BUTTON1_RIGHT), service_input1, LOW);

}

void loop() {
 while (!Serial.available());
 x = Serial.readString().toInt();
 Serial.print(x + 1);
 Serial.print("Hello");

 if (input_flag){
  Serial.print("Hello This was a button press");
  input_flag = !input_flag;
 }


}

///***Interrupt Functions***///
void service_input1() {
  static unsigned long last_interrupt_time = 0;
  unsigned long interrupt_time = millis();
  
  if (interrupt_time - last_interrupt_time > 200) 
  {
    // do yo thangggg!
    input_flag = true;
    Serial.print("Hello This was a button press");
  }
  last_interrupt_time = interrupt_time;
}