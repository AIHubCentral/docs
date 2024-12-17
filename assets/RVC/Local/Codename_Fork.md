---
icon: chevron-right
order: 3000
---

``Last update: Dec 16, 2024``
***
###### ‎
:::content-center
## Introduction ‎ :icon-book:
:::

- The codename fork is a <u>[fork</u>](https://docs.ai-hub.wtf/essentials/whats-rvc/#forks) of Applio made by <u>[Codename](https://github.com/codename0og)</u>.

- This fork has more features compared to others and changes to increase quality.

- This guide will be only talking about the new features since everything else has been covered in the <u>[Applio guide](https://docs.ai-hub.wtf/rvc/local/applio/)</u>.

#### Pros & Cons :icon-tasklist:
==- ***Unfold***
!!! *The pros & cons are subjective to your necessities.*        
!!!

||| ✔️ **PROS** 
- All of the pros of Applio.                   
- Supports MRF HiFi-GAN
- Supports RefineGAN
- Has a Warmup Phase option
- Uses the Ranger2020 optimizer
- Avg running loss
- 44.1k Sample rate support
||| ❌ **CONS** 
- More complicated.     
- Doesn't have a precompiled version.      
||| 
===
***
###### ‎
:::content-center
## Downloading :icon-download:
:::
1. Go to the github repo <u>[here](https://github.com/codename0og/codename-rvc-fork-3)</u>. Then go to the top right and click the green code button and then copy the link under https. 
    ‎
    <img src="../codename-img/1.png" alt="image" width="300" height="auto"> 
    ‎
2. Then go into your C drive and create a folder (you can name it anything) and go into it and then type cmd into the bar at the top.

<img src="../codename-img/cmd.png" alt="image" width="300" height="auto"> 

3. Type `git clone https://github.com/codename0og/codename-rvc-fork-3.git` and hit enter.

4. Go into the codename fork folder and run the `INSTALLATION.bat` file then once it's done run `go-fork.bat`.
***
###### ‎
:::content-center
## New Features :icon-sliders:
:::
***
### 44.1k Sample Rate:
Under Training there is the option to use 44.1k as your trainng sample rate, however there are currently no pretrains for it.

<img src="../codename-img/sr.png" alt="image" width="550" height="auto"> 

***
### MRF HifiGAN & RefineGAN:
- In the training section you are given the option to choose your vocoder
    - HiFi-GAN: the default vocoder for RVC.
    - MRF HiFi-GAN: a version of HiFi-GAN with MRF instead of MPD and new loss functions. This has higher fidelity but **only** works with this fork and the MRF branch of Applio.
    - RefineGAN: an entirely new GAN which is in a very experimental phase, this is for for devs only.

<img src="../codename-img/voco.png" alt="image" width="500" height="auto"> 

***
### Warmup Phase:
In the training section there is an option to enable a warmup phase and a slider to choose how long it lasts.

<img src="../codename-img/warm.png" alt="image" width="1000" height="auto"> 

- The warmup phase is where the learning rate (lr) linearly increased for a certain amount of epochs, this can be used to prevent large destabilizing updates in the early stages of training.
    - There isn't much testing on what using a warmup in RVC does so expect varying results. 

***
### Avg Running Loss:
In the training section you can find the avg running loss settings.

<img src="../codename-img/avg.png" alt="image" width="1200" height="auto"> 

- The avg running loss averages the loss per X steps / mini-batches. This is a better indicator for per epoch performence.

***
### Ranger2020  Optimizer:
This fork uses the Ranger2020 optimizer (optim) as the default optim instead of the AdamW optim. The Ranger2020 optim is much more complex optim that combines multiple techniques from other optims to be able to provide a more stable and faster convergence then other optims. 

- The three key components are:
   - **RAdam:** An adaptive learning rate method that dynamically adjusts the learning rate based on the variance of the gradients.
   - **LookAhead:** A method that improves convergence by interpolating between the current weights and a set of "lookahead" weights.
   - **Gradient Centralization:** A technique that normalizes gradients to stabilize training and potentially improve generalization.

***
### Upcoming Features:
- More / different configurable optimizers.
- Adjustable hop length for RMVPE.
- Custom initial learning rate per Generator and Discriminator.
- Custom gradient norm value ( from the ui level )
- Ability to delay / headstart the Generator or Discriminator.
- More warmup options ( Cosine anneal and so on ).
- Toggleable mute files.
- And more...

***
###### ‎
:::content-center
#### `You have reached the end.`

[!badge variant="info" size="xl" corners="pill" icon="paper-airplane" iconAlign="right" text="Report Issues"](https://docs.ai-hub.wtf/contributions/)
:::