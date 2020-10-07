'''
英文文本纠错：
# 错误词更正为正确词的概率
p(正确词 | 错误词) = p(正确词) * p(错误词|正确词)/p(错误词)
p(正确词 | 错误词) = p(正确词，错误词)/p(错误词)

# 正确词写错的概率
p(错误词 | 正确词) = p(错误词，正确词)/p(正确词) = p(正确词，错误词)/p(正确词)  ====>
    p(正确词，错误词) = p(错误词 | 正确词) * p(正确词)  ====>
    p(正确词，错误词)/p(错误词) = p(错误词 | 正确词) * p(正确词)/p(错误词) ====>
    p(正确词 | 错误词) = p(正确词) * p(错误词|正确词)/p(错误词)
    因为p(错误词|正确词)/p(错误词)无法得到，则假设p(错误词|正确词)/p(错误词)的值为1，则将p(正确词)的概率作为
    p(正确词 | 错误词)的概率，即用文本中词出现的频次作为选择该词作为正确的词概率（即用该词替换错误词的概率）

前提：
    文本等长
    假设已经知道了错误词的位置
'''

import re,collections

# 去掉不必要的字符（标点符号）
def words(text):
    return re.findall("[a-z]+",text.lower())

# 构建字典（词表）
def train(words):
    model = collections.defaultdict(int)        #创建字典
    for word in words:
        model[word] += 1
    return model


alphabet = "abcdefghijklmnopqrstuvwxyz"     # 26个英文字母表
word_list = train(words(open('./data.txt').read()))
# print(word_list)

# 判断一个词是不是正确的词（如果词不在data.txt文档中，则认为不是一个正确的词）
def know(words):
    return set(w for w in words if w in word_list)

# 求编辑距离，假设编辑距离为1（word为输入的错别字）
def edist1(word):
    n = len(word)

    # 正确词可能来自以下几种情况
    #删除（删除i对应索引的字母）
    s1 = [word[0:i] + word[i+1:] for i in range(n)]
    #相邻的字母调换（将索引i和i+1对应的字母调换）
    s2 = [word[0:i] + word[i+1]+word[i] + word[i+2:] for i in range(n-1)]
    #从26个字母表里选择一个做替换（用字母c替换i索引对应的字母）
    s3 = [word[0:i] + c + word[i+1:] for i in range(n) for c in alphabet]
    #插入（增加），从26个英文字母里面做插入（将字母c插入到索引i位置）
    s4 = [word[0:i] + c + word[i:] for i in range(n) for c in alphabet]

    edits_words = set(s1 + s2 + s3 + s4)    # 正确词候选集
    edits_words = know(edits_words)
    return edits_words

# 假设编辑距离为2，如错了2个词，交换了2个词等。（在编辑距离为1的基础上再做一个编辑距离为1，即编辑距离为2的情况）
def edits2(word):
    edits2_words = set(e2 for e1 in edist1(word) for e2 in edist1(e1))
    edits2_words = know(edits2_words)       # 判断候选集词是否为一个正确的词
    return edits2_words

# 纠错，从候选集中选择正确的词
def correct(word):
    if word not in word_list:       #word为错误的词
        candidates = edist1(word) or edits2(word)
        print(candidates)   #正确词候选集
        return max(candidates, key=lambda w:word_list[w])   #word_list[w]：词的频率
    else:       # word不是错误的词
        return word


if __name__ == "__main__":
    print(correct("firr"))      # 已经知道firr为错误的词
