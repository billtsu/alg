input_list = [i for i in input().split(',')]
num_list = [int(i.ljust(6,'0')) for i in input_list]

print('num_list:',num_list)

sort_num_list = sorted(num_list)
print(sort_num_list)
sort_num_list.reverse()
print(sort_num_list)
index_list = []
for j in sort_num_list:
    k = num_list.index(j)
    index_list.append(k)

print('index_list:',index_list)
t_str = ''
for l in index_list:
    t_str+=str(input_list[l])
print('t_str:',t_str)
