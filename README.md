# Durghotona GPT

Durghotona GPT is a web scraping and LLM-based application that can automatically collect and process accident news to generate an Excel file.

## Introduction

Welcome to Durghotona GPT's GitHub repository. This project aims to generate an accident dataset fully automatically. The program first visits a newspaper website specified by the user. It then collects accident news automatically using Selenium. The collected news is processed through an LLM specified by the user to generate an accident dataset. Currently, this application can scrape news from three websites in Bangladesh: First one is **Prothom Alo**, 2nd one is **The Daily Star**, and the 3rd one is **Dhaka Tribune**. The user can choose from three LLMs: **GPT-4, GPT-3.5, and Llama3**. This dataset can be useful for building Machine Learning models and policy decision-making.

This project was built as part of the author's thesis work. This work is accepted in 27th International Conference on Computer and Information Technology (ICCIT). The paper is available on IEEE Xplore. If you find this work useful, please give our paper a cite: [link](https://ieeexplore.ieee.org/document/11021969/)

## How to Use

There are two ways to use this program:

1. **Using the app as a web application**
2. **Using the app locally on the user's PC**

The explanation of each method is given below:

### Using it as a Web Application

The authors built this work as a Streamlit application and hosted it on Hugging Face Spaces. If you want to see a demo of this work, it is strongly recommended to use this method.

**Steps:**

1. Go to this [link](https://huggingface.co/spaces/Thamed-Chowdhury/Automated_Accident_Dataset). **If you face any loading issues, connect to a VPN and try again.**
2. You will see an interface like this:
   ![image](https://github.com/user-attachments/assets/082b690e-aec0-4db4-8629-0bfdc673f728)

3. Choose a newspaper from which you want to collect news.
4. Choose an LLM to process the news.
5. Click the 'Generate Dataset' button.
6. You will need to wait a few minutes, depending on your input, as the process takes some time.
7. Once the process is finished, you will see the generated dataset and can download it as a CSV file.
   ![image](https://github.com/user-attachments/assets/ee4d6921-1af6-40cf-81af-a1f8a0552ae1)

**Disclaimer:** Since this is only a demo, it has some limitations. It does not allow users to collect news from the "Dhaka Tribune" newspaper and does not allow to use GPT-3.5. Also, due to the costs involved in using the LLMs, a maximum of 20 news reports can be processed. **If you want to avoid these limitations, follow the second method**.

### Using it Locally on the User's PC

This method is for those who want to run the application on their own PC and avoid the limitations of the first method. The steps are given below. Note that we are using Anaconda for this purpose:

1. Download this repository and unzip it into a folder.
2. To use this app locally on your PC, you will need two API keys: one from OpenAI and another from Groq. You will need to make some changes to the downloaded files using these keys. The steps are as follows:
   
   i) Open the "LLM_automation_GPT" Python file. On line 17, paste your OpenAI API key inside the quotation marks as shown below. Then save and close the file:
   
   ![image](https://github.com/user-attachments/assets/803a8e51-bf2a-4d07-9a66-6d154cb9b496)

   ii) Now open the "LLM_automation_GPT35" Python file. Go to line 15 and paste your OpenAI API key as shown. Save and close the file.
   
   ![image](https://github.com/user-attachments/assets/8355a0f1-e049-4179-9b3c-3cddd0ba7364)

   iii) Now open the "LLM_automation_Groq" Python file. Go to line 17 and paste your Groq API key as shown. Save and close the file.
   
   ![image](https://github.com/user-attachments/assets/c7d2a5f4-2133-43ec-9977-c7cad1555728)

3. Next, open Anaconda Prompt and navigate to the folder where you have kept the downloaded files.
4. Create a virtual environment using Anaconda. The virtual environment must use Python 3.12.3. Here we are giving an example. Note that during this process, Anaconda might ask for permissions several times. You have to type "y" and press enter in these cases. In this example, we are naming our virtual environment `Accident_env` and ensuring our Python version is 3.12.3. To create a virtual environment, run the following command in Anaconda Prompt:
```
conda create -n Accident_env python=3.12.3 anaconda
```
![image](https://github.com/user-attachments/assets/18e70cfd-f19c-431f-928d-06c94f4d59cf)

5. After creating the virtual environment, we must activate the virtual environment in Anaconda and install the dependencies listed in the `requirements.txt` file using pip. To activate the virtual environment and install dependencies, run the following commands in Anaconda Prompt:
```
conda activate Accident_env
pip install -r requirements.txt
```
If the installation is successful, a window similar to the image below should appear:
![image](https://github.com/user-attachments/assets/fab95804-c8fc-4717-bc55-66e8a01ffdeb)



6. Once the installation is completed, type the following command in Anaconda Prompt:
```
streamlit run app.py
```
7. If everything is successful, a browser window will open up containing the web app, as shown below:
![image](https://github.com/user-attachments/assets/16df1c52-8156-4e1a-b781-dba704f507f8)

8. Now you are done! You can collect accident data to your heart's content 😉
