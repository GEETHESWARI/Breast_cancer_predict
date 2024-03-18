    BREAST CANCER PREDICTION 


      Breast cancer is the most common cancer amongst women in the world. It accounts for 25% of all cancer cases and affected over 2.1 Million people in 2015 alone. It starts when cells in the breast begin to grow out of control. These cells usually form tumors that can be seen via X-ray or felt as lumps in the breast area.        


 ABOUT THE DATASET:


1. Collecting the Dataset  :  

        Breast Cancer (WDBC) dataset is a widely used dataset in the field of  machine learning. This dataset consist of 569 rows and 33 coloumns.This dataset is obtained from Kaggle (link:https://www.kaggle.com/datasets/nancyalaswad90/breast-cancer-dataset/data).The dataset comprises a single CSV (Comma-Separated Values) file containing the attribute values for each instance, along with the corresponding class labels indicating whether the breast mass is benign (B) or malignant (M).
        In this data consists of the data of sample of biopsy collected from patients. The sample collected from them can help them diagonised the conditions based on the radius, texture, perimeter etc, and rule out that the patient has Benign Tumor (non-cancerous ,slow growing,do not metastasized,cells are normal) or Malignant Tumor(Cancerous, fast growing, metastasized, Cells are abnormal, Treatment needed).

2. Importing the library:

       Importing the libraries like pandas,numpy,seaborn and matplotlib. Using pandas to read the csv file and checking the shape, size of the data. 

3. Missing Values :

      Checking the dataset has missing by using isnull().sum(). And if there are missing values in the dataset handling it by using mean,median or mode.

4. EDA:

     Understanding the datset through visuvalization. Creating a correlation to check the correlation of the coloumns. Using the pairplots and heatmap  to see which coloumns are depend on each other.
     Correlated features can lead to multicollinearity, which affects model interpretability and stability. Highly correlated features provide redundant information, and including both may not improve model performance significantly. Removing correlated columns can reduce the dimensionality of the dataset, making training faster and more efficient.
     Encode the class labels from categorical (B, M) to numerical values (e.g., 0 and 1) to enable compatibility with machine learning algorithms.

5. Splitting the dataset: Separate the dataset into features (X) and labels (y). Extracting the 12 features columns from the dataset as the feature matrix (X) and the class labels column as the target vector (y).  

6. Train-Test Split: Split the dataset into training and testing subsets to evaluate the performance of machine learning models.

Machine Learning Algorithms:


* Logistic Regression: Logistic Regression is a linear classification algorithm that models the relationship between the input features and the probability of a binary outcome. Logistic Regression achieved the accuracy of
 91%

* K-Nearest Neighbors (KNN): The KNN algorithm is a non-parametric classification algorithm that assigns a class label to an instance based on the majority class labels of its k nearest neighbors in the feature space.  K-Nearest Neighbors achieved the accuracy of 90%

* GaussianNB :  GNB assumes that continuous attributes follow a Gaussian (normal) distribution within each class.
It estimates the mean (μ) and variance (σ²) for every feature in every class.The algorithm then predicts the probability of a dependent variable being classified into each group. GaussianNB achieved the accuracy of 90%.


Result :
  
   Overall, all the evaluated machine learning algorithms demonstrated strong performance in breast cancer  dataset. The top accuracy achieved algorithm is Logistic Regression.


