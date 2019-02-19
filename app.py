from flask import Flask, render_template, request, json, redirect, url_for
from models.sign import Sign

app = Flask(__name__)

with open('data/signlist.json', encoding='utf-8') as f:
    signlist = json.load(f)

@app.route('/')
def home():
    """Render Main Search Box"""
    query = request.args.get('query')
    
    # TODO: Parse the search query to determine what I'm looking up
    signs = parse_search_query(query)

    return render_template("search.html", signs=signs)

def parse_search_query(query):
    """Takes a query strng and returns a list of sign entries"""
    
    # FIXME: Fake return data
    
    data = []

    return data

@app.route('/signs/<sign_id>')
def sign(sign_id):
    """Render one sign page based on ID"""
    sign = sign_by_id(sign_id)

    if sign:
        return render_template("sign.html", sign=sign)
    else:
        return redirect(url_for('home'))

def sign_by_id(sign_id):
    if sign_id in signlist:
        return signlist[sign_id]
    else:
        return False

###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
