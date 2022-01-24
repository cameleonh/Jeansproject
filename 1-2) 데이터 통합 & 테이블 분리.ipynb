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
