import web
import db
from lxml.html.clean import Cleaner

VALIDTAGS = ['b', 'p', 'i', 'li', 'ul', 'span', 'div']

urls = ('/', 'default',
        '/add', 'add',
        '/alter', 'alter',
        '/search/(\S*)', 'search'
        )

render = web.template.render('.')

class default:
        def GET(self):
            return render.dict(db.get_entries(), db.get_total_entries())
class add:
    def POST(self):
        i = web.input()
        if(len(i.word) and len(i.description)):
            print "sanitising strings..."
            word = sanitize(i.word)
            desc = sanitize(i.description)
            if db.add_entry(word, desc) != None:
                return "ah-okay!"
            else:
                return "something went haywire..."
        return "booo..."
        
        
class alter:
    def GET(self):
        return "entry alteration goes here..."

def sanitize(inputstr):
    cleaner = Cleaner(allow_tags = VALIDTAGS, remove_unknown_tags=False)
    return cleaner.clean_html(inputstr)

web.internalerror = web.debugerror
if __name__ == '__main__':
    print "starting balkdict"
    app = web.application(urls, globals())
    app.run()