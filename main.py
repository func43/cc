from flask import Flask, request, render_template_string
import math

app = Flask(__name__)

HTML_FORM = '''
<!doctype html>
<title>Factorial Calculator</title>
<h2>Enter a number to calculate its factorial:</h2>
<form method=post>
  <input type="number" name="number" min="0" required>
  <input type="submit" value="Calculate">
</form>
{% if result is not none %}
  <h3>Factorial: {{ result }}</h3>
{% endif %}
'''

@app.route('/', methods=['GET', 'POST'])
def calculate_factorial():
    result = None
    if request.method == 'POST':
        try:
            num = int(request.form['number'])
            result = math.factorial(num)
        except (ValueError, OverflowError):
            result = "Invalid input. Please enter a non-negative integer."
    return render_template_string(HTML_FORM, result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

