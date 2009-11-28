
/*
 * The amount of time the button will remain in the press state
 */
#define PRESS_INTERVAL 500

struct button_t { 
  int pin, state;
  long last_change;
};

struct button_t buttons[9];
int command = 0;

void init_button(struct button_t *b, int pin, int mode = OUTPUT) {
  b->pin = pin;
  b->state = LOW;
  b->last_change = 0;
  pinMode(pin, mode);
}

void setup_all_buttons() {
  for(int i=2; i<9; i++) {
   init_button(&buttons[i], i); 
  }
}

void press_button(int button_id) {
  struct button_t *b = &buttons[button_id];
  digitalWrite(b->pin, HIGH);
  b->state = HIGH;
  b->last_change = millis();
}

void refresh_button(struct button_t *b) {
 if(b->state == LOW) {
   return;
 } 
 if((millis() - b->last_change) > PRESS_INTERVAL) {
   digitalWrite(b->pin, LOW);
   b->state = LOW;
 }
}

void refresh_all_buttons() {
  for(int i=2; i<7; i++) {
   refresh_button(&buttons[i]);
  } 
}

/**
 * Board initilization procedure
 */
void setup() {
 setup_all_buttons();
 Serial.begin(9600);
}

/**
 * Main application loop: Read command and press button
 */
void loop() {
  if(Serial.available() > 0) {
   command = Serial.read();
   if(command >= '2' && command < '9') {
     Serial.println(command-'0', DEC);
     press_button(command - '0'); 
   }
  }
  refresh_all_buttons();
}

