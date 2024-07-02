from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np

# 准备一段文本
text = "Python is a high-level programming language. It is general-purpose, meaning that it can be used for various tasks, including web development, data science, and machine learning."

# 生成词云图的对象
wordcloud = WordCloud(background_color="white", width=800, height=600, random_state=1).generate(text)

# 显示词云图
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()