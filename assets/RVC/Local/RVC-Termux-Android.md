---
icon: device-mobile
order: 1000
---

``Last update: March 17, 2026``

``Last Tested on Honor 90 Lite — Termux v0.118.3 — proot-distro v4.38.0 — Ubuntu 25.10 (Questing)``

***
:::content-center
## Introduction
:::

- This guide allows you to run **RVC Locally** on your Android phone via **Termux**, a Linux Terminal Emulator.

- After setup, it can work **without the Internet**. Setup time depends on your internet speed.

- **Performance depends on your phone's CPU speed.** It's recommended to only do inference. Long audios can cause the app to crash, it's best to split audios, especially on 6 GB RAM phones.

- TTS Offline is **not available**, as Applio uses the Microsoft Edge API.

!!!danger Warning
DO IT AT YOUR OWN RISK. There is a possibility of overheat or damage to your device, especially when Training or on older devices. This guide is more for experimenting rather than for actual heavy usage.
!!!


***
:::content-center
## Requirements
:::

| Requirement | Minimum | Recommended |
|---|---|---|
| **Storage** | ~6 GB + model storage | More depending on models/usage |
| **RAM** | 6 GB | 8 GB+ |
| **OS** | Android 5.0 | Android 10+ |
| **CPU Architecture** | aarch32 / armv7-a | aarch64 / arm64 |

!!!info CPU Architecture
Most modern phones use `aarch64` (also known as `arm64`). You can verify yours by running `uname -m` after downloading Termux.
!!!


***
:::content-center
## Download Termux
:::

Download Termux from its [GitHub Installation Page](https://github.com/termux/termux-app?tab=readme-ov-file#installation). The **F-Droid** method is recommended.


***
:::content-center
## Setup Environment :icon-terminal:
:::

Run each command in order inside Termux:

***

**1.** Install packages and set up Ubuntu in Termux. Allow storage access if prompted.
```bash
pkg update && pkg upgrade -y && termux-setup-storage && pkg install git proot proot-distro -y && proot-distro install ubuntu && proot-distro login ubuntu
```


!!!info What to expect
On a fresh Termux install, `pkg update` will first test all available mirrors and automatically pick the best one. This is normal and can take up to a minute. The rest of the command will then download and install Ubuntu inside Termux, which may take a few minutes depending on your connection speed.

If you have used Termux before, you may see a prompt like this during `pkg upgrade`:

```
Configuration file '/data/data/com.termux/files/usr/etc/bash.bashrc'
 ==> File on system created by you or by a script.
 ==> File also in package provided by package maintainer.
   What would you like to do about it ?
    Y or I  : install the package maintainer's version
    N or O  : keep your currently-installed version
*** bash.bashrc (Y/I/N/O/D/Z) [default=N] ?
```

This can appear for multiple config files. In most cases it is safe to type `Y` and press Enter to accept the maintainer's version.
!!!

***

**2.** Update package lists and the distribution:
```bash
apt update -y && apt dist-upgrade -y
```

***

**3.** Install required packages:
```bash
apt install git libportaudio2 -y
```

!!!info Python
Python does not need to be installed manually. The Applio installer downloads and manages its own Python 3.12 environment via UV.
!!!

!!!warning Realtime tab
The Realtime tab requires selecting audio input/output devices. On Android, proot has no access to the device audio layer, so no devices will appear and the Realtime tab cannot function. There is also no Virtual Audio Cable available on Android without root.
`libportaudio2` is still required above to prevent Applio from crashing on startup when it loads the tab.
!!!

***

**4.** Set the maximum HTTP/HTTPS push buffer size to 2 GB:
```bash
git config --global http.postBuffer 2097152000 && git config --global https.postBuffer 2097152000
```

***

**5.** Force HTTP/1.1 to prevent framing layer errors:
```bash
git config --global http.version HTTP/1.1
```

***

**6.** Ensure localhost is properly defined:
```bash
echo "127.0.0.1 127.0.0.0 localhost" >> /etc/hosts
```

***
:::content-center
## Applio Setup :icon-tools:
:::

**1.** Clone the Applio repository (uses the latest `main` branch by default):
```bash
git clone https://github.com/IAHispano/Applio && cd Applio
```

!!!info Specific Release
To pin to a specific release, append `--branch <your_branch_name> --single-branch` after the URL. For example:
```bash
git clone https://github.com/IAHispano/Applio --branch 3.6.2 --single-branch && cd Applio
```
!!!

***

**2.** Patch the installer and requirements before running them.

proot-distro has several limitations that break UV's default behaviour. The following patches address all of them:

- `run-install.sh` needs `sudo` removed (not available in proot), `UV_LINK_MODE=copy` and `UV_NO_CACHE=1` exported so UV installs directly into the venv without cross-filesystem hardlinks or cache references (both of which proot breaks), `--python-platform aarch64-unknown-linux-gnu` added so UV resolves aarch64 wheels instead of defaulting to x86_64, and its CUDA PyTorch index changed to the CPU one while keeping it as `--extra-index-url` so PyPI stays available for all other packages.
- `requirements.txt` hardcodes `+cu128` builds of torch/torchaudio/torchvision for Linux (no aarch64 wheels exist for these).

Run all patches in one go:
```bash
sed -i 's/sudo //g' run-install.sh \
&& sed -i '/^set -e/a export UV_LINK_MODE=copy\nexport UV_NO_CACHE=1' run-install.sh \
&& sed -i 's|uv pip install|uv pip install --python-platform aarch64-unknown-linux-gnu|g' run-install.sh \
&& sed -i 's|--extra-index-url https://download.pytorch.org/whl/cu[0-9]*|--extra-index-url https://download.pytorch.org/whl/cpu|g' run-install.sh \
&& sed -i 's|torch==\([^+;]*\)+cu[0-9]*|torch==\1|g' requirements.txt \
&& sed -i 's|torchaudio==\([^+;]*\)+cu[0-9]*|torchaudio==\1|g' requirements.txt \
&& sed -i 's|torchvision==\([^+;]*\)+cu[0-9]*|torchvision==\1|g' requirements.txt
```

!!!info Why this is future-proof
- `UV_LINK_MODE=copy` and `UV_NO_CACHE=1` fix proot filesystem limitations globally for the entire install, regardless of which proot distro or Ubuntu version is used.
- `--python-platform aarch64-unknown-linux-gnu` explicitly tells UV to resolve aarch64 wheels. Without this, UV defaults to x86_64 inside proot, installing binaries that cannot run on ARM.
- Keeping `--extra-index-url` means PyPI stays as the primary index. Torch and friends, which have no aarch64 wheels on PyPI, are pulled from the pytorch CPU index.
- `cu[0-9]*` matches any CUDA suffix (cu128, cu126, cu130, etc.), so the torch patches do not need updating when Applio bumps the CUDA version.
!!!


***

**3.** Install Applio:
```bash
chmod +x run-install.sh && ./run-install.sh
```

!!!warning UV not found on first run
The installer downloads UV to `~/.local/bin`, but that path is not in the current shell's PATH yet, so the first run will stop after installing uv saying it's needed to add it to PATH via restarting the shell (which is bash in our case).
This is expected. Run the following command to add UV to PATH and re-run the installer:
```bash
source $HOME/.local/bin/env && ./run-install.sh
```
`chmod +x` does not need to be run again.
!!!


***

**4.** Launch Applio:
```bash
chmod +x run-applio.sh && ./run-applio.sh
```

***

**5.** Wait until the terminal shows `Running on local URL: http://127.0.0.1:6969`. Then open your browser (in multitasking or window mode) and navigate to:
```
localhost:6969
```

!!!warning First launch
The first launch downloads required model files from HuggingFace, it's normal that it may take some time. You may notice the download speed drop significantly partway through as this is HuggingFace throttling the connection on certain files and recovers on its own.
!!!


***

**6.** To **exit**: press `Ctrl + C`, close the app, and fully stop it from the Termux notification by pressing **EXIT**.

***

**7.** To **resume later**:
```bash
proot-distro login ubuntu
cd Applio && ./run-applio.sh
```

***

**8.** To **update**:
```bash
proot-distro login ubuntu
rm -rf Applio
```
Then restart from Step 1 of the Applio Setup section.


***
## Applio Usage
Now that you have the web interface running, the rest of the process is **almost identical to using a Local Applio PC Installation.**

For all subsequent steps please continue by following the Local Applio PC Guide.

[!button text="Continue with the Local Applio PC Guide" icon="arrow-right" target="blank"](https://docs.aihub.gg/rvc/local/applio/#inference)


***
## Performance Examples

**NOTE:** Those benchmarks are based on the First Inference of a model on startup, which may contain a warmup time and future inferences might take less time.

==- *See benchmarks*
**Applio v3.2.7 on Ubuntu 24.04 (Noble)**

| Device | Audio Length | Conversion Time | Notes |
|---|---|---|---|
| Honor 90 Lite | 8 seconds | 69.08 seconds | None |
| Pixel 6 Pro (12 GB RAM) | 13 seconds | ~109 seconds | rmvpe + contentvec, EX kernel manager |
| Galaxy A9 2018 (6 GB RAM) | 10 seconds | ~147 seconds | Longer audio causes crash |

<img src="..\rvc-termux-android-img\appliov327-honor90lite-first-inference.png" alt="Proof of First Inference time on Applio V3.2.7 on Honor 90 Lite" width="300">


**Applio v3.6.2 on Ubuntu 25.10 (Questing) on Termux v0.118.3 with proot-distro v4.38.0**

| Device | Audio Length | Conversion Time | Notes |
|---|---|---|---|
| Honor 90 Lite | 8 seconds | 58.39 seconds | None |

<img src="..\rvc-termux-android-img\appliov362-honor90lite-first-inference.jpg" alt="Proof of First Inference time on Applio V3.6.2 on Honor 90 Lite" width="300">
===


***
:::content-center
## FAQ / Troubleshooting :icon-question:
:::

==- Is it possible to do it on an iPhone?
Termux is **Android only**. iPhone alternatives include:
- [iSH](https://ish.app/)
- [A-Shell](https://holzschu.github.io/a-Shell_iOS/)

!!!warning
Termux is not associated with either app above, and this guide may have issues with them.
!!!
===

==- Why is there no Mainline or other RVC Forks?
Applio is the easiest to use: it automatically creates the venv and allows direct file uploads via the WebUI, unlike Mainline. Moving files from phone storage to Termux Ubuntu is otherwise difficult. There was previously also easyGUI but it's no longer maintained now.
===

==- How to delete?
**Applio only:**
```bash
proot-distro login ubuntu
rm -rf Applio
```

**Everything:** Delete the entire Termux app.
===

==- How can I open the Web UI on other devices on the same network?

**1.** Open Termux and log into Ubuntu:
```bash
proot-distro login ubuntu
```

**2.** Find your local IP address:
```bash
apt install net-tools -y && ifconfig
```
Look for an IP in one of these ranges:
- `192.168.x.x`
- `10.x.x.x`
- `172.16.x.x` to `172.31.x.x`

**3.** Set the server name and launch:

- **Applio:**
```bash
export GRADIO_SERVER_NAME="0.0.0.0"
cd Applio && ./run-applio.sh
```
Then on the other device open `http://<your-phone-ip>:6969`.

**4.** To revert:
- **Applio:** Restart the Termux session, or run `unset GRADIO_SERVER_NAME`.
===

==- How can I share my Web UI to people on a different network?

!!!warning
Sharing publicly exposes your phone and consumes more resources. This is not recommended.
!!!

**1.** Log into Ubuntu:
```bash
proot-distro login ubuntu
```

**2.** Patch `run-applio.sh` to forward arguments to Python. Without this, `--share` is consumed by the shell script and never reaches `app.py`:
```bash
sed -i 's|python app.py --open|python app.py --open "$@"|' ~/Applio/run-applio.sh
```

**3.** Build or download the frpc binary needed for public tunnelling:

- For **aarch64 (pre-built, recommended):**
    - **Applio:**
    ```bash
    apt update && apt install wget -y && wget -O frpc_linux_aarch64_v0.2 "https://huggingface.co/Nick088/termux-built-arm64-files/resolve/main/pre-built-binaries/frpc_linux_aarch64_v0.2?download=true" && mv frpc_linux_aarch64_v0.2 ~/Applio/.venv/lib/python3.12/site-packages/gradio/frpc_linux_aarch64_v0.2
    ```

- For **other architectures (manually build):** check your arch with `uname -m` and replace `aarch64` in the destination path accordingly.
    - **Applio:**
    ```bash
    apt install golang-go -y && git clone https://github.com/huggingface/frp && cd frp && make frpc && mv bin/frpc ~/Applio/.venv/lib/python3.12/site-packages/gradio/frpc_linux_aarch64_v0.2 && cd ..
    ```

**4.** Launch with sharing enabled:

```bash
cd Applio && ./run-applio.sh --share
```

Wait for `Running on Public url` and share that link.

**5.** To revert (press `Ctrl+C` first), simply launch normally without `--share`:

```bash
./run-applio.sh
```

To fully restore all changes:
```bash
sed -i 's|python app.py --open "$@"|python app.py --open|' ~/Applio/run-applio.sh
rm -rf ~/frp && rm -rf ~/Applio/.venv/lib/python3.12/site-packages/gradio/frpc_linux_aarch64_v0.2 && apt purge golang-go -y
```
===

==- It crashes during inference
Ensure your phone has **at least 6 GB of RAM** and try using a shorter audio clip.
===

==- I get a "Read time out" error

<img src="..\rvc-termux-android-img\read-timeout.png" alt="Read Timeout Error" width="300">

This means your connection is too slow and uv pip is hitting its default timeout. Make sure you are still inside the Applio folder and try the following:

- Use a better internet connection, **or**
- Increase the UV HTTP timeout:
  - **Applio:** `export UV_HTTP_TIMEOUT=200 && ./run-install.sh`

If it still fails, increase the value beyond `200` and try again.
===

==- (NOT SUGGESTED) How to train?
!!!danger
Training may have issues. You need a very powerful phone with **more than 8 GB of RAM**. This is not recommended.
!!!

Train normally in Applio, check the [Local PC Guide for reference](https://docs.aihub.gg/rvc/local/applio/). If clicking **Start Training** produces an error like:

```
RuntimeError: [enforce fail at .../gloo/transport/tcp/device.cc:184] rv != -1. -1 vs -1. Permission denied
```

Press `Ctrl+C` and apply the fix:

- **Applio:**
```bash
cd ~/Applio
sed -i '/dist\.init_process_group(/,/)/s/^/#/' rvc/train/train.py
./run-applio.sh
```

Select your project, and click **Start Training**. Use very short datasets and a low batch size (2, 4, or 6) to reduce crash risk.

**Example (Honor 90 Lite with Applio v3.6.2, default settings):**
- Dataset: 1:58 min | Sample Rate: 40k | Architecture: V2
- Preprocess time: 15.25s
- Pitch extraction (rmvpe, CPU): 194.91s
- Embedding extraction (8 cores, CPU): 88.39s
- Index generated successfully
- ⚠️ Crashed shortly after the first training epoch began (shortly after the third step)

**Example (Honor 90 Lite with Applio v3.2.7):**
- Dataset: 1:58 min | Sample Rate: 40k | Architecture: V2
- Preprocess time: 21.29s
- Pitch extraction (rmvpe, 8 CPU cores): ~319.96s
- Embed extraction (contentvec): ~62.69s
- Index generated successfully
- ⚠️ Crashed while training the first epoch
===

==- How was the pre-built aarch64 wheel for praat-parselmouth made?

This was a requirement in an older Applio version (before 3.2.8-bugfix) and in easyGUI (now removed as no longer maintained). Kept here for reference and possible future usage.

!!!info Context
This was done on **Ubuntu 24.04 (Noble)** via proot-distro, using **Python 3.10** via the deadsnakes PPA, since that was the Python version required at the time.
!!!

1. In Termux (not Ubuntu), create a symlink to make files accessible:
```bash
ln -rs $PREFIX/var/lib/proot-distro/installed-rootfs $HOME/proot-distro-rootfs
```
2. Log into Ubuntu: `proot-distro login ubuntu`
3. Install build dependencies (required to compile praat-parselmouth from source):
```bash
apt install build-essential python3.10-dev libx11-dev -y
```
4. Run `pip3.10 install praat-parselmouth`. This builds from source and takes 30-40 minutes as no official pre-built wheel exists (see [this issue](https://github.com/YannickJadoul/Parselmouth/issues/100)).
5. Package it as a wheel:
```bash
python3.10 -m venv my_praat_env && source my_praat_env/bin/activate && pip install wheel && pip install praat-parselmouth && pip wheel --wheel-dir dist/ praat-parselmouth
```
6. Output: `./dist/praat_parselmouth-0.4.4-cp310-cp310-linux_aarch64.whl`
7. Access the file via **Material Files** (by Hai Zhang): grant full file access → Add Storage → External → Termux → proot-distro-rootfs → ubuntu → root → dist. Copy the `.whl` file to storage and upload to HuggingFace.
===

{{ include "troubleshooting/report-missing-issue.md" }}


###### ‎
:::content-center
#### `You have reached the end.`

[!badge variant="info" size="xl" corners="pill" icon="paper-airplane" iconAlign="right" text="Report Issues"](https://docs.aihub.gg/contributions/)
:::
