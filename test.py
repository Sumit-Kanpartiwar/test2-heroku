from flask import jsonify, request, Flask

app=Flask(__name__)
@app.route('/xyz', methods=['GET','POST'])
def fun():
    if request.method=='POST':
        a=request.json['num_a']
        b=request.json['num_b']
        return jsonify(str(a+b))
if __name__=='__main__':
    app.run()