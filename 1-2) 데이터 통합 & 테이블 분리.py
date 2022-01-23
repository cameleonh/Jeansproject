{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 1. 온라인 청년 정책 사이트 정책과 지자체 정책 통합하기"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "\n",
    "dir = 'C:/Users/juwan/Desktop/산학프로젝트/'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [],
   "source": [
    "jijachae = pd.read_excel(dir + '지자체 정책 통합.xlsx')   # 직접 수집한 자자체 사이트 데이터\n",
    "df_ex = pd.read_csv(dir + 'online_jeongchaek_fix.csv', encoding = 'euc-kr')    # 크롤링한 온라인 청년센터 데이터"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 필요한 행 추출\n",
    "df1 = df_ex[['index','name','description','content','URL','min_age','max_age','region','edu','job']]\n",
    "df2 = jijachae[['index','정책명','정책내용','지원내용','URL','min_age','max_age','region','edu','job']]\n",
    "df2.columns = ['index','name','description','content','URL','min_age','max_age','region','edu','job']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [],
   "source": [
    "policy_total = pd.concat([df1,df2])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
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
       "      <th>min_age</th>\n",
       "      <th>max_age</th>\n",
       "      <th>region</th>\n",
       "      <th>edu</th>\n",
       "      <th>job</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>국민취업지원제도</td>\n",
       "      <td>한국형 실업부조로 고용안전망 사각지대에 있는 취업취약계층에게 취업지원서비스 및 생활...</td>\n",
       "      <td>1. 취업취약계층에 취업지원\\n- 취업지원서비스를 종합적으로 제공하고, 저소득 구직...</td>\n",
       "      <td>https://www.youthcenter.go.kr/youngPlcyUnif/yo...</td>\n",
       "      <td>15</td>\n",
       "      <td>69</td>\n",
       "      <td>정부기관</td>\n",
       "      <td>제한없음</td>\n",
       "      <td>미취업자</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>청년추가고용장려금 지원사업</td>\n",
       "      <td>청년을 정규직으로 추가로 고용한 중소?중견기업에 인건비를 지원함으로써, 양질의 청년...</td>\n",
       "      <td>1. 청년 추가채용 1명당 연 최대 900만원을 3년간 지원2. 고용위기 지역 지정...</td>\n",
       "      <td>https://www.youthcenter.go.kr/youngPlcyUnif/yo...</td>\n",
       "      <td>15</td>\n",
       "      <td>34</td>\n",
       "      <td>정부기관</td>\n",
       "      <td>제한없음나 재학중인자는 불가</td>\n",
       "      <td>해당기업 신규취업자</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>청년 구직활동 수당 지원</td>\n",
       "      <td>도내 미취업 청년들에게 취업에 필요한 최소한의 경비를 지원하여 취업의욕 고취 및 노...</td>\n",
       "      <td>월 50만원×6개월 총 300만원 지원, 지원금 수급 중 취업 시 50만원 지원최대...</td>\n",
       "      <td>https://www.youthcenter.go.kr/youngPlcyUnif/yo...</td>\n",
       "      <td>18</td>\n",
       "      <td>34</td>\n",
       "      <td>전라남도</td>\n",
       "      <td>제한없음</td>\n",
       "      <td>미취업자</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>3</td>\n",
       "      <td>3</td>\n",
       "      <td>국민내일배움카드</td>\n",
       "      <td>국민 누구나 일자리에 도움이 되는 훈련을 받을 수 있는 평생능력개발 기반 마련을 위...</td>\n",
       "      <td>1. 국민 누구나 국민내일배움카드 신청 가능\\n- 분리 운영되었던 실업자/재직자 내...</td>\n",
       "      <td>https://www.youthcenter.go.kr/youngPlcyUnif/yo...</td>\n",
       "      <td>0</td>\n",
       "      <td>75</td>\n",
       "      <td>정부기관</td>\n",
       "      <td>제한없음</td>\n",
       "      <td>제한없음</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>4</td>\n",
       "      <td>4</td>\n",
       "      <td>청년내일채움공제</td>\n",
       "      <td>중소·중견기업 청년 근로자의 장기근속과 자산형성을 지원하기 위해 청년, 기업, 정부...</td>\n",
       "      <td>1. 청년 지원내용\\n - 청년 본인이 2년간 300만원(매월 12만 5천원)을 적...</td>\n",
       "      <td>https://www.youthcenter.go.kr/youngPlcyUnif/yo...</td>\n",
       "      <td>15</td>\n",
       "      <td>34</td>\n",
       "      <td>정부기관</td>\n",
       "      <td>제한없음</td>\n",
       "      <td>재직자</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   index            name                                        description  \\\n",
       "0      0        국민취업지원제도  한국형 실업부조로 고용안전망 사각지대에 있는 취업취약계층에게 취업지원서비스 및 생활...   \n",
       "1      1  청년추가고용장려금 지원사업  청년을 정규직으로 추가로 고용한 중소?중견기업에 인건비를 지원함으로써, 양질의 청년...   \n",
       "2      2   청년 구직활동 수당 지원  도내 미취업 청년들에게 취업에 필요한 최소한의 경비를 지원하여 취업의욕 고취 및 노...   \n",
       "3      3        국민내일배움카드  국민 누구나 일자리에 도움이 되는 훈련을 받을 수 있는 평생능력개발 기반 마련을 위...   \n",
       "4      4        청년내일채움공제  중소·중견기업 청년 근로자의 장기근속과 자산형성을 지원하기 위해 청년, 기업, 정부...   \n",
       "\n",
       "                                             content  \\\n",
       "0  1. 취업취약계층에 취업지원\\n- 취업지원서비스를 종합적으로 제공하고, 저소득 구직...   \n",
       "1  1. 청년 추가채용 1명당 연 최대 900만원을 3년간 지원2. 고용위기 지역 지정...   \n",
       "2  월 50만원×6개월 총 300만원 지원, 지원금 수급 중 취업 시 50만원 지원최대...   \n",
       "3  1. 국민 누구나 국민내일배움카드 신청 가능\\n- 분리 운영되었던 실업자/재직자 내...   \n",
       "4  1. 청년 지원내용\\n - 청년 본인이 2년간 300만원(매월 12만 5천원)을 적...   \n",
       "\n",
       "                                                 URL min_age max_age region  \\\n",
       "0  https://www.youthcenter.go.kr/youngPlcyUnif/yo...      15      69   정부기관   \n",
       "1  https://www.youthcenter.go.kr/youngPlcyUnif/yo...      15      34   정부기관   \n",
       "2  https://www.youthcenter.go.kr/youngPlcyUnif/yo...      18      34   전라남도   \n",
       "3  https://www.youthcenter.go.kr/youngPlcyUnif/yo...       0      75   정부기관   \n",
       "4  https://www.youthcenter.go.kr/youngPlcyUnif/yo...      15      34   정부기관   \n",
       "\n",
       "               edu         job  \n",
       "0             제한없음        미취업자  \n",
       "1  제한없음나 재학중인자는 불가  해당기업 신규취업자  \n",
       "2             제한없음        미취업자  \n",
       "3             제한없음        제한없음  \n",
       "4             제한없음         재직자  "
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "policy_total.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1051, 10)"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "policy_total.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [],
   "source": [
    "# policy_total.to_csv(dir + 'policy_total.csv', encoding = 'utf-8',index=False) # policy_total.csv"
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
    "### 2. ' 정책 내용 ' 과 ' 정책 지원 조건 ' 분리하기\n",
    "- 정책 내용 : 형태소 분석 & 자연어처리\n",
    "- 지원 조건 : 사용자 개인정보 필터링\n",
    "\n",
    "명확하게 활용하는 분야가 다르므로 두 데이터셋으로 분리"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [],
   "source": [
    "policy_total = pd.read_csv(dir + 'policy_total.csv', encoding = 'euc-kr')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [],
   "source": [
    "condition = policy_total[['index','name','min_age','max_age','region','edu','job']]\n",
    "content = policy_total[['index','name','description','content','URL']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "content = content.drop_duplicates() # 정책내용은 겹치는거 필요 X -> 중복 제거"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "# condition.to_csv(dir + 'policy_condition.csv', encoding = 'utf-8', index = False) # policy_condition.csv\n",
    "# content.to_csv(dir + 'policy_content.csv', encoding = 'utf-8', index = False) # policy_content.csv"
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
       "(1036, 5)"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "content.shape"
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
   "display_name": "Python 3",
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
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
