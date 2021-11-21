int p = 13;

void setup() {
  pinMode(p, OUTPUT);
  pinMode(3, INPUT);
  Serial.begin(9600);
}
 
void loop() {
  int in = analogRead(A3);  
  if (in > 1000)
  {
    digitalWrite(p, HIGH);
    Serial.println(in, '\n');
    delay(1000);
  }
  else
  {
    digitalWrite(p,LOW);
    Serial.println(in, '\n'); 
    delay(1000); 
  }
}
