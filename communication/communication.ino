#define BUTTON1_LEFT 2
#define BUTTON1_RIGHT 3
#define BUTTON1_ATTACK 18
#define VORTEX_BUTTON 21

int x;
const char LEFT_BUTTON_PRESS = '0';
const char RIGHT_BUTTON_PRESS = '1';
const char ATTACK_BUTTON_PRESS = 'A';

bool input_flag = false;
bool input2_flag = false;
bool input3_flag = false;

// New Variables
unsigned long debounce_delay = 500; // Debounce time in milliseconds
unsigned long last_button_press_time = 0;
int currentLed = 0;
bool isButtonPressed = false;
bool gameActive = true;
const int pinsOf_Leds[] = {22, 24, 26, 28, 30, 32, 34, 36, 38, 40};
const int lenOf_Leds = sizeof(pinsOf_Leds) / sizeof(pinsOf_Leds[0]);

// State of Game 
bool vortex_playing = false;


void setup() {
 Serial.begin(9600);
 //Serial.setTimeout(1);

 for (int i = 0; i < lenOf_Leds; i++) {
    pinMode(pinsOf_Leds[i], OUTPUT);
  }

 pinMode(BUTTON1_LEFT, INPUT_PULLUP);
 pinMode(BUTTON1_RIGHT, INPUT_PULLUP);
 pinMode(BUTTON1_ATTACK, INPUT_PULLUP);
 pinMode(VORTEX_BUTTON, INPUT_PULLUP);

 attachInterrupt(digitalPinToInterrupt(BUTTON1_LEFT), service_input1, LOW);
 attachInterrupt(digitalPinToInterrupt(BUTTON1_RIGHT), service_input2, LOW);
 attachInterrupt(digitalPinToInterrupt(BUTTON1_ATTACK), service_input3, LOW);
 attachInterrupt(digitalPinToInterrupt(VORTEX_BUTTON), handleButtonInterrupt, LOW);


}

void loop() {
  if (Serial.available() > 0) {
    char charReceived = Serial.read(); // Read the incoming character
    
    // Kelvin: the code here will handle the game based on Arduino
    if (charReceived == '0') {  // Command received from PC to start the game
      vortex_playing = true;
      play_vortex(vortex_playing);
    }
  }

 if (input_flag){
  Serial.print(LEFT_BUTTON_PRESS);
  input_flag = false;
 }
 if (input2_flag){
  Serial.print(RIGHT_BUTTON_PRESS);
  input2_flag = false;
 }
 if (input3_flag){
  Serial.print(ATTACK_BUTTON_PRESS);
  input3_flag = false;
 }

 


}

///***Interrupt Functions***///
void service_input1() {
  static unsigned long last_interrupt_time = 0;
  unsigned long interrupt_time = millis();
  
  if (interrupt_time - last_interrupt_time > 50) 
  {
    // do yo thangggg!
    input_flag = true;
  }
  last_interrupt_time = interrupt_time;
}

void service_input2() {
  static unsigned long last_interrupt_time = 0;
  unsigned long interrupt_time = millis();
  
  if (interrupt_time - last_interrupt_time > 50) 
  {
    // do yo thangggg!
    input2_flag = true;
  }
  last_interrupt_time = interrupt_time;
}

void service_input3() {
  static unsigned long last_interrupt_time = 0;
  unsigned long interrupt_time = millis();
  
  if (interrupt_time - last_interrupt_time > 50) 
  {
    // do yo thangggg!
    input3_flag = true;
  }
  last_interrupt_time = interrupt_time;
}
/***********************************************/
/***********************************************/
/***********************************************/
//New functions
bool isButtonPressedDebounced() {
  // Read the button pin state
  bool buttonState = digitalRead(VORTEX_BUTTON) == LOW;
  unsigned long currentTime = millis();

  // Check if the button state is stable for the debounce delay duration
  if (buttonState && (currentTime - last_button_press_time > debounce_delay)) {
    return true;
  }

  return false;
}

void handleButtonInterrupt() {
  unsigned long currentTime = millis();

  if (currentTime - last_button_press_time > debounce_delay) {
    last_button_press_time = currentTime;

    if (gameActive) {
      // If the game is active, stop the game
      Serial.println("Triggered");
      gameActive = false;
    } else {
      // If the game is stopped, restart the game
      Serial.println("Triggered2");
      gameActive = true;
      currentLed = 0;
      digitalWrite(pinsOf_Leds[currentLed], HIGH);
    }
  }
}

void play_vortex(bool is_game_playing){

  while (is_game_playing) {
    isButtonPressed = isButtonPressedDebounced();

    if (gameActive) {
      // Turn off the current LED
      digitalWrite(pinsOf_Leds[currentLed], LOW);

      // Move to the next LED
      currentLed = (currentLed + 1) % lenOf_Leds;

      // Turn on the next LED
      digitalWrite(pinsOf_Leds[currentLed], HIGH);

      // Add a delay to control the speed of LED rotation
      delay(75);
    }

        //Check if the '4' character is received to terminate the game
    if (Serial.available() > 0 && Serial.read() == '4') {
      is_game_playing = false;
      for (int i = 0; i < lenOf_Leds; i++) {
        digitalWrite(pinsOf_Leds[i], LOW);
      }
      Serial.println("Vortex Quit");
    }
  }
}