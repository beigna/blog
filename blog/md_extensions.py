from markdown.extensions import Extension
from markdown.treeprocessors import Treeprocessor


class URLTreeprocessor(Treeprocessor):
    def run(self, root):
        self._replace_url(root, 'img', 'src')
        self._replace_url(root, 'a', 'href')

    def _replace_url(self, root, tag, attr):
        for element in root.iter(tag):
            src = element.get(attr, '')
            if '://' not in src:
                element.set(attr, f'/articulos/{self.post_name}/{src}')


class URLExtension(Extension):
    def __init__(self, **kwargs):
        self.config = {
            'post_name': ['value1', 'description1']
        }
        super(URLExtension, self).__init__(**kwargs)

    def extendMarkdown(self, md):
        processor = URLTreeprocessor(md)
        processor.post_name = self.getConfig('post_name')
        md.treeprocessors.register(processor, 'url_extension', 0)
