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


@app.route("/baidu/indoor")
def indoor():
    return render_template("testindoor.html")


if __name__ == "__main__":
    app.run(debug=True)
