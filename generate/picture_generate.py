from wordcloud import WordCloud
import matplotlib.pyplot as plt
import word_handle as wh
plt.rcParams["font.sans-serif"]=["SimHei"]
def generate_picture(file_path,width=800, height=600):
    word_dict= wh.get_word_dict(file_path)
    # 生成词云图的对象
    wordcloud = WordCloud(font_path=r"../font/msyh.ttc",background_color="white", width=width, height=height, random_state=1).generate_from_frequencies(word_dict)

    # 显示词云图
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()
