from wordcloud import WordCloud
from jieba import posseg
import numpy as np
import PIL.Image as img


def word_segmentation(txt_content: str) -> list:
    """
    文本分词，使用jieba库的词性分词，保留文本中的名词(n)，人名(nr)，地名(ns)

    :param txt_content: 文本内容
    :return: 分词之后的列表
    """
    # word_list = []
    for _ in posseg.cut(txt_content):
        if _.flag in ["n", "nr", "ns"] and len(_.word) >=2:
            yield _.word
            # word_list.append(_.word)
    # return word_list


def word_frequency_count(word_list: list) -> list:
    """
    生成词频的哈希表
    :param word_list: 文本分词之后的列表
    :return: 词频排序之后的列表
    """

    word_frequency = {}
    for word in word_list:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
    # 将结果按照出现的频率排序
    sorted_word_frequency = sorted(word_frequency.items(), key=lambda x:x[1], reverse=True)
    return sorted_word_frequency


def create_world_cloud(name: str, text: str):
    """
    生成图云

    :param name: 文件名
    :param text: 要生成图云的文本
    """
    mask = np.array(img.open("../static/tree.jpg"))
    wordcloud = WordCloud(
        mask=mask,
        font_path="/home/zhi/code/jiandan/jiandan/static/simhei.ttf",
        # background_color="white"
    ).generate(text)
    wordcloud.to_file("../images/%s.jpg" % name)


if __name__ == '__main__':
    c = [('物品', 6), ('垃圾箱', 4), ('踩扁', 4), ('分类', 4), ('系统', 4), ('形状', 3), ('计划', 2), ('浪费', 2), ('铝罐', 2), ('罐子', 2), ('压扁', 2), ('扁平', 2), ('中心', 2), ('材料', 2), ('容器', 1), ('过程', 1), ('正确处理', 1), ('空间', 1), ('棘手', 1), ('工厂', 1), ('标记', 1), ('废物', 1), ('垃圾', 1), ('填埋场', 1), ('塑料瓶', 1), ('盖子', 1), ('铝业', 1), ('协会', 1), ('公共事务', 1), ('情况', 1), ('纸张', 1), ('纸板', 1), ('错误', 1), ('纸质', 1), ('习惯', 1), ('居住地', 1), ('美国', 1), ('单流', 1), ('多流', 1), ('双流', 1), ('市政当局', 1), ('区域', 1), ('明智', 1), ('变形', 1), ('大碍', 1)]
    word_content = " ".join([x[0] for x in c])
    create_world_cloud("test", word_content)
