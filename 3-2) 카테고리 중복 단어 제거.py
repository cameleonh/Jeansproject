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
    "# 불용어 제거 - 2글자 이상인 단어만 추출\n",
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
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "tagging.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 각 카테고리별 데이터 프레임 만들기\n",
    "\n",
    "money_df = tagging.loc[tagging['money'] == 1].reset_index(drop=True)\n",
    "interview_df = tagging.loc[tagging['interview'] == 1].reset_index(drop=True)\n",
    "edu_df = tagging.loc[tagging['edu'] == 1].reset_index(drop=True)\n",
    "job_df = tagging.loc[tagging['job'] == 1].reset_index(drop=True)\n",
    "consult_df = tagging.loc[tagging['consult'] == 1].reset_index(drop=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 각 카테고리별 단어들 리스트 생성\n",
    "\n",
    "nouns_money = []\n",
    "for i in range(len(money_df['content'])):\n",
    "    nouns_money.extend(mecab.nouns(money_df['content'][i]))\n",
    "    \n",
    "nouns_interview = []\n",
    "for i in range(len(interview_df['content'])):\n",
    "    nouns_interview.extend(mecab.nouns(interview_df['content'][i]))\n",
    "\n",
    "nouns_edu = []\n",
    "for i in range(len(edu_df['content'])):\n",
    "    nouns_edu.extend(mecab.nouns(edu_df['content'][i]))\n",
    "    \n",
    "nouns_job = []\n",
    "for i in range(len(job_df['content'])):\n",
    "    nouns_job.extend(mecab.nouns(job_df['content'][i]))\n",
    "    \n",
    "nouns_consult = []\n",
    "for i in range(len(consult_df['content'])):\n",
    "    nouns_consult.extend(mecab.nouns(consult_df['content'][i]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 불용어 똑같이 제거 (2글자 이상인 단어)\n",
    "\n",
    "nouns_money = [i for i in nouns_money if len(i) >= 2]\n",
    "nouns_interview = [i for i in nouns_interview if len(i) >= 2]\n",
    "nouns_edu = [i for i in nouns_edu if len(i) >= 2]\n",
    "nouns_job = [i for i in nouns_job if len(i) >= 2]\n",
    "nouns_consult = [i for i in nouns_consult if len(i) >= 2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "15855\n",
      "3781\n",
      "16411\n",
      "14446\n",
      "10669\n"
     ]
    }
   ],
   "source": [
    "print(len(nouns_money))\n",
    "print(len(nouns_interview))\n",
    "print(len(nouns_edu))\n",
    "print(len(nouns_job))\n",
    "print(len(nouns_consult))\n",
    "\n",
    "# 다해서 61162"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 각 카테고리별 단어들 리스트 합친것 (중복 매우 많음, 다해서 61162개의 단어)\n",
    "\n",
    "nouns = nouns_money + nouns_interview + nouns_edu +  nouns_job + nouns_consult"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 전체 정책의 단어들의 빈도수 출력\n",
    "\n",
    "cnt_df0 = pd.DataFrame()\n",
    "cnt_df0['description_word'] = dict(Counter(nouns_list)).keys()\n",
    "cnt_df0['total_cnt'] = dict(Counter(nouns_list)).values()\n",
    "\n",
    "cnt_df0.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "### money/지원금 ### 카테고리의 단어들과 빈도수\n",
    "\n",
    "cnt_rank = pd.DataFrame()\n",
    "cnt_rank['description_word'] = pd.Series(list(dict(Counter(nouns_money)).keys()))\n",
    "cnt_rank['cnt_money'] = pd.Series(list(dict(Counter(nouns_money)).values()))\n",
    "\n",
    "cnt_rank = cnt_rank.sort_values(by='cnt_money', ascending = False)\n",
    "\n",
    "### 전체 정책의 단어들의 빈도수 조인\n",
    "cnt_rank = pd.merge(cnt_rank, cnt_df0, how = 'left', on = ['description_word'])\n",
    "\n",
    "### 카테고리 안에서 단어 빈도수 / 전체 정책에서의 단어 빈도수\n",
    "cnt_rank['pnt_money'] = cnt_rank['cnt_money'] / cnt_rank['total_cnt']\n",
    "\n",
    "cnt_money_df = cnt_rank.copy() # 따로 저장"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [],
   "source": [
    "### interview/면접 ### 카테고리의 단어들과 빈도수\n",
    "\n",
    "cnt_rank = pd.DataFrame()\n",
    "cnt_rank['description_word'] = pd.Series(list(dict(Counter(nouns_interview)).keys()))\n",
    "cnt_rank['cnt_interview'] = pd.Series(list(dict(Counter(nouns_interview)).values()))\n",
    "\n",
    "cnt_rank = cnt_rank.sort_values(by='cnt_interview', ascending = False)\n",
    "\n",
    "cnt_rank = pd.merge(cnt_rank, cnt_df0, how = 'left', on = ['description_word'])\n",
    "cnt_rank['pnt_interview'] = cnt_rank['cnt_interview'] / cnt_rank['total_cnt']\n",
    "\n",
    "cnt_interview_df = cnt_rank.copy()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [],
   "source": [
    "### edu/교육 ### 카테고리의 단어들과 빈도수\n",
    "\n",
    "cnt_rank = pd.DataFrame()\n",
    "cnt_rank['description_word'] = pd.Series(list(dict(Counter(nouns_edu)).keys()))\n",
    "cnt_rank['cnt_edu'] = pd.Series(list(dict(Counter(nouns_edu)).values()))\n",
    "\n",
    "cnt_rank = cnt_rank.sort_values(by='cnt_edu', ascending = False)\n",
    "\n",
    "cnt_rank = pd.merge(cnt_rank, cnt_df0, how = 'left', on = ['description_word'])\n",
    "cnt_rank['pnt_edu'] = cnt_rank['cnt_edu'] / cnt_rank['total_cnt']\n",
    "\n",
    "cnt_edu_df = cnt_rank.copy()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [],
   "source": [
    "### job/일자리 ### 카테고리의 단어들과 빈도수\n",
    "\n",
    "cnt_rank = pd.DataFrame()\n",
    "cnt_rank['description_word'] = pd.Series(list(dict(Counter(nouns_job)).keys()))\n",
    "cnt_rank['cnt_job'] = pd.Series(list(dict(Counter(nouns_job)).values()))\n",
    "\n",
    "cnt_rank = cnt_rank.sort_values(by='cnt_job', ascending = False)\n",
    "\n",
    "cnt_rank = pd.merge(cnt_rank, cnt_df0, how = 'left', on = ['description_word'])\n",
    "cnt_rank['pnt_job'] = cnt_rank['cnt_job'] / cnt_rank['total_cnt']\n",
    "\n",
    "cnt_job_df = cnt_rank.copy()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [],
   "source": [
    "### consult/상담 ### 카테고리의 단어들과 빈도수\n",
    "\n",
    "cnt_rank = pd.DataFrame()\n",
    "cnt_rank['description_word'] = pd.Series(list(dict(Counter(nouns_consult)).keys()))\n",
    "cnt_rank['cnt_consult'] = pd.Series(list(dict(Counter(nouns_consult)).values()))\n",
    "\n",
    "cnt_rank = cnt_rank.sort_values(by='cnt_consult', ascending = False)\n",
    "\n",
    "cnt_rank = pd.merge(cnt_rank, cnt_df0, how = 'left', on = ['description_word'])\n",
    "cnt_rank['pnt_consult'] = cnt_rank['cnt_consult'] / cnt_rank['total_cnt']\n",
    "\n",
    "cnt_consult_df = cnt_rank.copy()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 카테고리 5개 모두 포함된 단어 제거"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 이너조인 - 5개 모두 포함되는 단어 추출\n",
    "\n",
    "df = pd.merge(cnt_money_df, cnt_interview_df, on = 'description_word', how = 'inner')\n",
    "df = pd.merge(df, cnt_edu_df, on = 'description_word', how = 'inner')\n",
    "df = pd.merge(df, cnt_job_df, on = 'description_word', how = 'inner')\n",
    "df = pd.merge(df, cnt_consult_df, on = 'description_word', how = 'inner')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = df[['description_word','cnt_money','pnt_money','cnt_interview','pnt_interview','cnt_edu','pnt_edu','cnt_job','pnt_job','cnt_consult','pnt_consult','total_cnt']]\n",
    "pnt_df = df[['description_word','pnt_money','pnt_interview','pnt_edu','pnt_job','pnt_consult','total_cnt']]\n",
    "\n",
    "pnt_df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 450,
   "metadata": {},
   "outputs": [],
   "source": [
    "# cnt_money를 기준으로 가중치 곱해주기\n",
    "\n",
    "pnt_df['pnt_interview'] = pnt_df['pnt_interview'] * (len(cnt_money) / len(cnt_interview))\n",
    "pnt_df['pnt_edu'] = pnt_df['pnt_edu'] * (len(cnt_money) / len(cnt_edu))\n",
    "pnt_df['pnt_job'] = pnt_df['pnt_job'] * (len(cnt_money) / len(cnt_job))\n",
    "pnt_df['pnt_consult'] = pnt_df['pnt_consult'] * (len(cnt_money) / len(cnt_consult))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [],
   "source": [
    "# pnt_df.to_csv('five_nouns.csv', index = False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 각 카테고리별로 pnt를 내림차순으로 정렬한 후 상위 20개 단어는 각 카테고리에 포함(그 이외는 삭제)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "61162"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 각 카테고리별 단어들 리스트 합친것 (중복 매우 많음, 다해서 61162개의 단어)\n",
    "\n",
    "nouns = nouns_money + nouns_interview + nouns_edu + nouns_job + nouns_consult\n",
    "len(nouns)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 각 카테고리별 유니크 단어들로 데이터프레임 + 빈도수까지 추가\n",
    "\n",
    "word_df = pd.DataFrame({'description_word' : list(set(nouns))})\n",
    "word_df = pd.merge(word_df, cnt_df0, on = 'description_word', how='left')\n",
    "word_df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 더미변수 생성\n",
    "\n",
    "word_df['money'] = pd.Series([i in nouns_money for i in word_df['description_word']])\n",
    "word_df['interview'] = pd.Series([i in nouns_interview for i in word_df['description_word']])\n",
    "word_df['edu'] = pd.Series([i in nouns_edu for i in word_df['description_word']])\n",
    "word_df['job'] = pd.Series([i in nouns_job for i in word_df['description_word']])\n",
    "word_df['consult'] = pd.Series([i in nouns_consult for i in word_df['description_word']])\n",
    "\n",
    "word_df = word_df.replace(True, 1).replace(False, 0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 5개 카테고리 모두 포함되는 단어 삭제\n",
    "\n",
    "for i in range(len(word_df)):\n",
    "    if word_df['money'][i] + word_df['interview'][i] + word_df['edu'][i] + word_df['job'][i] + word_df['consult'][i] == 5:\n",
    "        word_df.drop(i, inplace = True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 5개 포함 단어 중 포함시킬 것들\n",
    "\n",
    "five = pd.read_csv('five_nouns_add.csv', encoding = 'euc-kr')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 5개 카테고리 모두 포함되는 단어 중 포함시킬 단어들 리스트로 만들기\n",
    "\n",
    "add_list = list(five['pnt_money']) + list(five['pnt_interview']) + list(five['pnt_edu']) + list(five['pnt_job']) + list(five['pnt_consult'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 위 word_df와 같은 형식으로 추가할 단어들 데이터프레임 만들기\n",
    "\n",
    "add_df = pd.DataFrame({'description_word' : list(set(add_list)), 'money':0,'interview':0,'edu':0,'job':0,'consult':0})\n",
    "add_df = pd.merge(add_df,cnt_df0, on = 'description_word', how = 'left')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 더미변수 채우기\n",
    "\n",
    "for i in range(len(add_df)):\n",
    "    if add_df['description_word'][i] in list(five['pnt_money']):\n",
    "        add_df.iloc[i,1] = 1\n",
    "        \n",
    "    if add_df['description_word'][i] in list(five['pnt_interview']):\n",
    "        add_df.iloc[i,2] = 1\n",
    "        \n",
    "    if add_df['description_word'][i] in list(five['pnt_edu']):\n",
    "        add_df.iloc[i,3] = 1\n",
    "        \n",
    "    if add_df['description_word'][i] in list(five['pnt_job']):\n",
    "        add_df.iloc[i,4] = 1\n",
    "        \n",
    "    if add_df['description_word'][i] in list(five['pnt_consult']):\n",
    "        add_df.iloc[i,5] = 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {},
   "outputs": [],
   "source": [
    "word_df = pd.concat([word_df, add_df]).reset_index(drop = True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [],
   "source": [
    "# word_df.to_csv('word_dataframe.csv', index = False)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 카테고리 3, 4개 모두 포함된 단어 제거\n",
    "\n",
    "### 4개 추출"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 카테고리 4개에 포함되는 단어 추출\n",
    "\n",
    "word_df_4 = word_df.loc[word_df['money'] + word_df['interview'] + word_df['edu'] + word_df['job'] + word_df['consult'] == 4]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 카테고리 4개 겹치는 단어에 percent 붙이기\n",
    "\n",
    "word_df_4 = pd.merge(word_df_4, cnt_money_df[['description_word','pnt_money']], how = 'left', on = 'description_word')\n",
    "word_df_4 = pd.merge(word_df_4, cnt_interview_df[['description_word','pnt_interview']], how = 'left', on = 'description_word')\n",
    "word_df_4 = pd.merge(word_df_4, cnt_edu_df[['description_word','pnt_edu']], how = 'left', on = 'description_word')\n",
    "word_df_4 = pd.merge(word_df_4, cnt_job_df[['description_word','pnt_job']], how = 'left', on = 'description_word')\n",
    "word_df_4 = pd.merge(word_df_4, cnt_consult_df[['description_word','pnt_consult']], how = 'left', on = 'description_word')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "word_df_4 = word_df_4[['description_word','pnt_money','pnt_interview','pnt_edu','pnt_job','pnt_consult','total_cnt']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 470,
   "metadata": {},
   "outputs": [],
   "source": [
    "# word_df_4.to_csv('four_nouns.csv', index = False)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 카테고리 3, 4개 모두 포함된 단어 제거\n",
    "\n",
    "### 3개 추출"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 카테고리 3개에 포함되는 단어 추출\n",
    "\n",
    "word_df_3 = word_df.loc[word_df['money'] + word_df['interview'] + word_df['edu'] + word_df['job'] + word_df['consult'] == 3]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "metadata": {},
   "outputs": [],
   "source": [
    "word_df_3 = pd.merge(word_df_3, cnt_money_df[['description_word','pnt_money']], how = 'left', on = 'description_word')\n",
    "word_df_3 = pd.merge(word_df_3, cnt_interview_df[['description_word','pnt_interview']], how = 'left', on = 'description_word')\n",
    "word_df_3 = pd.merge(word_df_3, cnt_edu_df[['description_word','pnt_edu']], how = 'left', on = 'description_word')\n",
    "word_df_3 = pd.merge(word_df_3, cnt_job_df[['description_word','pnt_job']], how = 'left', on = 'description_word')\n",
    "word_df_3 = pd.merge(word_df_3, cnt_consult_df[['description_word','pnt_consult']], how = 'left', on = 'description_word')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "word_df_3 = word_df_3[['description_word','pnt_money','pnt_interview','pnt_edu','pnt_job','pnt_consult','total_cnt']]\n",
    "word_df_3.sort_values(by='total_cnt')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "metadata": {},
   "outputs": [],
   "source": [
    "# word_df_3.to_csv('three_nouns.csv', index = False)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 3,4 카테고리 들어간 단어 삭제, 살릴 단어만 추가"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "metadata": {},
   "outputs": [],
   "source": [
    "four = pd.read_csv('C:/Users/juwan/Desktop/산학프로젝트/four_nouns_add.csv', encoding = 'euc-kr')\n",
    "three = pd.read_csv('C:/Users/juwan/Desktop/산학프로젝트/three_nouns_add.csv', encoding = 'euc-kr')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "metadata": {},
   "outputs": [],
   "source": [
    "### 4개 카테고리 모두 포함되는 단어 삭제\n",
    "\n",
    "for i in range(len(word_df)):\n",
    "    if word_df['money'][i] + word_df['interview'][i] + word_df['edu'][i] + word_df['job'][i] + word_df['consult'][i] == 4:\n",
    "        word_df.drop(i, inplace = True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 4개 카테고리 모두 포함되는 단어 중 포함시킬 단어들 리스트로 만들기\n",
    "\n",
    "four_list = list(four['pnt_money']) + list(four['pnt_interview']) + list(four['pnt_edu']) + list(four['pnt_job']) + list(four['pnt_consult'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "metadata": {},
   "outputs": [],
   "source": [
    "add_df = pd.DataFrame({'description_word' : list(set(four_list)), 'money':0,'interview':0,'edu':0,'job':0,'consult':0})\n",
    "add_df = pd.merge(add_df,cnt_df0, on = 'description_word', how = 'left')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "metadata": {},
   "outputs": [],
   "source": [
    "add_df = add_df.dropna()\n",
    "add_df = add_df.reset_index(drop = True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 더미변수 채우기\n",
    "\n",
    "for i in range(len(add_df)):\n",
    "    if add_df['description_word'][i] in list(four['pnt_money']):\n",
    "        add_df.iloc[i,1] = 1\n",
    "        \n",
    "    if add_df['description_word'][i] in list(four['pnt_interview']):\n",
    "        add_df.iloc[i,2] = 1\n",
    "        \n",
    "    if add_df['description_word'][i] in list(four['pnt_edu']):\n",
    "        add_df.iloc[i,3] = 1\n",
    "        \n",
    "    if add_df['description_word'][i] in list(four['pnt_job']):\n",
    "        add_df.iloc[i,4] = 1\n",
    "        \n",
    "    if add_df['description_word'][i] in list(four['pnt_consult']):\n",
    "        add_df.iloc[i,5] = 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "metadata": {},
   "outputs": [],
   "source": [
    "word_df = pd.concat([word_df, add_df])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "metadata": {},
   "outputs": [],
   "source": [
    "word_df = word_df.reset_index(drop = True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "### 3개 카테고리 모두 포함되는 단어 삭제\n",
    "\n",
    "for i in range(len(word_df)):\n",
    "    if word_df['money'][i] + word_df['interview'][i] + word_df['edu'][i] + word_df['job'][i] + word_df['consult'][i] == 3:\n",
    "        word_df.drop(i, inplace = True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 3개 카테고리 모두 포함되는 단어 중 포함시킬 단어들 리스트로 만들기\n",
    "\n",
    "three_list = list(three['pnt_money']) + list(three['pnt_interview']) + list(three['pnt_edu']) + list(three['pnt_job']) + list(three['pnt_consult'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "metadata": {},
   "outputs": [],
   "source": [
    "add_df = pd.DataFrame({'description_word' : list(set(three_list)), 'money':0,'interview':0,'edu':0,'job':0,'consult':0})\n",
    "add_df = pd.merge(add_df,cnt_df0, on = 'description_word', how = 'left')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "metadata": {},
   "outputs": [],
   "source": [
    "add_df = add_df.dropna()\n",
    "add_df = add_df.reset_index(drop = True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 더미변수 채우기\n",
    "\n",
    "for i in range(len(add_df)):\n",
    "    if add_df['description_word'][i] in list(three['pnt_money']):\n",
    "        add_df.iloc[i,1] = 1\n",
    "        \n",
    "    if add_df['description_word'][i] in list(three['pnt_interview']):\n",
    "        add_df.iloc[i,2] = 1\n",
    "        \n",
    "    if add_df['description_word'][i] in list(three['pnt_edu']):\n",
    "        add_df.iloc[i,3] = 1\n",
    "        \n",
    "    if add_df['description_word'][i] in list(three['pnt_job']):\n",
    "        add_df.iloc[i,4] = 1\n",
    "        \n",
    "    if add_df['description_word'][i] in list(three['pnt_consult']):\n",
    "        add_df.iloc[i,5] = 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "metadata": {},
   "outputs": [],
   "source": [
    "word_df = pd.concat([word_df, add_df])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 104,
   "metadata": {},
   "outputs": [],
   "source": [
    "word_df = word_df.reset_index(drop = True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "metadata": {},
   "outputs": [],
   "source": [
    "# cnt행 붙여넣기\n",
    "\n",
    "word_df_cnt = pd.merge(word_df, cnt_money_df[['description_word','cnt_money']], on = 'description_word', how = 'left')\n",
    "word_df_cnt = pd.merge(word_df_cnt, cnt_interview_df[['description_word','cnt_interview']], on = 'description_word', how = 'left')\n",
    "word_df_cnt = pd.merge(word_df_cnt, cnt_edu_df[['description_word','cnt_edu']], on = 'description_word', how = 'left')\n",
    "word_df_cnt = pd.merge(word_df_cnt, cnt_job_df[['description_word','cnt_job']], on = 'description_word', how = 'left')\n",
    "word_df_cnt = pd.merge(word_df_cnt, cnt_consult_df[['description_word','cnt_consult']], on = 'description_word', how = 'left')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "metadata": {},
   "outputs": [],
   "source": [
    "# word_df에 포함되지 않은 단어 NA 없애기\n",
    "\n",
    "word_df_cnt = word_df_cnt.fillna(0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 113,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 위에서 5,4,3카테고리 --> 2개로 바꿀 때 제외된 카테고리 0값 주기\n",
    "\n",
    "for i in range(len(word_df_cnt)):\n",
    "    if word_df_cnt['money'][i] == 0:\n",
    "        word_df_cnt.iloc[i,7] = 0\n",
    "    if word_df_cnt['interview'][i] == 0:\n",
    "        word_df_cnt.iloc[i,8] = 0\n",
    "    if word_df_cnt['edu'][i] == 0:\n",
    "        word_df_cnt.iloc[i,9] = 0\n",
    "    if word_df_cnt['job'][i] == 0:\n",
    "        word_df_cnt.iloc[i,10] = 0\n",
    "    if word_df_cnt['consult'][i] == 0:\n",
    "        word_df_cnt.iloc[i,11] = 0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 114,
   "metadata": {},
   "outputs": [],
   "source": [
    "# pnt 다시 넣기\n",
    "\n",
    "word_df_cnt['pnt_money'] = word_df_cnt['cnt_money'] / word_df_cnt['total_cnt']\n",
    "word_df_cnt['pnt_interview'] = word_df_cnt['cnt_interview'] / word_df_cnt['total_cnt']\n",
    "word_df_cnt['pnt_edu'] = word_df_cnt['cnt_edu'] / word_df_cnt['total_cnt']\n",
    "word_df_cnt['pnt_job'] = word_df_cnt['cnt_job'] / word_df_cnt['total_cnt']\n",
    "word_df_cnt['pnt_consult'] = word_df_cnt['cnt_consult'] / word_df_cnt['total_cnt']"
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
