Ecom GeoInsights: Enhancing Online Shopping with Big Data & Spatial Computing

Overview
Ecom GeoInsights utilizes big data and spatial computing technologies to transform the online shopping experience by analyzing eBay's extensive data. This project integrates Apache Spark, QGIS, and advanced machine learning techniques to uncover insights into product trends, sales distributions, and customer preferences based on geographic data. Our comprehensive analysis helps enhance strategic decision-making for sellers and improves shopping experiences for customers through interactive heatmaps, cluster maps, and predictive modeling.

Key Features
Spatial Analysis with QGIS: Visualize sales hotspots and trends across different regions using interactive, heat, and cluster maps.
Predictive Analysis Using Machine Learning: Implement machine learning models like Random Forest to predict prices and categorize sales data, aiding both buyers and sellers.
Interactive Dashboards with Tableau and GeoPandas: Navigate through dynamic visualizations to explore complex datasets intuitively.
Data Processing at Scale: Utilize Apache Spark for efficient big data processing, with support from Hadoop's distributed file system.
Machine Learning Integration
This project employs various machine learning models to enhance predictive accuracy and user experience:

Random Forest Classifier: Used for predicting product prices, helping users make informed purchasing decisions and allowing sellers to set competitive prices effectively. This model stands out for its high accuracy and robustness against overfitting, making it ideal for our diverse and voluminous datasets.
Logistic Regression: Applied for basic binary classification tasks within the dataset, useful for initial trend identification and benchmarking model performance.
Decision Tree Classifier: Provides a clear visualization of the decision-making process, useful for understanding feature importance and the structure of the data.
Support Vector Machine (SVM): Employs a kernel trick to handle non-linear decision boundaries, which is crucial for classifying complex datasets with multiple features.
K-Nearest Neighbors (KNN): A simple yet powerful model that classifies new data points based on a similarity measure (distance functions).
Each of these models contributes to a comprehensive machine learning strategy, enhancing the project's analytical capabilities and providing substantial benefits to both sellers and consumers.

Installation Prerequisites
Python 3.8 or later
Apache Spark
Hadoop (HDFS)
QGIS
Tableau (for optional visualization enhancements)
A web server if deploying web interface locally

Setup Instructions
Clone the Repository
git clone https://github.com/yourgithubusername/ecom-geoinsights.git
cd ecom-geoinsights

Set Up a Python Virtual Environment

python -m venv venv
source venv/bin/activate  # On Windows use `.\venv\Scripts\activate`

Install Required Python Libraries

pip install -r requirements.txt

Running the Application
Start the Django Web Server
sh
Copy code
python manage.py runserver
Access the Web Interface
Open a browser and navigate to http://127.0.0.1:8000/ to view the application.
Interacting with the Predictive Models
Use the provided interfaces to interact with the predictive models and explore different insights through the visualizations.

Application
![alt text](image.png)

Price Predictor
![alt text](image-2.png)

Big Data Insights:
![alt text](image-3.png)
![alt text](image-4.png)
![alt text](image-5.png)
![alt text](image-6.png)

Insights based on location:
![alt text](image-7.png)
![alt text](image-8.png)

Contributors
Vaibhav Gupta
Dhrumil Ankola
Viha B Raju
Suveda Niranjan
Harsh Gunwant

The team used Apache Spark for cluster computing, Tableau and GeoPandas for visualization, and QGIS for creating interactive maps to provide deeper insights into the data collected from eBay.