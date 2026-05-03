# Keyword arguements in py
# keyword arguements= an argument preceded by an identifier, helps with readability

def hello(greeting, title, first_name, last_name):
    print(f"{greeting}, {title} {first_name} {last_name}")
    
hello(greeting="Hello",title="Mr.",first_name="spongeBob",last_name="Squarepants")

for counter in range(1,11):
    print(counter, end="")