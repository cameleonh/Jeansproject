{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 필요한 라이브러리 불러오기\n",
    "\n",
    "from konlpy.tag import Mecab \n",
    "\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "\n",
    "from collections import Counter\n",
    "\n",
    "import warnings\n",
    "warnings.filterwarnings('ignore')\n",
    "\n",
    "dir = 'C:/Users/juwan/Desktop/산학프로젝트/using_data/'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "# mecab 실행\n",
    "\n",
    "mecab = Mecab(dicpath=r\"C:\\Mecab\\mecab-ko-dic\") # dictation path 설정 / mecab-ko-dic이 mecab의 단어사전임"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 형태소 분석할 데이터 준비 - 정책 내용 데이터 불러오기 \n",
    "\n",
    "tagging = pd.read_csv(dir + 'content_tagging.csv', encoding = 'utf-8')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "# name, description, content의 모든 내용으로 단어 추출\n",
    "\n",
    "nouns_list = []\n",
    "\n",
    "for i in range(len(tagging['content'])):\n",
    "    nouns_list.extend(mecab.nouns(tagging['content'][i]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 불용어 제거(1) - 2글자 이상인 단어만 추출\n",
    "\n",
    "nouns_list = [i for i in nouns_list if len(i) >= 2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 행 전체 다 보기\n",
    "\n",
    "pd.set_option('display.max_rows',None)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "word_df_cnt = pd.read_csv(dir + 'word_df_cnt.csv', encoding = 'utf-8')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 사용자 정의 함수 \n",
    "\n",
    "#### 1. score함수 \n",
    "- 각 카테고리 마다의 점수를 합하여 리스트로 반환"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "def score(text): # input: 문자열 텍스트\n",
    "    \n",
    "    nl = mecab.nouns(text)\n",
    "    \n",
    "    score_money = 0\n",
    "    score_interview = 0\n",
    "    score_edu = 0\n",
    "    score_job = 0\n",
    "    score_consult = 0\n",
    "\n",
    "    for i in nl:\n",
    "        if i in list(word_df_cnt['description_word']):\n",
    "            score_money += int(word_df_cnt.loc[word_df_cnt['description_word'] == i, 'pnt_money'])\n",
    "            score_interview += int(word_df_cnt.loc[word_df_cnt['description_word'] == i, 'pnt_interview'])\n",
    "            score_edu += int(word_df_cnt.loc[word_df_cnt['description_word'] == i, 'pnt_edu'])\n",
    "            score_job += int(word_df_cnt.loc[word_df_cnt['description_word'] == i, 'pnt_job'])\n",
    "            score_consult += int(word_df_cnt.loc[word_df_cnt['description_word'] == i, 'pnt_consult'])\n",
    "        else:\n",
    "            continue\n",
    "    return [score_money, score_interview, score_edu, score_job, score_consult]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 2. whatcategory함수 \n",
    "- score함수로 만든 점수 리스트를 넣으면 어떤 카테고리가 가장 높은 점수인지 출력(복수개면 복수개 출력)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "def whatcategory(score_list):\n",
    "    category = []\n",
    "    for i in range(len(score_list)):\n",
    "        if score_list[i] == max(score_list):\n",
    "            if i == 0:\n",
    "                category.append('money')\n",
    "            if i == 1:\n",
    "                category.append('interview')\n",
    "            if i == 2:\n",
    "                category.append('edu')\n",
    "            if i == 3:\n",
    "                category.append('job')\n",
    "            if i == 4:\n",
    "                category.append('consult')\n",
    "    return category"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['edu']"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "whatcategory(score('안녕하세요 저는 빅데이터 분야로 취업하고 싶어 교육을 신청하는 사람입니다'))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 테스트"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "nums = []\n",
    "text_list = tagging.loc[(tagging['index'] == 34)|(tagging['index'] == 48)|(tagging['index'] == 30)|(tagging['index'] == 62)|(tagging['index'] == 72)|(tagging['index'] == 82)|(tagging['index'] == 87)|(tagging['index'] == 127)|(tagging['index'] == 137)|(tagging['index'] == 295),'content']\n",
    "text_list= text_list.reset_index(drop=True)\n",
    "text_list = list(text_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "cat = []\n",
    "for i in text_list:\n",
    "    cat.append(whatcategory(score(i)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "text_df = tagging.loc[(tagging['index'] == 34)|(tagging['index'] == 48)|(tagging['index'] == 30)|(tagging['index'] == 62)|(tagging['index'] == 72)|(tagging['index'] == 82)|(tagging['index'] == 87)|(tagging['index'] == 127)|(tagging['index'] == 137)|(tagging['index'] == 295)]\n",
    "text_df = text_df[['name','description','content']]\n",
    "text_df['predict_cat'] = [', '.join(i) for i in cat]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "text_df['actual_cat'] = ['money','interview','interview','money','job','job','edu','edu','consult','consult']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "counseling = pd.read_csv(dir + 'counseling.csv', encoding = 'euc-kr')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "pred_cat = []\n",
    "\n",
    "for i in list(counseling['title'] + ' ' + counseling['text']):\n",
    "    pred_cat.append(whatcategory(score(i)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [],
   "source": [
    "counseling['pred_cat'] = [', '.join(i) for i in pred_cat]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "pd.options.display.max_colwidth = 2000"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {
    "scrolled": false
   },
   "outputs": [],
   "source": [
    "lisst = [i.split(', ') for i in counseling['tag']]\n",
    "\n",
    "for i in lisst:\n",
    "    for j in range(len(i)):\n",
    "        if i[j] == '취업상담':\n",
    "            i[j] = 'consult'\n",
    "        if i[j] == '면접지원':\n",
    "            i[j] = 'interview'\n",
    "        if i[j] == '일자리':\n",
    "            i[j] = 'job'\n",
    "        if i[j] == '지원금':\n",
    "            i[j] = 'money'\n",
    "        if i[j] == '교육지원':\n",
    "            i[j] = 'edu'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "metadata": {},
   "outputs": [],
   "source": [
    "counseling['tag2'] = [', '.join(i) for i in lisst]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(342, 4)"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "counseling.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
