from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def page_name(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(
            f'\nEmail:{email}, Subject:{subject}, Message:{message}')


def write_to_csv(data):
    with open('database.csv', mode='a') as db:
        email = data['email']
        subject = data['subject']
        message = data['message']
        write_csv_db = csv.writer(
            db, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        write_csv_db.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            # write_to_file(data)
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Did not save to DB!'
    else:
        return 'Something went Wrong!'
