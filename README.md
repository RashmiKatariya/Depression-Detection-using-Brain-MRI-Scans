### 🧠 Depression Detection Using Brain MRI Scan
This project uses deep learning and image processing techniques to analyze brain MRI scans and detect potential signs of depression by identifying patterns in grayscale intensity.

### 🎯 Goal: 
🩺 Automatically detect depression using MRI brain scans.

🧠 Uses image processing to convert MRI RGB images into grayscale for feature extraction.

🤖 Applies deep learning models for classification and report generation.

🏥 Can assist doctors and researchers in early detection of mental health conditions.

### 📚 Problem Background
Depression is a serious and common medical illness that negatively affects:

Mood and feelings

Thinking patterns

Daily functioning and behavior

### 🩺 Types of Depression Studied:
Major Depressive Disorder (MDD) – Insomnia, weight loss, worthlessness

Bipolar Disorder (BD) – Mood swings, high/low phases

Dysphoric Disorder (DC) – Fatigue, anxiety, sleep change

Psychiatric Disorder (HC) – Hallucinations, delusions

### 🧪 Literature References
Neural Networks for Brain Abnormality Detection – E. Lashkari

Tumor detection using SVM – Swapnil R. Telrandhe et al.

MRI-based cancer classification – Syed & Narayanan

Gabor feature-based neural networks – AmirEhsan Lashkari

### 🧬 Technologies Used
![image](https://github.com/user-attachments/assets/eae0b432-1a99-474d-afc5-386401d683fb)

### 🧰 Module Breakdown
1. 📥 MRI Image Input
Takes patient MRI scan images as input

2. 🔧 Preprocessing
Resizing, renaming, and converting to grayscale

3. 🧠 Deep Learning Analysis
Trained models extract patterns for detecting depression

4. 📄 Classification & Reporting
Output report indicating depression class or severity

### 🖼️ Image Conversion Example

RGB Image -> Gray scale Image

![1004](https://github.com/user-attachments/assets/ef15a66d-3dbe-4717-aa93-6dc72686e930)  ![1015](https://github.com/user-attachments/assets/b2957184-3333-41c6-999a-76c8fc4aa5a9)


### 📌 System Design
![image](https://github.com/user-attachments/assets/680f66d5-f9c5-4631-a4cb-ec691e85aadb)


### 🏗️ System Architecture
MRI Input → Preprocessing → DL Model → Classification → Output Report

### 🧪 Sample Data
⚠️ Note: The MRI datasets used in this project are private and cannot be shared publicly.
To run the project, you may use your own dataset following the same structure.

### 📋 How to Run
##### Clone the repository

git clone https://github.com/yourusername/depression-mri-detection.git

##### Change directory

cd depression-mri-detection

##### Install requirements (if any)

pip install -r requirements.txt

##### Run the analysis

python main.py --input path/to/mri/image

### OutPut

#### Screen 1:

![image](https://github.com/user-attachments/assets/34e86bbd-cc92-4275-b13e-2e2ebedc1afb)

#### Screen 2:

![image](https://github.com/user-attachments/assets/58353ffd-ce3c-4383-abd7-7c56758a7891)


### 👩‍💻 Author
Rashmi Manoj Katariya, Prof. M.M.Patil

### 📄 License
This project is open for educational and research purposes. Please contact the authors for commercial use or collaboration.
