from flask import Flask, render_template, request
import sqlite3
import pandas as pd
from flask import jsonify
from joblib import load
from sklearn.pipeline import Pipeline  # Add this import
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split

app = Flask(__name__)
df = None
model = None

db_path = 'testDB.db' 
conn = sqlite3.connect(db_path, check_same_thread=False)

query = "SELECT * FROM table1"  
df = pd.read_sql_query(query, conn)


@app.route('/welcome')
def index():
    return render_template('welcome.html')

@app.route('/search', methods=['POST'])
def search():
    if request.method == 'POST':
        keyword = request.form['keyword'].lower()
        gender = request.form['gender']
        
        query = "SELECT * FROM table1 WHERE LOWER(Title) LIKE '%{}%' AND Gender = '{}' AND Rating != 'Not Available' AND Price != 'Not Available'".format(keyword, gender)

        result_df = pd.read_sql_query(query, conn)
  
        result_df = result_df.drop_duplicates(subset='Title')
        result_df = result_df.sort_values(by=['Rating'], ascending=[False])
        result_df = result_df.sort_values(by=['Total Sold Items'], ascending=[False])
        result_df = result_df[result_df['Total Available Items'] != 'Not Available']
        
        matching_titles = result_df['Title'].head(20).tolist()
        
        matching_titles = [title.encode('utf-8').decode('unicode-escape') for title in matching_titles]
        result_df_encoded = result_df.applymap(lambda x: x.encode('utf-8').xdecode('unicode-escape') if isinstance(x, str) else x)

        return render_template('results.html', matching_titles=matching_titles, result_df=result_df_encoded)

@app.route('/product/<title>')
def product_detail(title):
    product_info = df[df['Title'] == title].iloc[0] 
 
    return render_template('product.html', product_info=product_info)

@app.route('/heatmap')
def heatmap():
    return render_template('heatmap.html')

@app.route('/Choropleth_US_categories')
def choropleth():
    return render_template('generalAnalysis.html')



@app.route('/product/category/<category>')

def category_result(category):
    print(category)
    if category == 'Women Clothing':
        clothing_df = df[df['Category'] == 'Women Clothing']
    elif category == 'Mens Accessories':
        clothing_df = df[df['Category'] == 'Mens Accessories']
    elif category == 'Electronics':
        clothing_df = df[df['Category'] == 'Electronics']
    elif category == 'Musical Instruments':
        clothing_df = df[df['Category'] == 'Musical Instruments']
    elif category == 'Antiques':
        clothing_df = df[df['Category'] == 'Antiques']
    elif category == 'Miscellaneous':
        clothing_df = df[df['Category'] == 'Miscellaneous']
    else:
        return render_template('unknown_category.html')
    return render_template('Category_result.html', clothing_df=clothing_df)
@app.route('/analysis', methods=['GET'])
def analysis():
    print(request.args)
    category = request.args.get('Category')
    print(category)
    return render_template('analysis.html', category=category)


@app.route('/pricePrediction', methods=['GET'])
def price_prediction():
    title = request.args.get('Title')
    seller_name = request.args.get('Seller Name')
    location = request.args.get('Location')
    product_condition = request.args.get('Product Condition')
    price = request.args.get('Price')
    product_info = {
        'Title': title,
        'Seller Name': seller_name,
        'Location': location,
        'Product Condition': product_condition,
        'Price': price
    }
    return render_template("price_prediction_result.html", product_info=product_info)



if __name__ == '__main__':
    app.run(debug=True)


