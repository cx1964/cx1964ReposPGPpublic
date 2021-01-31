# Filenaam:       encrypt_file_py35_v001.py
# Functie:        Encrypt een file met gpg obv de python library gnupg
# python versie:  3.x
#
# Opmerking:      Onder Ubuntu 16.04 installeer python3 library gpupg
#                 mbv de Ubuntu package python3-gnugp
# Uitgangspunt:   Om dit script te laten werken moet gpg zijn geinstalleerd
#                 en de public en private keys aanwezig zijn.

# Voorbeeld code zie:
# https://stackoverflow.com/questions/19298171/python-gnupg-encrypt-no-errors-but-not-encrypting-data-or-files
# http://pythonhosted.org/gnupg/gnupg.html
# http://pythonhosted.org/python-gnupg/
# https://www.saltycrane.com/blog/2011/10/python-gnupg-gpg-example/


import gnupg # ubuntu 16.04 installeer de package python3-gnugp
from pprint import pprint
# from encrypt_py35 import PASSPHRASE


# zie https://www.saltycrane.com/blog/2011/10/python-gnupg-gpg-example/
# Toon gpg onformatie van het platform
gpg = gnupg.GPG()
public_keys = gpg.list_keys()
private_keys = gpg.list_keys(True)
print ('public keys:')
pprint(public_keys)
print ('private keys:')
pprint(private_keys)
print ('\n\n')



my_un_encrypted_file = 'my-unencrypted.txt'
my_encrypted_file = my_un_encrypted_file+'.gpg'

# Maak een dummy file my-unencrypted.txt aan met test data om te encrypten
open('my-unencrypted.txt', 'w').write('Dit is test data voor de file.')


# Encrypt de file
afile=open(my_un_encrypted_file, 'rb')
# inlezen van de ID van private key
rkeys = input("Enter key ID from private key: ") 
status = gpg.encrypt_file( afile
                          ,rkeys.split()
                          ,always_trust=True
                          ,output=my_encrypted_file)
    
print ('ok: ', status.ok)
print ('status: ', status.status)
print ('stderr: ', status.stderr)


print ("Klaar")
print ("Unencrypyted file: "+my_un_encrypted_file )
print ("Encrypted file: "+my_encrypted_file )
