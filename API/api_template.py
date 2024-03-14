from flask import Flask, render_template, request, redirect, url_for, jsonify

'''
This is a basic example of an api, this is connected to a web front end, but it could equally be connected to 
a device that is set up for consuming or reporting things to the data repository 

NOte though that this is in a development environment and not in any way safe for production that
would require a WSGI interface WSGI stands for "Web Server Gateway Interface."
It's a specification for a universal interface between web servers and web applications
 or frameworks written in Python. 
 The goal of WSGI is to provide a standard interface that allows for interoperability between various web servers 
 and web applications.
'''
app = Flask(__name__)

tasks = []  # Our in-memory database for tasks


@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)


@app.route('/add', methods=['POST'])
def add_task():
    name = request.form['name']
    task = {'id': len(tasks) + 1, 'name': name}
    tasks.append(task)
    return redirect(url_for('index'))


@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)