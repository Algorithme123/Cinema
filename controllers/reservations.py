import os

def liste_reservations():
        #db().select(db.affiches.ALL)
    requete = db.reservations.id > 0
    rows = db(requete).select()
    #rows = db().select(db.affiches.ALL);
    return response.render('reservation/liste.html', dict(reservations=rows))


@auth.requires_login()
# CREATE  affiches
def create_reservations():
    
    form = SQLFORM(db.reservations)
    if form.process().accepted:
        session.flash = 'reservations créée'
        redirect(URL('reservations', 'liste_reservations'))
    return dict(form=form)


# UPDATE


def edit_reservations():
    reservations = db.reservations(request.args(0)) or redirect(URL('liste_affiches'))
    form = SQLFORM(db.reservations, reservations)
    if form.process().accepted:
        redirect(URL('liste_reservations'))
    return dict(form=form)


def delete_reservations():
    reservations_id = request.vars.id
    reservations = db.reservations(reservations_id)
    if not reservations:
        raise HTTP(404, "L' reservations n'existe pas")
    db(db.reservations.id == reservations_id).delete()
    session.flash = 'reservations supprimée'
    redirect(URL('reservations', 'liste_reservations'))