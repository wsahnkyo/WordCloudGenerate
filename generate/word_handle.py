import jieba
def get_word_dict(file_path):
    txt = open(file_path, "r",encoding="utf-8").read()
    words = jieba.lcut(txt)
    counts = {}
    for word in words:
        if len(word) == 1: #排除单个字符的分词结果
            continue
        else:
            counts[word] = counts.get(word,0) + 1
    items = list(counts.items())
    items.sort(key=lambda x:x[1], reverse=True)
    dict = {}
    for i in range(10):
        word, count = items[i]
        dict[word] = count
    return dict