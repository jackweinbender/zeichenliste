from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    """Render Main Search Box"""
    query = request.args.get('query')
    
    # TODO: Parse the search query to determine what I'm looking up
    signs = parse_search_query(query)

    return render_template("search.html", signs=signs)

@app.route('/signs/<sign_id>')
def sign(sign_id):
    """Render one sign page based on ID"""
    sign = sign_by_id(sign_id)
    return render_template("sign.html", sign=sign)

def parse_search_query(query):
    """Takes a query strng and returns a list of sign entries"""
    
    # FIXME: Fake return data
    
    data = []

    return data

def sign_by_id(sign_id):
    # FIXME: Fake Data
    return {
        "borger": "1",
        "labat": "1",
        "huehnergard": "1",
        "deimel": "1",
        "mittermayer": "1",
        "heth_z_l": "1",
        "hinke": "1",
        "clay": "1; 3",
        "ranke": "1",
        "sign_depiction": "single horizontal line",
        "borger_sign_name": "AŠ",
        "unicode_sign_name": "ASH",
        "labat_name": "aš",
        "id": 0
      }

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
