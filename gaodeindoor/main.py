from flask import Flask, render_template


# 创建flask实例对象
app = Flask(__name__,
            template_folder='./templates',
            static_folder='./static',
            static_url_path=''
            )


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/gaode/indoor")
def indoor():
    return render_template("testindoor.html")


@app.route("/gaode/indoor3d")
def indoor3d():
    return render_template("testindoor3d.html")


if __name__ == "__main__":
    app.run(debug=True)
