from flask import Flask, render_template, request, json, redirect, url_for
from models.sign import Sign

app = Flask(__name__)

with open('data/signlist.json', encoding='utf-8') as f:
    signlist = json.load(f)
with open('data/search_index.json', encoding='utf-8') as f:
    search_index = json.load(f)

@app.route('/')
def search():
    query = request.args.get('search')
    
    if not query:
        return render_template("home.html")
    
    signs = search_query(query)
    
    if len(signs) == 0:
        return render_template("search.html", signs=False, query=query)
    elif len(signs) == 1:
        sign_id = signs[0].borger_id
        return redirect(url_for('sign', sign_id=sign_id))
    else:
        return render_template("search.html", signs=signs, query=True)

def search_query(query):
    """Takes a query string and returns a list of sign entries"""
    results = []
    # FIXME: Fake return data
    
    if query in search_index:
        results = []
        for sign_id in search_index[query]:
            sign = sign_by_id(sign_id)
            results.append(sign)
        return results
    else:
        return []

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
        return Sign(signlist[sign_id])
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
