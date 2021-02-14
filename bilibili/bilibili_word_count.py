from collections import Counter
import jieba.posseg as pseg
import requests

url = 'https://api.bilibili.com/x/web-interface/ranking/v2?rid=0&type=all'

filter_words = ['【', '】' ,'（', '）', ]

word_count_dict = {}
response = requests.get(url)
top_100_list = response.json()['data']['list']
for e in top_100_list:
    title = e['title']
    # word_list = jieba.cut_for_search(title)
    word_list = pseg.cut(title)
    for word, flag in word_list:
        if flag != 'n':
            continue
        if word in word_count_dict.keys():
            word_count_dict[word] = word_count_dict[word] + 1
        else:
            word_count_dict[word] = 1

most_common = Counter(word_count_dict).most_common()

for e in most_common:
    print("{0}: {1}".format(e[0], e[1]))