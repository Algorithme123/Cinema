import os

def liste_films():
        #db().select(db.films.ALL)
    requete = db.films.id > 0
    rows = db(requete).select()
    #rows = db().select(db.films.ALL);
    return response.render('film/liste.html', dict(films=rows))


# CREATE  films
def create_film():
    
    form = SQLFORM(db.films)
    if form.process().accepted:
        session.flash = 'Films créée'
        redirect(URL('films', 'liste_films'))
    return dict(form=form)


# UPDATE


def edit_film():
    films = db.films(request.args(0)) or redirect(URL('liste_films'))
    form = SQLFORM(db.films, films)
    if form.process().accepted:
        redirect(URL('liste_films'))
    return dict(form=form)


def delete_film():
    films_id = request.vars.id
    films = db.films(films_id)
    if not films:
        raise HTTP(404, "Le Films n'existe pas")
    db(db.films.id == films_id).delete()
    session.flash = 'Films supprimée'
    redirect(URL('films', 'liste_films'))