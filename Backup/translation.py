import goslate
gs = goslate.Goslate()
language_id = gs.detect('hallo welt')
language_id
gs.get_languages()[language_id]
