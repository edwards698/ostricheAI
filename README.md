
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
1. Go to the OpenAI [website](https://platform.openai.com/api-keys)and sign up for an account.
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
    prompt = "What is the capital of France?"
    response = get_gpt_response(prompt)
    print(f"Response: {response}")

```
