from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

num_row_a = 0
num_col_a = 0
num_row_b = 0
num_col_b = 0

matrix_a_elements = []
matrix_b_elements = []

@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        form = request.form
        num_row_a = int(request.form["num_row_a"])
        num_col_a = int(request.form["num_col_a"])
        num_row_b = int(request.form["num_row_b"])
        num_col_b = int(request.form["num_col_b"])

        return render_template(
            'matrix_a_elements_form.html', 
            num_row_a=num_row_a, 
            num_col_a=num_col_a,        
        )
    return render_template("index.html",)


@app.route("/matrix_a_elements", methods=["GET", "POST"])
def matrix_a_elements():
    if request.method == "POST":
        form = request.form
        for k, v in form.items():
            matrix_a_elements.append(v)
        print(matrix_a_elements)
        return render_template(
            'matrix_b_elements_form.html', 
            num_row_b=num_row_b, 
            num_col_b=num_col_b
            )
    return render_template("matrix_a_elements_form.html",)


@app.route("/matrix_b_elements", methods=["GET", "POST"])
def matrix_b_elements():
    if request.method == "POST":
        form = request.form
        for k, v in form.items():
            matrix_b_elements.append(v)
        print(matrix_a_elements)
        return render_template(
            "result.html",
            matrix_a_elements=matrix_a_elements,
            matrix_b_elements=matrix_b_elements
        )
    return render_template("matrix_b_elements_form.html",)

if __name__ == '__main__':
	app.run(debug=True)
