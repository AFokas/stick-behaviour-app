import os
import webbrowser

from flask import Flask, render_template, request
import bokeh
app = Flask(__name__)


@app.route("/")
def main():
    return render_template('index.html')


from flask import request

@app.route('/ticker_submit', methods=['POST'])
def login():
    ticker  =  request.form['ticker_name']
    list = []
    list.append(request.form.getlist('list'))
    args = []
    args.append(ticker)
    for i in range(len(list[0])):
        args.append(list[0][i])
    f=open('tmp.txt','w')
    for item in args:
        f.write("%s\n" % item)
    f.close()
    import scrape
    return render_template('load_network.html')



if __name__ == '__main__':
    app.run(port=33507)
