---
icon: chevron-right
order: 3000
---

``Last update: May 5, 2025``
***
###### ‎
:::content-center
## Introduction ‎ :icon-book:
:::

- The codename fork is a <u>[fork</u>](https://docs.aihub.gg/essentials/whats-rvc/#forks) of Applio made by <u>[Codename](https://github.com/codename0og)</u>.

- This fork has more features compared to others and changes to increase quality.

- This guide will be only talking about the new features since everything else has been covered in the <u>[Applio guide](https://docs.aihub.gg/rvc/local/applio/)</u>.

***
#### Are RVC Models Safe?

RVC Models are PyTorch Models, a Python library used for AI.
PyTorch uses serialization via Pythons' Pickle Module, converting the model to a file.
Since pickle can execute arbitrary code when loading a model, it could be theoretically used for malware, but this fork has a **built-in feature to prevent code execution along the model.**
Also, **HuggingFace has a <u>[Security Scanner](https://huggingface.co/docs/hub/security-pickle#hubs-security-scanner)</u>** which scans for any unsafe pickle exploits and uses also ClamAV for scanning dangerous files.
***

#### Pros & Cons :icon-tasklist:
==- ***Unfold***
!!! *The pros & cons are subjective to your necessities.*        
!!!

||| ✔️ **PROS** 
- All of the pros of Applio.                   
- Has a Warmup Phase option
- Multiple optimizer choices
- Avg running loss
- Mel similarity metric
- SoX resampler
- fcpe training
- L1 mel loss
||| ❌ **CONS** 
- More complicated features.     
||| 
===
***
###### ‎
:::content-center
## Downloading :icon-download:
:::
1. Go to the github repo <u>[here](https://github.com/codename0og/codename-rvc-fork-3)</u>. Then find the releases tab and click it. 

    ‎
    <img src="../codename-img/rel.png" alt="image" width="500" height="auto"> 
    ‎
2. Click on the zip file and download it. Then go into your C drive and extract it.

<img src="../codename-img/zip.png" alt="image" width="800" height="auto"> 


3. Go into the codename fork folder and run the `run-install.bat` file then once it's done run `go-fork.bat`.
***
###### ‎
:::content-center
## New Features :icon-sliders:
:::
***
### MRF HifiGAN & RefineGAN:
- In the training section you are given the option to choose your vocoder
    - HiFi-GAN: the default vocoder for RVC.
    - MRF HiFi-GAN: a version of HiFi-GAN with MRF instead of MPD and new loss functions. This has higher fidelity but **only** works with this fork and the latest version Applio.
    - RefineGAN: an entirely new GAN which is in a experimental phase. This only works with this fork and Applio.

<img src="../codename-img/voco.png" alt="image" width="500" height="auto"> 

***
### Warmup Phase:
In the training section there is an option to enable a warmup phase and a slider to choose how long it lasts. **Do not use this with Ranger21 or RAdam since they do this on their own.**

<img src="../codename-img/warm.png" alt="image" width="1000" height="auto"> 

- The warmup phase is where the learning rate (lr) linearly increased for a certain amount of epochs, this can be used to prevent large destabilizing updates in the early stages of training.
    - There isn't much testing on what using a warmup in RVC does so expect varying results. 

***
### Avg Running Loss:
While training it logs the average loss per epoch as the standard loss and rolling average loss over 5 epochs to evaluate general trends and the model's performance over time. 

***
### Multiple Optimizers:
This fork gives you the option to choose between three optimizers. 

- AdamW
- RAdam
- Ranger21

<img src="../codename-img/optimizer.png" alt="image" width="400" height="auto">


***
### Custom LR for gen and disc:
In the training section under advanced there is a option to set a custom learning rate for both the generator and discriminator. 

<img src="../codename-img/lr.png" alt="image" width="800" height="auto"> ‎


- This controls how quickly or slowly either the gen or disc learn.

***
### FCPE Training:

Fast Context-based Pitch Estimation (fcpe) is another f0 like rmvpe. The benafit of using this f0 is that it can add that "human softness" and can give models nicer end breaths. However fcpe is not as percise as rmvpe. 


***
### L1 Mel Loss:
In the training section under advanced settings for training you can find a toggle to enable or disable Multi-scale Mel loss function. The results of using L1 might be less detailed but may potentially mitigate the 'metalic voice' effect.

<img src="../codename-img/l1.png" alt="image" width="800" height="auto">


***
### Upcoming Features:
- Custom gradient norm value ( from the ui level )
- Ability to delay / headstart the Generator or Discriminator.
- More warmup options ( Cosine anneal and so on ).
- Ability to choose lr_decay from the ui
- And more...

***
###### ‎
:::content-center
#### `You have reached the end.`

[!badge variant="info" size="xl" corners="pill" icon="paper-airplane" iconAlign="right" text="Report Issues"](https://docs.aihub.gg/contributions/)
:::
