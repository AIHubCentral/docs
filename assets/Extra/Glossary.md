---
icon: chevron-right
order: 1000
---

``Last update: August 9, 2025``
***
:::content-center

#### *List of smaller keywords.* 
:::
‎
:::
### :icon-chevron-down:Backing vocals
- Vocal lines that contribute to the sound of the lead vocals in a song.      


***
### :icon-chevron-down:Bit depth
- In the field of digital audio, it defines the dynamic range of each sample.

- This determines the difference between the quietest & loudest sound. 

- Basically, higher bit depths represent more accurately the loudness of an audio.     


***
### :icon-chevron-down:Bitrate
- The amount of data processed per certain unit of time, usually in kilobits per second (KBPS).

- Higher bitrate equals a higher quality.

- You can think of it as video resolution (240, 480, 1080, etc.).     


***
### :icon-chevron-down:DAW
- It stands for **Digital Audio Workstation**, and it's any software used for making and mixing music.    

- For **basic** audio editing, we recommend <u>[Audacity</u>](https://www.audacityteam.org/).     

- For **professional** mixing, <u>[FL Studio</u>](https://www.image-line.com/fl-studio-download/).


***
### :icon-chevron-down:Checkpoints

- In RVC, these are files of a model that generate over the course of training, that can be very useful.        

- The rate at which they're saved is determined by the **save frequency** value (or save rate or similar names). **For newbies, it's recommended use a value of `15`.**      

- **They are divided by two types:**  
    - <u>**Weights:**</u>    
        - These are actual models.
        - They're organized with this format: **modelname_epoch_step.pth**
        - Example: `Tyler_e60_s120.pth`    
    - <u>**G and D:**</u>
        - Named **G_** and **D_**, followed by the step number & **.pth**.
        - Example: `G_70.pth` and `D_70.pth` 
        - These allow you to resume training, if G and D's numbers match.


***
### :icon-chevron-down:GPU
- It stands for Graphics Processing Unit. It's designed to rapidly manipulate and alter memory to accelerate creation of images.
- In AI training, is used for quick parallel independent computations, which increases the speed substantially.     
- Basically the speed at which RVC/UVR will work will depend on how good your GPU is.       


***
### :icon-chevron-down:Local running
- Running locally is a process that involves running apps in your own machine, using its resources.
- Done by users with a powerful <u>[GPU](https://docs.aihub.gg/extra/glossary/#gpu)</u>.
- The opposite of <u>[cloud-based](https://docs.aihub.gg/extra/glossary/#cloud-based)</u>.


***
### :icon-chevron-down:Cloud-based
- Any software or application that's stored, managed, and available through the provider's virtual servers, and is accessed through a web browser.
- Used by users with a weak <u>[GPU](https://docs.aihub.gg/extra/glossary/#gpu)</u>, which can't do <u>[local running</u>](https://docs.aihub.gg/extra/glossary/#local-running).
- The opposite of <u>[local running</u>](https://docs.aihub.gg/extra/glossary/#local-running).       


***
### :icon-chevron-down:CUDA
- A technology developed by NVIDIA, that uses the power of graphics cards to perform calculations that require great processing power.
- It's especially useful for AI tools, such as RVC and UVR, which greatly optimizes the process.
- CUDA is downloaded automatically as a part of the NVIDIA driver.
- Which Nvidia driver you use might affect performance, Studio Drivers can help AI, but this is mostly for other types of AIs such as Stable Diffusion, rather than RVC.    


***
### :icon-chevron-down:Fine-tuning
- Further improving an AI model, training it with a another dataset.


***
### :icon-chevron-down:Fork
- It's a copy of a main GitHub project. It aims to make a different version of the project with improvements, changes & new features.       


***
### :icon-chevron-down:Gradio
- Gradio is an open-source Python packag that makes it easy for developers to create user-friendly web interfaces for machine learning models and other applications, such as RVC.
  
- It deploys the program on a Local URL, which is the one running locally on the machine, and a Public Share Link, which is a tunnel that exposes the Local URL. The Public Share Link is used, for example, in Google Colabs, powered by their Share API. Sometimes, the Share API goes down, you can check its <u>[status](https://status.gradio.app/)</u>.


Of course. Here is a standalone section about Jupyter Notebooks, written in the same glossary style.

***
### :icon-chevron-down:Jupyter Notebook
- An interactive, web-based document that lets you combine runnable code, explanatory text, and media (like images and charts) into a single file.
- It's organized into individual **cells**. Code cells can be run one by one to perform tasks, while text cells (using Markdown) are used for documentation and instructions.
- This cell-based format is perfect for creating step-by-step guides and running AI applications, which is why it's the standard interface for platforms like **Google Colab**, **Kaggle**, and **Lightning.AI**.
- Jupyter Notebook files are saved with the `.ipynb` file extension.


***
### :icon-chevron-down:Google Colab
- Google Colaboratory, also known as Google Colab or just Colab, is a <u>[cloud-based](https://docs.aihub.gg/extra/glossary/#cloud-based)</u> platform by Google to run <u>[Jupyter Notebooks](https://docs.aihub.gg/extra/glossary/#jupyter-notebook)</u>.
- It requires a Google Account.
- It doesn't Web User Interfaces in the Free Tier, meaning it needs encrypted <u>[Jupyter Notebooks](https://docs.aihub.gg/extra/glossary/#jupyter-notebook)</u>) and has ban risk like Kaggle.
- It's free tier offers **max 4 hours a day of T4 GPU**, but it's random. Once you exhaust it, you'll have to wait 12 - 24 hours or [get a paid tier](https://colab.research.google.com/signup).
- Learn how to bypass their limitations <u>[here](https://docs.google.com/document/d/1Pr-AZndodmWgsbOeuHQU4IrgbatFgYc1ChOq_ZAf_5s/edit?usp=sharing)</u>.


***
### :icon-chevron-down:Kaggle
- A <u>[cloud-based](https://docs.aihub.gg/extra/glossary/#cloud-based)</u> is a <u>[cloud-based](https://docs.aihub.gg/extra/glossary/#cloud-based)</u> platform by Google to run <u>[Jupyter Notebooks](https://docs.aihub.gg/extra/glossary/#jupyter-notebook)</u>.
- It's focused on data science and machine learning.
- It doesn't Web User Interfaces, meaning it needs encrypted <u>[Jupyter Notebooks](https://docs.aihub.gg/extra/glossary/#jupyter-notebook)</u>) and has ban risk like Google Colab.
- If you have trouble verifying your phone number, [Contact Kaggle](https://www.kaggle.com/contact).
- It requires a phone number verification to access the internet (which is needed to run most <u>[Jupyter Notebooks](https://docs.aihub.gg/extra/glossary/#jupyter-notebook)</u>).
- The free tier provides a limited quota of **30 free GPU hours per week** of either T4x2 (2 T4 GPUs at once) or P100, which you can swap at any time, using either will consume the quota, which resets weekly.


***
### :icon-chevron-down:Lightning.AI
- A <u>[cloud-based](https://docs.aihub.gg/extra/glossary/#cloud-based)</u> platform designed for developing and running AI applications in persistent environments called "Studios.", and one of the options is via (but not limited to) running <u>[Jupyter Notebooks](https://docs.aihub.gg/extra/glossary/#jupyter-notebook)</u>.
- It requires a phone number verification to full access.
- It features persistent storage, meaning your files are saved between sessions.
- It allows Web User Interfaces on the Free tier, avoiding any encryption or ban risk unlike Google Colab or Kaggle.
- Studios Auto Sleep (stop running) after 10 minutes of inactivity (such as closing the site or not running anything in the background) in the Free tier.
- Users inactive for a 6 month period and do not have an active paid subscription will be scheduled for deletion. Users will be notified 30 days before the scheduled deletion, with several reminders sent during this period.
- Free tier users get free 15 monthly credits that can be used on CPUs or GPUs. Be sure to monitor your usage and stop the Studio when not in use.
- "free studios" are considerated the free *CPU* studios, which have a 4 hour limit session, after that they will become paid CPU studios using your credits unless you restart them. Unlike GPU Studios which directly use credits.
- In Free tier you can change GPU/CPUs at any time, but if you used all free 15 credits **monthly** only on a specific computing, you'd have:     
    - **GPUs (Powerful, Recommended):**   
        - **T4** (16GB VRAM): **75 hours**
        - **L4** (24GB VRAM): **31 hours**
        - **L40S** (48GB VRAM): **15 hours**
    - **CPUs:**
        - **Default (CPU)** (4 cores, 16GB RAM): **unlimited** (first 4 hours are free and you'd need to restart, or keep paying, and if you pay you'd have **45 hours** monthly)
        - **Large (CPU)**: (8 cores, 32GB RAM): **29 hours**
        - **X-Large (CPU)**: (16 cores, 64GB RAM): **15 hours**
- You can check the [pricing](https://lightning.ai/pricing) for more info.


***
### :icon-chevron-down:Inference
- In the context of AI, it's using an AI model to complete any task. 

- For this, using the GPU is more convenient as it's faster. Though normally you can still use CPU, which takes longer.

- For example, in RVC is when a voice model is used to transform an audio, to make it sound like the model.       


***
### :icon-chevron-down:Lossless Formats
- Audio formats that **don't compress** (lose) the original quality.        
- They're recommended for RVC, as the more quality an audio has, the more accurate results they'll offer.       
- The main ones are **WAV & FLAC**:     
    - **FLAC:**   
        - Its algorithm compresses the data without losing quality. 
        - It's recommended over WAV since it's space-efficient.          
    - **WAV:**
        - Doesn't do any kind of compression. It's purely the original data.
        - Therefore it has a much bigger file size.
        - It's more accurate to describe it as an *uncompressed* format
        
!!!
Both formats give the same results & don't have an audible difference.      
Converting a lossy audio to a lossless one won't restore the lost quality.
!!!


***
### :icon-chevron-down:Lossy Formats

- Audio formats that **compress** (lose) the original quality. They're built to be space-efficient.

- So by getting rid of some data (in this case, quality), they achieve a smaller file size.       

- Common lossy formats are **MP3**, OGG, OPUS, M4A, etc.


***
### :icon-chevron-down:Localtunnel

- Localtunnel is a tunnel made to expose a local url (like http://localhost:3000).

- It's used in Google Colabs to **expose the Local URL** so that users on Cloud can access the program.

***
### :icon-chevron-down:Model training
- In the field of AI, is the process where an AI model is fed with its dataset & learns from it.


***
### :icon-chevron-down:Specs
- It refers to a computer's specifications. Hardware like <u>[GPU</u>](https://docs.aihub.gg/extra/glossary/#gpu), CPU, RAM, etc.     

- The performance of the hardware of a computer directly correlates to the performance of all its software.


***
### :icon-chevron-down:0 Shot Training
- Doing <u>[inference](https://docs.aihub.gg/rvc/extra/glossary/#inference)</u> on an AI model without explicitly training on it. 

- It's faster but with less quality, and you won't be able to save the model.

- For example, in TTS you do inference by cloning a voice with an audio, a data it hasn't seen before.

- Different from making a dataset & doing the long training process, based on lots of criteria such as <u>[epochs](https://docs.aihub.gg/rvc/resources/epochs--tensorboard/)</u>. 

- In some cases you can do it on GPU, some in CPU.


***
### :icon-chevron-down:Optim
- It is a shorter way to say optimizer.

- A optimizer is an algorithm used to minimize the loss function during the training of neural networks. It helps adjust the model's weights and biases.

***
:::content-center
#### `You have reached the end.`

[!badge variant="info" size="xl" corners="pill" icon="paper-airplane" iconAlign="right" text="Report Issues"](https://docs.aihub.gg/contributions/)
:::
