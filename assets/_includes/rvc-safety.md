***
#### Is this Program Safe?

RVC Models are PyTorch Models, a Python library used for AI.
PyTorch uses serialization via Pythons' Pickle Module, converting the model to a file.
Since pickle can execute arbitrary code when loading a model, it could be theoretically used for malware, but this software has a **built-in feature to prevent code execution along the model.**
Also, **HuggingFace has a [Security Scanner](https://huggingface.co/docs/hub/security-pickle#hubs-security-scanner)** which scans for any unsafe pickle exploits and uses also ClamAV for scanning dangerous files.
