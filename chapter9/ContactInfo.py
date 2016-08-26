class ContactInfo:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def print_info(self):
        print('{0} : {1}'.format(self.name, self.email))
        contact = {'name': self.name, 'email': self.email}
        print(contact)


if __name__ == '__main__':
    contactInfo = ContactInfo('이상훈', 'digimon.1740@gmail.com')
    contactInfo.print_info()
