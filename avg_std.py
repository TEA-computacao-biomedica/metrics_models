import pandas as pd
import utils as utils

def calc_avg_std(df, columns_target, rows, size_interaction):
    average = []
    std = []
    results = []

    for i in range(0, len(df), size_interaction):
        df_subset = df.iloc[i:i + size_interaction]
        average.append(df_subset[columns_target].mean().round(2))
        std.append(df_subset[columns_target].std().round(2))

    
    for average, std in zip(average, std):
        result = average.astype(str) + ' ± ' + std.astype(str)
        results.append(result)

    final_df = pd.DataFrame(results, columns=columns_target, index=rows) 


    return final_df

    
if __name__ == '__main__':
    
    df = pd.read_csv(utils.INPUT_PATH)
    
    df_avg_std = calc_avg_std(df, utils.COLUMNS_TARGET, utils.LABELS_ROWS, utils.SIZE_INTERACTION)

    df_avg_std.to_csv(utils.OUTPUT_PATH, sep=';', decimal=',', index_label='Model')







