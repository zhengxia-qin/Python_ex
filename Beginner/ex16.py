import string
import random

n_lower = random.randint(1,10)
n_upper = random.randint(1,10)
n_symbol = random.randint(1,10)

pass_lowercase = random.sample(string.ascii_lowercase, n_lower)
pass_uppercase = random.sample(string.ascii_uppercase, n_upper)
pass_symbol = random.sample(string.punctuation, n_symbol)

password = random.sample(pass_lowercase + pass_uppercase + pass_symbol,n_lower+n_upper+n_symbol)
# print pass_lowercase + pass_uppercase + pass_symbol
print ''.join(pass_lowercase + pass_uppercase + pass_symbol)
print ''.join(password)