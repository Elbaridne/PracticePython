# El codigo del primer generador es mas seguro! Yay!
import random

password = "QWERTYUIOPASDFGHJKLZXCVBNM1234567890abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+"
ranpass = "".join(random.sample(password,10))

print(ranpass)