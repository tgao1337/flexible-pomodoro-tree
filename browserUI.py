from flask import Flask, render_template, redirect, request
import pomodorotree_v2

app = Flask(__name__, static_folder='assets')
taskList = []

@app.route("/")
def home():
    return redirect("/templates/index")

@app.route("/templates/index")
def home_template():
    return render_template("index.html")


#@app.route("/templates/pomodoro", methods=['POST', 'GET'])
#def pomodoro_template():
#    setMode("POMODORO_W")
#    currentPWorkTime = displayTime
#    return render_template("pomodoro.html")

@app.route("/templates/task", methods=['POST', 'GET'])
def task_template():
    if request.method == "POST":
        taskList.append(request.form['taskDescr'])
    return render_template("task.html", taskList=pomodorotree_v2.taskList, taskDone=pomodorotree_v2.taskDone, taskNum=pomodorotree_v2.taskNum)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True, threaded=True)
