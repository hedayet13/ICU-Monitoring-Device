# Covid-19 ICU Monitoring

This project focuses on developing a centralized ICU monitoring system using individual ESP-32 cams to capture live images of the ICU monitors and send them to a central server at regular intervals (1 second or less). These images are displayed in real-time on a monitor in the doctors’ and nurses’ room to show patient status.

## Background

Chittagong General Hospital didn’t have an ICU to start with. With the emergence of Covid-19, a 10-bed COVID ICU was set up in a couple of weeks. However, the ICU monitors (Nihon kohden BSM-3562) didn’t come with central monitoring software, and the licensing fee of ~17,000 USD was way over their budget. This feature was essential as they were trying to reduce virus exposure for hospital personnel who otherwise had to frequently enter the ICU to record the patients’ status. The lack of PPE and other protective systems only made the situation worse.

When they reached out to us, we were excited to help. The first obvious way would be to look into the communication protocols and data packets. Unfortunately, we didn’t have access to such monitors, and it was not possible for us to enter the COVID ward to work with them. Additionally, we weren’t sure about the encryption used and if it would be possible to find a workaround in a short time. Instead, we decided to develop a camera system that we could work on safely in our “non-COVID” office space.

## Requirements

- Data from all monitors should be available on a central monitor in the doctor's room.
- The same data should be accessible from any mobile phone within the hospital premises.
- The same data should be available to multiple doctors outside the hospital premises.
- Any indication of network disruption should be obvious so that doctors don’t misjudge from old data.
- An alarm should be generated whenever any parameter (SpO2 or HR) goes below a critical number.
- The system should be easy to install and adjust by the ICU doctors and nurses.

## Implementation in the ICU

### Device in Front of Bedside Display
We set the device in front of the display in an accessible manner, allowing ICU personnel to easily move it according to their needs. This setup ensures that the live feed from the monitors is captured clearly and sent to the central server without obstruction.


<img src="/media/implementation/demo1.jpg" alt="Device in Front of Bedside Display" height="350"/><img src="/media/implementation/demo2.jpg" alt="Device in Front of Bedside Display" height="350"/>



### A Glimpse of ICU with Setup
Here’s an image of the fully setup ICU with our devices. If you zoom in, you can see that every display is equipped with a device connected wirelessly to the camera. This setup allowed us to monitor all ICU patients from a central location, reducing the need for frequent physical checks.


<img src="/media/implementation/mainFloor2.jpg" alt="ICU Setup" width="800"/>

### Behind the Scenes
A glimpse of my working area shows just how hodgepodge it was! The behind-the-scenes effort involved in creating a functional and reliable monitoring system was immense, but seeing it all come together was incredibly rewarding.


<img src="/media/implementation/office.jpg" alt="Behind the Scenes" width="800"/>

### Floor Plan
To set up, I sketched out our entire implementation procedure. This detailed plan includes where the router would be placed, where the displays would be set up, and how the cables would be managed. Proper planning was crucial to ensure smooth and efficient installation.

<img src="/media/implementation/floorPlan.jpg" alt="Floor Plan" width="600"/>

## ESP-32 Cam
This image shows our testing setup, where we placed a device in front of our PC display. Due to COVID restrictions, we did not have access to bedside monitors, so we simulated the environment using available resources. This allowed us to fine-tune the system before deploying it in the ICU.


<img src="/media/image2.jpg" alt="ESP-32 Cam" width="400"/>
<img src="/media/esp.jpg" alt="ESP-32 Cam" width="600"/>

## Data Extraction
We used OpenCV for extracting data from device images sent to the server. First, we reorganized the images and then sent them to another Python script for data extraction. We followed two image-based algorithms: one pixel-based and another color-based. Finally, we extracted the data using pytesseractOCR. This combination of techniques ensured accurate and reliable data extraction.


<img src="/media/imageProcessing.jpg" alt="Data Extraction" width="600"/>

## 3D Casing
These cases were designed using Solidworks3D. The custom-designed casings provided protection and proper mounting for the ESP-32 cams, ensuring they stayed in place and functioned correctly in the ICU environment.


<img src="/media/3d/camera_Case2.JPG" alt="3D Casing" width="250"/><img src="/media/3d/clamp.JPG" alt="3D Clamp" width="250"/><img src="/media/3d/clamp2.JPG" alt="3D Clamp" width="250"/>

## Web View
The web interface allowed doctors and nurses to monitor the ICU patients in real-time from a central location. This view was accessible from within the hospital premises and ensured that patient data was available whenever needed.


<img src="/media/webView.jpg" alt="Web View" width="600"/>

## Mobile App
This mobile app was developed using Flutter. I used the `url_launcher` package to run the app locally. The app displays graphs of patients' heart rates and oxygen saturation, making it easy for doctors to monitor patient vitals on the go. The mobile interface ensured that doctors could access critical patient data even when they were not in the ICU.


<img src="/media/android/img1.jpg" alt="Mobile App" width="250"/><img src="/media/android/img2.jpg" alt="Mobile App" width="250"/><img src="/media/android/img3.jpg" alt="Mobile App" width="250"/>
