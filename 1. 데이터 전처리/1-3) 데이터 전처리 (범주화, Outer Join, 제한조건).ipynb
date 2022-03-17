{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 중복 정책 제거(같은 내용, 띄어쓰기 차이로 다른 이름)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "\n",
    "dir = 'C:/Users/juwan/Desktop/산학프로젝트/'\n",
    "\n",
    "from collections import Counter"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "x292cmVbmM29"
   },
   "outputs": [],
   "source": [
    "# policy_content.csv에서 name 컬럼을 띄어쓰기 제거해서 가져오기\n",
    "\n",
    "df = pd.read_csv('policy_content_strip.csv', encoding='cp949')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "e3DOGaConebV"
   },
   "outputs": [],
   "source": [
    "# row 전체 확인\n",
    "pd.set_option('display.max_rows',None)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 1000
    },
    "id": "bmOgfZE1mSha",
    "outputId": "69baa170-39e2-4ae9-89de-bfebf30cc87b"
   },
   "outputs": [],
   "source": [
    "# 조건이 같은데 지자체별 name 띄어쓰기가 달라 중복된 정책 검색\n",
    "duplicate = df[df.duplicated(['name'])].sort_values(by=['name'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 145
    },
    "id": "tHsiAl-0m0fV",
    "outputId": "e06af5a1-fc53-4096-abff-1c016317e88c"
   },
   "outputs": [],
   "source": [
    "# 예시\n",
    "df[df['name']== '2021년대학생아르바이트']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "eTKJ4UAlofRc"
   },
   "outputs": [],
   "source": [
    "# 중복된 row중 일부만 나와 csv로 저장 후 policy_condition과 비교하여 csv 내에서 작업\n",
    "duplicate.to_csv('duplicate.csv', index=False, header=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### policy_condition를 전처리 -> 수작업       "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "condition = pd.read_csv(dir + 'policy_condition.csv', encoding = 'utf-8')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "condition.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 데이터 수정한거 통합 (outer join)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_edu_change = pd.read_csv(dir + 'policy_condition_edu_장희정오소연.csv', encoding = 'euc-kr') \n",
    "df_job_change = pd.read_csv(dir + 'policy_condition_job_한민규.csv', encoding = 'euc-kr')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_edu_change.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.merge(df_edu_change, df_job_change, on = ['index','name','min_age','max_age','region'], how='outer')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = df[['index','name','min_age','max_age','region','edu_x','job_y']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "# df.to_csv(dir + 'df.csv', encoding = 'euc-kr', index =False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_csv(dir + 'df.csv', encoding = 'euc-kr')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "# df.to_csv(dir + 'policy_condition_final.csv', encoding = 'euc-kr', index = False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "condition = pd.read_csv(dir + 'policy_condition_final.csv', encoding = 'euc-kr')\n",
    "condition.head()"
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
