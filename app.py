from flask import Flask, render_template, request
from scraper import scrape_case_details
from log_query import init_db, log_query
import sqlite3

app = Flask(__name__)
init_db()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        case_type = request.form['case_type']
        case_number = request.form['case_number']
        filing_year = request.form['filing_year']

        result = scrape_case_details(case_type, case_number, filing_year)
        log_query(case_type, case_number, filing_year, result)

        return render_template("index.html", result=result,
                                case_type=case_type,
                                case_number=case_number,
                                filing_year=filing_year)

    return render_template("index.html", result=None)

@app.route('/queries')
def view_queries():
    conn = sqlite3.connect('queries.db')
    c = conn.cursor()
    c.execute('SELECT id, case_type, case_number, filing_year, timestamp FROM queries ORDER BY timestamp DESC')
    rows = c.fetchall()
    conn.close()
    return render_template("queries.html", queries=rows)

if __name__ == '__main__':
    app.run(debug=True)