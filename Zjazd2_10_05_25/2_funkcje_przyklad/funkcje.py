users = {
    'Kamil': '1234',
    'GosiaXD': 'Wiosna',
    'max': 'max' }

def user_exists(user):
    if user in users.keys():
        return True
    return False

def correct_passwd(user, passwd):
    if users[user] == passwd:
        return True
    return False

def registration(user):

def password_complexity_ok(passwd):


