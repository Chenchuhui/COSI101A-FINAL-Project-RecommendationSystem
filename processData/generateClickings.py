import pandas as pd
import numpy as np

np.random.seed(511)

num_users = 1000
num_items = 4104
# clicking_ratio = [3,1]

user_ids = np.random.randint(1, num_users + 1, size=num_users * 10)
item_ids = np.random.randint(1, num_items + 1, size=len(user_ids))
clickings = np.random.poisson(lam=2, size=len(user_ids)) + 1
# clickings = np.random.choice(np.concatenate([np.arange(1, 6)] * clicking_ratio[0] + [np.arange(6, 51)] * clicking_ratio[1]), size=len(user_ids))

clickings_df = pd.DataFrame({'user_id': user_ids, 'item_id': item_ids, 'clicking': clickings})

clickings_df = clickings_df.drop_duplicates(['user_id', 'item_id'])

clickings_df.reset_index(drop=True, inplace=True)

num_generated_rows = clickings_df.shape[0]
print(f"生成的数据行数: {num_generated_rows}")

clickings_df.to_csv('./data/clickings.csv', index=False)
