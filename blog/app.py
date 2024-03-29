from flask import Flask, render_template, send_file

from markupsafe import Markup

from services import post_render_md_to_html, index_render


app = Flask(__name__)


@app.route('/')
def index():
    content = index_render()

    return render_template(
        'base.html',
        content=Markup(content),
        show_back_button=False
    )


@app.route('/leer/<post_slug>.html')
def post_render(post_slug):
    try:
        content = post_render_md_to_html(post_slug)

    except Exception as e:
        content = f'<h1>{e}</h1>'

    return render_template(
        'base.html',
        content=Markup(content),
        show_back_button=True
    )


@app.route('/articulos/<post_slug>/<file_path>')
def static_response(post_slug, file_path):
    return send_file(f'articulos/{post_slug}/{file_path}')
