from flask import Flask, render_template, request, redirect
import csv
#activate flask on powershell nav to tester - Webserver\Scripts\Activate.ps1
app = Flask(__name__)

@app.route('/')
def portfolio_home():
    return render_template('index.html')
#change colour of top text main.css line 2222 drop down button 2512
#change colour of background sections line 2250-2263

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)
#need to make html pages for each project and update the
#names by adding .html in index.html

def write_to_csv(data):
    with open('webserver/Portfoliowebpage/database.csv', mode='a', newline='') as database2:
        name = data['name']
        email = data['email']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name,email,message])

@app.route('/submitform', methods=['POST', 'GET'])
def submitform():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong please try again'