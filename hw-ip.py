
def chk_all_ips(iplist): #这里返回false，就是IP错误
    try:
        for i in iplist:
            if int(i) not in range(0,256):
                return False
        return True
    except:
        return False




a_nw_range = [1,...,126]
b_nw_range = [128,...,191]
c_nw_range = [192,...,223]
d_nw_range = [224,...,239]
e_nw_range = [240,...,255]
range_ck_list = ['A',"B","C","D","E"]

a_p_range = [[10]]
b_p_range = [[172],[16,...,31]]
c_p_range = [[192],[168]]


private_ck_list = [a_p_range,b_p_range,c_p_range,[],[]]


#错误ip or 掩码 0 错误，1 正确
# abcde 直接数 abcde
# 私有IP 私有1 非私有0

def chk_first(iplist):
    res = []
    if chk_all_ips(iplist):
        first = int(iplist[0]) # 错误ip or 掩码
        res_list = [first in a_nw_range, first in b_nw_range, first in c_nw_range, first in d_nw_range,first in e_nw_range]
        if res_list.count(True) == 0:
            res=[-1,0,'',0] # ip or mask错误
        else:
            index = res_list.index(True)
            ip_type = range_ck_list[index]
            res.append(ip_type)
            p_ck = private_ck_list[index]
            if len(p_ck)>0:
                p_res = True
                for i in range(len(p_ck)):
                    p_ip = p_ck[i]
                    t_ip = iplist[i]
                    if t_ip not in p_ip:
                        p_res = False
                res = [index,1,ip_type,p_res]
            else:
                res = [index,1,ip_type,0] # d e 类地址
    else:
        res=[-1,0,'',0]
    return res
        

msk_ck_list = ['255.0.0.0','255.255.0.0','255.255.255.0','','']

def ck_all(ip_msk_str):
    ipstr, mskstr = ip_msk_str.split('~')
    index,good,ip_type,is_p_add = chk_first(ipstr.split('.'))
    if index in [0,1,2] and mskstr != msk_ck_list[index]:
        good = 0
    return [good,ip_type,is_p_add]
        

#[0, '', 0]
#[0, '', 0]
#[1, 'A', False]
#[1, 'C', False]

    

if __name__ == '__main__':
    # res = ck_all('19..0.~255.255.255.0')
    # res = ck_all('10.70.44.68~255.254.255.0')
    # res = ck_all('1.0.0.1~255.0.0.0')
    res = ck_all('192.168.0.2~255.255.255.0')
    print(res)
    
