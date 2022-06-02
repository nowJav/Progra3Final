#include <SPI.h>
#include <MFRC522.h>
#include <Servo.h> 
 
Servo microservo9g;
#define SS_PIN 10
#define RST_PIN 9

MFRC522 mfrc522(SS_PIN, RST_PIN); 

int led_liberado = 5;
int led_negado = 6;
char st[20];
void setup() 
{
  pinMode(led_liberado, OUTPUT);
  pinMode(led_negado, OUTPUT);
  microservo9g.attach(3);
  microservo9g.write(-90);
  // Inicia a serial
  Serial.begin(9600);
  // Inicia  SPI bus
  SPI.begin();
  // Inicia MFRC522
  mfrc522.PCD_Init(); 
  
  Serial.println("Aproxime su RFID...");
  Serial.println();
}
void loop() 
{
 
  if ( ! mfrc522.PICC_IsNewCardPresent()) 
  {
    return;
  }

  if ( ! mfrc522.PICC_ReadCardSerial()) 
  {
    return;
  }
  
  Serial.print("UID :");
  String conteudo= "";
  byte letra;
  for (byte i = 0; i < mfrc522.uid.size; i++) 
  {
     Serial.print(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " ");
     Serial.print(mfrc522.uid.uidByte[i], HEX);
     conteudo.concat(String(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " "));
     conteudo.concat(String(mfrc522.uid.uidByte[i], HEX));
  }
  Serial.println();
  Serial.print("Mensaje : ");
  conteudo.toUpperCase();
  
  // Testa se o cartao1 foi lido
  if (conteudo.substring(1) == "99 8D 13 C3")
  {
    // Levanta a cancela e acende o led verde
    microservo9g.write(90);
    digitalWrite(led_liberado, HIGH);
    Serial.println("Acceso Liberado !");
    Serial.println();
    delay(5000);
    microservo9g.write(-90);
    digitalWrite(led_liberado, LOW);
    }
    
  // Testa se o cartao2 foi lido
  if (conteudo.substring(1) == "49 6F 14 B4")
  {
    Serial.println("Acceso denegado !!");
    Serial.println();
    // Pisca o led vermelho
    for (int i= 1; i<5 ; i++)
    {
      digitalWrite(led_negado, HIGH);
      delay(200);
      digitalWrite(led_negado, LOW);
      delay(200);
    }
  }
  delay(1000);
}
