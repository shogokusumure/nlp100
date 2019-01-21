#!/usr/bin/env python
# coding: utf-8

# # 言語処理100本ノック 2015
# http://www.cl.ecei.tohoku.ac.jp/nlp100/

# ## 第1章: 準備運動

# ### 00. 文字列の逆順
# 文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．

# In[9]:


txt = 'stressed'
reversed_txt= list(reversed(txt))
str_txt = ''.join(reversed_txt)
print(str_txt)


# ### 01.「パタトクカシーー」
# 「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．

# In[13]:


txt = 'パタトクカシーー'
listed_txt = list(txt)
ans = listed_txt[0] + listed_txt[2] + listed_txt[4] + listed_txt[6]

print(ans)


# ### 02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
# 「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．

# In[91]:


txt1 = 'パトカー'
txt2 = 'タクシー'
listed_txt1 = list(txt1)
listed_txt2 = list(txt2)

len1 = len(listed_txt1)
len2 = len(listed_txt2)

if abs(len1-len2) > 1:
    print('テキストの長さがあいません')
else:
    ans = ''
    for i in range(len1):
        ans +=  listed_txt1[i] + listed_txt2[i]
    print(ans)


# ### 03. 円周率
# "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."という文を単語に分解し，
# 各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．

# In[89]:


txt = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
# 句読点消し
txt = txt.replace(',','')
txt = txt.replace('.','')

word_list = txt.split(' ')
ans = []
for i in word_list:
    ans.append(len(i))

ans


# ### 04. 元素記号
# "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．

# In[88]:


txt = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
# 句読点消し
txt = txt.replace(',','')
txt = txt.replace('.','')

single_list = [1,5,6,7,8,9,15,16]

word_list = txt.split(' ')
ans = {}
for i,name in enumerate(word_list):
    if i + 1 in single_list:
        ans[name[:1]] = i
        continue
    ans[name[:2]] = i

ans


# ### 05. n-gram
# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．

# In[57]:


def createNgram(str, mode):
    ans = []
    if mode == 'moji':
        devidedTxt = list(str)
        length = len(devidedTxt)
        for i in range(length - 1):
            ans.append(devidedTxt[i] + devidedTxt[i + 1])
    elif mode == 'word':
        str = txt.replace(',','')
        str = txt.replace('.','')
        
        devidedTxt = str.split(' ')
        length = len(devidedTxt)
        for i in range(length - 1):
            ans.append(devidedTxt[i] + ' ' + devidedTxt[i + 1])
    else:
        return '無効なモードです'    
    return ans

txt = 'I am an NLPer'
print(createNgram(txt,'moji'))
print(createNgram(txt,'word'))


# ### 06. 集合
# "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．

# In[66]:


txt1 = 'paraparaparadise'
txt2 = 'paragraph'

list1 = set(createNgram(txt1,'moji'))
list2 = set(createNgram(txt2,'moji'))

print(list1 | list2)
print(set(list1 & list2))
print(list1 - list2)


# ### 07. テンプレートによる文生成
# 引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．

# In[87]:


def makeSentence(x,y,z):
    return str(x)+'時の'+str(y)+'は'+str(z)

makeSentence(12, '気温', 22.4)


# ### 08. 暗号文
# 与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
# 
# 英小文字ならば(219 - 文字コード)の文字に置換<br>
# その他の文字はそのまま出力<br>
# この関数を用い，英語のメッセージを暗号化・復号化せよ．

# In[86]:


def cipher(str):
    str_list = list(str)
    
    ans = ''
    for i in str_list:
        if i.islower():
            ans += chr(219-ord(i))
        else:
            ans += i
            
    return ans

print (cipher('I have a Pen.'))
print (cipher(cipher('I have a Pen.')))


# ### 09. Typoglycemia
# スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）を与え，その実行結果を確認せよ．

# In[110]:


txt = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
import random

def shuffleTxt(str):
    if len(str) < 4:
        return str
    else:
        head = str[:1]
        body = str[1:-1]
        foot = str[-1:]
        
        body_list = list(body)
        random.shuffle(body_list)
        
        ans = head + ''.join(body_list) + foot
        
        return ans
    
shuffleTxt(txt)

