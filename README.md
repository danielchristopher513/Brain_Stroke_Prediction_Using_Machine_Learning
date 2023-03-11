
# Brainstroke Prediction

Kaggle dataset link : https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset

---
Libraries used for **dataset processing**
  + Numpy
  + Pandas
  
Libraries used for **graphical representation** 
  +  Matplotlib
  +  Seaborn

Libraries used for **Scaling and Oversampling** 
  + Sklearn.preprocessing
  + Imblearn

---
### PREPROCESSING
--- 

* **Removed the id column** – decreasing the dimension – did not add to insights in the data analysis.
```python
df = df.drop(['id'],axis=1)
```

* **Count for NULL values** are checked among the attributes of the dataset
```python
print(df.isna().sum())
```
  + Only BMI-Attribute had NULL values <br>
  + Plotted **BMI's value distribution** - **looked skewed** - therefore **imputed** the missing values using the **median**. <br>
  + Didn’t eliminate the records due to **dataset being highly skewed** on the target attribute – stroke and a good portion of the missing BMI values had accounted for positive stroke 

* The dataset was skewed because there were only few records which had a positive value for stroke-target attribute

* In the gender attribute, there were 3 types - Male, Female and Other. There was only 1 record of the type "other", Hence it was converted to the majority type – decrease the dimension

* Most of the attributes in the dataset were binary values – converting the numeric bin values into string bin values for **dummy encoding**.
  * Dummy encoding similar to one-hot encoding – Values in the binary ecoded columns are 1/0 – Additional attributes/columns created.

* **Random oversampling** done on the dataset to **balance the skew** in the target attributes.
  * Boosting the number of records in the minority class – records
---
### EDA - Exploratory Data Analysis
---

* Plotted **plots of each attribute** - Analyse **trends** if any – **plots:** pie, histogram.
* Plotted **relation of target attribute to other attributes** to find any correlation.
* Plotted the **heatmap** – correlation plot between the attributes.
  * Heatmap showed very less correlation between the attribute values.

---
### MODEL BUILDING
---

* Creating a train and test split of the oversampled dataset. (80-20)

Applied various Machine learning models for predictive analysis
1.	**Decision tree**
2.	**KNN**
3.	**XG-Boost**
4.	**Random forest**
5.	**Logistic regression**

Analysed the results generated using confusion matrix - accuracy, precision, recall and plotting the ROC plot and generating the AUC scores. <br>

**Accuracies calculated:**
1.	Decision tree       : **97.89%**
2.	KNN : **97.22%**
3.	XG-Boost : **97.48%**
4.	Random forest : **99.48%**
5.	Logistic regression : **76.34%**

Chosen model - **RANDOM FOREST**

Results were validated using the **k fold (20 splits) validation** for overfitting 
+ Accuracy:  95.01 <br>
For Random Forest
