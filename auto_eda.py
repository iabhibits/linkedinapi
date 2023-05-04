import pandas as pd
import numpy as np
import scipy.stats as st
from pingouin import welch_anova

class data_explorer:
    def __init__(self, df):
        self.df = df
        
    def get_anova_results(self, pvalue_thresh=0.05):
        df = self.df
        num_col = 'MonthlyIncome'
        cat_cols = df.dtypes[df.dtypes==object].index.tolist()
        #num_cols = np.setdiff1d([df.columns, cat_cols])
        #num_cols = df.describe().columns
        num_cols = df._get_numeric_data().columns
        thresh = 0.05
        results = []
        for num_col in num_cols:
            for cat_col in cat_cols:
                if df[cat_col].nunique()>1:
                    fresults = welch_anova(data=df,
                                       dv=num_col,
                                       between=cat_col
                                      )
                    pvalue = fresults.loc[0, 'p-unc']
                    if pvalue < thresh:
                         results.append((cat_col, num_col))
        df_results = pd.DataFrame(results, columns=['categorical',
                                                    'numerical'])
        return df_results



    def get_correlated_metrics_long(self, thresh=0.6):
        df = self.df
        corr_matrix = df.corr()
        corr_matrix = pd.DataFrame(np.tril(corr_matrix, -1),
                    columns=corr_matrix.columns,
                    index=corr_matrix.index)
        res = []
        thresh = 0.6
        for col in corr_matrix.columns:
                corr_col_abs = corr_matrix[col].abs()
                corr_col_abs = corr_col_abs[corr_col_abs >= thresh]
                temp = pd.DataFrame({'col2': corr_col_abs.index,
                                     'val': corr_col_abs.values})
                temp['col1'] = col
                if len(temp):
                    res.extend(temp.values.tolist())
        res = pd.DataFrame(res, columns=['col1', 'corr', 'col2'])
        return res

    def get_correlated_metrics(self, thresh=0.6):
        df = self.df
        corr_matrix = df.corr()
        thresh=0.6
        df_corr = pd.DataFrame(np.tril(corr_matrix, -1),
                              columns=corr_matrix.columns,
                              index=corr_matrix.index)
        df_corr_melted = df_corr.reset_index().melt(id_vars='index')
        df_corr_melted = df_corr_melted[df_corr_melted['value']>= thresh]
        df_corr_melted = df_corr_melted.rename(columns={'index': 'col1',
                                                        'variable': 'col2',
                                                        'value': 'corr'})
        df_corr_melted = df_corr_melted.reset_index(drop=True)
        return df_corr_melted