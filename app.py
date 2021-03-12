app = Flask(__name__,template_folder=r'<path of your html file>')

@app.route('/')
def show_cpu():
    return render_template('dynamic.html')    #Rendering the webpage

@app.route('/stuff', methods= ['GET'])
def stuff():
    recieve=random.randint(0,9)
    return jsonify(recieve=recieve)    #Sending json object 

if __name__=="__main__":
    app.run(debug=True)
