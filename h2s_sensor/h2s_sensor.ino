int sensorPin = A3;
int val = 0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  val = analogRead(sensorPin);
  // Send a value by string rather than bytes to determine new line character.
  Serial.print(val);
  Serial.print('\n');
  delay(300000);  // 5 minutes
}
