
![ostrichAIImage](https://github.com/user-attachments/assets/1ba87e97-e8fc-49b2-9107-29e30c5c929e)
# OstricheAI
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
python3 run.py
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
2. Locate the file you want to run, in this case, `run_ai.py.py`.
3. Run the file with the following command:
```shell
python run_ai.py
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

# Recognition in real-time with OpenCV On a Raspberry pi 5
With face recognition, we not only identify the person by drawing a box on his face but we also know how to give a precise name. With OpenCV and Python, through a database, we compare the person’s photo and we know how to identify it precisely.

we will use as a basis a code created by `Adam Geitgey` and this is the original [GitHub Project](https://github.com/ageitgey/face_recognition) repository of Github 

1. Installations
The first library to install is `opencv-python`, as always run the command from the terminal.
```shell
pip install opencv-python
```
Proceed with `face_recognition`, this too installs with pip.
```shell
pip install face_recognition
```
2. Face recognition on image
To make face recognition work, we need to have a dataset of photos also composed of a single image per character and comparison photo. For example, in our example, we have a dataset consisting of 1 photo each of `Edgar_Lungu`,`Revy_Mwanawasa`,`Frederick_Chiluba`,`Kenneth_Kaunda`.

And in the comparison, we will use the photo of `Edgar_Lungu`

```python
import cv2
import face_recognition
```
## Face encoding first image
With the usual OpenCV procedure, we extract the image, in this case, Messi1.webp, and convert it into RGB color format. Then we do the “face encoding” with the functions of the Face recognition library.

```python
img = cv2.imread("Revy_Mwanawasa.png")
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_encoding = face_recognition.face_encodin
gs(rgb_img)[0]
```
## Face encoding second image
Same procedure for the second image, we only change the name of the variables and obviously the path of the second image, in this case: images/Messi.webp.

```python
img2 = cv2.imread("images_data_set/Edgar_Lungu.png")
rgb_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
img_encoding2 = face_recognition.face_encodings(rgb_img2)[0]
```
### Comparison of images
With a single line, we make a simple face comparison and print the result. If the images are the same it will print True otherwise False.
```python
result = face_recognition.compare_faces([img_encoding], img_encoding2)
print("Result: ", result)
```
# Encode all faces in the dataset

Now we have to encode all the images in our database, so that through the webcam video stream if it finds the match it shows the name otherwise it says “name not found”.

This is a function of the file I have prepared and it simply takes all the images contained in the `images_data_set/ directory` and encodes them. In our case, there are 5 images.

### Encode faces from a directory
```python
sfr = SimpleFacerec()
sfr.load_encoding_images("images_data_set/")
```
# Face recognition in real-time on a webcam
Even for face recognition in real-time, the procedure is similar to that of a single image but with something more. As a first step remember to `clone`
```shell
git clone https://github.com/edwards698/ostricheAI.git
```
### OR
 `download` the files from the link terminal and among the various Python files you will also find `visual.py`, remember that this is not a library so to include it in your project, put this file in the same folder and these are the correct lines of code to start.

```python
import cv2
from simple_facerec import SimpleFacerec
```
# Take webcam stream
With a simple Opencv function, We take the webcam stream and loop it
```python
# Load Camera
cap = cv2.VideoCapture(0)# choose the Webcam that you want to use starting from 0
while True:
ret, frame = cap.read()
```
# Face location and face recognition
Now we identify the face passing the frame of the webcam to this function detect_known_faces(frame). It will give us the name of the person and an array with the position at each moment of the movement.

```python 
# Detect Faces
face_locations, face_names = sfr.detect_known_faces(frame)
for face_loc, name in zip(face_locations, face_names):
y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
```
# Show name and rectangle
Now that we have all the elements we show them with OpenCV.
```python
        cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)
cv2.imshow("Frame", frame)
key = cv2.waitKey(1)
if key == 27:
break
```
# Now you can do some test facial recognition on a Raspberry Pi 5
You can clone the following command into your terminal and download the files by simply runing:

```shell
git clone https://github.com/edwards698/ostricheAI.git

```
Now that you have cloned the repository, follow these steps to run the specific file:
1. Navigate to the project directory:
```shell
cd ostricheAI
```
2. Locate the file you want to run, in this case, `main_video.py`.
3. Run the file with the following command:
```shell
python main_video.py
```

 