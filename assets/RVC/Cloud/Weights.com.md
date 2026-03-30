---
icon: /img/weights-icon.svg
order: 1000
---

`Last update: March 24, 2026` 


***
:::content-center
<img src="/img/weights-logo.png" alt="Weights Logo" width="600" height="auto">


***
###### ‎  
:::content-center
## Introduction
:::

- **Weights.com** is an easy, freemium AI Cloud Website platform that provides tools for creating AI voice covers, text-to-speech, and more. It serves as an all-in-one web UI, eliminating the need for powerful local hardware or complex setups.
- The platform is designed to be user-friendly, catering to both beginners and experienced users. You can train your own custom voice models or use a vast library of high-quality, community-made models, from both the [AI Hub Discord](https://discord.gg/aihub) & the [Weights.com Models Page](https://weights.com/models).
- [Weights](https://discord.gg/weights) is partnered with [AI HUB](https://discord.gg/aihub) & [DreamTavern](https://discord.gg/dreamtavern).
- It's named Weights, as it was originally meant only for RVC with the domain Weights.gg, storing RVC Models, which are PyTorch *Weights*. Later on, the domain changed to Weights.com and expanded to other things, but for this specific guide, we will focus on the RVC-related side.

!!!danger
# Goodbye to Weights

After much reflection, we’ve made the difficult decision to shut down Weights, Voyages, and our family of apps on **March 31st, 2026**.

# What to Know

**Before March 31st, 2026:**
- Download any content, models, or creations you want to keep
- Request a full data export from your account settings
- Active subscriptions will be canceled automatically
- Credits can be used until the shutdown date

**After March 31st, 2026:**
- The website, apps, and all services will be permanently offline
- Content and accounts will no longer be accessible
- Support for Weights, Voyages, and other products will end

#  Replay

[Replay](https://www.weights.com/replay) is not affected by this shutdown. It will remain available and usable, though no new updates will be released. **NOTE:** Since Replay needs to download required files, it might not work if you didn't set it up before the shutdown.

# ❤️ Thank You

Thank you for being part of the Weights community. We’ve loved seeing what you built and how you pushed the boundaries of AI creativity. This platform wouldn’t have existed without you.

# ❓ Questions
If you need help with exports, subscriptions, or anything else, contact us at support@weights.com or here on the Discord server. We'll be here until the end.

!!!
***

#### Pros & Cons :icon-tasklist:
==- *Learn more*
!!! *The pros & cons are subjective to your necessities.*        
!!! 
||| ✔️ **PROS** 
- All-in-one web cloud platform.
- No need for a powerful PC.
- Mobile friendly, with even an app.
- User-friendly interface suitable for beginners.
- Large library of public RVC voice models (anime, singers, etc.).
- Free tier available for basic usage.
- Integrated TTS and direct recording options.
- Active community for sharing and collaboration.
||| ❌ **CONS** 
- Free plan has limitations on creations and features.
- Processing and training times could be slow due to queues in certain, but it's better on Paid Tiers.
- Less granular advanced control compared to forks like Applio or Mainline/Original RVC, Because it's meant for everyone and not just tech experts.
||| 
===

***
:::content-center
## Training a Voice Model :icon-dependabot:
:::

#### <u>Training Disclaimer</u>
Before you train your first model, Weights will present you with a disclaimer that you must accept. This ensures that the tool is used ethically and legally.

!!!success The key terms are:
- :icon-check-circle-fill: Never use the voice of someone without their consent.
- :icon-check-circle-fill: Don’t use voices for fraud, scams, or bullying.
- :icon-check-circle-fill: Protected intellectual property rights must be respected.
- :icon-check-circle-fill: Voices should be used for good, not for harm. Have fun!
!!!


<img src="../weights-com-img/training-disclaimer.png" alt="Training Disclaimer on Weights" width="400" height="auto">


You can review the full legal documents here:
- **[Terms of Service](https://www.weights.com/terms-of-service)**
- **[End-User License Agreement (EULA)](https://www.weights.com/eula)**

***

#### <u>Instructions:</u>
**1.** Navigate to the [**Train Model**](https://www.weights.com/train/voice) tab from the main menu. You will be presented with the "New Voice Model" page.

<img src="../weights-com-img/train-voice-model.png" alt="Weights new voice model page." width="800" height="auto">

**2.** Fill in the **Model Details**:
   - **Select or drop image:** Upload a picture to serve as the thumbnail for your model.
   - **Model Name:** Assign a clear and descriptive name.
   - **Model Description:** Add optional details about the voice or its intended use.
   - **Private Model:** Enable this option if you want the model to be visible only to you. Premium only

**3.** Upload your **Input Audio**:
   - This section is for your dataset, the collection of voice recordings the AI will learn from.
   - You can drag and drop audio files directly. Minimum 3 minutes, It is recommended to upload at least 5-10+ minutes of clean audio with minimal background noise for good results.
   - Premium users can train longer datasets, up to 30 minutes.
   - Weights will automatically clean your dataset.

**4.** Start the training process by clicking **Start Training**.
   - Depending on your subscription, you may see different options, such as "Train and Publish" or "Use Premium Training Item".

<img src="../weights-com-img/train-voice-models-2.png" alt="Start training options on Weights." width="600" height="auto">

!!!
Learn more about Free Premium Items via [Streaks](https://docs.aihub.gg/rvc/cloud/weights-com/#streaks).
!!!

***
:::content-center
## Creating a Cover (Inference) :icon-unmute:
:::
Once you have a model, you can use it to generate voice covers. This process is also known as inference.

#### <u>Instructions:</u>
**1. Choose a Voice to Use**
   - You can select one of your own trained models or browse the extensive public library of **Voice Models**.
   - Use the search bar to find specific characters or artists.
   
<img src="../weights-com-img/cover-model.png" alt="Selecting a voice model on Weights." width="500" height="auto">

**2. Choose your Input Audio**
   - You have three main options for providing the audio to be converted:

   +++ Audio
   Upload an audio file from your device. This is the most common method for creating song covers.
   +++ Text-to-Speech (TTS)
   Write text directly into the provided box. Since RVC is Speech-To-Speech Natively, You will need to select a base TTS voice (like "John") which  will be used as an input for RVC Model.
     
   <img src="../weights-com-img/cover-tts.png" alt="Text-to-Speech input on Weights." width="450" height="auto">

   +++ Recording
   Record audio directly through your microphone, which is useful for quick tests or generating voice lines.

   <img src="../weights-com-img/cover-recording.png" alt="Recording audio directly on Weights." width="450" height="auto">

   +++


***
#### **3. (Optional) Choose Your Settings**
   - Before creating the cover, you can adujst the output with several settings.
   
==- Basic Settings
- **Pre-Stemmed:** Turn this on if your uploaded audio file contains only vocals without any instrumental backing.
- **Pitch:** Adjust the pitch of the output voice. A positive value makes it higher, while a negative value makes it lower.

<img src="../weights-com-img/cover-basic.png" alt="Basic settings for creating a cover." width="500" height="auto">
===
   
==- Advanced Settings
- **De-Echo & Reverb:** Removes echo and reverb from the source vocal track for a cleaner conversion.
- **Isolate Main Singer:** Attempts to convert only the lead vocals, ignoring background singers.
- **Instrumental Pitch:** Changes the pitch of the instrumental track separately from the vocals.
- **Volume Envelope:** Lower values make the output volume closer to the original vocal's volume dynamics.
- **Consonant Protection:** Helps reduce audio artifacts and slurring on consonants, especially at lower volumes.

<img src="../weights-com-img/cover-advanced.png" alt="Advanced settings for creating a cover." width="400" height="auto">
===

#### **4. Create and Download**
- Click the **Create** button to start the conversion process.
- Your request will be added to a queue. You can view its status on the **My Creations** page, where it will show as "Processing".
   
<img src="../weights-com-img/cover-creations.png" alt="A cover being processed in My Creations." width="900" height="auto">

- Once finished, you can play the result directly and download it to your device.


***
:::content-center
## Pricing & Plans :icon-credit-card:
:::
- Weights.com operates on a freemium model. It offers a **Free Plan** with core features, alongside paid **Basic** and **Pro** plans for users who need more and better resources.
- Subscriptions increase the number of daily covers, queued items, and weekly voice trainings, while also allowing for longer maximum audio lengths.

<img src="../weights-com-img/pricing.png" alt="Pricing plans on Weights." width="900" height="auto">

!!!warning
Limits and features are subject to change. Always check the [**Weights.com Official Pricing Page**](https://weights.com/pricing) for the most current information.
!!!


***
:::content-center
## Streaks :icon-flame:
:::
- Weights.com rewards users for daily activity through a **Streak** system.
- To keep your streak going, you must create at least one item (Voice Cover, Image, or Chat) each day before the streak resets.
- As a reward for consistency, you will **earn a Free Premium Training every 5 days** you maintain your streak. This allows you to train more RVC voice models with a bigger dataset without a paid subscription.

<img src="../weights-com-img/streaks.png" alt="Weights daily streak system." width="700" height="auto">


***
:::content-center
## Communities :icon-people:
:::

<style>
  .social-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
    justify-content: center;
    margin: 1.5rem 0;
  }
  .social-card {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 0.8rem 1.2rem;
    min-width: 240px;
    border: 1px solid rgba(150, 150, 150, 0.2);
    border-radius: 10px;
    text-decoration: none !important;
    color: inherit !important;
    background: rgba(128, 128, 128, 0.05);
    transition: all 0.2s ease;
  }
  .social-card:hover {
    transform: translateY(-2px);
    background: rgba(128, 128, 128, 0.12);
    border-color: rgba(150, 150, 150, 0.5);
  }
  .social-card img {
    width: 24px;
    height: 24px;
  }
  .social-card span {
    font-weight: 600;
    font-size: 0.95rem;
  }
</style>

<div class="social-grid">
    <a href="https://discord.gg/aihub" class="social-card">
        <img src="/img/discord-logo.svg" alt="Discord">
        <span>AI HUB's Discord</span>
    </a>
    <a href="https://discord.gg/weights" class="social-card">
        <img src="/img/discord-logo.svg" alt="Discord">
        <span>Weights' Discord</span>
    </a>
    <a href="https://www.reddit.com/r/weights/" class="social-card">
        <img src="/img/reddit-logo-fullcolor.svg" alt="Reddit">
        <span>Weights' Reddit</span>
    </a>
</div>


***
:::content-center
## Mobile Apps :icon-device-mobile:
:::

<style>
  .app-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 1.2rem;
    justify-content: center;
    margin: 1.5rem 0;
  }
  .app-card {
    display: flex;
    align-items: center;
    gap: 14px;
    padding: 1rem 1.5rem;
    min-width: 180px;
    border: 1px solid rgba(150, 150, 150, 0.2);
    border-radius: 12px;
    text-decoration: none !important;
    color: inherit !important;
    background: rgba(128, 128, 128, 0.05);
    transition: all 0.2s ease;
  }
  .app-card:hover {
    transform: translateY(-3px);
    background: rgba(128, 128, 128, 0.12);
    border-color: rgba(150, 150, 150, 0.5);
    box-shadow: 0 8px 15px rgba(0,0,0,0.2);
  }
  .app-card img {
    width: 28px;
    height: 28px;
  }
  .app-card-text {
    display: flex;
    flex-direction: column;
    text-align: left;
  }
  .app-card-text .store-name {
    font-size: 0.75rem;
    opacity: 0.6;
    text-transform: uppercase;
    letter-spacing: 0.05em;
  }
  .app-card-text .platform-name {
    font-weight: 700;
    font-size: 1.1rem;
    line-height: 1.1;
  }
</style>

<div class="app-grid">
    <!-- iOS Link -->
    <a href="https://apps.apple.com/us/app/weights-create-with-ai/id6480142052" class="app-card">
        <img src="/img/app-store-ios-icon.svg" alt="App Store">
        <div class="app-card-text">
            <span class="store-name">Download on</span>
            <span class="platform-name">App Store</span>
        </div>
    </a>
    <!-- Android Link -->
    <a href="https://play.google.com/store/apps/details?id=com.weights.app" class="app-card">
        <img src="/img/google-play-2022-current-icon.svg" alt="Play Store">
        <div class="app-card-text">
            <span class="store-name">Get it on</span>
            <span class="platform-name">Google Play</span>
        </div>
    </a>
</div>


######
:::content-center
#### `You have reached the end.`

[!badge variant="info" size="xl" corners="pill" icon="paper-airplane" iconAlign="right" text="Report Issues"](https://docs.aihub.gg/contributions/)
:::