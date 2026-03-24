***
## Virtual Audio Cable

#### A Virtual Audio Cable (VAC) is required to use the realtime voice changer on Discord & Games.

- A VAC makes a virtual audio device, used to re-route audio between programs.

- In this context, it allows you to set the AI Converted Voice Output as your input device in programs like Discord.

!!! For Windows
Download [VAC Lite (Virtual-Audio-Cable by Muzychenko)](https://software.muzychenko.net/freeware/vac470lite.zip). 

- Run `setup64` if you are on a standard PC (Intel/AMD).

- Run `setup64a` if you are on an ARM-based Windows Laptop (e.g., Snapdragon CPUs).

- After installation, it may change your default audio system. Click **Yes** when asked to open audio settings (or press WIN+R and type "mmsys.cpl"). Change your **Recording** and **Playback** devices back to your preferred default devices, and ensure they are also set as "Default Communication Devices."
!!!

!!! For Mac
Download either: 
[Blackhole Virtual Audio Cable](https://existential.audio/blackhole) or [VB-Audio](https://vb-audio.com/Cable)
!!!

!!! For Linux
- **Debian/Ubuntu:** `sudo apt-get update && sudo apt-get install -y portaudio19-dev`
- **Fedora/RHEL:** `sudo yum install -y portaudio`
- **Arch:** `sudo pacman -Syu portaudio`
!!!