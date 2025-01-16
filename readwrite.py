with open('name.txt') as f:
    my_name = f.read()

print(my_name)

import os
os.makedirs('output', exist_ok=True)

with open('output/hello.txt', 'w') as f:
    f.write(f'hello, my name is {my_name}')
    f.write('\n')