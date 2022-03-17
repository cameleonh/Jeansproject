{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "\n",
    "dir = 'C:/Users/juwan/Desktop/산학프로젝트/using_data/'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {},
   "outputs": [],
   "source": [
    "pd.options.display.max_colwidth = 2000"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "content_raw = pd.read_csv(dir + 'policy_content.csv', encoding = 'euc-kr')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "content = content_raw.copy()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "content['content'] = content_raw['name'] + content_raw['description'] + content_raw['content']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 단어 속해있는지 확인하는 함수\n",
    "# 해당 텍스트에 단어 리스트 중 하나라도 들어있으면 True\n",
    "\n",
    "def find_word(text, words_list):\n",
    "    for i in words_list:\n",
    "        if text.find(i) == -1:\n",
    "            continue\n",
    "        else:\n",
    "            return True"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "index_list = []"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 1. 지원금\n",
    "\n",
    "words_list = ['만원','0원','수당','교육비','인건비','등록금','훈련비','지원비','지원금','자금','사업비','활동비','교통비', \\\n",
    "              '임차비','만 원','천 원','2원','급여','연구비','금전 지원','장려금','운영비', '체재비', '재료비', '의료비', '식비', '자기계발비', '교재비', '생활비', '부대비', '면접비',\n",
    "             '개발비', '조사비', '관리비', '노무비' ,'숙박비' ,'휴가비', '직무교육비', '구입비', '출장비', '주거비', \n",
    "             '교통복지비용', '문화활동비', '주거정착금', '준비금', '퇴직금', '장학금', '고용장려금', '임금', '고용장려금',\n",
    "             '보조금', '생활임금', '창업자금', '보상금', '상여금', '대여료']\n",
    "tf_list = []\n",
    "\n",
    "for text in content['content']:\n",
    "    if find_word(text,words_list) == True:\n",
    "        tf_list.append(True)\n",
    "    else:\n",
    "        tf_list.append(False)\n",
    "\n",
    "# 합치는 용\n",
    "index_list.extend(content.loc[pd.Series(tf_list)]['index'])\n",
    "        \n",
    "df1 = content.loc[pd.Series(tf_list)]\n",
    "df1.shape[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "123"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 2. 면접\n",
    "\n",
    "words_list = ['면접','면접정장','대여']\n",
    "tf_list = []\n",
    "\n",
    "for text in content['content']:\n",
    "    if find_word(text,words_list) == True:\n",
    "        tf_list.append(True)\n",
    "    else:\n",
    "        tf_list.append(False)\n",
    "        \n",
    "# 합치는 용\n",
    "index_list.extend(content.loc[pd.Series(tf_list)]['index'])        \n",
    "        \n",
    "df2 = content.loc[pd.Series(tf_list)]\n",
    "df2.shape[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "476"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 3. 교육\n",
    "\n",
    "words_list = ['교육','학습','강좌','양성','훈련','연수과정','기본과정','수강','자격증 취득지원'] \n",
    "tf_list = []\n",
    "\n",
    "for text in content['content']:\n",
    "    if find_word(text,words_list) == True:\n",
    "        tf_list.append(True)\n",
    "    else:\n",
    "        tf_list.append(False)\n",
    "        \n",
    "# 합치는 용\n",
    "index_list.extend(content.loc[pd.Series(tf_list)]['index'])\n",
    "        \n",
    "df3 = content.loc[pd.Series(tf_list)]\n",
    "df3.shape[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "422"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 4. 일자리\n",
    "\n",
    "words_list = ['일자리제공','실습','구인구직','중소기업','인턴십','인턴','직접일자리','기업연계','현장실습', \\\n",
    "              '단기일자리','실무 경험','연계','취업 매칭', '청년일자리', '일자리창출', '민간일자리', '여성일자리']\n",
    "tf_list = []\n",
    "\n",
    "for text in content['content']:\n",
    "    if find_word(text,words_list) == True:\n",
    "        tf_list.append(True)\n",
    "    else:\n",
    "        tf_list.append(False)\n",
    "        \n",
    "# 합치는 용\n",
    "index_list.extend(content.loc[pd.Series(tf_list)]['index'])\n",
    "\n",
    "df4 = content.loc[pd.Series(tf_list)]\n",
    "df4.shape[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "288"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 5. 취업상담\n",
    "\n",
    "words_list = ['멘토링','취업컨설팅','특강','해석','자기소개서','이력서','취업지원상담','상담','스터디공간','스터디룸','컨설팅' \\\n",
    "              ,'취업박람회','일자리센터','탐방','청년공간', '일자리카페','활동공간','일자리 센터','일자리정보망']\n",
    "tf_list = []\n",
    "\n",
    "for text in content['content']:\n",
    "    if find_word(text,words_list) == True:\n",
    "        tf_list.append(True)\n",
    "    else:\n",
    "        tf_list.append(False)\n",
    "        \n",
    "# 합치는 용\n",
    "index_list.extend(content.loc[pd.Series(tf_list)]['index'])\n",
    "        \n",
    "df5 = content.loc[pd.Series(tf_list)]\n",
    "df5.shape[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from collections import Counter\n",
    "\n",
    "# 카테고리에 속하는 애들 개수\n",
    "\n",
    "len(dict(Counter(index_list)).keys())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>index</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>cnt</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>337</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>396</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>178</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>36</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     index\n",
       "cnt       \n",
       "1      337\n",
       "2      396\n",
       "3      178\n",
       "4       36\n",
       "5        2"
      ]
     },
     "execution_count": 66,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cnt_df = pd.DataFrame({'index': dict(Counter(index_list)).keys(),\n",
    "                       'cnt' : dict(Counter(index_list)).values()})\n",
    "\n",
    "cnt_df.groupby('cnt').count() # sum 949"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [],
   "source": [
    "false_list = []\n",
    "for i in content['index']:\n",
    "    if i not in dict(Counter(index_list)).keys():\n",
    "        false_list.append(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [],
   "source": [
    "pd.set_option('display.max_rows',None)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(51, 5)"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "content.loc[pd.Series([i not in dict(Counter(index_list)).keys() for i in content['index']])].shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 기타\n",
    "l1 = [43, 217, 267,435, 562, 582, 587] # 지원금\n",
    "l2 = [] # 면접\n",
    "l3 = [] # 교육\n",
    "l4 = [15, 111, 129, 540, 551, 659, 700, 1008, 2002, 2015, 2038, 3052] # 일자리\n",
    "l5 = [29, 51, 67, 74, 110, 152, 164, 168, 180, 329, 423, 477, 480, 496, 561, 591, 705, 725, 779, 1018, 1043, 1044, 1050, 1051, 1071, 2002, 2016, 2061, 3066, 3069] # 상담"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [],
   "source": [
    "etc_1 = content.loc[pd.Series([i in l1 for i in content['index']])]\n",
    "etc_2 = content.loc[pd.Series([i in l2 for i in content['index']])]\n",
    "etc_3 = content.loc[pd.Series([i in l3 for i in content['index']])]\n",
    "etc_4 = content.loc[pd.Series([i in l4 for i in content['index']])]\n",
    "etc_5 = content.loc[pd.Series([i in l5 for i in content['index']])]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_money = pd.concat([df1, etc_1])\n",
    "df_interview = pd.concat([df2, etc_2])\n",
    "df_edu = pd.concat([df3, etc_3])\n",
    "df_job = pd.concat([df4, etc_4])\n",
    "df_consult = pd.concat([df5, etc_5])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_money['cat'] = 'money'\n",
    "df_interview['cat'] = 'interview'\n",
    "df_edu['cat'] = 'edu'\n",
    "df_job['cat'] = 'job'\n",
    "df_consult['cat'] = 'consult'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_cat = pd.concat([df_money, df_job, df_interview, df_edu, df_consult])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "a = list(content['index'])\n",
    "num = list(df_cat['index'].unique())\n",
    "\n",
    "for i in a:\n",
    "    if i not in num:\n",
    "        print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_cat.groupby('cat').count()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [],
   "source": [
    "content['money'] = 0\n",
    "content['interview'] = 0\n",
    "content['edu'] = 0\n",
    "content['job'] = 0\n",
    "content['consult'] = 0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [],
   "source": [
    "for i in range(len(df_cat)):\n",
    "    if df_cat.iloc[i]['cat'] == 'money':\n",
    "        content.loc[content['index'] == df_cat.iloc[i]['index'], 'money'] = 1\n",
    "    elif df_cat.iloc[i]['cat'] == 'interview':\n",
    "        content.loc[content['index'] == df_cat.iloc[i]['index'], 'interview'] = 1\n",
    "    elif df_cat.iloc[i]['cat'] == 'edu':\n",
    "        content.loc[content['index'] == df_cat.iloc[i]['index'], 'edu'] = 1\n",
    "    elif df_cat.iloc[i]['cat'] == 'job':\n",
    "        content.loc[content['index'] == df_cat.iloc[i]['index'], 'job'] = 1\n",
    "    elif df_cat.iloc[i]['cat'] == 'consult':\n",
    "        content.loc[content['index'] == df_cat.iloc[i]['index'], 'consult'] = 1  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [],
   "source": [
    "pd.options.display.max_colwidth = 50"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [],
   "source": [
    "content.to_csv('content_tagging.csv', index = False)"
   ]
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
