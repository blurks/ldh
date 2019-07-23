from clld.web.adapters.download import Download
from clld.db.models.common import Source


class BibTeX(Download):
    ext = 'bib'

    def dump(self, req, fp, item, index):
        rec = item.bibtex()
        if item.languages:
            rec['lgcode'] = ', '.join('[{0}]'.format(l.id) for l in item.languages)
        fp.write((str(rec) + '\n\n').encode('utf8'))


def includeme(config):
    pass
