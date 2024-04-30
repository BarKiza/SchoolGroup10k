sztring = 'aLmafA' 
        
# Az első betűt nagybetűvé alakítja,
# de csak a kiírás erejéig, maga a sztring nem változik, 
# hiszen a sztringek elemei nem változtathatóak meg!
print(sztring.capitalize())

# Csupa nagybetűssé alakítja a sztringet
print(sztring.upper())

# Csupa kisbetűssé alakítja a sztringet
print(sztring.lower())

# Megszámolja, hányszor fordul elő a megadott karakter
print(sztring.count('a'))

# Megadja, hányadik indexű helyen fordul elő először a megadott karakter
print(sztring.find('a'))

#True-val tér vissza, ha a sztring minden eleme kisbetű 
print(sztring.islower())

# True-val tér vissza, ha a sztring minden eleme nagybetű 
print(sztring.isupper())
