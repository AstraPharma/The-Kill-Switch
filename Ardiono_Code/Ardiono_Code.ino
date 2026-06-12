#include <Keyboard.h>

const int buttonPin = 2;

void setup() {
  pinMode(buttonPin, INPUT_PULLUP);
  Keyboard.begin();
}

void loop() {
  if (digitalRead(buttonPin) == LOW) {
    delay(50); // debounce

    Keyboard.press(KEY_LEFT_CTRL);
    Keyboard.press(KEY_LEFT_ALT);
    Keyboard.press('k');

    delay(100);

    Keyboard.releaseAll();

    while (digitalRead(buttonPin) == LOW) {
      delay(10);
    }

    delay(500);
  }
}