*`Written by Julia & Alex`*       
``Last update: Jan 27, 2024``   

***
###### ‎     
:::content-center
## Introduction
:::
Here we'll go over the essentials regarding audio quality. The best audio format for RVC, how to determine your dataset's sample rate, and some extra info.     

The first part is a **very important** read, it goes over a mistake many RVC users make.   

We also left some simple and understandable analogies, so you can fully get a grasp of the essentials regarding audio.
***
###### ‎   
:::content-center
## Lossy Formats
##### *(avoid these for RVC)*
:::

- Common lossy formats are **MP3**, OGG, OPUS, M4A, etc.

- These compress (lose) the original quality.       
They're built to be faster for transmission & be space-efficient. 

- By getting rid of some data (in this case, quality), they achieve a smaller file size.       
- Platforms like as YouTube, Spotify, or YouTube Music don't offer lossless streaming.      
(even if you use a cracked Spotify "Premium", you're still limited 160kbps [<u>bitrate</u>](https://aihubdocs.github.io/en/rvc-resources/audio-formats--sample-rate/#bitrate--bit-depth-extra))        
‎   
==- *<u>Example</u>* 👈
{.list-icon}
- :icon-triangle-right: You record a video with your phone & send it to a friend through social media.     
- :icon-triangle-right: The video ends up losing quality, looking more "pixelated" & with a worse audio, compared to the original.        
- :icon-triangle-right: That's because the app compressed the quality so it transmits faster.     
- :icon-triangle-right: The sent video is now a video with lossy quality.
===
***
###### ‎ 
:::content-center
## Lossless Formats
#### *(the right ones for RVC)*   
:::
- The main ones are WAV & FLAC. These don't compress the original quality.

- **FLAC** uses an algorithm that compresses the data without losing quality.       
We recommend it over WAV since it's space-efficient.        
- **WAV** doesn't do any kind of compression. It's purely the full original data.       
Therefore it has a much bigger file size.

- They're recommended for RVC/vocal isolation apps, as the more quality an audio has, the more accurate results they'll give.

- Platforms like Qobuz, Deezer, Tidal, Apple Music, or Amazon Music do offer lossless streaming.

!!! <u>NOTES:</u>
-Both formats give the same results & don't have an audible difference between eachother.      
-Converting a lossy audio to a lossless one won't bring back the lost quality.
!!!
***
###### ‎  
:::content-center
## Sample Rate
:::
- Sample rate is a unit that determines the total amount of samples (data) that can fit within one second of an audio.     

- This higher the sample rate, the more information it stores, therefore the higher the quality.

- They are measured in kilohertz.    

- The most common sample rates are **32kHz, 40kHz, 44.1kHz, & 48kHz**.      
‎ 
==- <u>*Simple Analogy*</u> 👈
Let's compare it with frames of a video.     

:icon-triangle-right: A key component of a video are its FPS (frames per second).         
:icon-triangle-right: FPS measure how many frames (images) exist over the course of a second.       
:icon-triangle-right: Higher FPS entail a smoother, visually appealing video.       
:icon-triangle-right: Think of sample rate as how many frames (in this case, audio data) fit in each second, all over the course of a video (an audio, in this case). 
===
###### ‎ 
### How to Determine Sample Rate
While training in RVC, you'll have to determine the model's target sample rate, according to your dataset's sample rate.        
Inputting one that doesn't match with the dataset will screw the final quality a bit.      
‎       

To know its sample rate, we'll use **Ilaria Audio Analyzer**.        
A tool hosted in [<u>Hugging Face</u>](https://aihubdocs.github.io/en/other/glossary/#hugging-face) for determining different characteristics of an audio file.

- **<u>Step 1:</u>** Enter the HF space [<u>here</u>](https://huggingface.co/spaces/TheStinger/Ilaria_Audio_Analyzer).        

- **<u>Step 2:</u>** Click the ``🎵 Audio`` box to input your audio.      
Or just simply drag the file into it.       

    <img src="../audioformats-img/1.png" alt="image" width="500" height="auto">‎   
‎  
- **<u>Step 3:</u>** Click `Create Spectogram and Get Info`.      
In ``Samples per second`` you'll see the audio's full sample rate.        

    <img src="../audioformats-img/2.png" alt="image" width="400" height="auto">   
      
==- :icon-alert: What to do if the frequencies <u> don't reach the top</u> of the spectogram.
‎       
See at which number peaks & multiply it by **2**.        
That would be its actual sample rate.

#### <u>Example:</u>
###### ‎
<img src="../audioformats-img/3.png" alt="image" width="480" height="auto">‎    
   
>- Here it reached 20 kHz. **Doubling** it gives 40kHz.        
>- Therefore in this case the ideal target sample rate is ``40k`` 
===
***
###### ‎
:::content-center
## Bitrate & Bit Depth (Extra)
:::
###### ‎
#### <u>BITRATE</u>:
- The amount of data processed per unit of time. Usually measured in kilobits per second (KBPS).
- Higher bitrate equals a higher quality.
- You can think of it as video resolution (240, 480p, 1080p, etc.).     
‎   
#### <u>BIT DEPTH</u>:
- Defines the dynamic range of each sample.
- This determines the difference between the quietest & loudest sound of an audio.        
- Basically, higher bit depths represent more accurately the loudness of an audio.        

Here's an example of how different bit depths sound like:
https://youtu.be/ubCMI3Jq6e4?t=40
***
:::content-right
||| *Did I miss anything?*        
Send any feedback [<u>here</u>](https://forms.gle/5i6hTJRVkXRohvVF9) 👈
|||
:::
