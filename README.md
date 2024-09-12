
![ostrichAIImage](https://github.com/user-attachments/assets/1ba87e97-e8fc-49b2-9107-29e30c5c929e)
# ostricheAI
OpenAI GPT models and Meta's LLaMA models on a Raspberry Pi 5. This guide focuses on efficient ways to interact with these models by leveraging APIs and lightweight model setups.

# Hardware Setup
Before starting, make sure your Raspberry Pi 5 is set up with the following:
To get started with your Raspberry Pi, you’ll need the following:

* a power supply
* boot media (e.g. a microSD card with ample storage and speed) atleast 32GB and above.

You can set up your Raspberry Pi as an interactive computer with a desktop, or as a headless computer accessible only over the network. To set your Raspberry Pi up headless, you don’t need any additional peripherals: you can preconfigure a hostname, user account, network connection, and SSH when you install an operating system. If you want to use your Raspberry Pi directly, you’ll need the following additional accessories:

* display
* cable to connect your Raspberry Pi to your display
* keyboard
* mouse

# Power supply
The following table shows the USB-PD power mode required to power various Raspberry Pi models. You can use any high-quality power supply that provides the correct power mode.

| Model          | Power supply (voltage/current)                | Raspberry Pi power supply|
|----------------|-----------------------------------------------|--------------------------|
| `Raspberry Pi 5` | `5V/5A, 5V/3A limits peripherals to 600mA`      | `27W USB-C power supply`   |

 Getting started with your Raspberry Pi and setting up the Raspberry pi  [follow this instruction here](https://www.raspberrypi.com/documentation/computers/getting-started.html)

 # Section 1: Running OpenAI GPT Models
 Since GPT models like `gpt-3.5-turbo` or `gpt-4` are resource-intensive, it’s best to use OpenAI’s API to offload the heavy computation to their servers.

 ### Step 1: Install Python and Dependencies
First, ensure your environment is set up, and install the required dependencies:

```shell
sudo apt update
```
This will updates the list of available packages and their versions stored in the system's package index.
```shell
sudo apt install python3-pip
```
After Installation is succesful, run the the following command below:
```shell
python --version

```
you should see `python 3.12.6` If this is not possible, you can also use a Python installer from [www.python.org](https://www.python.org/)  to install python3 or other versions 

After that run the command below:
```shell
pip3 install openai
```
The OpenAI Python library provides convenient access to the OpenAI REST API from any Python 3.7+ application. The library includes type definitions for all request params and response fields, and offers both synchronous and asynchronous clients powered by `httpx`.

### Step 2: Get Your OpenAI API Key
1. Go to the OpenAI [website](https://platform.openai.com/api-keys) and sign up for an account.
2. Generate an API key from your OpenAI account dashboard.

### Step 3: Write Python Script to Test OpenAI API
Create a Python file (e.g., `run_openai_gpt.py`) and use the following code to interact with the API:
```py
'''
Author: Edward Phiri Jr.
Date: 12/09/2024
'''
import openai

# Set your API key here
openai.api_key = 'your-api-key-here'

def get_gpt_response(prompt):
    response = openai.Completion.create(
        model="gpt-3.5-turbo",  # You can also use gpt-4
        prompt=prompt,
        max_tokens=100,
        temperature=0.7
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    prompt = "What is the capital of Zambia?"
    response = get_gpt_response(prompt)
    print(f"Response: {response}")

```
Replace `your-api-key-here` with your actual API key.

### Step 4: Run the Script
Run the Python script to make an API call to OpenAI’s servers:
```shell
python3 run_openai_gpt.py
```

The response should be displayed in your terminal. You can customize the prompt to test different queries.

You can clone the following command into your terminal and download the files by simply runing:

```shell
git clone https://github.com/edwards698/ostricheAI.git

```
Now that you have cloned the repository, follow these steps to run the specific file:
1. Navigate to the project directory:
```shell
cd ostricheAI
```
2. Locate the file you want to run, in this case, `run_openai_gpt.py`.
3. Run the file with the following command:
```shell
python run_openai_gpt.py
```

That's it! Now you modify and run the program and access its contents.

# Section 2: Running Meta's LLaMA Model on Raspberry Pi 5
LLaMA models are larger and need to be run locally. However, running the full-size LLaMA model is impractical on a Raspberry Pi due to limited hardware resources. Instead, I'll show you how to run a smaller quantized version of the LLaMA model using llama.cpp to optimize for the Raspberry Pi.

### Step 1: Install Required Packages
First, install the required packages:
```shell
sudo apt update
sudo apt install build-essential git cmake python3-pip
pip3 install torch transformers
```
### Step 2: Clone the llama.cpp Repository
Clone the optimized LLaMA codebase that allows you to run quantized models efficiently:
```shell
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp
```
### Step 3: Build the LLaMA Model
Use `CMake` to build the llama.cpp project:
```shell
mkdir build
cd build
cmake ..
make
```
### Step 4: Download LLaMA Model Weights
You will need to request access to the LLaMA model weights from Meta. [visit Hugging face](https://huggingface.co/meta-llama/Meta-Llama-3.1-8B-Instruct). Read and agree to the license agreement. Fill in your details and accept the license, and click on submit. Once your request is approved, you'll be granted access to all the Llama 3 models.

Once you have the weights, convert them into a format suitable for llama.cpp and place them in the `models`/ directory.

### Step 5: Quantize the Model
Quantization is key to making LLaMA run on low-resource devices like the Raspberry Pi. You can quantize the model using:

```shell
python3 convert.py --model llama_model_path --out models/quantized_llama
```
This will generate a quantized model that can run more efficiently on your Raspberry Pi.

### Step 6: Run LLaMA
Finally, run the LLaMA model on the Raspberry Pi:

```shell
./main -m models/quantized_llama.bin -p "Tell me a joke."
```
This will load the model and generate a response to the prompt.