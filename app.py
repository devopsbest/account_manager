from flask import Flask,request,render_template, jsonify
from account_api.search_account import query_account
from flask_cors import CORS

app = Flask(__name__)
# 请求跨域
CORS(app)


@app.route('/')
def index():
    return render_template("home.html")

@app.route('/accounts', methods=['GET'])
def get_accounts():

    if request.method == "GET":

        username = request.args.get("account")
        password = query_account(username)
        if password == "":
            return "no result"
        else:
            #return render_template("home.html",message=username,password=password)
            return jsonify({"password": password})


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)
