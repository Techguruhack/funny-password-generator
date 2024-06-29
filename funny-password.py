import random


fun_adjectives = ['Silly', 'Goofy', 'Cheeky', 'Wacky', 'Bouncy']
fun_nouns = ['Banana', 'Penguin', 'Sausage', 'Noodle', 'Pajamas']


selected_adjective = random.choice(fun_adjectives)
selected_noun = random.choice(fun_nouns)


funny_password = f"{selected_adjective}_{selected_noun}_{random.randint(100, 999)}"


print(f"Your funny password suggestion is: {funny_password}")
