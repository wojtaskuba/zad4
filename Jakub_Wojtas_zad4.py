import time

from random import randint
long_list = [randint(0, 3000) for element in range(1000000)]


start = time.time()
for i in long_list:
    if i == -1:
        print('found')
        break
end = time.time()
print('upłynęło: ', end-start, 'sekund')



start = time.time()
for i in range(1000000):
    if long_list[i] == -1:
        print('found')
        break
end = time.time()
print('upłynęło: ', end-start, 'sekund')




print('\n time.process_time')

t = time.process_time()
for i in long_list:
    if i == -1:
        print('found')
        break
elapsed_time = time.process_time() - t
print('upłynęło', elapsed_time, 'sekund')


t = time.process_time()
for i in range(1000000):
    if long_list[i] == -1:
        print('found')
        break
elapsed_time = time.process_time() - t
print('upłynęło', elapsed_time, 'sekund')