**tp-link c20 router intro pass= qwerty12345 (GENHICU1 stellarBD)**

//const char* ssid = "Home_TP";
//const char* password = "llIlIIl0O~`IlIl";

stellarBD

## Problems
      1. Image will not send when distance is long.
      2. Image 

## Instruments/Components
      1. ESP32 Camera: 8 ... (ok)
      2. Clamp
      3. Handle
      4. GO pro handler
      5. Router + powerSupply
      6. Display For show the website + power supplier
      7. Wire + Adapter 8 (For Camera)
      8. Wire + Adapter for Raspberry pi (Ok)
      9. Raspberry pi 3B + SD card 32GB (ok)
      10. Raspberry pi cooler
      11. All screws.. (Big and Small)
      12. Case For ttgo camera Plus
      13. Case for Raspberry pi
      14. Ups for raspberry pi (optional)
      15. HDMI cable (OK)
      16.

# Problems
## 18.10.2020
   1. In demo.py if the image text size is not ok it doesnt read the image and problem the whole server and stop the data read things in the serever. Try to solve it by checking the file is image or not. it creates problem if cv.imread("") doesnt get any image. List list of text size is not found types error blah blah. 

## 17.10.2020
   1. Ajax get create more load on raspberry pi.. because it connects every time to send data to the webpage , every time pass a data in 5 sec it needs to open the url gets the josn data and ajax set it to HTMlL page. But its reliable for the project.
   2. Socketio create less load on raspberry pi.. because it connects only once with the clint and start passing data to the webpage, but it is less reliable than ajax load. Every time we reload it creates broken pipe error, again at first the cpu usgae is 40% with GUI. But when we reload the web page one time its load becomes high...
   3. Learn what is eventlet.monkeypatch
### (solution 17.10.2020)
create an if loop inside while loop where a varible named **num** called.. if **num** true than run data read else stop the event.In socketio connect change the value of the variable **num= True** and on disconnect make it **False**. It solves the reloading problem.cpu usgae reduce.
 previously i run background code in rc.local. If i run server on rc.local it create mistakes. But when i run it in systemd service it works fine. Both service like python script and chromium browser can run through this ... and also data read is fast now

# Tree
## Laptop

```
├───pythonTest
├───static
│   ├───images
│   ├───imagesFixAngle
│   ├───imagesForData
│   ├───js
│   └───ovr
├───templates
│   └───css
└───__pycache__

```

## RaspberryPi3B

```
├── demo.py
├── fixAngle.py
├── fixAngle.pyc
├── nano.save
├── posts.db
├── sample_app.py
├── sample_app.pyc
├── sample_app.py.save
├── sample_app.py.save.1
├── static
│   ├── images
│   │   ├── res0.jpg
│   │   ├── res1.jpg
│   │   ├── res2.jpg
│   │   ├── res3.jpg
│   │   ├── res4.jpg
│   │   ├── res5.jpg
│   │   ├── res6.jpg
│   │   ├── res7.jpg
│   │   ├── res8.jpg
│   │   └── res9.jpg
│   ├── imagesFixAngle
│   │   ├── res0.jpg
│   │   ├── res1.jpg
│   │   ├── res2.jpg
│   │   ├── res3.jpg
│   │   ├── res4.jpg
│   │   ├── res5.jpg
│   │   ├── res6.jpg
│   │   ├── res7.jpg
│   │   ├── res8.jpg
│   │   └── res9.jpg
│   └── imagesForData
│       ├── res0.jpg
│       ├── res1.jpg
│       ├── res2.jpg
│       ├── res3.jpg
│       ├── res4.jpg
│       ├── res5.jpg
│       ├── res6.jpg
│       ├── res7.jpg
│       ├── res8.jpg
│       └── res9.jpg
├── templates
│   ├── base.html
│   ├── dashboard.html
│   ├── dashboard.html.save
│   ├── heartRate.html
│   ├── oxygenSaturation.html
│   ├── posted.html
│   └── test.html
├── uwsgi_config.ini
└── wsgi.py


```

# Time Interval
    1. Esp32 to server (5s+serversendTime)
    2. Image change server side to client side (3000ms)
    3. Data change (5000ms) [using Ajax request get , can't use socektio because client get disconnected]
    4. DataRead code run almost ((40 sec - 1 min) plus )
    5. 30000ms = display show time. then start communication with server
    6. 10000ms = if esp32 can't send image it will start to restart.
    7. 3600000ms to reload the web page (optional) (For data not stop)

# Procedure
    1.







# What tools i learn and use for this project?
  ## Web (server+client)
    1.Flask
      i) Flask SQLAlchemy
      ii) Sqlite3 (Database)
      iii) Flask SocketIO
      iv) Image post get
      v)
    2.Ajax
    3.Jquery
    4.Html
    5.Css
    6.Nginx
    7.Uwsgi
    8.Tft_espi
    9.Esptoop.py
    
  ## Hardware side
    1. Raspberry pi 3
    2. Esp32
    3. Esp32+cam(ov2640)
    4. Esp32+ tft_espi Display(ST7789)
    5. HTTP post to server
    6. TTGO Camera Plus
    7. ESPtool
  ## Image Processing
    1. Opencv python
    2. Tesseract-ocr
    
  ## Application That i use
    1. Pycharm community (Opencv,tesseract,flask)
    2. Pycharm Pro (opencv,tesseract,flask)
    3. Visual Studio Code 
    4. Arduino (Esp32)
    5. Virtual Box (Ubuntu 18.04 , Ubuntu 20.04)
    6. VNC viewer (To check raspberry pi at home from office)
    7. Putty (Runnuing shell of Raspberry pi 3 headless)
    8. Raspberry pi os Full, Raspberry pi os lite, raspberry pi os shell command , ubuntu mate
    9. Sqlite Studio
  
  ## For port forwarding
   1. [Ngrok](https://ngrok.com/)
   2. [Serveo]
   3. [Pagekite](https://www.youtube.com/watch?v=ENjRzQkqEVA&ab_channel=Techbeast.org)
    
  ## Link That i follows more
   1. Create Raspberry pi server
      i) [For create a server in raspberry pi](https://iotbytes.wordpress.com/python-flask-web-application-on-raspberry-pi-with-nginx-and-uwsgi/)
      ii) [For all linux server](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uswgi-and-nginx-on-ubuntu-18-04)
   2. [For Http post to local server](https://randomnerdtutorials.com/esp32-http-get-post-arduino/)
   3. [To use Raspberry pi headless](https://www.raspberrypi.org/documentation/configuration/wireless/headless.md)
   4. Learn flask [under Construction]
   5. [Diable Swap for long time SD card](https://www.paulcourt.co.uk/article/pi-swap)
   6. [Way to run a program on raspberry pi startup](https://www.dexterindustries.com/howto/run-a-program-on-your-raspberry-pi-at-startup/)
   7. [Free FontAwesome](https://www.youtube.com/watch?v=cpTHtDbN-Z4&ab_channel=JetProduction)
   8. [Off low voltage warning in raspberry pi](https://scribles.net/lightning-bolt-under-voltage-warning-on-raspberry-pi/)
   9. [Disable Chrome auto update](https://arcanesciencelab.wordpress.com/2020/04/11/disable-chromium-update-dialog-on-raspbian-buster/)
   10. [PC to mobile view mediaquery](https://www.youtube.com/watch?v=fA1NW-T1QXc&ab_channel=QuentinWattTutorials)
   11. [Use Raspberry pi as wifi HOTspot](https://www.youtube.com/watch?v=XgcDipALFOc&ab_channel=AmineTech)
  
  ## Other thing that i learn when do this project!!
    1. Http Post to local or web server 
    2. Handle a server 
    3. why use ajax post in case of websocket
    4. How to initiate a database in flask
    5. How to use threading, multiprocessing, subprocess
    6. use of glob,shutil,os for file moving
    7. How to run raspberry pi 3 or all headless.
    8. Object detection
    9. Big rectangle Detection
    10. Read data from image using Color segmantation.
    11. Read data from image using pixel based segmentation
    12. Esp32 + cam + tft_espi
    13. Show image to display from esp32 camera to tft_espi display and send it to server at a time
    14. How to flash or reset esp32 using cmd.
    15. Database query from cmd 
    
    
  ## Error I get
    1. Errno 32
    2. Errno 10053
    3. Sometimes Client disconnect happens in Socket.io
    
  
# Data read Issue in image
    1. Here we read data for a single display image that means the image which i used to read data must be fixed. If the image style is change , demo.py can't read the image properly and return data as None , None
    2. For initiate tesseract OCR , the time that we need are -- 
        i) for rpi 3B 2 sec
        ii) In windows .2 sec sometimes 0.45sec
        iii) In Ubuntu it depend on processor, if use from dual boot it must be faster if your processor is faster. Again if use virtual box for ubuntu in windows it sometimes faster again some timese slower than windows OCR.
    3. We can't crop image to two part for reading data. Because in this case we need to run tesseract-OCR twice .So it takes more time that is twice. if 2 sec it would be 4 sec.
    4. Because data read from image is color based, it depend on images color. If color is accurate than mask available. else it mask would be white and no data can shown.
    5.

# Esp32 issue
    1. Using HTTP post method we send image from esp32-cam to rpi server. Here we get an issue that is image sending issue. When we send image from esp32 to rpi it does n't sent frequently that means sending time is not same .. actually image size is not change so sending time must differ. But here we get the is between ** 200ms to 6 ** sec for per image. Some times it frequenty send image at between **500ms-600ms**.  Here we send image which is UXGA and image size is **90kb-110kb**
    2. Image send from different size
    
   |  frame     | resolution  | size(kb)   |
   | ---------- | ----------  | ---------- |
   |  UXGA      | 1600 x 1200 | 90-110     |
   |  XGA       | 1280 x 1024 | 60-70      |
   |  SVGA      | 800 x 600   | 40-50      |


# Precautions
    1. After rebooting the server must need to reload the web page 
    2. sometimes Data read stack At this point you need to remove all the data(image) from the **imageForData** folder. Then need to reboot the server and After that reload the webpage again.
    3. Don't open more webpage.
    4. Image send from esp32 cam to server per 2sec. 
    5. Sometimes image get and show(actually callback) does  at the same time .. this will create an bug **errno 32 Broken Pipe**  .. but after sometime like 10 to 15 sec it will disappear (if image get fluently)

# Why need ajax request in case of web sockets?
When pass data from python code to html webpage , sometime my data passing get blocked. Then I got another way to pass data that is ajax request.
1. For many developers, AJAX is easier to code, especially when it comes to coding and designing the backend.
The AJAX API was practically designed for REST API calls and it's a great fit.

REST calls and uploads using AJAX are significantly easier to code, both on the client and the backend.

As data payload increases, Websocket connections might get blocked unless message fragmentation / multiplexing logic is coded.

If an upload is performed in a single Websocket send call, it could block a Websocket stream until the upload had finished. This will reduce performance, especially on slower clients.
### For sequrity
AJAX by nature would have the upper hand, since it's security is built in to the browser's code (which is sometimes questionable, but it's still there).

On the other hand, AJAX calls are more susceptible to "man in the middle" attacks, while Websockets security issues are usually bugs in the application code that introduced a security flaw (usually backend authentication logic is where you'll find these).


# errno 32 Broken pipe Error (solved: Get data through ajax get from another URL) or [Errno 10053] An established connection was aborted by the software in your host machine (solved: Get data through ajax get from another URL)

```
Traceback (most recent call last):
  File "/usr/local/lib/python2.7/dist-packages/eventlet/wsgi.py", line 598, in handle_one_response
    write(b''.join(towrite))
  File "/usr/local/lib/python2.7/dist-packages/eventlet/wsgi.py", line 538, in write
    wfile.flush()
  File "/usr/lib/python2.7/socket.py", line 307, in flush
    self._sock.sendall(view[write_offset:write_offset+buffer_size])
  File "/usr/local/lib/python2.7/dist-packages/eventlet/greenio/base.py", line 405, in sendall
    tail += self.send(data[tail:], flags)
  File "/usr/local/lib/python2.7/dist-packages/eventlet/greenio/base.py", line 396, in send
    return self._send_loop(self.fd.send, data, flags)
  File "/usr/local/lib/python2.7/dist-packages/eventlet/greenio/base.py", line 383, in _send_loop
    return send_method(data, *args)
error: [Errno 32] Broken pipe


```
# Most Important Problem
## [Flask route called twice](https://www.xspdf.com/resolution/51868169.html#:~:text=Flask%20route%20called%20twice&text=When%20building%20a%20Flask%20service,in%20development%20(debug)%20mode.)
One of the most most most most most most important problem

Why the GET request in flask is called twice?, So the reason why my request was getting fired twice was because of some extension installed in chrome. I removed a couple of my extensions  One of the possible reason why the Flask app run itself twice is a configuration of WEB_CONCURRENCY setting on Heroku. To set into one, you can write in console heroku config:set WEB_CONCURRENCY=1 share | improve this answer | follow |

Every route running twice · Issue #172 · hack4impact/flask-base , I'm pretty new to this project but I'd be surprised if every route is being called twice. This is likely a logging issue. To validate this, you could try a  Closed last year. When building a Flask service in Python and setting the debug mode on, the Flask service will initialise twice. When the initialisation loads caches and the like, this can take a while. Having to do this twice is annoying when in development (debug) mode. When debug is off, the Flask service only initialises once.

App seems to run twice, with debug OFF : flask, Hi everybody, I'm a novice to python, flask and web development in general, and then every time that route is run, it increments the value in the database by 1. but, I am not able to figure out how to make the call using flask app python. Flask Tutorial: Routes. Modern web apps use a technique named routing. This helps the user remember the URLs. For instance, instead of having /booking.php they see /booking/.


# Is swap memory enable or disable

Disabling swap file, will speed up system response time.
If you're running headless, it's recommended.
If you're running a GUI, it's recommended to do this only if you're having 512MB or more of RAM installed; as 256MB of RAM would be nearly 75% used by the GUI and system; leaving very little for programs.

On the Pi Zero W, with 512MB of RAM, and no Swap, I'm not able to browse on websites anymore, because it's lacking RAM.
But I can do anything else.
In fact, just Raspbian full desktop with some programs installed, idling has about 223MB free.
If you're not running any graphical applications from terminal, and you're running 256 or less MB of RAM, you take some of the VRAM.
By default 32<72MB is used for shared VRAM.
Since I'm not watching movies, I've set mine to 24MB (with GUI). Without GUI, you can go as low as 16MB, saving you between 16-56MB of RAM.
For more arguement [visit](https://www.raspberrypi.org/forums/viewtopic.php?t=244130#:~:text=If%20your%20system%20needs%20to,mean%20it%20is%20being%20used.)


# Change static IP of raspberry pi 

goto 

sudo nano /etc/dhcocd.conf

then write there:

```

interface wlan0 (if ethernet write eth0 (chcek it from ipconfig))
static ip_address=192.168.120
static routers=192.168.0.1 (Default GAteway)
static domain_name_Server=8.8.8.8 8.8.4.4

```


# kiosk.sh

```


```


# kiosk.sh

```
#!/bin/bash
xset s noblank
xset s off
xset -dpms

unclutter -idle 0.5 -root &

sed -i 's/"exited_cleanly":false/"exited_cleanly":true/' /home/pi/.config/chromium/Default/Preferences
sed -i 's/"exit_type":"Crashed"/"exit_type":"Normal"/' /home/pi/.config/chromium/Default/Preferences

/usr/bin/chromium-browser --noerrdialogs --disable-infobars --kiosk http://192.168.0.109:5000/image &

while true; do
      sleep 15
done
```

# kiosk.service

```

[Unit]
Description=Chromium Kiosk
Wants=graphical.target
After=graphical.target

[Service]
Environment=DISPLAY=:0.0
Environment=XAUTHORITY=/home/pi/.Xauthority
Type=simple
ExecStart=/bin/bash /home/pi/kiosk.sh
Requires=icu.service
Restart=on-abort
User=pi
Group=pi

[Install]
WantedBy=graphical.target


```

# ICU.service

```
[Unit]
Description=My Sample Service
After=multi-user.target

[Service]
Type=idle
ExecStart=/usr/bin/python /home/pi/sampleApp/sample_app.py

[Install]
WantedBy=multi-user.target

```

