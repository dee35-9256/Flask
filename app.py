from flask import Flask,render_template,request
import csv

app = Flask(__name__)

@app.route('/')
def root():
    results = []
    with open('E:/PycharmProjects/assignment/2020-12-02.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            results.append(row)
       # print(results)
    return render_template('index.html',results=results)

if __name__ == '__main__':
    app.run(debug=True)