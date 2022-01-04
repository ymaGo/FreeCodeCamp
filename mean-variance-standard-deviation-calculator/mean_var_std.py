import numpy as np

def calculate(list):
    try:
        se=np.array(list).reshape(3,3)
        mean=[np.mean(se,axis=0).tolist(),np.mean(se,axis=1).tolist(),np.mean(list)]
        variance=[np.var(se,axis=0).tolist(),np.var(se,axis=1).tolist(),np.var(list)]
        standard_deviation=[np.std(se,axis=0).tolist(),np.std(se,axis=1).tolist(),np.std(list)]
        max_value=[np.max(se,axis=0).tolist(),np.max(se,axis=1).tolist(),np.max(list)]
        min_value=[np.min(se,axis=0).tolist(),np.min(se,axis=1).tolist(),np.min(list)]
        sum_value=[np.sum(se,axis=0).tolist(),np.sum(se,axis=1).tolist(),np.sum(list)]
        calculations={'mean':mean,'variance':variance,'standard deviation':standard_deviation,'max':max_value,'min':min_value,'sum':sum_value}
        return calculations
    except ValueError:
        raise ValueError("List must contain nine numbers.")


  