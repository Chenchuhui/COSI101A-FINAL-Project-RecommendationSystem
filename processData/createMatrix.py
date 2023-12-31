import pandas as pd

df = pd.read_csv('data/devpost_data_update2.csv')

# 将包含themes信息的列转换为字典列表
df['themes'] = df['themes'].apply(eval)

# 获取所有唯一theme
unique_themes = sorted(set(theme['name'] for themes in df['themes'] for theme in themes))

# 创建themeid和name的映射关系
theme_mapping = {theme['name']: {'id': theme['id'], 'name': theme['name']} for themes in df['themes'] for theme in themes}

# 为每个唯一theme创建一列，并初始化为0
for theme_name, theme_info in theme_mapping.items():
    df[f"{theme_info['id']}_{theme_info['name']}"] = 0

# 将包含每个theme的单独列设置为1
for index, row in df.iterrows():
    themes = row['themes']
    for theme in themes:
        theme_name = theme['name']
        theme_info = theme_mapping[theme_name]
        df.loc[index, f"{theme_info['id']}_{theme_info['name']}"] = 1

# 删除原始的themes列
df = df.drop('themes', axis=1)

df.to_csv('data/devpost_data_updateMatrix.csv', index=False)

