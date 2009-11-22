/**
 * Remote control kernel
 * 
 */

/* 
 Define directions represented by buttons
 */
#define LEFT_FORWARD 2
#define LEFT_BACKWARD 3

#define RIGHT_FORWARD 4
#define RIGHT_BACKWARD 5

/*
 * The amount of time the button will remain in the press state
 */
#define PRESS_INTERVAL 1000

struct button_t { 
  int pin, state;
  int last_change;
};

struct button_t buttons[7];
int command = 0;

void init_button(struct button_t *b, int pin, int mode = OUTPUT) {
  b->pin = pin;
  b->state = LOW;
  b->last_change = 0;
  pinMode(pin, mode);
}

void setup_all_buttons() {
  for(int i=2; i<7; i++) {
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

void setup() {
 setup_all_buttons();
 Serial.begin(9600);
 Serial.println("waiting for commands ...");
}

void loop() {
  if(Serial.available() > 0) {
   command = Serial.read();
   process_command(command);
  }
  refresh_all_buttons();
}

void process_command(int command) {
    switch(command) {
     case 'q':
      press_button(LEFT_FORWARD);
      Serial.println("moving left forward");
      break;
     case 'a':
      press_button(LEFT_BACKWARD);
      Serial.println("moving left backward");
      break;
     case 'w':
      press_button(RIGHT_FORWARD);
      Serial.println("moving right forward");
      break;
     case 's':
      press_button(RIGHT_BACKWARD);
      Serial.println("moving right backward");
      break;
     default:
      Serial.println("Undefined command");
   }  
}
