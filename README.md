### 🧠 Depression Detection Using Brain MRI Scan
This project uses deep learning and image processing techniques to analyze brain MRI scans and detect potential signs of depression by identifying patterns in grayscale intensity.

### 🎯 Goal: 
🩺 Automatically detect depression using MRI brain scans.

🧠 Uses image processing to convert MRI RGB images into grayscale for feature extraction.

🤖 Applies deep learning models for classification and report generation.

🏥 Can assist doctors and researchers in early detection of mental health conditions.

### ❗ Problem Statement
🧠 Mental Health: A Silent Crisis
Depression is one of the most widespread yet underdiagnosed mental health conditions, affecting over 300 million people globally, according to the WHO. Despite its prevalence, it often remains unnoticed or untreated due to social stigma, lack of awareness, and limited access to mental health diagnostics.

### 🩺 Types of Depression Studied:
Major Depressive Disorder (MDD) – Insomnia, weight loss, worthlessness

Bipolar Disorder (BD) – Mood swings, high/low phases

Dysphoric Disorder (DC) – Fatigue, anxiety, sleep change

Psychiatric Disorder (HC) – Hallucinations, delusions

### 🧪 The Challenge
Diagnosing depression typically relies on self-reported symptoms, interviews, and psychological evaluations — all of which are subjective and may vary based on a patient's ability or willingness to communicate. There is no universally accepted biological marker for diagnosing depression, making early detection challenging.

### 🧬 The Opportunity
Recent advancements in neuroimaging technologies like Magnetic Resonance Imaging (MRI) and deep learning have opened new possibilities. MRI can detect structural and functional abnormalities in the brain that may correlate with depressive states. By leveraging automated image processing and AI, we can identify visual biomarkers of depression in MRI scans.

### 🎯 Objective
To develop a system that can:

Accept brain MRI scans as input

Preprocess and convert them into a form suitable for analysis

Use deep learning models to analyze patterns in grayscale intensity

Classify the brain scan based on possible indicators of depression

Output a diagnostic report that can assist medical professionals in identifying early signs of depression

### 💡 Why This Matters
Provides a non-invasive, objective, and automated approach to detect depression

Can assist psychiatrists and radiologists by augmenting human analysis

Has the potential to reduce diagnosis time, enabling earlier treatment

Bridges the gap between medical imaging and mental health diagnosis




### 🧪 Literature References
## 📚 Literature References

1. [ A neural network-based method for brain abnormality detection in MR images using Zernike moments and geometric moments](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=7a713a9a3409f63f21215d7e03dbd3d457dcf04b)

2. [Detection of brain tumor from MRI images by using segmentation & SVM](https://www.researchgate.net/profile/Amit-Pimpalkar/publication/328784445_BRAIN_TUMOR_DETECTION_USING_OBJECT_LABELING_ALGORITHM_SVM/links/5be2e0f04585150b2ba57bec/BRAIN-TUMOR-DETECTION-USING-OBJECT-LABELING-ALGORITHM-SVM.pdf)
   
3. [Detection of tumor in MRI images using artificial neural networks](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=31132cd944c914f7c2a71d098195b8e01d388eb1)
   
4. [A Review on Automated Brain Tumor Detection and Segmentation from MRI of Brain](https://arxiv.org/abs/1312.6150)


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

```bash
# Clone the repository
git clone https://github.com/yourusername/depression-mri-detection.git

# Change directory
cd depression-mri-detection

# Install requirements
pip install -r requirements.txt

# Run the analysis
python main.py --input path/to/mri/image

```
### OutPut

#### Screen 1:

![image](https://github.com/user-attachments/assets/34e86bbd-cc92-4275-b13e-2e2ebedc1afb)

#### Screen 2:

![image](https://github.com/user-attachments/assets/58353ffd-ce3c-4383-abd7-7c56758a7891)


### 👩‍💻 Author
Rashmi Manoj Katariya, Prof. M.M.Patil

### 📄 License
This project is open for educational and research purposes. Please contact the authors for commercial use or collaboration.
