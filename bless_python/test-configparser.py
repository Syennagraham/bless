#!/bless/venv/bin/python3

import configparser

filename = 'bless_deploy.cfg'
password = 'abc123'
blessca = 'bless-ca'

config = configparser.ConfigParser()
syen = config.read(filename)

#test = config.get( 'Bless CA', 'default_password' )
#print(test)
config.set('Bless CA','default_password',password )
test2 = config.get('Bless CA','default_password' )
print(test2)


with open('bless_deploy.cfg', 'w') as configfile: 
    config.write(configfile)


