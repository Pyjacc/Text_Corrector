# -*- coding: utf-8 -*-
"""
@author:XuMing（xuming624@qq.com)
@description: 
"""
import sys

sys.path.append('..')
import pycorrector

text = ['做的最倒霉的一件事就帮尼哥檫脚。'
        '那天花板上的钻石可比鸡弹还大啊'
        '才般进装修好没多久的新宫殿里。'
        '一但死去，以前花费的心血都会归零。'
        '战士微笑著轻轻拍了拍少年的肩膀。'
        '差点拌到自己的脚。'
        '面对着熙熙嚷嚷的城市。'
        '你等我和老大商却一下。'
        '这家伙还蛮格尽职守的。'
        '玩家取明“什么”已被占用。'
        '报应接中迩来。'
        '人群穿流不息。'
        '这个消息不径而走。'
        '眼前的场景美仑美幻简直超出了人类的想象。'
        '看着这两个人谈笑风声我心理不由有些忌妒。'
        '有老怪坐阵难怪他们高枕无忧了。'
        '有了这一番旁证博引。',
        '这个跟 原木纯品 那个啥区别？不是原木纸浆做的?'
        ]


def demo1():
    for i in text:
        print(i, pycorrector.detect(i))
        print(i, pycorrector.correct(i))


x = ['做的最倒霉的一件事就帮尼哥檫脚,'
     '那天花板上的钻石可比鸡弹还大啊，'
     '有老怪坐阵难怪他们高枕无忧了。'
     '战士微笑著轻轻拍了拍少年的肩膀？'
     '差点拌到自己的脚？'
     '你等我和老大商却一下、'
     '这家伙还蛮格尽职守的，'
     '报应接中迩来："谢谢"，'
     '这个消息不径而走；'
     '眼前的场景美仑美幻简直超出了人类的想象，'
     '看着这两个人谈笑风声我心理不由有些忌妒。',
     '有了这一番旁证博引']


def demo2():
    for i in x:
        print(i, pycorrector.detect(i))
        print(i, pycorrector.correct(i))


if __name__ == '__main__':
    demo1()
    demo2()
