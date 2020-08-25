# 输入 M 从 1-100 中删除 M，n*M。再从n*M+1开始计数，数到M，再次删除，循环操作
M = int(input())
ori_list = [i for i in range(1,101)]
ori_dict = {}
for i in ori_list:
    ori_dict[str(i)] = i
    
def run(ori_dict,M):
    cd = len(ori_dict)
    # print('cd:',cd,"M:",M)
    if cd<= M:
        # print('gg:',ori_dict,list(ori_dict.values())[:len(ori_dict)-1])
        print(','.join([str(i) for i in list(ori_dict.values())[:len(ori_dict)-1]]))
        return ori_dict
    else:
        N = int(cd / M)
        pop_num_list = []
        # print('oridic:len::',len(ori_dict))
        for j in range(1,N):
            pop_num_list.append(j * M)
            ori_dict.pop(str(j * M))
        # print('pop:',pop_num_list,'len:',len(pop_num_list))
        # print('oridic:len::after',len(ori_dict))
        cur_len = len(ori_dict)
        new_dict = {}
        cur_num_list = [ori_dict[k] for k in sorted(ori_dict.keys())]
        first_part_list = cur_num_list[:N*M-N+1]
        second_part_list = cur_num_list[N*M+N:]
        second_part_list.extend(first_part_list)
        new_list = second_part_list
        # print('cur_num_list:',cur_num_list,len(cur_num_list))
        for k in range(1, len(new_list) +1):
            # print('k:',k,len(new_list))
            new_dict[str(k)] = new_list[k-1]
        # print('new_dict:',new_dict)
        run(new_dict,M)
if __name__ == '__main__':
    res = run(ori_dict,M)
    print('res:',res)
    
    

