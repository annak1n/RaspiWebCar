from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/control_car', methods=['POST'])
def led_handler():
    print("Button pressed!")
    if request.form['ctrlbtn'] == "forward":
        print("...forward...")
    elif request.form['ctrlbtn'] == "backward":
        print("...backward...")
    elif request.form['ctrlbtn'] == "turnleft":
        print("...turnleft...")
    elif request.form['ctrlbtn'] == "turnright":
        print("...turnright...")
    else:
        print("ERROR")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='192.168.169.2', port=8080)
