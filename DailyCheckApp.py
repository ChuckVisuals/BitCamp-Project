#Package import
from flask import Flask, render_template, request 
from DailyChecks import YourRooms
 
#initialise app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    input_string = request.form['input_string']
    processed_string = YourRooms(input_string)
    return render_template('results.html', processed_string=processed_string)

if __name__ == '__main__':
    app.run(debug=True)