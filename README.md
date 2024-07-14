# Covid-19 ICU Monitoring
This project focuses on developing a centralized ICU monitoring system using individual ESP-32 cams to capture live images of the ICU monitors and send them to a central server at regular intervals (1 second or less). These images are displayed in real-time on a monitor in the doctors’ and nurses’ room to show patient status.

'Add youtube Videos'

Chittagong General Hospital didn’t have an ICU to start with. With the emergence of Covid19, a 10 beds COVID ICU was set up in a couple of weeks. However the ICU monitors (Nihon kohden BSM-3562) didn’t come with a central monitoring software and the licensing fee of ~17,000 USD was way over their budget. This feature was essential as they were trying to reduce virus exposure of the hospital personnels who otherwise had to frequently get inside the ICU to record the patients’ status. Lack of PPE and other protective systems only made the situation worse. So when they reached out to us, we were excited to look into it. The first obvious way would be to look into the communication protocols and data packets. Unfortunately we didn’t have any such monitor at our disposal and it was not possible for us to go into the covid ward to work with that. On top of that we weren’t sure what kind of encryption they were using and if it would be possible to find a way around within a short time. Instead we decided to develop a camera system that we can easily work in the safety of our ”non covid” office space.

Few requirements are:
Data from all monitors should be available in a central monitor at the doctor's room.
Same data should be accessed from any mobile phone within the hospital premises.
Same data should be available to multiple doctors outside the hospital's premises.
Any indication of network disruption should be obvious so that doctors don’t misjudge from old data.
An alarm should be generated whenever any parameter (SpO2 or HR) goes below a critical number.
This should be easy to install and to adjust by the ICU doctors and nurses.

## Implemented on ICU

### Device in front of bed side display
<img src="/media/implementation.jpg" alt="Retinal Image of a DR Patient" width="400"/>

### Floor Plan

<img src="/media/floorPlan.jpg" alt="Retinal Image of a DR Patient" width="400"/>

### A Glimpse of ICU with setup

<img src="/media/implementation.jpg" alt="Retinal Image of a DR Patient" width="400"/>

### Behind the scene
<img src="/media/implementation.jpg" alt="Retinal Image of a DR Patient" width="400"/>


## ESP-32 cam

<img src="/media/esp.jpg" alt="Retinal Image of a DR Patient" width="400"/>

## Date extraction

<img src="/media/fundusImages.jpg" alt="Retinal Image of a DR Patient" width="400"/>

## 3D casing

<img src="/media/case1.jpg" alt="Retinal Image of a DR Patient" width="400"/>
<img src="/media/case2.jpg" alt="Retinal Image of a DR Patient" width="400"/>

## Webview

<img src="/media/fundusImages.jpg" alt="Retinal Image of a DR Patient" width="400"/>

## Mobile app
<img src="/media/fundusImages.jpg" alt="Retinal Image of a DR Patient" width="400"/>
