import csv

# 读取csv文件
with open('fyx_chinamoney.csv','r') as file:
    # 将csv文件转为列表
    reader = csv.reader(file)
    data = list(reader)

def csv_decode(lis,batch_size):
    batches = []
    for i in range(0,len(lis),batch_size):
        batch = lis[i:i+batch_size] # 分批次(每80个一个批次)
        batches.append(batch)
    return batches


if __name__ == '__main__':
    #获得所有批次的列表
    batches = csv_decode(data,80)
    for batch in batches:
        print("---------------------")
        print(batch)
        print("---------------------")