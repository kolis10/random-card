import random
import time

time.sleep(2)
excuse1 = ['My niece','My dog','My boss','My Mom']
excuse2 = ['destroyed','ate','burnt','broke','took away']
excuse3 = ['the phone','my homework','the tv','money', 'your car']
excuse4 = ['ecstatically','spitefully','crazily','while drunk','while sleepwalking']

rand_excuse1 = random.choice(excuse1)
rand_excuse2 = random.choice(excuse2)
rand_excuse3 = random.choice(excuse3)
rand_excuse4 = random.choice(excuse4)

print(rand_excuse1,rand_excuse2,rand_excuse3,rand_excuse4)