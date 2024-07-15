
INPUT_PATH = '.csv' #* Caminho onde está o .csv de saída do WEKA

OUTPUT_PATH = 'resultado.csv' #* Caminho para salvar as médias e desvios 

COLUMNS_TARGET = ['Percent_correct', 'Kappa_statistic', 'True_positive_rate', 'True_negative_rate', 'Area_under_ROC'] #* Colunas que as métricas serão feitas

LABELS_ROWS = ['Bayes Net', 'Naive Bayes', 'Random Tree','Random Forest-10', 'Random Forest-100', 'Random Forest-500', 'SMO/SVM-poli-1', 'SMO/SVM-poli-2', 'SMO/SVM-poli-3'] #* Ordem dos classificadores utilizados

SIZE_INTERACTION = 300 #* Número de interções por classificador (Número de repetições x Folds)