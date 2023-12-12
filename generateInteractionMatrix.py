import numpy as np
import pandas as pd
# Generate the interaction matrix for number of clicks (with the set seed for reproducibility)
np.random.seed(42)
click_matrix = np.random.poisson(lam=1, size=(5, 4104))  # Poisson distribution for clicks

# Convert zeros to NaN to represent absence of interaction
click_matrix_nan = np.where(click_matrix == 0, np.nan, click_matrix)

# Convert the click matrix to a DataFrame
normalized_click_df = pd.DataFrame(click_matrix_nan)

# Save the DataFrame to a CSV file
click_matrix_csv_file_path = './data/click_matrix.csv'
normalized_click_df.to_csv(click_matrix_csv_file_path, index=False, header=False)

normalized_click_matrix_row_max = np.copy(click_matrix).astype(float)
for i in range(normalized_click_matrix_row_max.shape[0]):
    max_value_row = np.max(normalized_click_matrix_row_max[i, :])
    if max_value_row != 0:
        normalized_click_matrix_row_max[i, :] =  np.round(normalized_click_matrix_row_max[i, :]/max_value_row, 2)

# Convert the normalized click matrix to a DataFrame
normalized_click_df = pd.DataFrame(np.where(click_matrix == 0, np.nan, normalized_click_matrix_row_max))

# Save the DataFrame to a CSV file
click_matrix_csv_file_path = './data/click_matrix_normalized.csv'
normalized_click_df.to_csv(click_matrix_csv_file_path, index=False, header=False)

