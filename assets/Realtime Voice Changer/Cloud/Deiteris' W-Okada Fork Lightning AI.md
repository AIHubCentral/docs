---
icon: ":zap:"
order: 2000
---
`Last update: August 6, 2025`
***
:::content-center
<img src="../lightning-img/lightning-ai-banner.png" alt="LightningAI Banner" width="600">
:::

:::content-center
## Introduction
:::
- This is a <u>[cloud-based](http://docs.aihub.gg/extra/glossary/#cloud-based)</u> alternative to run [Wokada Deiteris Fork](https://docs.aihub.gg/realtime-voice-changer/local/deiteris-w-okada-fork/#virtual-audio-cable), Realtime Voice Changer for calls/games, only for people who don't have a good PC GPU, via the <u>[Lightning.AI Service](http://docs.aihub.gg/extra/glossary/#lightningai)</u>.

!!!danger Lightning.AI Service
**Check the <u>[Lightning.AI Glossary](http://docs.aihub.gg/extra/glossary/#lightningai)</u> for more info on Free Tier, Limits, Verification, Pricing and other things.**
!!!

!!! Note on the Free Tier "10 Mins Inactivity Auto Sleep"
This doesn't affect when the Wokada Deiteris Fork is running, this is affected only if no cell is running or the site is closed, which will shutdown the studio session. So you don't have to check every 10 minutes the site after you're sure the server cell is running and you're using the Web User Interface after starting it.
!!!


***
## Virtual Audio Cable

#### A Virtual Audio Cable (VAC) is what you need to use the realtime voice changer on Discord & Games.

- A VAC (Virtual Audio Cable) makes a fake audio device, used to re-route the audio of different programs.
- In the context of the Wokada Deiteris Fork, it's used to get the output from the realtime voice changer as an input in other programs such as Discord.

!!! For Windows
Download this: <u>[VAC Lite (Virtual-Audio-Cable by Muzychenko)](https://software.muzychenko.net/freeware/vac470lite.zip)</u>.
(Be sure to not use any other VAC like VB Audio Cable.)
!!!

- Run `setup64` (not 64a) after extracting the zip to a new folder.
- After installing the VAC Lite, it may change your default audio system. Click **Yes** when it asks to open audio device settings (or press WIN+R and type "mmsys.cpl" if you closed it). Change your **Recording** and **Playback** devices back to your usual devices. Do the same for the default communication device.

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

For Arch / Arch-based Systems (Endeavour, Manjaro Linux), run in the terminal:
```bash
sudo pacman -Syu portaudio
```
!!!

***
## Create an Account   
#### 1. <u>Set up account.</u>
a. Start by making an account <u>[here](https://lightning.ai/)</u>. You can sign up using your email, Google, or GitHub account. Using a work or .edu email may result in faster verification.

<img src="../lightning-img/signup.png" alt="LightningAI Sign up" width="450" height="auto">

b. Depending on the chosen sign-up method, you may need to verify your account via Phone Number to get full access.

c. You can check more info about the different sign-up methods and trouble on the [Lightning.AI Create an Account Docs Page](https://lightning.ai/docs/overview/getting-started/create-account)


***
## Studio Setup & Installation

#### 2. <u>Access the Notebook</u>
a. After creating your Lightning.AI account, open the [Wokada-Deiteris-Fork Notebook](https://lightning.ai/nick088/studios/wokada-deiteris-fork?view=public&section=featured) and Clone it.

#### 3. <u>Activate GPU (Very Important!)</u>
a. If you aren't on a GPU environment by default, you must switch to a GPU environment. This is crucial for performance.
b. On the right-hand lateral menu, click on **Studio Environment** (the processor icon).
c. Click **Switch To GPU**, select an available GPU, and wait for the environment to restart.

#### 4. <u>Clone Repository and Install Dependencies</u>
a. Run the first code cell. This will download the latest version of the realtime voice changer and install necessary dependencies.
b. This step may take a few minutes to complete. It will print "Installed!" when finished.

#### 5. <u>Set Server Configuration</u>
a. Run the second code cell to apply the server configuration.
b. It will print "Server successfully configurated!" upon completion.


***
### Tunnels & Server Setup

#### 6. <u>Launch the Server via Tunnels</u>
This final code cell is the most important one—it starts the voice changer's server and uses a "tunneling" service to create a secure, public web address (URL) for you to access it from your own computer.

a. Navigate to the third code cell, titled "Start Server **using Tunnels**". This cell boots up the Wokada Deiteris Fork application inside your Lightning.AI Studio.

b. **Select a Tunnel:** A tunnel securely exposes the application running in your private cloud environment to the public internet. The notebook gives you five different services to do this. Choose one from the `Tunnel` code menu in the code cell.

    - **Port Viewer (Recommended & Default method)**
        - **How it works:** This is a built-in Lightning.AI feature. It's the most straightforward method as it doesn't require any external accounts or tokens.
        - **Steps:**
            1. Select "Port Viewer" from the `Tunnel` code.
            2. Click the + at the bottom of the right tab, click on Web Apps and install Port Viewer.
            3. Run the code cell. Wait for the output to show that the server is listening.
            4. In the right-hand sidebar of the Lightning.AI interface, click the **Web Apps** tab.
            5. Click on **Port Viewer** and then click **Add a new port**.
            6. Enter `18888` as the Port Number and optionally give it a name (e.g., "Voice Changer").
            7. Click your Port in Port Viewer, you can also click Open to open it in an external tab.
            8. You can optionally go back to the Jupyter session in the right-hand sidebar of the Lightning.AI interface, to check if any error appears in the code output.

    - **Ngrok (Fast, Popular & Reliable)**
        - **How it works:** Ngrok is a popular service that creates secure tunnels. It requires a free account and an authentication token.
        - **Steps:**
            1. Go to the [Ngrok Dashboard](https://dashboard.ngrok.com/get-started/your-authtoken) to get your free authtoken.
            2. In the notebook cell, paste your token into the `Token` field, replacing `'Ngrok | Horizon TOKEN'`.
            3. (Optional) To potentially reduce latency, select a geographical `Region` from the list of parameter options next to it, that is closest to you.
            4. Run the cell. The public Ngrok URL (ending in `ngrok.io`) will be printed in the output once the server is ready. Click on it to access the UI.

    - **Cloudflare (Easy, No Account Needed)**
        - **How it works:** This option uses Cloudflare's free `trycloudflare` service. It's very easy to use as it requires no accounts or tokens.
        - **Steps:**
            1. Select "Cloudflare" from the `Tunnel` code.
            2. Run the cell. The script will automatically download the necessary tools. After a few moments, a public URL (ending in `trycloudflare.com`) will be printed in the output. Click it to open the interface.

    - **LocalTunnel (No Account, Password Protected)**
        - **How it works:** LocalTunnel is another free service that doesn't require an account. For security, it generates a unique URL that is protected by a password.
        - **Steps:**
            1. Select "LocalTunnel" from the `Tunnel` code.
            2. Run the cell.
            3. The output will display two key pieces of information: the public URL (ending in `loca.lt`) and a `Local Tunnel Password` below it.
            4. Click the URL. A new page will ask for a password.
            5. Copy the password from the notebook output and paste it into the password prompt in your browser to access the voice changer.

    - **Horizon (Fast, Requires Account & ID)**
        - **How it works:** Horizon is another tunneling service that requires a free account and a personal ID for authentication.
        - **Steps:**
            1. Go to the [Horizon Dashboard](https://hrzn.run/dashboard/) and sign up. On the second step of the setup, you will see a command like `hrzn login YOUR_ID`. Copy that `YOUR_ID` part.
            2. In the notebook cell, paste this ID into the `Token` field.
            3. Run the cell. The first time you use it, the output may ask you to authorize the connection by clicking a link (`https://hrzn.run/dashboard/settings/cli-token-requests/...`). Click this link and approve the request in your Horizon dashboard.
            4. The public Horizon URL (ending in `hrzn.run`) will then be printed in the output. Click it to access the UI.

c. After configuring your chosen tunnel, run the cell. The first time you run it, it will download the necessary voice models, which might take a minute or two.

d. Once the setup is complete, the output will display a message: **"--------- SERVER READY! ---------"**, followed by your public URL. Click this link to open the Wokada Deiteris Fork interface and start using the voice changer.

!!!warning Note:
The server runs in the foreground. If you stop the cell or close the Lightning.AI site, the server will shut down. Keep the cell running to use the program.
!!!


***
## Usage
***

Now that you have the web interface running via Lightning.AI, the rest of the process is **identical to using a local installation.**

For all subsequent steps, including audio routing, application settings, and model usage, please continue by following the Local PC guide.

[!button text="Continue with the Local PC Guide" icon="arrow-right" target="blank"](https://docs.aihub.gg/realtime-voice-changer/local/deiteris-w-okada-fork/#voice-models)


***
## Maintenance
***
#### Deleting Everything
If you need to update the Wokada Deiteris Fork or start fresh, you can run the final cell in the notebook, "Delete everything". This will remove all downloaded files and configurations from your persistent storage, allowing for a clean installation.


***
###### ‎
:::content-center
#### `You have reached the end.`

[!badge variant="info" size="xl" corners="pill" icon="paper-airplane" iconAlign="right" text="Report Issues"](https://discord.gg/aihub)
:::