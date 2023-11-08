// HW2 - 202355517

int nState = 1;
int num1, num2, sum;

void setup()
{ Serial.begin(9600);
  Serial.println("Enter 2 integers to add");
}

void loop()
{ if (Serial.available() >= 2)
  { num1 = Serial.parseInt();

    num2 = Serial.parseInt();

    sum = num1 + num2;

    Serial.print(num1);
    Serial.print(" + ");
    Serial.print(num2);
    Serial.print(" = ");
    Serial.println(sum);
    Serial.println("Enter 2 integers to add");
  }
}