#include <esp_camera.h>
#include <rom/tjpgd.h>
#include "cam.h"
#include "ST7789.h"
#include <Arduino.h>
#include <WiFi.h>
#include "soc/soc.h"
#include "tjpgdec.h"
#include "soc/rtc_cntl_reg.h"

String serverName = "********";
String serverPath = "/upload";
const int serverPort = 5000;
WiFiClient client;

const int timerInterval = 000;
unsigned long previousMillis = 0;
const int timerIntervalDisplay = 10000;
int wifiNumber;
const int timerWeb = 10000; 
unsigned long pMillis = 0;
long lastTime=0;



ST7789 tft = ST7789(); 

char tmpStr[256];
int i = 0;
static uint16_t *preview;
sensor_t *s;
camera_fb_t *fb = NULL;
JPGIODEV dev;
char *work = NULL; 

void setup()
{
  WRITE_PERI_REG(RTC_CNTL_BROWN_OUT_REG, 0);
  Serial.begin(115200);

  tft.init();
  tft.invertDisplay(true);
  tft.setSwapBytes(true);
  tft.setRotation(0);
  tft.fillScreen(TFT_BLACK);
  tft.setTextSize(2);
  tft.setTextColor(TFT_MAROON);
  tft.drawString("Searching Wifi!!", 28, 110);
  // Serial.setDebugOutput(true);
  WiFi.mode(WIFI_STA);
  Serial.println();
  Serial.print("Connecting to ");
//  Serial.println(ssid);
  Serial.println("scan start");

  // WiFi.scanNetworks will return the number of networks found
  int n = WiFi.scanNetworks();
  Serial.println("scan done");
 
  if (n == 0) {
    Serial.println("no networks found");
  } else {
    Serial.print(n);
    Serial.println(" networks found");
    for (int i = 0; i < n; ++i) {
      if (WiFi.SSID(i) == "******"or WiFi.SSID(i) == "*******" or  WiFi.SSID(i)=="*******") {
        if (WiFi.SSID(i) == "*******") {
          Serial.print(WiFi.SSID(i));
          wifiNumber = i;
          
          const char* ssid = "*******";
          const char* password = "*****";
          WiFi.begin(ssid, password);
          while (WiFi.status() != WL_CONNECTED) {
            Serial.print(".");      
            // Code for restart ESP : Start
            unsigned long cMillis = millis();
            if (cMillis - pMillis >= 10000) {
              ESP.restart();
              pMillis = cMillis;
            }

            // End
            delay(500);
          }
          break;
          } 
          else if (WiFi.SSID(i) == "*******") {
          Serial.print(WiFi.SSID(i));
          wifiNumber = i;
          
          const char* ssid = "*******";
          const char* password = "REMCOR56";
          WiFi.begin(ssid, password);
          while (WiFi.status() != WL_CONNECTED) {
            Serial.print(".");      
            // Code for restart ESP : Start
            unsigned long cMillis = millis();
            if (cMillis - pMillis >= 10000) {
              ESP.restart();
              pMillis = cMillis;
            }

            // End
            delay(500);
          }
          break;
          } 
          else if (WiFi.SSID(i) == "*******") {
          Serial.println(WiFi.SSID(i));
          wifiNumber = i;
          const char* ssid = "*******";
          const char* password = "*****";
          WiFi.begin(ssid, password);
          while (WiFi.status() != WL_CONNECTED) {
            Serial.print(".");
            // Code for restart ESP : Start
            unsigned long cMillis = millis();
            if (cMillis - pMillis >= 10000) {
              ESP.restart();
              pMillis = cMillis;
            }

            // End
            delay(500);
          }
          break;
        }
      }

    }

  }
  Serial.println();
  Serial.print("ESP32-CAM IP Address: ");
  Serial.println(WiFi.localIP());

  esp_err_t err = cam_init();
  if (err != ESP_OK)
  {
    snprintf(tmpStr, sizeof(tmpStr), "Camera init failed with error 0x%x", err);
    tft.drawString(tmpStr, 0, 208);
    Serial.println(tmpStr);
    delay(1000);
    ESP.restart();
  }
  sensor_t * s = esp_camera_sensor_get();
  s->set_brightness(s, 2);
  s->set_contrast(s, 2);
  s->set_saturation(s, 2);
  s->set_sharpness(s, 2);
  s->set_aec2(s, true);
  s->set_denoise(s, true);
  s->set_lenc(s, true);
  s->set_hmirror(s, true);
  s->set_vflip(s, true);
  s->set_quality(s, 15);

  preview = new uint16_t[200 * 200];
  work = (char *)malloc(WORK_BUF_SIZE);
  dev.linbuf_idx = 0;
  dev.x = 0;
  dev.y = 0;
  dev.linbuf[0] = (color_t *)heap_caps_malloc(JPG_IMAGE_LINE_BUF_SIZE * 3, MALLOC_CAP_DMA);
  dev.linbuf[1] = (color_t *)heap_caps_malloc(JPG_IMAGE_LINE_BUF_SIZE * 3, MALLOC_CAP_DMA);
}

esp_err_t cam_init()
{
  camera_config_t config;
  config.ledc_channel = LEDC_CHANNEL_0;
  config.ledc_timer = LEDC_TIMER_0;
  config.pin_d0 = Y2_GPIO_NUM;
  config.pin_d1 = Y3_GPIO_NUM;
  config.pin_d2 = Y4_GPIO_NUM;
  config.pin_d3 = Y5_GPIO_NUM;
  config.pin_d4 = Y6_GPIO_NUM;
  config.pin_d5 = Y7_GPIO_NUM;
  config.pin_d6 = Y8_GPIO_NUM;
  config.pin_d7 = Y9_GPIO_NUM;
  config.pin_xclk = XCLK_GPIO_NUM;
  config.pin_pclk = PCLK_GPIO_NUM;
  config.pin_vsync = VSYNC_GPIO_NUM;
  config.pin_href = HREF_GPIO_NUM;
  config.pin_sscb_sda = SIOD_GPIO_NUM;
  config.pin_sscb_scl = SIOC_GPIO_NUM;
  config.pin_pwdn = PWDN_GPIO_NUM;
  config.pin_reset = RESET_GPIO_NUM;
  config.xclk_freq_hz = 20000000;
  config.pixel_format = PIXFORMAT_JPEG;
  if (psramFound()) {
    config.frame_size = FRAMESIZE_UXGA;
    config.jpeg_quality = 20;  //0-63 lower number means higher quality
    config.fb_count = 2;
  }
  else {
    config.frame_size = FRAMESIZE_SXGA;
    config.jpeg_quality = 10;  //0-63 lower number means higher quality
    config.fb_count = 1;
  }


  // camera init
  return esp_camera_init(&config);
  sendPhoto();
}


void loop()
{
  if (i == 0) // count down
  {
    unsigned long starttime = millis();
    unsigned long endtime = starttime;
    while ((endtime - starttime) <= 10000) //here change the time to 30000
    {
      tft.setTextSize(2);
      tft.setTextColor(TFT_DARKCYAN);
      tft.drawString("Set The Camera!!", 30, 3);
      tft.drawString("Bed No: 8", 30, 23);
      Serial.println("Wait 10 second"); 
      fb = esp_camera_fb_get();
      if (!fb)
      {
        Serial.printf("Camera capture failed!");
        tft.drawString("Camera capture failed!", 0, 224);
      }
      else
      {
        decodeJpegBuff(fb->buf, fb->len, 3);
        //      tft.pushRect(20, 50, 200, 150, preview);
        tft.pushRect(20, 50, 200, 150, preview);
        esp_camera_fb_return(fb);
        fb = NULL;
      }
      int loopcount = loopcount + 1;
      endtime = millis();
    }
    i = 1;
  }
  else {
    unsigned long currentMillis = millis();
    if (currentMillis - previousMillis >= timerInterval) {
      tft.fillScreen(TFT_BLACK);
      tft.setTextSize(1);
      tft.setTextColor(TFT_GREEN);
      tft.drawString(WiFi.SSID(wifiNumber), 190, 10);
      tft.setTextSize(2);

      if (WiFi.RSSI()<-60){
        tft.setTextColor(TFT_RED);
        tft.drawNumber(WiFi.RSSI(), 190, 25);
      }
      else{
        tft.drawNumber(WiFi.RSSI(), 190, 25);
      }
      
      tft.setTextSize(2);
      tft.setTextColor(TFT_DARKCYAN);
;     tft.drawString("Image Sending!!!", 30, 100);
      tft.drawString("Bed No: 8", 30, 120);
      sendPhoto();
      //    Serial.println();
      previousMillis = currentMillis;
    }
  }
  //  Serial.println(i);
  //  i++;
}



// User defined call-back function to input JPEG data from memory buffer
//-------------------------
static UINT tjd_buf_input(
  JDEC *jd,   // Decompression object
  BYTE *buff, // Pointer to the read buffer (NULL:skip)
  UINT nd     // Number of bytes to read/skip from input stream
)
{
  // Device identifier for the session (5th argument of jd_prepare function)
  JPGIODEV *dev = (JPGIODEV *)jd->device;
  if (!dev->membuff)
    return 0;
  if (dev->bufptr >= (dev->bufsize + 2))
    return 0; // end of stream

  if ((dev->bufptr + nd) > (dev->bufsize + 2))
    nd = (dev->bufsize + 2) - dev->bufptr;

  if (buff)
  { // Read nd bytes from the input strem
    memcpy(buff, dev->membuff + dev->bufptr, nd);
    dev->bufptr += nd;
    return nd; // Returns number of bytes read
  }
  else
  { // Remove nd bytes from the input stream
    dev->bufptr += nd;
    return nd;
  }
}

// User defined call-back function to output RGB bitmap to display device
//----------------------
static UINT tjd_output(
  JDEC *jd,     // Decompression object of current session
  void *bitmap, // Bitmap data to be output
  JRECT *rect   // Rectangular region to output
)
{
  BYTE *src = (BYTE *)bitmap;
  //   Serial.printf("%d, %d, %d, %d\n", rect->top, rect->left, rect->bottom, rect->right);
  for (int y = rect->top; y <= rect->bottom; y++)
  {
    for (int x = rect->left; x <= rect->right; x++)
    {
      preview[y * 200 + x] = tft.color565(*(src++), *(src++), *(src++));
    }
  }
  return 1; // Continue to decompression
}

void decodeJpegBuff(uint8_t arrayname[], uint32_t array_size, uint8_t scale)
{
  JDEC jd; // Decompression object (70 bytes)
  JRESULT rc;

  //dev.fhndl = NULL;
  // image from buffer
  dev.membuff = arrayname;
  dev.bufsize = array_size;
  dev.bufptr = 0;

  if (scale > 3)
    scale = 3;

  if (work)
  {
    rc = jd_prepare(&jd, tjd_buf_input, (void *)work, WORK_BUF_SIZE, &dev);
    if (rc == JDR_OK)
    {
      // Start to decode the JPEG file
      rc = jd_decomp(&jd, tjd_output, scale);
    }
  }
}


//
String sendPhoto() {
  delay(1000);
  String getAll;
  String getBody;

  camera_fb_t * fb = NULL;
  fb = esp_camera_fb_get();
  if (!fb) {
    Serial.println("Camera capture failed");
    delay(1000);
    ESP.restart();
  }

//  Serial.println("Connecting to server: " + serverName);

  if (client.connect(serverName.c_str(), serverPort)) {
//    client.setNoDelay(1);
    client.setNoDelay(true);
//    Serial.println("Connection successful!");

    String head = "--RandomNerdTutorials\r\nContent-Disposition: form-data; name=\"image[]\"; filename=\"res7.jpg\"\r\nContent-Type: image/jpeg\r\n\r\n";
    String tail = "\r\n--RandomNerdTutorials--\r\n";

    uint32_t imageLen = fb->len;
    uint32_t extraLen = head.length() + tail.length();
    uint32_t totalLen = imageLen + extraLen;

    uint32_t t = millis();

    //    Serial.print(imageLen);
    //    Serial.print(extraLen);
    //    Serial.print(totalLen);


    client.println("POST " + serverPath + " HTTP/1.1");
    client.println("Host: " + serverName);
    client.println("Content-Length: " + String(totalLen));
    client.println("Content-Type: multipart/form-data; boundary=RandomNerdTutorials");
    client.println();
    client.print(head);



//    delay(2000);
    
    long sTimer = millis();
//    Serial.print(sTimer); Serial.println(" ms");
    uint8_t *fbBuf = fb->buf;
    size_t fbLen = fb->len;
    //    Serial.println(fbLen);
    for (size_t n = 0; n < fbLen; n = n + 1024) {
      if (n + 1024 < fbLen) {
        client.write(fbBuf, 1024);
        fbBuf += 1024;
      }
      else if (fbLen % 1024 > 0) {
        size_t remainder = fbLen % 1024;
        client.write(fbBuf, remainder);
      }
//      Serial.print(millis()); Serial.println(" ms");
      if ((millis() - sTimer) >= 6000) {
        Serial.print("ESP.getFreeHeap()");
        Serial.println(ESP.getFreeHeap());
//                while (1) {
//                  yield();
//                }
        break;
      }     
    }
    client.print(tail);


    t = millis() - t;
    Serial.println(WiFi.RSSI());
    Serial.print(t); Serial.println(" ms");

    //    client.read();
    esp_camera_fb_return(fb);

    int timoutTimer = 5000;
    long startTimer = millis();
    boolean state = false;
    Serial.println(startTimer);
    while ((startTimer + timoutTimer) > millis()) {
      Serial.print(".");
      delay(100);
      while (client.available()) {
//        client.getNoDelay();
        char c = client.read();
                Serial.print(c);
//                Serial.println(' ');
        if (c == '\n') {
          if (getAll.length() == 0) {
            state = true;
          }
          getAll = "";
        }
        else if (c != '\r') {
          getAll += String(c);
        }
        if (state == true) {
          getBody += String(c);
        }
        startTimer = millis();
      }
      if (getBody.length() > 0) {
        break;
      }
    }
//    Serial.println();
    client.stop();
//    Serial.println(getBody);
  }
  else {
    getBody = "Connection to " + serverName +  " failed.";
    Serial.println(getBody);
  }
  return getBody;
}
