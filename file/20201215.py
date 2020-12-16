ip_str = input('Enter Input String: ')
ip_lst = list(map(str,ip_str))

prio_dict = {'-':1,'*':2,'+':3,'/':4,'^':5,'!':6}
#prio_dict = {'-':1,'+':2,'*':3,'/':4}
op_lst = []
op_lst.append(['op','arg1','arg2','result'])

def find_top_prio(lst):
    top_prio = 1
    count_ops = 0
    
    for ops in lst :
        
        if ops in prio_dict:
            count_ops += 1
            
            if prio_dict[ops] > 1:
                top_prio = prio_dict[ops]
                
    return top_prio,count_ops

top_prio , count_ops =find_top_prio(ip_lst)

ip = ip_lst
i,res = 0, 0

while i in range (len(ip)):
    
    if ip[i] in prio_dict:
        op = ip[i]

        if (prio_dict[op]>=top_prio) and (ip[i+1] in prio_dict):
            res += 1
            op_lst.append([ip[i+1],ip[i+2],' ', 't'+str(res)])
            ip[i+1] = 't'+str(res)
            ip.pop(i+2)
            i=0
            top_prio,count_ops = find_top_prio(ip)

        elif prio_dict[op]>=top_prio:
            res+=1
            op_lst.append([op,ip[i-1],ip[i+1],'t'+str(res)])
            ip[i] = 't'+str(res)
            ip.pop(i-1)
            ip.pop(i)
            i=0
            top_prio,count_ops = find_top_prio(ip)
            
        if len(ip)==1:
            op_lst.append(['=',ip[i],' ','a'])
            print("{}".format(op_lst))
    i+=1