import pandas as pd

# dropna()方法
# DataFrame.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)

# df = pd.read_csv('property-data.csv')
# print(df['NUM_BEDROOMS'])
# # isnull()判断各个单元格是否为空
# print(df['NUM_BEDROOMS'].isnull())
#
# print('--------------------------------')
#
# missing_values = ["n/a", "na", "--"]
# df = pd.read_csv('property-data.csv', na_values=missing_values)
# print(df['NUM_BEDROOMS'])
# print(df['NUM_BEDROOMS'].isnull())
#
# print('---------------------------------')
#
# df = pd.read_csv('property-data.csv')
#
# new_df = df.dropna()
#
# print(new_df.to_string())
#
# print('---------------------------------')
#
# df = pd.read_csv('property-data.csv')
# # 默认的dropna()方法返回一个新的DataFrame, 不会修改源数据
# # inplace=True参数可以修改DataFrame源数据
# df.dropna(inplace=True)
# print(df.to_string())
#
# print('----------------------------------')
#
# df = pd.read_csv('property-data.csv')
# df.dropna(subset=['ST_NUM'], inplace=True)
# print(df.to_string())
#
# print('----------------------------------')
# # fillna()指定列替换数据
# df = pd.read_csv('property-data.csv')
# df.fillna(12345, inplace=True)
# print(df.to_string())
#
# print('----------------------------------')
#
# df = pd.read_csv('property-data.csv')
#
# df['PID'].fillna(12345, inplace=True)
# print(df.to_string())
#
# print('----------------------------------')
#
# # mean()、median()、mode()方法计算列的均值、中位数、众数
#
# df = pd.read_csv('property-data.csv')
# x = df["ST_NUM"].mean()
# df["ST_NUM"].fillna(x, inplace=True)
#
# print(df.to_string())
#
# print('----------------------------------')
# df = pd.read_csv('property-data.csv')
# x = df["ST_NUM"].median()
# df["ST_NUM"].fillna(x, inplace=True)
#
# print(df.to_string())
#
# print('----------------------------------')
#
# df = pd.read_csv('property-data.csv')
# x = df["ST_NUM"].mode()
# df["ST_NUM"].fillna(x, inplace=True)
#
# print(df.to_string())

# *****************************************************
# 清洗格式错误数据
# data = {
#     "Date": ['2020/12/01', '2020/12/02', '20201226'],
#     "duration": [50, 40, 45]
# }
#
# df = pd.DataFrame(data, index=["day1", "day2", "day3"])
# df['Date'] = pd.to_datetime(df['Date'])
# print(df.to_string())
# # ****************************************************
# print('-----------------------------------------------')
# # 清洗错误数据
# person = {
#     "name": ['Google', 'Runoob', 'Taobao'],
#     "age": [50, 40, 12345]  # 12345年龄数据是错误的
# }
# df = pd.DataFrame(person)
# # loc可以定位数据中的某一部分
# df.loc[2, 'age'] = 30  # 修改数据
# print(df.to_string())
#
# print('----------------------------------------------')
#
# person = {
#     "name": ['Google', 'Runoob', 'Taobao'],
#     "age": [50, 200, 12345]
# }
#
# df = pd.DataFrame(person)
#
# for x in df.index:
#     if df.loc[x, "age"] > 120:
#         df.loc[x, "age"] = 120
#
# print(df.to_string())
#
# print('----------------------------------------------')
#
# person = {
#     "name": ['Google', 'Runoob', 'Taobao'],
#     "age": [50, 40, 12345]  # 12345 年龄数据是错误的
# }
#
# df = pd.DataFrame(person)
#
# # 删除age大于120的数据
# for x in df.index:
#     if df.loc[x, "age"] > 120:
#         df.drop(x, inplace=True)
#
# print(df.to_string())

# *****************************************************
# 清洗重复数据
# duplicated()和drop_duplicates()

# duplicated()方法，数据重复为True

person = {
    "name": ['Google', 'Runoob', 'Runoob', 'Taobao'],
    "age": [50, 40, 40, 23]
}
df = pd.DataFrame(person)

print(df.duplicated())

print('----------------------------------------------')

# drop_duplicates()删除重复数据

persons = {
  "name": ['Google', 'Runoob', 'Runoob', 'Taobao'],
  "age": [50, 40, 40, 23]
}

df = pd.DataFrame(persons)

df.drop_duplicates(inplace=True)
print(df)
