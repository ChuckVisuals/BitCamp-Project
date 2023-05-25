from flask import Flask, request
from views import views 
from DailyChecks import YourRooms

app = Flask(__name__)
app.register_blueprint(views, url_prefix="/views") 

def index():
        input_str = request.form['input']
        output_str = YourRooms(input_str,1)
        return output_str

if __name__ == '__main__':
    app.run(debug=True, port=8000)

    