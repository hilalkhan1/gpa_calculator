from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_gpa(marks):
    return ((marks - 50) * 0.05) + 2.0 if marks >= 50 else 0.0

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            nlp = float(request.form['nlp'])
            dl = float(request.form['dl'])
            sp = float(request.form['sp'])
            pdc = float(request.form['pdc'])

            gpas = [calculate_gpa(m) for m in [nlp, dl, sp, pdc]]
            total_gpa = sum(gpas) / len(gpas)
            total_marks = nlp + dl + sp + pdc
            percentage = (total_marks / 400) * 100

            return render_template('index.html', total_gpa=round(total_gpa, 2),
                                   total_marks=total_marks, percentage=round(percentage, 2))
        except:
            return render_template('index.html', error="Please enter valid numeric marks.")
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)

