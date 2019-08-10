from flask import Flask, render_template, request, json, redirect, url_for
from models.sign import Sign
from models.normalizer import Normalizer

app = Flask(__name__)

with open('data/signlist.json', encoding='utf-8') as f:
    sign_list = json.load(f)
with open('data/search_index.json', encoding='utf-8') as f:
    search_index = json.load(f)

with open('data/freq_ebla.json', encoding='utf-8') as f:
    stats_eb = json.load(f)
with open('data/freq_na.json', encoding='utf-8') as f:
    stats_na = json.load(f)
with open('data/freq_nb.json', encoding='utf-8') as f:
    stats_nb = json.load(f)
with open('data/freq_ob BACKUP.json', encoding='utf-8') as f:
    stats_ob = json.load(f)

@app.route('/')
def search():

    # Render home if no q params    
    if not request.args.get('search'):
        return render_template("home.html")

    # Sanitize and Normalize search string for 
    query = Normalizer.normalize(request.args.get('search'))

    # Search the index based on SearchKey
    signs = search_query(query)
    
    # Render proper templates
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

        ebla_stat   = list(map(cast_freq_to_int, stats_eb[sign_id]))
        na_stat     = list(map(cast_freq_to_int, stats_na[sign_id]))
        nb_stat     = list(map(cast_freq_to_int, stats_nb[sign_id]))
        ob_stat     = list(map(cast_freq_to_int, stats_ob[sign_id]))


        ebla_total  = sum([f['freq'] for f in ebla_stat])
        na_total    = sum([f['freq'] for f in na_stat])
        nb_total    = sum([f['freq'] for f in nb_stat])
        ob_total    = sum([f['freq'] for f in ob_stat])

        stats = {
            "ebla": sorted(ebla_stat, key = lambda i: i['freq'], reverse=True),
            "na":   sorted(na_stat,   key = lambda i: i['freq'], reverse=True),
            "nb":   sorted(nb_stat,   key = lambda i: i['freq'], reverse=True),
            "ob":   sorted(ob_stat,   key = lambda i: i['freq'], reverse=True),
            "totals": {
                "ebla": ebla_total,
                "na":   na_total,
                "nb":   nb_total,
                "ob":   ob_total,
            }
        }
        return render_template("sign.html", sign=sign, stats=stats)
    else:
        return redirect(url_for('home'))
def cast_freq_to_int(freq_dict):
    freq_dict['freq'] = int(freq_dict['freq'])
    return freq_dict

def sign_by_id(sign_id):
    if sign_id in sign_list:
        return Sign(sign_list[sign_id])
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
