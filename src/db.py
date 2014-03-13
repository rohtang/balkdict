import web, datetime

db = web.database(dbn='mysql', host='127.0.0.1', port=3306, db='dictionary', user='user', pw='passwd')

def get_entries():
    return db.select('entries', order='id DESC')
def get_total_entries():
    return db.query("select count(*) as id from entries")[0]['id']

def get_entry(id):
    return db.select('entries', where='id=$id', vars=locals())[0]

def add_entry(word, description):
    return db.insert('entries', word=word, description=description)
def alter_post(id, word, description):
    return db.update('entries', where="id=$id", vars=locals(), word=word, description=description)
 