from flask import Flask, render_template, request
import csv
import json

app = Flask(__name__)
filename = 'results.csv'

@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/index', methods=['POST'])
def  csv_saver():
        if request.method == 'POST':
            username = request.form['username']
            gender = request.form['gender']
            ling = request.form['ling']
            one = request.form['one']
            two = request.form['two']
            three = request.form['three']
            fieldnames = ['username','gender','ling','one','two','three']
            with open(filename, 'a+', encoding='utf-8') as csvfile:
                writer = csv.Dictwriter(csvfile, fieldnames=fieldnames)
                writer.writerow({'username':username, 'gender':gender, 'ling':ling,
                                 'one':one, 'two':two, 'three':three})
            return render_template('index.html', fin_form=fin_form)
        

           
if __name__ == '__main__':
    app.run(debug=False)
    
