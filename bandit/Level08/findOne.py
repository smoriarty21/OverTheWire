PASSWORD_FILE = 'passwords.txt'

def loadPasswordsIntoList():
    with open(PASSWORD_FILE) as f:
        return f.readlines()

def getPasswordCounts(passwords):
    pass_counts = {}

    for password in passwords:
        password = password.strip(' \t\n\r')
        if password in pass_counts.keys():
            pass_counts[password] += 1
        else:
            pass_counts[password] = 1

    return pass_counts

def findPassword(passwords):
    for key, value in passwords.iteritems():
        if value == 1:
            return key

def main():
    password_list = loadPasswordsIntoList()
    password_counts = getPasswordCounts(password_list)
    print 'Password: {0}'.format(findPassword(password_counts))

if __name__ == '__main__':
    main()