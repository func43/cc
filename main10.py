from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_FORM = '''
<!doctype html>
<title>Sum 10 Numbers</title>
<h2>Enter 10 numbers to add:</h2>
<form method=post>
  {% for i in range(10) %}
    Number {{ i+1 }}: <input type="number" name="num{{ i }}"><br>
  {% endfor %}
  <input type="submit" value="Calculate Sum">
</form>
{% if result is not none %}
  <h3>Sum: {{ result }}</h3>
{% endif %}
'''

@app.route('/', methods=['GET', 'POST'])
def sum_numbers():
    result = None
    if request.method == 'POST':
        try:
            nums = [float(request.form[f'num{i}']) for i in range(10)]
            result = sum(nums)
        except ValueError:
            result = "Invalid input. Please enter all numbers."
    return render_template_string(HTML_FORM, result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
