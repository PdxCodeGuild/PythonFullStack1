def decrypt(message):
   '''
   >>> decrypt('Fgrnx naq Rttf')
   steak and eggs

   '''
   alphabet = 'abcdefghijklmnopqrstuvwxyz'
   digest = 'nopqrstuvwxyzabcdefghijklm'
   mentaculus = dict(zip(digest, alphabet))
   exploded = list()

   for i in message.lower():
       if i == " ":
           continue
       else:
           d = i.maketrans(mentaculus)
           exploded.append(d)

   decrypted = "".join(exploded)

   return decrypted