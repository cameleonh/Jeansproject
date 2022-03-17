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
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
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
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 형태소 분석할 데이터 준비 - 정책 내용 데이터 불러오기 \n",
    "\n",
    "content = pd.read_csv('using_data/policy_content.csv', encoding = 'euc-kr')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
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
       "      <th>name</th>\n",
       "      <th>description</th>\n",
       "      <th>content</th>\n",
       "      <th>URL</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>국민취업지원제도</td>\n",
       "      <td>한국형 실업부조로 고용안전망 사각지대에 있는 취업취약계층에게 취업지원서비스 및 생활...</td>\n",
       "      <td>1. 취업취약계층에 취업지원\\n- 취업지원서비스를 종합적으로 제공하고, 저소득 구직...</td>\n",
       "      <td>https://www.youthcenter.go.kr/youngPlcyUnif/yo...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>청년추가고용장려금 지원사업</td>\n",
       "      <td>청년을 정규직으로 추가로 고용한 중소?중견기업에 인건비를 지원함으로써, 양질의 청년...</td>\n",
       "      <td>1. 청년 추가채용 1명당 연 최대 900만원을 3년간 지원2. 고용위기 지역 지정...</td>\n",
       "      <td>https://www.youthcenter.go.kr/youngPlcyUnif/yo...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>국민내일배움카드</td>\n",
       "      <td>국민 누구나 일자리에 도움이 되는 훈련을 받을 수 있는 평생능력개발 기반 마련을 위...</td>\n",
       "      <td>1. 국민 누구나 국민내일배움카드 신청 가능\\n- 분리 운영되었던 실업자/재직자 내...</td>\n",
       "      <td>https://www.youthcenter.go.kr/youngPlcyUnif/yo...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>청년내일채움공제</td>\n",
       "      <td>중소·중견기업 청년 근로자의 장기근속과 자산형성을 지원하기 위해 청년, 기업, 정부...</td>\n",
       "      <td>1. 청년 지원내용\\n - 청년 본인이 2년간 300만원(매월 12만 5천원)을 적...</td>\n",
       "      <td>https://www.youthcenter.go.kr/youngPlcyUnif/yo...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>청년고용지원</td>\n",
       "      <td>청년고용정책 지원</td>\n",
       "      <td>1. 지원내용 청년고용정책 심층 모니터링, 대학일자리센터 컨설팅 및 운영지원, 청년...</td>\n",
       "      <td>https://www.youthcenter.go.kr/youngPlcyUnif/yo...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   index            name                                        description  \\\n",
       "0      0        국민취업지원제도  한국형 실업부조로 고용안전망 사각지대에 있는 취업취약계층에게 취업지원서비스 및 생활...   \n",
       "1      1  청년추가고용장려금 지원사업  청년을 정규직으로 추가로 고용한 중소?중견기업에 인건비를 지원함으로써, 양질의 청년...   \n",
       "2      3        국민내일배움카드  국민 누구나 일자리에 도움이 되는 훈련을 받을 수 있는 평생능력개발 기반 마련을 위...   \n",
       "3      4        청년내일채움공제  중소·중견기업 청년 근로자의 장기근속과 자산형성을 지원하기 위해 청년, 기업, 정부...   \n",
       "4      5          청년고용지원                                          청년고용정책 지원   \n",
       "\n",
       "                                             content  \\\n",
       "0  1. 취업취약계층에 취업지원\\n- 취업지원서비스를 종합적으로 제공하고, 저소득 구직...   \n",
       "1  1. 청년 추가채용 1명당 연 최대 900만원을 3년간 지원2. 고용위기 지역 지정...   \n",
       "2  1. 국민 누구나 국민내일배움카드 신청 가능\\n- 분리 운영되었던 실업자/재직자 내...   \n",
       "3  1. 청년 지원내용\\n - 청년 본인이 2년간 300만원(매월 12만 5천원)을 적...   \n",
       "4  1. 지원내용 청년고용정책 심층 모니터링, 대학일자리센터 컨설팅 및 운영지원, 청년...   \n",
       "\n",
       "                                                 URL  \n",
       "0  https://www.youthcenter.go.kr/youngPlcyUnif/yo...  \n",
       "1  https://www.youthcenter.go.kr/youngPlcyUnif/yo...  \n",
       "2  https://www.youthcenter.go.kr/youngPlcyUnif/yo...  \n",
       "3  https://www.youthcenter.go.kr/youngPlcyUnif/yo...  \n",
       "4  https://www.youthcenter.go.kr/youngPlcyUnif/yo...  "
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "content.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### nouns_list  \n",
    "' description ' 에서 형태소 분석처리한 모든 단어 모음 (리스트)  \n",
    "' description ' 의 모든 단어를 다 보고 싶을 때 사용\n",
    "     \n",
    "     \n",
    "#### policy_nouns  \n",
    "' 한 정책 ' 의 인덱스 + 형태소 분석처리한 단어 리스트의 모음 (리스트) (DF)  \n",
    "' 한 정책 ' 에 어떤 단어가 들어있는지 볼 때 사용  \n",
    "  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "nouns_list = []\n",
    "policy_index = []\n",
    "policy_nouns = []\n",
    "\n",
    "for i in range(len(content['description'])):\n",
    "    nouns_list.extend(mecab.nouns(content['description'][i]))\n",
    "    policy_index.append(content['index'][i])\n",
    "    policy_nouns.append(mecab.nouns(content['description'][i]))\n",
    "\n",
    "policy_nouns = pd.DataFrame({'index': policy_index,\n",
    "                             'nouns': policy_nouns})"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 검색단어와 앞, 뒤 2단어를 추출하여 살펴보기"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "index_num = []\n",
    "front_back_list = []\n",
    "\n",
    "###### 단어를 입력하시오.##########\n",
    "word = '지원'\n",
    "###################################\n",
    "\n",
    "for i in range(len(policy_nouns)):\n",
    "    \n",
    "    # 정책 리스트에 이 단어가 있으면\n",
    "    if word in policy_nouns['nouns'][i]:\n",
    "        \n",
    "        # 검색단어가 제일 첫번째 순서면 실행\n",
    "        if policy_nouns['nouns'][i].index(word) == 0:\n",
    "            index_num.append(policy_nouns['index'][i])\n",
    "            front_back_list.append(policy_nouns['nouns'][i][:3]) # 검색단어 + 뒷2단어\n",
    "            \n",
    "        # 검색단어가 두번째 순서면 실행    \n",
    "        elif policy_nouns['nouns'][i].index(word) == 1:\n",
    "            index_num.append(policy_nouns['index'][i])\n",
    "            front_back_list.append(policy_nouns['nouns'][i][0:4])\n",
    "            \n",
    "        else:\n",
    "            index_num.append(policy_nouns['index'][i])\n",
    "            front_back_list.append(policy_nouns['nouns'][i][policy_nouns['nouns'][i].index(word)-2:policy_nouns['nouns'][i].index(word)+3])\n",
    "\n",
    "df = pd.DataFrame()\n",
    "df['index'] = index_num\n",
    "df['words'] = front_back_list"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 한 글자로 이루어진 단어 추출"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "one_word = [i for i in nouns_list if len(i) <= 2]\n",
    "\n",
    "from collections import Counter\n",
    "\n",
    "cnt_rank = pd.DataFrame()\n",
    "\n",
    "cnt_rank['word'] = pd.Series(list(dict(Counter(one_word)).keys()))\n",
    "cnt_rank['cnt'] = pd.Series(list(dict(Counter(one_word)).values()))\n",
    "\n",
    "cnt_rank.sort_values(by='cnt', ascending = False)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "###  모든 단어들의 빈도수 추출"
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
    "cnt_rank = pd.DataFrame()\n",
    "\n",
    "cnt_rank['description_word'] = pd.Series(list(dict(Counter(nouns_list)).keys()))\n",
    "cnt_rank['cnt'] = pd.Series(list(dict(Counter(nouns_list)).values()))\n",
    "\n",
    "cnt_rank.sort_values(by='cnt', ascending = True) # 내림차순으로 정렬"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "cnt_rank.loc[cnt_rank['description_word']=='물류']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "one_word = [i for i in nouns_list if len(i) > 1]\n",
    "\n",
    "from collections import Counter\n",
    "\n",
    "cnt_rank = pd.DataFrame()\n",
    "\n",
    "cnt_rank['word'] = pd.Series(list(dict(Counter(one_word)).keys()))\n",
    "cnt_rank['cnt'] = pd.Series(list(dict(Counter(one_word)).values()))\n",
    "\n",
    "cnt_rank.sort_values(by='cnt', ascending = False)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 단순하게 빈도수로 테스트"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "물류, 유통 분야에 취업을 희망하는데 관련된 직무 교육 사업이 있나요?\n"
     ]
    }
   ],
   "source": [
    "# 사용자 글 입력\n",
    "text = input()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['물류', '유통', '분야', '취업', '희망', '관련', '직무', '교육', '사업']"
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "words = [i for i in mecab.nouns(text) if len(i) > 1]\n",
    "words"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "score_list = []\n",
    "\n",
    "for i in policy_nouns['nouns']:\n",
    "    score = 0\n",
    "    for j in words:\n",
    "        if j in i:\n",
    "            score += 1\n",
    "    score_list.append(score)\n",
    "\n",
    "example = pd.DataFrame()\n",
    "example['score'] = score_list\n",
    "\n",
    "example.sort_values(by='score', ascending = False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "content.iloc[example.loc[example['score']  ==  max(example['score'])].index]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "mecab.nouns(content.loc[content['index']==1027]['description'].iloc[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "content.loc[content['index']==1027]['description'].iloc[0]"
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
