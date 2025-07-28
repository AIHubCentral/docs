---
icon: chevron-right
order: 5000
---
 
``Last update: July 28, 2025``

***

###### ‎
:::content-center
## Introduction :icon-book:
:::

- This is a guide on how to use most of the TTS' listed in the TTS Tools section in realtime.

***
:::content-center
## Installation 
:::


***
:::content-center
### TTS Program
:::

Choose any TTS in our <u>[TTS Tools](https://docs.aihub.gg/tts-tools/)</u>.


***
:::content-center
### Virtual Audio Cable
:::

- A VAC (Virtual Audio Cable) makes a fake audio device, used to re-route the audio of different programs.
- In Wokada Deiteris Fork context, it's used to get the output of Wokada Deiteris Fork as the input in other programs such as Discord.

!!! For Windows
Download this: <u>[VAC Lite (Virtual-Audio-Cable by Muzychenko)](https://software.muzychenko.net/freeware/vac470lite.zip)</u>.
(Be sure to not use any toher vac like VB Audio Cable.)
!!!

- Run `setup64`, not 64a, after extracting the zip to a new folder

- After installing the VAC Lite, it changes your default audio system. Click **Yes** when it asks you to open the audio device settings (or press WIN+R, type "mmsys.cpl" if you closed it already), and change your **Recording** and **Playback** devices back to your usual devices. Same for communications device aswell (right click -> set as default communication device)

!!! For Mac
Download either: 
<u>[Blackhole Virtual Audio Cable](https://existential.audio/blackhole)</u>
or
<u>[VB-Audio](https://vb-audio.com/Cable)</u>
!!!

!!! For Linux
For Debian / Ubuntu-based Systems (Ubuntu, Mint, Pop!_OS), run in the terminal:
```bash
sudo apt-get update && sudo apt-get install -y portaudio19-dev
```


For Fedora / RHEL-based Systems (CentOS, Rocky Linux), run in the terminal:
```bash
sudo yum install -y portaudio
```
!!!


***
:::content-center
## Setup
:::

1. After installing a VAC you need to:


!!! For Windows:
Press WIN+R and type `mmsys.cpl` and change the default audio devices back to your headphones and microphone, make sure you do this for default and communication default.
!!!

!!! For Mac:
 Press Command + Spacebar and type `Sound` and set the default audio device back to your headphones and microphone , make sure you do this for default and communication default.
!!!

2. After that:
!!! For Windows:
Press WIN+CTRL+V and select the VAC as the output device.
!!!

!!! For Mac:
Hold down the option key on your keyboard then click the sound icon in the upper right corner of the menu bar and then a dropdown menu will appear which allows you to select the VAC as the output device.
!!!!


3. Audio Setup in Games:
- In Discord go to Settings then Voice & Video and select your VAC for your input. 
- It's the same thing for game too, go into its audio settings and set its input to the VAC. 


***
###### ‎   ‎
:::content-center
#### `You have reached the end.`

[!badge variant="info" size="xl" corners="pill" icon="paper-airplane" iconAlign="right" text="Report Issues"](https://docs.aihub.gg/contributions/)
:::