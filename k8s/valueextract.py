#读聚类结果下的7个log 对每一个log 在value.log里找对应的value 再输出到四个部分
import  os
RootPath='LogClusterResult-k8s/'
log_pattern_folder_cluster = RootPath+'clusters/'
file_names = os.listdir(log_pattern_folder_cluster)
for i in file_names:
    with open(log_pattern_folder_cluster +i, 'r') as in_text:
        in_text.readline()
        in_text.readline()
        in_text.readline()
        num=in_text.readline()
        num=num[:-1]
        nums=num.split(" ")
        print(nums)
        nums=nums[:-1]
        for j in nums:
            if(j!=" "or j!=''):
                j=int(j)
                with open("normalize_value.log", 'r')as value:
                    values = value.readlines()
                    if(j!=1 and j!=2001 and j!=2501 and j!=3001):
                        if(j<=2000):
                            text = values[j - 1-1]
                            #写到logvalue_train lide 1.log li
                            with open(RootPath+'logvalue/logvalue_train/'+i,'a+')as t:
                                    t.write(text)
                        elif(j<2500):
                            text = values[j - 2-1]
                            with open(RootPath+'logvalue/logvalue_val/'+i,'a+')as t:
                                    t.write(text)
                        elif(j<3000):
                            text = values[j - 3-1]
                            with open(RootPath + 'logvalue/logvalue_test/' + i, 'a+')as t:
                                t.write(text)
                        else:
                            text = values[j - 4-1]
                            with open(RootPath + 'logvalue/logvalue_abnormal/' + i, 'a+')as t:
                                t.write(text)
                    else:
                        continue
