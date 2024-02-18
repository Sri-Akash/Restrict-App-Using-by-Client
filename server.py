from flask import Flask, render_template, request

app = Flask(__name__)

requested_paths = {}

@app.route('/')
def index():
    return render_template('index.html', requested_paths=requested_paths)

@app.route('/update_access', methods=['GET'])
def update_access():
    global requested_paths
    path = request.args.get('path')
    
    if path not in requested_paths:
        requested_paths[path] = False  
    
    access_status = "restricted" if not requested_paths[path] else "granted"
    
    return access_status

@app.route('/grant_access', methods=['POST'])
def grant_access():
    global requested_paths
    path = request.form.get('path')
    
    if path in requested_paths:
        requested_paths[path] = True 
    
    return render_template('index.html', requested_paths=requested_paths)

@app.route('/restrict_access', methods=['POST'])
def restrict_access():
    global requested_paths
    path = request.form.get('path')
    
    if path in requested_paths:
        requested_paths[path] = False 
    
    return render_template('index.html', requested_paths=requested_paths)

if __name__ == '__main__':
    app.run(debug=True)
