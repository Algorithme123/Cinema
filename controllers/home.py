import os

def liste_home_films():
        #db().select(db.films.ALL)
    requete = db.films.id > 0
    rows = db(requete).select()
    #rows = db().select(db.films.ALL);
    return response.render('film/liste.html', dict(films=rows))


def liste_home_affiches():
        #db().select(db.affiches.ALL)
    requete = db.affiches.id > 0
    rows = db(requete).select()
    #rows = db().select(db.affiches.ALL);
    return response.render('affiches/liste.html', dict(affiches=rows))
