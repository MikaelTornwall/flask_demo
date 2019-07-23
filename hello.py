from flask import Flask, render_template
app = Flask(__name__)

class Item:
    def __init__(self, name):
        self.name = name

nimi = "Python Mies"

lista = [101, 102, 103, 104, 105]

esineet = []
esineet.append(Item("Kello"))
esineet.append(Item("Vasara"))
esineet.append(Item("Sorvi"))
esineet.append(Item("Polkupyörä"))

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/demo")
def content():
	return render_template("demo.html", nimi=nimi, lista=lista, esineet=esineet)

if __name__ == "__main__":
	app.run(debug=True)
