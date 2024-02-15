from flask import Flask, render_template, redirect, url_for, request
import numpy as np
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'eb0904b3d82e476cac9e3b823a3eef2d'

@app.route('/vectors/<int:vsize>',methods=['GET','POST'])
def vectors(vsize):
    x=random.randint(20, size=(vsize))
    y=random.randint(20, size=(vsize))
    return redirect(url_for('home'))
    


@app.route('/', methods = ["GET","POST"])
def home():
    if request.method == 'POST':
        vsize = int(request.form['VectorSize'])
        x = np.random.randint(20, size=(vsize))
        y = np.random.randint(20, size=(vsize))
        scalar_product = np.dot(x, y)
        return render_template('result.html', scalar_product=scalar_product, x = x, y = y)
    return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True)