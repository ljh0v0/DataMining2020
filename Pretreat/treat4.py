# 按照github上的model格式化数据集

prefix1 = '../Dataset/Formatted/'
prefix2 = '../Model/Formatted/data/'

dic = {'家居': 0, '房产': 1, '教育': 2, '时尚': 3, '时政': 4, '科技': 5, '财经': 6, '游戏': 7, '体育': 8, '娱乐': 9}

with open(prefix2 + 'class.txt', 'w', encoding='utf-8') as fw:
    for key in dic.keys():
        print(key, file=fw)

fw1 = open(prefix2 + 'train.txt', 'w', encoding='utf-8')
fw2 = open(prefix2 + 'dev.txt', 'w', encoding='utf-8')

with open('../Dataset/labeled_data.csv', 'r', encoding='utf-8') as fr:
    lines = fr.readlines()
    for i, line in enumerate(lines[1:]):
        data_id, label, content = line.split(',', 2)
        if i % 5 != 0:
            print(str(dic[label]) + '\t' + content, file=fw1, end='')
        else:
            print(str(dic[label]) + '\t' + content, file=fw2, end='')

game_count = 0

with open('../Dataset/treated/ud_partial_labeled_game_sport_entertainment.csv', 'r', encoding='utf-8') as fr:
    lines = fr.readlines()
    for i, line in enumerate(lines[1:]):
        data_id, label, content = line.split(',', 2)

        # 对游戏进行降采样处理
        if label == '游戏':
            game_count += 1
            if game_count % 2 == 0:
                continue

        if i % 5 != 0 or label == '娱乐': # 娱乐标签很少，尽可能都放到训练集中
            print(str(dic[label]) + '\t' + content, file=fw1, end='')
        if i % 5 == 0:
            print(str(dic[label]) + '\t' + content, file=fw2, end='')

fw1.close()
fw2.close()

fw = open(prefix2 + 'test.txt', 'w', encoding='utf-8')

with open('../Dataset/test_data.csv', 'r', encoding='utf-8') as fr:
    lines = fr.readlines()
    for line in lines[1:]:
        data_id, content = line.split(',', 1)
        print('0\t' + content, file=fw, end='')

fw.close()
