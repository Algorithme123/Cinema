import os

def liste_affiches():
        #db().select(db.affiches.ALL)
    requete = db.affiches.id > 0
    rows = db(requete).select()
    #rows = db().select(db.affiches.ALL);
    return response.render('affiche/liste.html', dict(affiches=rows))


# CREATE  affiches
def create_affiches():
    
    form = SQLFORM(db.affiches)
    if form.process().accepted:
        session.flash = 'affiches créée'
        redirect(URL('affiches', 'liste_affiches'))
    return dict(form=form)


# UPDATE


def edit_affiche():
    affiches = db.affiches(request.args(0)) or redirect(URL('liste_affiches'))
    form = SQLFORM(db.affiches, affiches)
    if form.process().accepted:
        redirect(URL('liste_affiches'))
    return dict(form=form)


def delete_affiche():
    affiches_id = request.vars.id
    affiches = db.affiches(affiches_id)
    if not affiches:
        raise HTTP(404, "L' affiches n'existe pas")
    db(db.affiches.id == affiches_id).delete()
    session.flash = 'affiches supprimée'
    redirect(URL('affiches', 'liste_affiches'))