==- :icon-bug: Silent Crash / XHR Poll Error (Pro Audio & DJ Hardware)
If in a Wokada Fork, you click "Start Server" and the command-line window closes instantly without an error, followed by `[SIO] rconnection failed Error: xhr poll error` pop-ups in the browser:

- **Possible Cause:** You have Professional Audio or DJ **hardware drivers** installed (e.g., Native Instruments Traktor Kontrol). When the voice changer uses `PortAudio` to scan for audio devices on startup, querying an ASIO/hardware driver while its physical device is **unplugged** causes a fatal low-level C crash. This kills the server instantly and silently.

!!!info DAW Software is Safe
You do **not** need to uninstall your DAW (Traktor Pro 4, FL Studio, Ableton, etc.). The issue is strictly caused by the hardware drivers, not the music software itself.
!!!

**Solutions:**
- **Method 1 (Recommended): Disable the drivers**
  1. Right-click your Windows Start button and open **Device Manager**.
  2. Expand the **Sound, video and game controllers** category.
  3. Find your pro-audio hardware drivers (e.g., `Native Instruments Traktor Kontrol S8 Driver`).
  4. Right-click them and select **Disable device**. You can easily re-enable them later when you need to use your audio equipment.

- **Method 2: Uninstall the drivers**
  - If you no longer use the physical hardware, completely uninstall the specific hardware drivers from your system. The voice changer will open normally immediately after.

- **Method 3: Plug the hardware in**
  - Plugging your physical DJ Controller or Audio Interface into your PC and turning it on before starting the voice changer may prevent the driver from crashing when scanned.

- **Method 4 (Advanced): Hide the ASIO driver in Registry**
  - If you suspect an ASIO driver is causing the issue and Method 1 didn't work, you can temporarily hide it from Windows. Open the Registry Editor (`regedit`), navigate to `Computer\HKEY_LOCAL_MACHINE\SOFTWARE\ASIO`, right-click the folder of your specific audio software, and rename it (e.g., add `.backup` to the end). Rename it back when you want to use it again.
===