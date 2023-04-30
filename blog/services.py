import os.path

import markdown

from md_extensions import URLExtension


def post_url_isvalid(value):
    avoid = ['.', '/', '\\', '|']

    for char in avoid:
        if char in value:
            return False

    return True


def post_path_generate(value):
    return os.path.join('articulos', value, 'index.md')


def post_file_exist(path):
    return os.path.isfile(path)


def post_render_md_to_html(name):
    if not post_url_isvalid(name):
        raise Exception('La URL es inválida')

    path = post_path_generate(name)
    if not post_file_exist(path):
        raise Exception('La URL no existe')

    with open(path, 'r') as fp:
        return markdown.markdown(
            fp.read(),
            extensions=['fenced_code', URLExtension(post_name=name)]
        )
