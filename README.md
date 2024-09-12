
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

 ### Section 1: Running OpenAI GPT Models
 Since GPT models like `gpt-3.5-turbo` or `gpt-4` are resource-intensive, it’s best to use OpenAI’s API to offload the heavy computation to their servers.