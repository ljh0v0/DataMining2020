import numpy as np

classes = {0: ',家居,可公开', 1: ',房产,中风险', 2: ',教育,低风险', 3: ',时尚,低风险', 4: ',时政,高风险',
           5: ',科技,中风险', 6: ',财经,高风险', 7: ',游戏,低风险', 8: ',体育,可公开', 9: ',娱乐,可公开'}

predict_all = np.array([], dtype=int)

for i in range(0, 10):
    predict_all = np.append(predict_all, i)

for i, result in enumerate(predict_all):
    print(str(i) + classes[result])
