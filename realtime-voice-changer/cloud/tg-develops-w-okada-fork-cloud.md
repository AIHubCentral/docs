``Last update: April 1, 2026``

***
:::content-center
## Introduction
:::
- This is a [cloud-based](https://docs.aihub.gg/extra/glossary/#cloud-based) alternative to run [Wokada Tg-Develop's Fork](https://docs.aihub.gg/realtime-voice-changer/local/tg-develops-w-okada-fork/), for users without a powerful local PC GPU, via Google Colab, Kaggle, or Lightning.AI.

!!!danger Server Audio not available
"Server audio not available" is normal on cloud platforms as they have no physical sound card. Always use Client mode for audio input/output.
!!!

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

***
:::content-center
## Choose your Cloud Service
:::
Set up the program using your preferred cloud service guide. Once configured, use the Public Tunnel URL to open the interface and continue with the next steps

<style>
  /* Local styling that only affects this page */
  .cloud-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 1.5rem;
    justify-content: center;
    margin: 2rem 0;
  }
  .cloud-card {
    flex: 1 1 220px;       /* Allows cards to shrink/grow, base width 220px */
    max-width: 280px;      /* Prevents cards from getting comically wide */
    padding: 1.5rem;
    border: 1px solid rgba(150, 150, 150, 0.2); /* Subtle border for light/dark mode */
    border-radius: 12px;
    text-align: center;
    text-decoration: none !important;
    color: inherit !important;
    background: rgba(128, 128, 128, 0.03); /* Barely visible background */
    transition: all 0.2s ease;
  }
  .cloud-card:hover {
    transform: translateY(-4px);
    border-color: rgba(150, 150, 150, 0.6);
    background: rgba(128, 128, 128, 0.08);
    box-shadow: 0 10px 20px rgba(0,0,0,0.1);
  }
  .cloud-card img {
    width: 54px;
    height: 54px;
    margin-bottom: 1rem;
    object-fit: contain;
  }
  .cloud-card h3 {
    margin: 0 0 0.5rem 0 !important;
    font-size: 1.25rem;
    border-bottom: none !important; /* Overrides Retype's default header lines */
  }
  .cloud-card p {
    font-size: 0.9rem;
    opacity: 0.7; /* Makes description text slightly muted */
    margin: 0;
    line-height: 1.4;
  }
</style>

<div class="cloud-grid">
    
    <a href="#google-colab" class="cloud-card">
        <img src="/img/google-colaboratory-logo.svg" alt="Colab">
        <h3>Google Colab</h3>
        <p>Decent performance for standard use.</p>
    </a>
    
    <a href="#kaggle" class="cloud-card">
        <img src="/img/kaggle-icon.svg" alt="Kaggle">
        <h3>Kaggle</h3>
        <p>Generous free GPU quotas. Great alternative if Colab is limited.</p>
    </a>
    
    <a href="#lightningai" class="cloud-card">
        <img src="/img/lightning-ai-logo.svg" alt="Lightning">
        <h3>Lightning.AI</h3>
        <p>Persistent storage and powerful GPUs.</p>
    </a>
</div>

<br><br>

***
:::content-center
### Google Colab
:::

!!!danger Google Colab Service
**Check the [Google Colab Glossary](https://docs.aihub.gg/extra/glossary/#google-colab) for more info on Free Tier, Limits, Verification, Pricing and other things.**
!!!

!!!danger Paid
You need the Google Colab Paid Tier to run this, as it uses a Web UI; otherwise, you could risk getting disconnected or banned.
!!!

- **1. Access:** Go to the [Tg-Develop Colab](https://colab.research.google.com/github/tg-develop/voice-changer/blob/master-custom/Colab_RealtimeVoiceChanger.ipynb).

- **2. Install:** Start from the top and run the first cell.
<img src="../wokada-colab-img/colab1.png" alt="Colab Install" width="900">

- **3. Second Cell:** When it finishes (it will output `Done! Proceed with the next steps`), run the second cell.
<img src="../wokada-colab-img/colab2.png" alt="Colab Second Cell" width="600">

- **4. Ngrok:** Scroll to the last cell, place your [Ngrok token](https://dashboard.ngrok.com/get-started/your-authtoken) in the `TOKEN_HERE` field.
<img src="../wokada-colab-img/colab3.png" alt="Ngrok Token" width="600">

- **5. Launch:** Run the cell. (Optional) Under the token field, you can change the region selection for lower latency. Once it finishes downloading, click the generated Ngrok link to start the Web UI.

***
:::content-center
### Kaggle
:::

!!!danger Kaggle Service
**Check the [Kaggle Glossary](https://docs.aihub.gg/extra/glossary/#kaggle) for more info on Free Tier, Limits, Verification, Pricing and other things.**
!!!

#### <u>Account Setup</u>

- Start by making an account [here](https://www.kaggle.com/account/login?phase=startRegisterTab&returnUrl=%2F).

<img src="/img/cloud-services/kaggle-img/kaggle-sign-in.png" alt="Kaggle Sign In" width="575">

- Verify your account with a phone number. This is required to enable the "Internet" option in your notebooks, which is necessary for downloading models and dependencies.

<img src="/img/cloud-services/kaggle-img/kaggle-phone.png" alt="Kaggle Phone Verification" width="575">

#### <u>Notebook Creation & Setup</u>

- **Create:** Go to [Kaggle](https://www.kaggle.com) and click **Create** then **New Notebook** at the top left. 
<img src="/img/cloud-services/kaggle-img/new.png" alt="New Notebook" width="400"> 

- **Import:** Under your session's name click **File** then **Import Notebook**.
<img src="/img/cloud-services/kaggle-img/import.png" alt="Import Notebook" width="450">     

- **Link:** In the new window, click the **Link** tab and paste the following URL: `https://github.com/tg-develop/voice-changer/blob/master-custom/Kaggle_RealtimeVoiceChanger.ipynb`. Click **Import**.
<img src="/img/cloud-services/kaggle-img/link.png" alt="Link Tab" width="700"> 

- **Settings:** In the sidebar on the right, turn on the **Internet** switch. Make sure persistence is set to **Files and variables**.

<img src="/img/cloud-services/kaggle-img/kaggle-internet.png" alt="Internet" width="250"> 

- **GPU:** Turn on T4 x2 GPUs in the Accelerator settings.
<img src="/img/cloud-services/kaggle-img/kaggle-gpu.png" alt="GPU" width="250"> 

- **Save:** (Optional) Turn on "Save version" to save your progress.
<img src="/img/cloud-services/kaggle-img/kaggle-pers.png" alt="Persistence" width="250"> 

!!!warning
Your runtime will continue draining when you're not running any cells with this option on. 
!!!

#### <u>Installation & Tunnels</u>

- **Install:** Starting from the top, run the first installation cell. When it outputs `Done! Proceed with the next steps`, run the third cell.
<img src="../wokada-kaggle-img/install-1.png" alt="Install 1" width="900"> 
<img src="../wokada-kaggle-img/install-2.png" alt="Install 2" width="600"> 

- **Ngrok:** Put your token in the last cell.
<img src="../wokada-kaggle-img/token.png" alt="Token" width="600"> 

***
:::content-center
### Lightning.AI
:::

!!!danger Lightning.AI Service
**Check the [Lightning.AI Glossary](https://docs.aihub.gg/extra/glossary/#lightningai) for more info on Free Tier, Limits, Verification, Pricing and other things.**
!!!

#### <u>Create an Account</u>

- First, make an account with [Lightning Ai](https://lightning.ai).

<img src="/img/cloud-services/lightning-ai-img/signup.png" alt="LightningAI Signup" width="300">

- Make sure you verify yourself with a phone number. Once you've done that you will get an email that looks like this:

<img src="/img/cloud-services/lightning-ai-img/verification.png" alt="LightningAI Verification" width="400">

!!!danger Verification Time
You will need to wait 2-3 business days to become fully verified.
!!!

- **Studio:** Clone the [Wokada-TgDevelop-Fork Studio](https://lightning.ai/nick088/studios/wokada-tg-develop-fork).

<img src="/img/cloud-services/lightning-ai-img/lightning-ai-clone-studio.png" alt="Clone" width="300">

- **GPU:** Switch to a GPU environment (Studio Environment -> Switch To GPU).

<img src="/img/cloud-services/lightning-ai-img/gpu-setting.png" alt="GPU Settings" width="500">

- **Install:** Run the first cell to install, run the second cell to configure.

- **Tunnels:** In the third cell, choose your tunnel (Port Viewer recommended) and run it. Use the provided file drive to upload models and TensorBoard to monitor training.

- **File Management:** Use the **Teamspace Drive** button on the right sidebar to upload files.
<img src="/img/cloud-services/lightning-ai-img/teamspace-drive.png" alt="LightningAI Teamspace Drive" width="500">

- **Maintenance:** If you need to update the Program or start fresh, you can run the final cell in the notebook, "Delete everything". This will remove all downloaded files and configurations from your persistent storage, allowing for a clean installation by re-following the notebook with perhaps a changed branch variable.

***
:::content-center
## Usage
:::
Now that you have the Web UI running, the rest of the process is **identical to using a local installation.**

[!button text="Continue with the Local Guide" icon="arrow-right" target="blank"](https://docs.aihub.gg/realtime-voice-changer/local/tg-develops-w-okada-fork/#voice-models)

***
:::content-center
## Troubleshooting
:::

==- :icon-terminal: Getting Detailed Server Logs (Debug Mode)
The web interface (client) is just a control panel; the actual voice conversion and backend processes happen on the server. If the cloud server crashes or fails to launch properly, you can enable **Debug Mode** to read the exact error logs directly in your notebook's output cell.

To do this, you need to append the `--log-level debug` argument to the command that launches the server.

+++ Google Colab
1. Scroll to the bottom of your notebook to find the cell that starts the server.
2. Look for the execution command: `!./ML_Program`
3. Add the debug flag to the end of the command so it looks like this:
```bash
!./ML_Program --log-level debug
```
4. Run the cell again.

+++ Kaggle & Lightning.AI
1. Locate the final cell in your notebook/studio that actually starts the server.
2. Look for the execution command: `!./VoiceChanger`
3. Add the debug flag to the end of the command so it looks like this:
```bash
!./VoiceChanger --log-level debug
```
4. Run the cell again.
+++

The notebook output cell will now print detailed debug logs. If the server crashes, **copy the text output from that cell**. Save it to a `.txt` file, or paste it to a site like [Pastebin](https://pastebin.com/) to share with others when asking for support.

!!!info Other Log Levels
By default, the server runs on the `info` log level. While the server also supports `warning`, `error`, and `critical` levels, you should avoid using them for troubleshooting. They filter out background information, hiding the context developers need to figure out why your server crashed.
!!!
===

!!!info General Troubleshooting
Because the web interface and core server function the exact same way, most common errorsare identical to the local version.

[!button text="View Local General Troubleshooting" icon="tools" variant="secondary"](https://docs.aihub.gg/realtime-voice-changer/local/tg-develops-w-okada-fork/#troubleshooting)
!!!

***
###### ‎
:::content-center
#### `You have reached the end.`

[!badge variant="info" size="xl" corners="pill" icon="paper-airplane" iconAlign="right" text="Report Issues"](https://docs.aihub.gg/contributions/)
:::
