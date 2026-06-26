==- :icon-code: Model Weight Converter (.safetensors ↔ .pth)
- This utility allows you to convert model weights **both ways**: PyTorch (`.pth`) to Safetensors (`.safetensors`), and Safetensors (`.safetensors`) back to PyTorch (`.pth`).
- **Safetensors ➜ PyTorch:** W-Okada saves imported models internally as `.safetensors` files inside your `model_dir` folder. If you accidentally deleted your original `.pth` files, you can use this script to recover them.
- **PyTorch ➜ Safetensors:** You can also convert standard `.pth` weights to `.safetensors` for safer sharing, faster loading, or local archiving.

!!! Secure & Clean
This converter is standard, lightweight boilerplate using PyTorch and Hugging Face APIs [1]. It features basic error handling and utilizes `weights_only=True` to safely load weights without executing arbitrary code.
!!!

#### Step 1: Install Requirements
+++ Local PC
- You must have Python installed on your PC.
- Open your terminal or command prompt (cmd) and run:
  ```bash
  pip install torch safetensors
  ```
+++ Cloud Services
- **For Notebooks (Google Colab & Kaggle):** Run this command inside a new code cell:
  ```bash
  !pip install torch safetensors
  ```
- **For Studios (Lightning.AI):** Open a new terminal tab and run:
  ```bash
  pip install torch safetensors
  ```
+++

#### Step 2: Create the Script
- Create a file named **`safetensors-pytorch-converter.py`** and paste the code below into it. 
- *(For Google Colab & Kaggle, you can automatically create this file by running a new code cell with `%%writefile safetensors-pytorch-converter.py` as the very first line, followed by the script below).*

  ```python
  #  RVC Model Weight Converter (PTH <-> Safetensors)


  import argparse
  import os
  import sys
  import torch
  from safetensors.torch import load_file, save_file

  def convert_pth_to_safetensors(pth_path, output_path):
      # Loads a PyTorch .pth model and exports its state_dict to Safetensors
      print(f"Reading PyTorch weights from: {pth_path}")
      try:
          # weights_only=True prevents execution of arbitrary code during load
          weights = torch.load(pth_path, map_location="cpu", weights_only=True)
          
          # Unpack the state_dict if the file contains training metadata
          if isinstance(weights, dict) and "state_dict" in weights:
              weights = weights["state_dict"]
              
          print(f"Writing Safetensors weights to: {output_path}")
          save_file(weights, output_path)
          print("Conversion successful.")
      except Exception as e:
          print(f"Error during PTH conversion: {e}", file=sys.stderr)


  def convert_safetensors_to_pth(safetensors_path, output_path):
      # Loads a Safetensors model and exports it as a PyTorch .pth file
      print(f"Reading Safetensors weights from: {safetensors_path}")
      try:
          weights = load_file(safetensors_path, device="cpu")
          print(f"Writing PyTorch weights to: {output_path}")
          torch.save(weights, output_path)
          print("Conversion successful.")
      except Exception as e:
          print(f"Error during Safetensors conversion: {e}", file=sys.stderr)


  def main():
      parser = argparse.ArgumentParser(
          description="Convert RVC weights between PyTorch (.pth) and Safetensors formats."
      )
      parser.add_argument(
          "input_file", 
          type=str, 
          help="Path to the .pth or .safetensors file to convert"
      )
      parser.add_argument(
          "-o", "--output", 
          type=str, 
          default=None, 
          help="Optional custom output path"
      )

      args = parser.parse_args()
      input_path = args.input_file

      if not os.path.exists(input_path):
          print(f"Error: The file '{input_path}' does not exist.", file=sys.stderr)
          sys.exit(1)

      file_name, file_ext = os.path.splitext(input_path)
      ext = file_ext.lower()

      if ext == ".pth":
          output_path = args.output if args.output else f"{file_name}.safetensors"
          convert_pth_to_safetensors(input_path, output_path)
      elif ext == ".safetensors":
          output_path = args.output if args.output else f"{file_name}.pth"
          convert_safetensors_to_pth(input_path, output_path)
      else:
          print("Error: Input file must be a .pth or .safetensors file.", file=sys.stderr)
          sys.exit(1)


  if __name__ == "__main__":
      main()
  ```

#### Step 3: Run the Script
+++ Local PC
1. Place your target file (`.safetensors` or `.pth`) in the same folder as `safetensors-pytorch-converter.py`.
2. Open your command prompt (cmd) or terminal in that folder.
3. Run the script by passing your filename:

   **To convert Safetensors to PyTorch (.pth):**
   ```bash
   python safetensors-pytorch-converter.py "model.safetensors"
   ```

   **To convert PyTorch (.pth) to Safetensors:**
   ```bash
   python safetensors-pytorch-converter.py "model.pth"
   ```
+++ Cloud Services
1. Find the path to your target file (`.safetensors` or `.pth`) in your cloud workspace or notebook file manager.
2. Execute the conversion:
   - **For Notebooks (Google Colab & Kaggle):** Run the script using `!python` in a new code cell:
     ```bash
     !python safetensors-pytorch-converter.py "/path/to/model.safetensors"
     ```
   - **For Studios (Lightning.AI):** Open your Lightning Studio terminal and run:
     ```bash
     python safetensors-pytorch-converter.py "/path/to/model.safetensors"
     ```
+++
===
