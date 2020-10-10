import math

# 合成加速度
def get_SynAcc(x, y, z):
    return math.sqrt(x*x + y*y + z*z)

# 平均
def get_ave(df):
    stack_list=[]
    for row in df.itertuples():
        x, y, z=row[1], row[2], row[3]
        stack_list.append(get_SynAcc(x, y, z))
    return sum(stack_list)/len(stack_list)

# 各軸の平均
def get_Ave_value(value):
    return sum(value)/len(value)

# 各軸の標準偏差
def get_Std_value(value):
    stack_list=[]
    ave=get_Ave_value(value)
    stack_list=[(v-ave)**2 for v in value]
    return math.sqrt(sum(stack_list)/(len(value)-1))

# 幅
def get_Range(df):
    stack_list=[]
    for row in df.itertuples():
        x, y, z=row[1], row[2], row[3]
        stack_list.append(get_SynAcc(x, y, z))
    return max(stack_list) - min(stack_list)

# 標準偏差
def get_Std(df):
    stack_list=[]
    ave=get_ave(df)
    for row in df.itertuples():
        syn=get_SynAcc(row[1], row[2], row[3])
        stack_list.append((syn-ave)**2)
    return math.sqrt(sum(stack_list)/(len(df)-1))

# 歪度
def get_Skewness(df):
    stack_list=[]
    ave=get_ave(df)
    for row in df.itertuples():
        syn=get_SynAcc(row[1], row[2], row[3])
        stack_list.append((syn-ave)**3)
    return sum(stack_list)/(get_Std(df)**3)*(len(df)/((len(df)-1)*(len(df)-2)))

# 尖度
def get_Kurtosis(df):
    stack_list=[]
    ave=get_ave(df)
    for row in df.itertuples():
        syn=get_SynAcc(row[1], row[2], row[3])
        stack_list.append((syn-ave)**4)
    return ((sum(stack_list)/(get_Std(df)**4))*((len(df)*(len(df)+1))/((len(df)-1)*(len(df)-2)*(len(df)-3)))) - (3*(len(df)-1)**2)/((len(df)-2)*(len(df)-3))

# エネルギー
def get_Energy(df):
    stack_list=[]
    for row in df.itertuples():
        x, y, z=row[1], row[2], row[3]
        stack_list.append(get_SynAcc(x, y, z)**2)
    return sum(stack_list)

def get_Fft(df):
    stack_list=[]
    for row in df.itertuples():
        x,y,z=row[1], row[2], row[3]
        stack_list.append(get_SynAcc(x,y,z))
    return max(np.fft.fft(stack_list))