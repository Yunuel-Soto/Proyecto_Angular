from Logica.Models import usuarios as u

def create_user(nick_name, fullname):
    user = u.Users(nick_name=nick_name, fullname=fullname)
    try:
        u.session.add(user)
        u.session.commit()
        return "successfull created user"
    except Exception as error:
        u.session.rollback()
        raise Exception(error)
    