'''
使用bert模型进行中文文本纠错，bert中文模型："./pre_models/bert/chinese_L-12_H-768_A-12/bert_model.ckpt"
前提：假设已经知道了错别字的位置，将错别字位置用[mask]替换，通过预测[mask]位置的词来进行纠错

注：中文文本纠错github：https://github.com/shibing624/pycorrector
'''

from bert4keras.models import build_transformer_model
from bert4keras.tokenizers import Tokenizer
from config2 import Config
import numpy as np
import time
import os

os.environ['CUDA_VISIBLE_DEVICES'] = '0'

class MaskedLM():
    def __init__(self,topK):
        self.topK = topK
        self.tokenizer = Tokenizer(Config.BERT_VOCAB_PATH,do_lower_case=True)
        # with_mlm： mask language model， with_mlm =True：使用mask
        self.model = build_transformer_model(Config.BERT_CONFIG_PATH,Config.BERT_CHECKPOINT_PATH,with_mlm =True)
        self.token_ids , self.segments_ids = self.tokenizer.encode(' ')

    # 对输入的文本进行编码
    def tokenizer_text(self,text):
        self.token_ids,self.segments_ids = self.tokenizer.encode(text)

    #假设输入： 我喜欢吃程度的火锅  [5,6] （索引0对应的为句子的开始标记符）
    def find_topn_candidates(self,error_index):     #error_index：错字对应的index
        for i in error_index:
            self.token_ids[i] = self.tokenizer._token_dict['[MASK]']    #对错字进行mask

        # 文本text中每个词的概率
        probs = self.model.predict([np.array([self.token_ids]),np.array([self.segments_ids])])[0]
        print(probs)
        print(probs[5])

        for i in range(len(error_index)):
            error_id = error_index[i]
            # top_k_pros：为字典，k为字，value为对应的概率
            top_k_pros = np.argsort(-probs[error_id])[:self.topK]
            # fin_prob：候选词对应的概率。 decode：通过id找到对应的字
            candidates,fin_prob = self.tokenizer.decode(top_k_pros),probs[error_id][top_k_pros]
            print(dict(zip(candidates,fin_prob)))


if __name__ == "__main__":
    maskLm = MaskedLM(5)        # topk = 5
    text = "刚刚一直在和老黄谈天，他和他聊天很愉快"
    maskLm.tokenizer_text(text)
    maskLm.find_topn_candidates([9,12])
