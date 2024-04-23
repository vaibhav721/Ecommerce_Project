<h1 align="center">Ecom GeoInsights: Enhancing Online Shopping with Big Data & Spatial Computing</h1>
<h2>Overview</h2>
<p>Ecom GeoInsights utilizes big data and spatial computing technologies to transform the online shopping experience by analyzing eBay's extensive data. This project integrates Apache Spark, QGIS, and advanced machine learning techniques to uncover insights into product trends, sales distributions, and customer preferences based on geographic data. Our comprehensive analysis helps enhance strategic decision-making for sellers and improves shopping experiences for customers through interactive heatmaps, cluster maps, and predictive modeling.</p>
<h2>Key Features</h2>
<ul>
    <li><strong>Spatial Analysis with QGIS:</strong> Visualize sales hotspots and trends across different regions using interactive, heat, and cluster maps.</li>
    <li><strong>Predictive Analysis Using Machine Learning:</strong> Implement machine learning models like Random Forest to predict prices and categorize sales data, aiding both buyers and sellers.</li>
    <li><strong>Interactive Dashboards with Tableau and GeoPandas:</strong> Navigate through dynamic visualizations to explore complex datasets intuitively.</li>
    <li><strong>Data Processing at Scale:</strong> Utilize Apache Spark for efficient big data processing, with support from Hadoop's distributed file system.</li>
</ul>
<h2>Machine Learning Integration</h2>
<p>This project employs various machine learning models to enhance predictive accuracy and user experience:</p>
<ul>
    <li><strong>Random Forest Classifier:</strong> Used for predicting product prices, helping users make informed purchasing decisions and allowing sellers to set competitive prices effectively. This model stands out for its high accuracy and robustness against overfitting, making it ideal for our diverse and voluminous datasets.</li>
    <li><strong>Logistic Regression:</strong> Applied for basic binary classification tasks within the dataset, useful for initial trend identification and benchmarking model performance.</li>
    <li><strong>Decision Tree Classifier:</strong> Provides a clear visualization of the decision-making process, useful for understanding feature importance and the structure of the data.</li>
    <li><strong>Support Vector Machine (SVM):</strong> Employs a kernel trick to handle non-linear decision boundaries, which is crucial for classifying complex datasets with multiple features.</li>
    <li><strong>K-Nearest Neighbors (KNN):</strong> A simple yet powerful model that classifies new data points based on a similarity measure (distance functions).</li>
</ul>
<h2>Installation Prerequisites</h2>
<ul>
    <li>Python 3.8 or later</li>
    <li>Apache Spark</li>
    <li>Hadoop (HDFS)</li>
    <li>QGIS</li>
    <li>Tableau (for optional visualization enhancements)</li>
    <li>A web server if deploying web interface locally</li>
</ul>
<h2>Setup Instructions</h2>
<ol>
    <li><strong>Clone the Repository</strong><br>
        <code>git clone https://github.com/yourgithubusername/ecom-geoinsights.git</code><br>
        <code>cd ecom-geoinsights</code>
    </li>
    <li><strong>Set Up a Python Virtual Environment</strong><br>
        <code>python -m venv venv</code><br>
        <code>source venv/bin/activate  # On Windows use `.\venv\Scripts\activate`</code>
    </li>
    <li><strong>Install Required Python Libraries</strong><br>
        <code>pip install -r requirements.txt</code>
    </li>
</ol>
<h2>Running the Application</h2>
<ol>
    <li><strong>Start the Django Web Server</strong><br>
        <code>python manage.py runserver</code>
    </li>
    <li><strong>Access the Web Interface</strong><br>
        Open a browser and navigate to <a href="http://127.0.0.1:8000/">http://127.0.0.1:8000/</a> to view the application.
    </li>
    <li><strong>Interacting with the Predictive Models</strong><br>
        Use the provided interfaces to interact with the predictive models and explore different insights through the visualizations.
    </li>
</ol>
<h2>Application Visuals</h2>
<img src="path_to_your_image.png" alt="Application Overview" width="600">
<p><i>Interactive web interface showcasing predictive analytics and spatial data insights.</i></p>
<img src="path_to_your_additional_image.png" alt="Price Predictor" width="600">
<p><i>Machine learning model predictions displayed through interactive charts and graphs.</i></p>
<h2>Big Data Insights:</h2>
<img src="path_to_your_bigdata_image1.png" alt="Big Data Insight 1" width="600">
<img src="path_to_your_bigdata_image2.png" alt="Big Data Insight 2" width="600">
<img src="path_to_your_bigdata_image3.png" alt="Big Data Insight 3" width="600">
<img src="path_to_your_bigdata_image4.png" alt="Big Data Insight 4" width="600">
<h2>Insights based on location:</h2>
<img src="path_to_your_location_image1.png" alt="Location Insight 1" width="600">
<img src="path_to_your_location_image2.png" alt="Location Insight 2" width="600">
<h2>Contributors</h2>
<ul>
    <li>Vaibhav Gupta</li>
    <li>Dhrumil Ankola</li>
    <li>Viha B Raju</li>
    <li>Suveda Niranjan</li>
    <li>Harsh Gunwant</li>
</ul>
<p>The team used Apache Spark for cluster computing, Tableau and GeoPandas for visualization, and QGIS for creating interactive maps to provide deeper insights into the data collected from eBay.</p>