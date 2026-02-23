---
icon: chevron-right
order: 9000
---

`Last update: February 23, 2026` 


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
- **<u>[Terms of Service](https://www.weights.com/terms-of-service)</u>**
- **<u>[End-User License Agreement (EULA)](https://www.weights.com/eula)</u>**

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
Learn more about Free Premium Items via [Streaks](http://docs.aihub.gg/rvc/cloud/weights-com/#streaks).
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

<div style="display: flex; flex-direction: column; gap: 1rem; align-items: center; padding: 1rem 0;">
  <a href="https://discord.gg/weights" style="display: inline-flex; align-items: center; gap: 0.5rem; background-color: #1a1c1d; color: white; padding: 0.6rem 1.2rem; border-radius: 9999px; text-decoration: none; font-weight: bold; font-size: 1rem; min-width: 150px; justify-content: center; border: 1.5px solid #555;">
    <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMjcuMTQgOTYuMzYiPgogICAgPHBhdGggZmlsbD0iIzU4NjVmMiIKICAgICAgICBkPSJNMTA3LjcsOC4wN0ExMDUuMTUsMTA1LjE1LDAsMCwwLDgxLjQ3LDBhNzIuMDYsNzIuMDYsMCwwLDAtMy4zNiw2LjgzQTk3LjY4LDk3LjY4LDAsMCwwLDQ5LDYuODMsNzIuMzcsNzIuMzcsMCwwLDAsNDUuNjQsMCwxMDUuODksMTA1Ljg5LDAsMCwwLDE5LjM5LDguMDlDMi43OSwzMi42NS0xLjcxLDU2LjYuNTQsODAuMjFoMEExMDUuNzMsMTA1LjczLDAsMCwwLDMyLjcxLDk2LjM2LDc3LjcsNzcuNywwLDAsMCwzOS42LDg1LjI1YTY4LjQyLDY4LjQyLDAsMCwxLTEwLjg1LTUuMThjLjkxLS42NiwxLjgtMS4zNCwyLjY2LTJhNzUuNTcsNzUuNTcsMCwwLDAsNjQuMzIsMGMuODcuNzEsMS43NiwxLjM5LDIuNjYsMmE2OC42OCw2OC42OCwwLDAsMS0xMC44Nyw1LjE5LDc3LDc3LDAsMCwwLDYuODksMTEuMUExMDUuMjUsMTA1LjI1LDAsMCwwLDEyNi42LDgwLjIyaDBDMTI5LjI0LDUyLjg0LDEyMi4wOSwyOS4xMSwxMDcuNyw4LjA3Wk00Mi40NSw2NS42OUMzNi4xOCw2NS42OSwzMSw2MCwzMSw1M3M1LTEyLjc0LDExLjQzLTEyLjc0UzU0LDQ2LDUzLjg5LDUzLDQ4Ljg0LDY1LjY5LDQyLjQ1LDY1LjY5Wm00Mi4yNCwwQzc4LjQxLDY1LjY5LDczLjI1LDYwLDczLjI1LDUzczUtMTIuNzQsMTEuNDQtMTIuNzRTOTYuMjMsNDYsOTYuMTIsNTMsOTEuMDgsNjUuNjksODQuNjksNjUuNjlaIiAvPgo8L3N2Zz4=" alt="Discord Icon" style="width: 20px; height: 20px;"/>
    <span>Discord</span>
  </a>
  <a href="https://www.reddit.com/r/weights/" style="display: inline-flex; align-items: center; gap: 0.5rem; background-color: #1a1c1d; color: white; padding: 0.6rem 1.2rem; border-radius: 9999px; text-decoration: none; font-weight: bold; font-size: 1rem; min-width: 150px; justify-content: center; border: 1.5px solid #555;">
    <img src="data:image/svg+xml;base64,PHN2ZyBlbmFibGUtYmFja2dyb3VuZD0ibmV3IDAgMCAyNTYgMjU2IiB2aWV3Qm94PSIwIDAgMjU2IDI1NiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayI+PGxpbmVhckdyYWRpZW50IGlkPSJhIj48c3RvcCBvZmZzZXQ9IjAiIHN0b3AtY29sb3I9IiNmZWZmZmYiLz48c3RvcCBvZmZzZXQ9Ii40IiBzdG9wLWNvbG9yPSIjZmVmZmZmIi8+PHN0b3Agb2Zmc2V0PSIuNTEiIHN0b3AtY29sb3I9IiNmOWZjZmMiLz48c3RvcCBvZmZzZXQ9Ii42MiIgc3RvcC1jb2xvcj0iI2VkZjNmNSIvPjxzdG9wIG9mZnNldD0iLjciIHN0b3AtY29sb3I9IiNkZWU5ZWMiLz48c3RvcCBvZmZzZXQ9Ii43MiIgc3RvcC1jb2xvcj0iI2Q4ZTRlOCIvPjxzdG9wIG9mZnNldD0iLjc2IiBzdG9wLWNvbG9yPSIjY2NkOGRmIi8+PHN0b3Agb2Zmc2V0PSIuOCIgc3RvcC1jb2xvcj0iI2M4ZDVkZCIvPjxzdG9wIG9mZnNldD0iLjgzIiBzdG9wLWNvbG9yPSIjY2NkNmRlIi8+PHN0b3Agb2Zmc2V0PSIuODUiIHN0b3AtY29sb3I9IiNkOGRiZTIiLz48c3RvcCBvZmZzZXQ9Ii44OCIgc3RvcC1jb2xvcj0iI2VkZTNlOSIvPjxzdG9wIG9mZnNldD0iLjkiIHN0b3AtY29sb3I9IiNmZmViZWYiLz48L2xpbmVhckdyYWRpZW50PjxyYWRpYWxHcmFkaWVudCBpZD0iYiIgY3g9Ijk4MS4wMjUxIiBjeT0iMS44MTEiIGZ5PSItNy4zMTkiIGdyYWRpZW50VHJhbnNmb3JtPSJtYXRyaXgoLjQ3IDAgMCAtLjQxIC0yNjAuMDcgMTA4LjMpIiBncmFkaWVudFVuaXRzPSJ1c2VyU3BhY2VPblVzZSIgcj0iMTI3LjQ1IiB4bGluazpocmVmPSIjYSIvPjxyYWRpYWxHcmFkaWVudCBpZD0iYyIgY3g9IjY3Mi4yNTkyIiBjeT0iMS44MTEiIGZ5PSItNy4zMTkiIGdyYWRpZW50VHJhbnNmb3JtPSJtYXRyaXgoLjQ3IDAgMCAtLjQxIC0yNjAuMDcgMTA4LjMpIiBncmFkaWVudFVuaXRzPSJ1c2VyU3BhY2VPblVzZSIgcj0iMTI3LjQ1IiB4bGluazpocmVmPSIjYSIvPjxyYWRpYWxHcmFkaWVudCBpZD0iZCIgY3g9IjgzMC42NzUxIiBjeT0iLTIyNC42ODQ1IiBncmFkaWVudFRyYW5zZm9ybT0ibWF0cml4KC40NyAwIDAgLS4zMyAtMjYwLjA3IDI1LjAzKSIgZ3JhZGllbnRVbml0cz0idXNlclNwYWNlT25Vc2UiIHI9IjM4NC40NCIgeGxpbms6aHJlZj0iI2EiLz48bGluZWFyR3JhZGllbnQgaWQ9ImUiPjxzdG9wIG9mZnNldD0iMCIgc3RvcC1jb2xvcj0iI2Y2MCIvPjxzdG9wIG9mZnNldD0iLjUiIHN0b3AtY29sb3I9IiNmZjQ1MDAiLz48c3RvcCBvZmZzZXQ9Ii43IiBzdG9wLWNvbG9yPSIjZmM0MzAxIi8+PHN0b3Agb2Zmc2V0PSIuODIiIHN0b3AtY29sb3I9IiNmNDNmMDciLz48c3RvcCBvZmZzZXQ9Ii45MiIgc3RvcC1jb2xvcj0iI2U1MzgxMiIvPjxzdG9wIG9mZnNldD0iMSIgc3RvcC1jb2xvcj0iI2Q0MzAxZiIvPjwvbGluZWFyR3JhZGllbnQ+PHJhZGlhbEdyYWRpZW50IGlkPSJmIiBjeD0iLTI5NTcuMjU1MSIgY3k9IjE3My40MjIyIiBncmFkaWVudFRyYW5zZm9ybT0ibWF0cml4KC0uNDcgMCAwIC42OSAtMTIyNC42MyAzMS4zMSkiIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIiByPSIzMi4xMiIgeGxpbms6aHJlZj0iI2UiLz48cmFkaWFsR3JhZGllbnQgaWQ9ImciIGN4PSI3NDUuMjM1MSIgY3k9IjE3My40MjIyIiBncmFkaWVudFRyYW5zZm9ybT0ibWF0cml4KC40NyAwIDAgLjY5IC0yNjAuMDcgMzEuMzEpIiBncmFkaWVudFVuaXRzPSJ1c2VyU3BhY2VPblVzZSIgcj0iMzIuMTIiIHhsaW5rOmhyZWY9IiNlIi8+PHJhZGlhbEdyYWRpZW50IGlkPSJoIiBjeD0iODI2LjQ2NTEiIGN5PSItNTA4LjQ3NjQiIGdyYWRpZW50VHJhbnNmb3JtPSJtYXRyaXgoLjQ3IDAgMCAtLjMxIC0yNjAuMDcgMzcuMjgpIiBncmFkaWVudFVuaXRzPSJ1c2VyU3BhY2VPblVzZSIgcj0iMTEzLjI2Ij48c3RvcCBvZmZzZXQ9IjAiIHN0b3AtY29sb3I9IiMxNzJlMzUiLz48c3RvcCBvZmZzZXQ9Ii4yOSIgc3RvcC1jb2xvcj0iIzBlMWMyMSIvPjxzdG9wIG9mZnNldD0iLjczIiBzdG9wLWNvbG9yPSIjMDMwNzA4Ii8+PHN0b3Agb2Zmc2V0PSIxIi8+PC9yYWRpYWxHcmFkaWVudD48cmFkaWFsR3JhZGllbnQgaWQ9ImkiIGN4PSI5MjYuMzQ1MSIgY3k9IjI3Ny45MDE5IiBncmFkaWVudFRyYW5zZm9ybT0ibWF0cml4KC40NyAwIDAgLS40NyAtMjYwLjA3IDE2NC43MikiIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIiByPSI5OS40MiIgeGxpbms6aHJlZj0iI2EiLz48cmFkaWFsR3JhZGllbnQgaWQ9ImoiIGN4PSI4ODQuOTE1MSIgY3k9IjE3Ny41NjE5IiBncmFkaWVudFRyYW5zZm9ybT0ibWF0cml4KC40NyAwIDAgLS40NyAtMjYwLjA3IDE2OC41KSIgZ3JhZGllbnRVbml0cz0idXNlclNwYWNlT25Vc2UiIHI9IjgxLjQ5Ij48c3RvcCBvZmZzZXQ9Ii40OCIgc3RvcC1jb2xvcj0iIzdhOTI5OSIvPjxzdG9wIG9mZnNldD0iLjY3IiBzdG9wLWNvbG9yPSIjMTcyZTM1Ii8+PHN0b3Agb2Zmc2V0PSIuNzUiLz48c3RvcCBvZmZzZXQ9Ii44MiIgc3RvcC1jb2xvcj0iIzE3MmUzNSIvPjwvcmFkaWFsR3JhZGllbnQ+PHBhdGggZD0ibTEyOCAwYy03MC43IDAtMTI4IDU3LjMtMTI4IDEyOCAwIDM1LjQgMTQuMyA2Ny40IDM3LjUgOTAuNWwtMjQuNCAyNC40Yy00LjggNC44LTEuNCAxMy4xIDUuNCAxMy4xaDEwOS41YzcwLjcgMCAxMjgtNTcuMyAxMjgtMTI4cy01Ny4zLTEyOC0xMjgtMTI4eiIgZmlsbD0iI2ZmNDUwMCIvPjxjaXJjbGUgY3g9IjIwMC42IiBjeT0iMTIzLjciIGZpbGw9InVybCgjYikiIHI9IjI5LjkiLz48Y2lyY2xlIGN4PSI1NS40IiBjeT0iMTIzLjciIGZpbGw9InVybCgjYykiIHI9IjI5LjkiLz48ZWxsaXBzZSBjeD0iMTI4LjEiIGN5PSIxNDkuMyIgZmlsbD0idXJsKCNkKSIgcng9Ijg1LjMiIHJ5PSI2NCIvPjxwYXRoIGQ9Im0xMDIuOCAxNDMuMWMtLjUgMTAuOC03LjcgMTQuOC0xNi4xIDE0LjhzLTE0LjgtNS42LTE0LjMtMTYuNCA3LjctMTggMTYuMS0xOCAxNC44IDguOCAxNC4zIDE5LjZ6IiBmaWxsPSIjODQyMTIzIi8+PHBhdGggZD0ibTE4My42IDE0MS41Yy41IDEwLjgtNS45IDE2LjQtMTQuMyAxNi40cy0xNS42LTMuOS0xNi4xLTE0LjhjLS41LTEwLjggNS45LTE5LjYgMTQuMy0xOS42czE1LjYgNy4xIDE2LjEgMTh6IiBmaWxsPSIjODQyMTIzIi8+PHBhdGggZD0ibTE1My4zIDE0NC4xYy41IDEwLjEgNy4yIDEzLjggMTUgMTMuOHMxMy44LTUuNSAxMy40LTE1LjdjLS41LTEwLjEtNy4yLTE2LjgtMTUtMTYuOHMtMTMuOSA4LjUtMTMuNCAxOC43eiIgZmlsbD0idXJsKCNmKSIvPjxwYXRoIGQ9Im0xMDIuOCAxNDQuMWMtLjUgMTAuMS03LjIgMTMuOC0xNSAxMy44cy0xMy44LTUuNS0xMy4zLTE1LjdjLjUtMTAuMSA3LjItMTYuOCAxNS0xNi44czEzLjggOC41IDEzLjMgMTguN3oiIGZpbGw9InVybCgjZykiLz48cGF0aCBkPSJtMTI4LjEgMTY1LjFjLTEwLjYgMC0yMC43LjUtMzAuMSAxLjQtMS42LjItMi42IDEuOC0yIDMuMiA1LjIgMTIuMyAxNy42IDIxIDMyLjEgMjFzMjYuOC04LjYgMzIuMS0yMWMuNi0xLjUtLjQtMy4xLTItMy4yLTkuNC0uOS0xOS41LTEuNC0zMC4xLTEuNHoiIGZpbGw9IiNiYmNmZGEiLz48cGF0aCBkPSJtMTI4LjEgMTY3LjVjLTEwLjYgMC0yMC43LjUtMzAgMS41LTEuNi4yLTIuNiAxLjgtMiAzLjMgNS4yIDEyLjUgMTcuNiAyMS4zIDMyIDIxLjNzMjYuOC04LjggMzItMjEuM2MuNi0xLjUtLjQtMy4xLTItMy4zLTkuNC0xLTE5LjUtMS41LTMwLTEuNXoiIGZpbGw9IiNmZmYiLz48cGF0aCBkPSJtMTI4LjEgMTY2LjJjLTEwLjQgMC0yMC4zLjUtMjkuNSAxLjQtMS42LjItMi42IDEuOC0yIDMuMiA1LjIgMTIuMyAxNy4zIDIxIDMxLjUgMjFzMjYuMy04LjYgMzEuNS0yMWMuNi0xLjUtLjQtMy4xLTItMy4yLTkuMi0uOC0xOS4xLTEuNC0yOS41LTEuNHoiIGZpbGw9InVybCgjaCkiLz48Y2lyY2xlIGN4PSIxNzQuOCIgY3k9IjU1LjUiIGZpbGw9InVybCgjaSkiIHI9IjIxLjIiLz48cGF0aCBkPSJtMTI3LjggODhjLTIuNSAwLTQuNi0xLjEtNC42LTIuNyAwLTE5IDE1LjQtMzQuNCAzNC40LTM0LjQgMi41IDAgNC42IDIuMSA0LjYgNC42cy0yLjEgNC42LTQuNiA0LjZjLTEzLjkgMC0yNS4yIDExLjMtMjUuMiAyNS4yIDAgMS43LTIuMSAyLjctNC42IDIuN3oiIGZpbGw9InVybCgjaikiLz48cGF0aCBkPSJtOTcuMyAxNDkuMWMwIDMuOS00LjIgNS43LTkuMyA1LjdzLTkuMy0xLjgtOS4zLTUuNyA0LjItNy4xIDkuMy03LjEgOS4zIDMuMSA5LjMgNy4xeiIgZmlsbD0iI2ZmNjEwMSIvPjxwYXRoIGQ9Im0xNzcuNSAxNDkuMWMwIDMuOS00LjIgNS43LTkuMyA1LjdzLTkuMy0xLjgtOS4zLTUuNyA0LjItNy4xIDkuMy03LjEgOS4zIDMuMSA5LjMgNy4xeiIgZmlsbD0iI2ZmNjEwMSIvPjxnIGZpbGw9IiNmZmM0OWMiPjxlbGxpcHNlIGN4PSI5NC40IiBjeT0iMTM0LjgiIHJ4PSIzLjMiIHJ5PSIzLjYiLz48ZWxsaXBzZSBjeD0iMTczLjMiIGN5PSIxMzQuOCIgcng9IjMuMyIgcnk9IjMuNiIvPjwvZz48L3N2Zz4=" alt="Reddit Icon" style="width: 20px; height: 20px;"/>
    <span>Reddit</span>
  </a>
</div>

***
:::content-center
## Mobile Apps :icon-device-mobile:
:::

<div style="display: flex; flex-direction: column; gap: 1rem; align-items: center; padding: 1rem 0;">
  <a href="https://apps.apple.com/us/app/weights-create-with-ai/id6480142052" style="display: inline-flex; align-items: center; gap: 0.5rem; background-color: #1a1c1d; color: white; padding: 0.6rem 1.2rem; border-radius: 9999px; text-decoration: none; font-weight: bold; font-size: 1rem; min-width: 150px; justify-content: center; border: 1.5px solid #555;">
    <img src="data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjMyIiB2aWV3Qm94PSI0IDMyIDM3Ni40IDQ0OS40IiB3aWR0aD0iMzIiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHBhdGggZD0ibTMxOC43IDI2OC43Yy0uMi0zNi43IDE2LjQtNjQuNCA1MC04NC44LTE4LjgtMjYuOS00Ny4yLTQxLjctODQuNy00NC42LTM1LjUtMi44LTc0LjMgMjAuNy04OC41IDIwLjctMTUgMC00OS40LTE5LjctNzYuNC0xOS43LTU1LjguOS0xMTUuMSA0NC41LTExNS4xIDEzMy4ycTAgMzkuMyAxNC40IDgxLjJjMTIuOCAzNi43IDU5IDEyNi43IDEwNy4yIDEyNS4yIDI1LjItLjYgNDMtMTcuOSA3NS44LTE3LjkgMzEuOCAwIDQ4LjMgMTcuOSA3Ni40IDE3LjkgNDguNi0uNyA5MC40LTgyLjUgMTAyLjYtMTE5LjMtNjUuMi0zMC43LTYxLjctOTAtNjEuNy05MS45em0tNTYuNi0xNjQuMmMyNy4zLTMyLjQgMjQuOC02MS45IDI0LTcyLjUtMjQuMSAxLjQtNTIgMTYuNC02Ny45IDM0LjktMTcuNSAxOS44LTI3LjggNDQuMy0yNS42IDcxLjkgMjYuMSAyIDQ5LjktMTEuNCA2OS41LTM0LjN6IiBmaWxsPSIjZmZmIi8+PC9zdmc+" alt="Apple iOS Icon" style="width: 20px; height: 20px;"/>
    <span>iOS</span>
  </a>
  <a href="https://play.google.com/store/apps/details?id=com.weights.app" style="display: inline-flex; align-items: center; gap: 0.5rem; background-color: #1a1c1d; color: white; padding: 0.6rem 1.2rem; border-radius: 9999px; text-decoration: none; font-weight: bold; font-size: 1rem; min-width: 150px; justify-content: center; border: 1.5px solid #555;">
    <img src="data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4KDTwhLS0gVXBsb2FkZWQgdG86IFNWRyBSZXBvLCB3d3cuc3ZncmVwby5jb20sIEdlbmVyYXRvcjogU1ZHIFJlcG8gTWl4ZXIgVG9vbHMgLS0+Cjxzdmcgd2lkdGg9IjgwMHB4IiBoZWlnaHQ9IjgwMHB4IiB2aWV3Qm94PSIwIDAgMzIgMzIiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+DQo8bWFzayBpZD0ibWFzazBfODdfODMyMCIgc3R5bGU9Im1hc2stdHlwZTphbHBoYSIgbWFza1VuaXRzPSJ1c2VyU3BhY2VPblVzZSIgeD0iNyIgeT0iMyIgd2lkdGg9IjI0IiBoZWlnaHQ9IjI2Ij4NCjxwYXRoIGQ9Ik0zMC4wNDg0IDE0LjQwMDRDMzEuMzE3MiAxNS4wOTg2IDMxLjMxNzIgMTYuOTAxNCAzMC4wNDg0IDE3LjU5OTZMOS43NTYyNyAyOC43NjU5QzguNTIwNTIgMjkuNDQ1OSA3IDI4LjU2MzQgNyAyNy4xNjYzTDcgNC44MzM3NEM3IDMuNDM2NTcgOC41MjA1MiAyLjU1NDE1IDkuNzU2MjcgMy4yMzQxNUwzMC4wNDg0IDE0LjQwMDRaIiBmaWxsPSIjQzRDNEM0Ii8+DQo8L21hc2s+DQo8ZyBtYXNrPSJ1cmwoI21hc2swXzg3XzgzMjApIj4NCjxwYXRoIGQ9Ik03LjYzNDczIDI4LjU0NjZMMjAuMjkyMyAxNS44MTc5TDcuODQzMTkgMy4yOTg4M0M3LjM0NjUzIDMuNjE3MjEgNyA0LjE2NjkgNyA0LjgzMzlWMjcuMTY2NEM3IDI3LjczNTUgNy4yNTIyMyAyOC4yMTkxIDcuNjM0NzMgMjguNTQ2NloiIGZpbGw9InVybCgjcGFpbnQwX2xpbmVhcl84N184MzIwKSIvPg0KPHBhdGggZD0iTTMwLjA0OCAxNC40MDAzQzMxLjMxNjkgMTUuMDk4NSAzMS4zMTY5IDE2LjkwMTIgMzAuMDQ4IDE3LjU5OTRMMjQuOTI4NyAyMC40MTY1TDIwLjI5MiAxNS44MTc1TDI0LjY5MjMgMTEuNDUzMUwzMC4wNDggMTQuNDAwM1oiIGZpbGw9InVybCgjcGFpbnQxX2xpbmVhcl84N184MzIwKSIvPg0KPHBhdGggZD0iTTI0LjkyOTIgMjAuNDE2OEwyMC4yOTI0IDE1LjgxNzlMNy42MzQ3NyAyOC41NDY2QzguMTkxMzkgMjkuMDIzMiA5LjAyMzg5IDI5LjE2OTEgOS43NTYzNSAyOC43NjZMMjQuOTI5MiAyMC40MTY4WiIgZmlsbD0idXJsKCNwYWludDJfbGluZWFyXzg3XzgzMjApIi8+DQo8cGF0aCBkPSJNNy44NDI3NyAzLjI5ODY1TDIwLjI5MTkgMTUuODE3N0wyNC42OTIyIDExLjQ1MzNMOS43NTU4MyAzLjIzNDE1QzkuMTEwMDMgMi44Nzg3OCA4LjM4NjQ2IDIuOTUwMTMgNy44NDI3NyAzLjI5ODY1WiIgZmlsbD0idXJsKCNwYWludDNfbGluZWFyXzg3XzgzMjApIi8+DQo8L2c+DQo8ZGVmcz4NCjxsaW5lYXJHcmFkaWVudCBpZD0icGFpbnQwX2xpbmVhcl84N184MzIwIiB4MT0iMTUuNjc2OSIgeTE9IjEwLjg3NCIgeDI9IjcuMDcxMDYiIHkyPSIxOS41NTA2IiBncmFkaWVudFVuaXRzPSJ1c2VyU3BhY2VPblVzZSI+DQo8c3RvcCBzdG9wLWNvbG9yPSIjMDBDM0ZGIi8+DQo8c3RvcCBvZmZzZXQ9IjEiIHN0b3AtY29sb3I9IiMxQkUyRkEiLz4NCjwvbGluZWFyR3JhZGllbnQ+DQo8bGluZWFyR3JhZGllbnQgaWQ9InBhaW50MV9saW5lYXJfODdfODMyMCIgeDE9IjIwLjI5MiIgeTE9IjE1LjgxNzYiIHgyPSIzMS43MzgxIiB5Mj0iMTUuODE3NiIgZ3JhZGllbnRVbml0cz0idXNlclNwYWNlT25Vc2UiPg0KPHN0b3Agc3RvcC1jb2xvcj0iI0ZGQ0UwMCIvPg0KPHN0b3Agb2Zmc2V0PSIxIiBzdG9wLWNvbG9yPSIjRkZFQTAwIi8+DQo8L2xpbmVhckdyYWRpZW50Pg0KPGxpbmVhckdyYWRpZW50IGlkPSJwYWludDJfbGluZWFyXzg3XzgzMjAiIHgxPSI3LjM2OTMyIiB5MT0iMzAuMTAwNCIgeDI9IjIyLjU5NSIgeTI9IjE3Ljg5MzciIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIj4NCjxzdG9wIHN0b3AtY29sb3I9IiNERTI0NTMiLz4NCjxzdG9wIG9mZnNldD0iMSIgc3RvcC1jb2xvcj0iI0ZFMzk0NCIvPg0KPC9saW5lYXJHcmFkaWVudD4NCjxsaW5lYXJHcmFkaWVudCBpZD0icGFpbnQzX2xpbmVhcl84N184MzIwIiB4MT0iOC4xMDcyNSIgeTE9IjEuOTAxMzciIHgyPSIyMi41OTcxIiB5Mj0iMTMuNzM2NSIgZ3JhZGllbnRVbml0cz0idXNlclNwYWNlT25Vc2UiPg0KPHN0b3Agc3RvcC1jb2xvcj0iIzExRDU3NCIvPg0KPHN0b3Agb2Zmc2V0PSIxIiBzdG9wLWNvbG9yPSIjMDFGMTc2Ii8+DQo8L2xpbmVhckdyYWRpZW50Pg0KPC9kZWZzPg0KPC9zdmc+" alt="Google Play Android Icon" style="width: 20px; height: 20px;"/>
    <span>Android</span>
  </a>
</div>

***
######
:::content-center
#### `You have reached the end.`

[!badge variant="info" size="xl" corners="pill" icon="paper-airplane" iconAlign="right" text="Report Issues"](https://docs.aihub.gg/contributions/)
:::