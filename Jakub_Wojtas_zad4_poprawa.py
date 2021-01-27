import time

from random import randint
long_list = [randint(0, 3000) for element in range(1000000)]


start = time.time()
if -1 in long_list:
    print('found')
else:
    print('not found')
end = time.time()
print('upłynęło: ', end-start, 'sekund')



start = time.time()
if long_list.count(-1)>0:
    print('found')
else:
    print('not found')
end = time.time()
print('upłynęło: ', end-start, 'sekund')




print('\n time.process_time')

t = time.process_time()
if -1 in long_list:
    print('found')
else:
    print('not found')
elapsed_time = time.process_time() - t
print('upłynęło', elapsed_time, 'sekund')


t = time.process_time()
if long_list.count(-1)>0:
    print('found')
else:
    print('not found')
elapsed_time = time.process_time() - t
print('upłynęło', elapsed_time, 'sekund')