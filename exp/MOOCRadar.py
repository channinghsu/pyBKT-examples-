import pandas as pd
from pyBKT.models import Model

# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)
# 设置value的显示长度
pd.set_option('max_colwidth', 100)
# 设置1000列时才换行
pd.set_option('display.width', 1000)

if __name__ == '__main__':
    model = Model(num_fits=1)  # 创建模型对象

    # Load unfamiliar dataset.
    df = pd.read_csv('../data/student-problem-middle.csv')
    # df = pd.read_csv('../data/student-problem-coarse.csv')
    data_path = '../data/middle.csv'
    config = {'multigs': False,
              'multilearn': False,
              'forgets': False
              # 'multigs_cognitive_level': False,
              }
    defaults = {'order_id': 'num',
                'user_id': 'student',
                'skill_name': 'skill',
                'correct': 'right',
                'folds': 'student',
                'multigs': 'gs_classes'}

    # Fit using the defaults (column mappings) specified in the dictionary.
    model.fit(data=df, defaults=defaults, )

    # Predict/evaluate/etc.
    # training_acc = model.evaluate(data=df, metric='accuracy')

    # 使用默认的RMSE进行评估，然后指定AUC和ACC进行评估
    print(model.evaluate(data=df))
    print(model.evaluate(data=df, metric='auc'))
    print(model.evaluate(data=df, metric='accuracy'))

    # 进行交叉验证，默认为5折
    print(model.crossvalidate(data=df, defaults=defaults, **config))
    print(model.crossvalidate(data=df, metric='auc', defaults=defaults, **config))
    print(model.crossvalidate(data=df, metric='accuracy', defaults=defaults, **config))
