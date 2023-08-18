import pandas as pd

# df = pd.read_json('sites.json')

# print(df.to_string())

# -----------------------------------

# data = [
#     {
#       "id": "A001",
#       "name": "菜鸟教程",
#       "url": "www.runoob.com",
#       "likes": 61
#     },
#     {
#       "id": "A002",
#       "name": "Google",
#       "url": "www.google.com",
#       "likes": 124
#     },
#     {
#       "id": "A003",
#       "name": "淘宝",
#       "url": "www.taobao.com",
#       "likes": 45
#     }
#   ]
#
# df = pd.DataFrame(data)
#
# print(df)

# -------------------------------------

# 字典格式的JSON
#
# s = {
#     "col1": {"row1": 1, "row2": 2, "row3": 3},
#     "col2": {"row1": "x", "row2": "y", "row3": "z"}
# }
#
# # 读取JSON转为DataFrame
#
# df = pd.DataFrame(s)
#
# print(df)

# --------------------------------------------------

# URL = 'https://static.runoob.com/download/sites.json'
# df = pd.read_json(URL)
# print(df)

# -------------------------------------------------
#
# data = {
#     "school_name": "ABC primary school",
#     "class": "Year 1",
#     "students": [
#     {
#         "id": "A001",
#         "name": "Tom",
#         "math": 60,
#         "physics": 66,
#         "chemistry": 61
#     },
#     {
#         "id": "A002",
#         "name": "James",
#         "math": 89,
#         "physics": 76,
#         "chemistry": 51
#     },
#     {
#         "id": "A003",
#         "name": "Jenny",
#         "math": 79,
#         "physics": 90,
#         "chemistry": 78
#     }]
# }
#
# df = pd.DataFrame(data)
# print(df.to_string())

# -----------------------------------------------

# json_normalize()方法

# import json
#
# # 使用Python JSON模块载入数据
# with open('nested_list.json', 'r') as f:
#     data = json.loads(f.read())
#
# # 展开数据
# df_nested_list = pd.json_normalize(data, record_path=['students'])
# print(df_nested_list)

# ----------------------------------

# import json
#
# # 使用Python JSON模块载入数据
# with open('nested_list.json', 'r') as f:
#     data = json.loads(f.read())
#
# # 展开数据
# df_nested_list = pd.json_normalize(
#     data,
#     record_path=['students'],
#     meta=['school_name', 'class']
# )
#
# print(df_nested_list)

# ---------------------------------------
#
# import json
#
# with open('nested_mix.json', 'r') as f:
#     data = json.loads(f.read())
#
# df = pd.json_normalize(
#     data,
#     record_path=['students'],
#     meta=[
#         'class',
#         ['info', 'president'],
#         ['info', 'contacts', 'tel']
#     ]
# )
#
# print(df.to_string())

# ----------------------------------------

# glom 模块处理数据嵌套
from glom import glom
df = pd.read_json('nested_deep.json')

# apply函数会遍历series或dataframe
data = df['students'].apply(lambda row: glom(row, 'grade.math'))

print(data)
