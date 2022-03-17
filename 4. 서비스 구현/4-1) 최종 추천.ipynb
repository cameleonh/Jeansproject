{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "\n",
    "from konlpy.tag import Mecab"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "mecab = Mecab(dicpath=r\"C:\\Mecab\\mecab-ko-dic\") # dictation path 설정 / mecab-ko-dic이 mecab의 단어사전임"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "counseling = pd.read_csv('using_data/counseling_nolabel_4.csv', encoding = 'euc-kr')\n",
    "cat_nouns_df = pd.read_csv('using_data/cluster_nouns.csv')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### SCORE"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "def vocab_dictionary_onetext(text_list): \n",
    "    vocab = list(set(sum([mecab.nouns(i) for i in text_list], [])))\n",
    "    vocab1 = [i for i in vocab if len(i) >= 2]\n",
    "    \n",
    "    rm = ['어딜까', '가요', '건가요', '걸까요', '뭔가요', '입니다', '주세요', '취업', '지원', '어디','정책','이나','자리']\n",
    "    for i in vocab1:\n",
    "        if i in rm:\n",
    "            vocab1.remove(i)\n",
    "     \n",
    "    add = ['돈', '일']\n",
    "    for i in add:\n",
    "        if i in vocab:\n",
    "            vocab1.append(i)\n",
    "        \n",
    "    vocab1.sort()\n",
    "    return vocab1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "def tf(t, d):\n",
    "    df = 0\n",
    "    for word in mecab.nouns(d):\n",
    "        if word == t:\n",
    "            df += 1\n",
    "    return df\n",
    "\n",
    "def make_tf_dataset(text_list):\n",
    "    N = len(text_list) # 총 문서의 수: 1\n",
    "    result = []\n",
    "    for i in range(N):\n",
    "        result.append([])\n",
    "        d = text_list[i]\n",
    "        for j in range(len(vocab_dictionary_onetext(text_list))):\n",
    "            t = vocab_dictionary_onetext(text_list)[j]        \n",
    "            result[-1].append(tf(t, d))\n",
    "\n",
    "    tf_ = pd.DataFrame(result, columns = vocab_dictionary_onetext(text_list))\n",
    "    # tf_.sum(axis=0)\n",
    "    return tf_"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "scrolled": true
   },
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
       "      <th>백수</th>\n",
       "      <th>생활</th>\n",
       "      <th>일</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   백수  생활  일\n",
       "0   1   1  2"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "text_list = ['백수 생활한 지 오래되어서 일하기 싫고 귀찮아요. 일 안하고 먹고 살게 해주세요']\n",
    "make_tf_dataset(text_list)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 표준화한 점수 (저장 완료. 안돌려도됨)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.preprocessing import StandardScaler\n",
    "\n",
    "# Standardization 평균 0 / 분산 1\n",
    "scaler = StandardScaler()   \n",
    "\n",
    "scaler = scaler.fit_transform(cat_nouns_df[['cnt_0','cnt_1','cnt_2','cnt_3','cnt_4']])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "cat_nouns_df[['cnt_0','cnt_1','cnt_2','cnt_3','cnt_4']] = pd.DataFrame(scaler)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "# cat_nouns_df.to_csv('cluster_nouns.csv', index = False)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##  여기부터 돌리기"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "def cat_score(tf_):\n",
    "    score = []\n",
    "\n",
    "    for i in range(5):\n",
    "        tf_trans = tf_.transpose().reset_index()\n",
    "        tf_trans.columns = ['cat_{}_nouns'.format(i),'cnt_{}'.format(i)]\n",
    "\n",
    "        temp_df = pd.merge(cat_nouns_df[['cat_{}_nouns'.format(i),'cnt_{}'.format(i)]], tf_trans, on = 'cat_{}_nouns'.format(i), how = 'inner')\n",
    "\n",
    "        score.append(sum(temp_df['cnt_{}_x'.format(i)] * temp_df['cnt_{}_y'.format(i)]) )\n",
    "    return score"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "score = cat_score(make_tf_dataset(text_list))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [],
   "source": [
    "def whatcategory(score_list):\n",
    "    category = []\n",
    "    for i in range(len(score_list)):\n",
    "        if score_list[i] == max(score_list):\n",
    "            if i == 0:\n",
    "                category.append('edu')\n",
    "            if i == 1:\n",
    "                category.append('consult')\n",
    "            if i == 2:\n",
    "                category.append('money')\n",
    "            if i == 3:\n",
    "                category.append('interview')\n",
    "            if i == 4:\n",
    "                category.append('job')\n",
    "    return category"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "metadata": {},
   "outputs": [],
   "source": [
    "category = whatcategory(score)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 123,
   "metadata": {},
   "outputs": [],
   "source": [
    "pd.options.display.max_colwidth = 40"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 360,
   "metadata": {},
   "outputs": [],
   "source": [
    "idf_df = pd.read_csv('using_data/idf_정책_20211019.csv', encoding = 'euc-kr')\n",
    "policy = pd.read_csv('using_data/content_tagging_2.csv', encoding = 'euc-kr')\n",
    "similar = pd.read_csv('using_data/유사어.csv', encoding = 'euc-kr')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 222,
   "metadata": {},
   "outputs": [],
   "source": [
    "# similar = pd.merge(similar, idf_df, on = 'word', how = 'left')\n",
    "# similar.to_csv('using_data/유사어.csv', encoding = 'euc-kr', index = False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {},
   "outputs": [],
   "source": [
    "def df_for_recommend(category):\n",
    "    using_df = policy.loc[policy['money'] + policy['interview'] + policy['edu'] + policy['job'] + policy['consult'] == 0] # 일단 어떤 카테고리에도 포함안되는 애들은 포함시키고 봄\n",
    "\n",
    "    for i in category:\n",
    "        if i == 'money':\n",
    "            using_df = pd.concat([using_df, policy.loc[policy['money'] == 1]])\n",
    "        if i == 'interview':\n",
    "            using_df = pd.concat([using_df, policy.loc[policy['interview'] == 1]])\n",
    "        if i == 'edu':\n",
    "            using_df = pd.concat([using_df, policy.loc[policy['edu'] == 1]])\n",
    "        if i == 'job':\n",
    "            using_df = pd.concat([using_df, policy.loc[policy['job'] == 1]])\n",
    "        if i == 'consult':\n",
    "            using_df = pd.concat([using_df, policy.loc[policy['consult'] == 1]])\n",
    "        \n",
    "    using_df = using_df.drop_duplicates(subset=None, keep='first', inplace=False, ignore_index=False).reset_index(drop = True)\n",
    "    return using_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {},
   "outputs": [],
   "source": [
    "# using_df = policy # 전체 카테고리에서 추천할 때 얘 돌리기"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "metadata": {},
   "outputs": [],
   "source": [
    "def each_policy_nouns(using_df):\n",
    "    nouns_list = []\n",
    "    policy_index = []\n",
    "    policy_nouns = []\n",
    "\n",
    "    for i in range(len(using_df['content'])):\n",
    "        nouns_list.extend(mecab.nouns(using_df['content'][i]))\n",
    "        policy_index.append(using_df['index'][i])\n",
    "        policy_nouns.append(mecab.nouns(using_df['content'][i]))\n",
    "\n",
    "    policy_nouns = pd.DataFrame({'index': policy_index,\n",
    "                                 'nouns': policy_nouns})\n",
    "    return policy_nouns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 311,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'관련', '교육', '국비', '예술', '전공'}"
      ]
     },
     "execution_count": 311,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "text_list = ['예술 관련 취업하려고 하는데요. 비전공자여서요 혹시 국비 교육같은거 받을 수 있을까요?']\n",
    "set(vocab_dictionary_onetext(text_list))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def each_policy_score(policy_nouns):\n",
    "    score_list = []\n",
    "\n",
    "    for i in policy_nouns['nouns']:\n",
    "        \n",
    "        text_words = set(vocab_dictionary_onetext(text_list))\n",
    "        policy_words = set(i)\n",
    "        \n",
    "        intersection_words = list(text_words.intersection(policy_words))\n",
    "    \n",
    "        idf_df['cnt'] = pd.Series([i in intersection_words for i in idf_df['word']])\n",
    "    \n",
    "        score_list.append((idf_df['IDF'] * idf_df['cnt']).sum())\n",
    "    return score_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 315,
   "metadata": {},
   "outputs": [],
   "source": [
    "each_policy_nouns_df = each_policy_nouns(df_for_recommend(category))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 390,
   "metadata": {},
   "outputs": [],
   "source": [
    "policy_nouns = each_policy_nouns(df_for_recommend(category))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "each_policy_nouns(df_for_recommend(category))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "###########################\n",
    "\n",
    "def each_policy_score(policy_nouns):\n",
    "    \n",
    "    score_list = []\n",
    "\n",
    "    for i, j in enumerate(policy_nouns['nouns']): # 각 정책들마다의 단어 리스트\n",
    "\n",
    "        # 정책단어와 고민글단어의 교집합\n",
    "        intersection_words = list(set(set(vocab_dictionary_onetext(text_list))).intersection(set(j)))\n",
    "\n",
    "        inters_idf_df = idf_df.copy()\n",
    "        inters_idf_df['cnt'] = pd.Series([i in intersection_words for i in inters_idf_df['word']])\n",
    "        score1 = (inters_idf_df['IDF'] * inters_idf_df['cnt']).sum()\n",
    "\n",
    "        # 상담단어 - 정책단어 차집합\n",
    "        difference_words = list(set(vocab_dictionary_onetext(text_list)) - set(j))\n",
    "        differ = []\n",
    "\n",
    "        for i,j in enumerate(difference_words):\n",
    "            if len(similar.loc[similar['similar'] == j]) > 0:\n",
    "                differ.extend(list(similar.loc[similar['similar'] == j,'word']))\n",
    "\n",
    "        intersection_words = list(set(set(differ)).intersection(set(j)))\n",
    "        inters_idf_df = idf_df.copy()\n",
    "        inters_idf_df['cnt'] = pd.Series([i in intersection_words for i in inters_idf_df['word']])\n",
    "        score2 = (inters_idf_df['IDF'] * inters_idf_df['cnt']).sum()\n",
    "\n",
    "        score_list.append(score1 + score2)\n",
    "    return score_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 398,
   "metadata": {},
   "outputs": [],
   "source": [
    "using_df = df_for_recommend(category)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 401,
   "metadata": {},
   "outputs": [],
   "source": [
    "using_df['score'] = score_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 404,
   "metadata": {},
   "outputs": [],
   "source": [
    "pd.options.display.max_colwidth = 1000"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 305,
   "metadata": {},
   "outputs": [],
   "source": [
    "# pd.set_option('display.max_rows', None)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 200,
   "metadata": {},
   "outputs": [],
   "source": [
    "tf_ = make_tf_dataset(text_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 201,
   "metadata": {},
   "outputs": [],
   "source": [
    "score = cat_score(tf_)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 202,
   "metadata": {},
   "outputs": [],
   "source": [
    "category = whatcategory(score)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 203,
   "metadata": {},
   "outputs": [],
   "source": [
    "using_df = df_for_recommend(category)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 114,
   "metadata": {},
   "outputs": [],
   "source": [
    "each_policy_nouns_df = each_policy_nouns(using_df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 197,
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "using_df['score'] = score_list"
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
   "cell_type": "code",
   "execution_count": 146,
   "metadata": {},
   "outputs": [],
   "source": [
    "def check_my_poilcy(text_list):\n",
    "    tf_ = make_tf_dataset(text_list)\n",
    "    score = cat_score(tf_)\n",
    "    category = whatcategory(score)\n",
    "    using_df = df_for_recommend(category)\n",
    "    each_policy_nouns_df = each_policy_nouns(using_df)\n",
    "    using_df['score'] = each_policy_score(each_policy_nouns_df)\n",
    "    \n",
    "    return using_df[['content','money','edu','interview','job','consult','score']].sort_values(by='score', ascending = False).iloc[0,0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 153,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "채용사이트에 올린 저의 자소서와 이력서를 좀더 디테일하게 (경력서술이나 자격증 유무 관련) 수정하고 싶습니다.\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "'서울형 뉴딜 일자리청년을 비롯한 참여자들에게 일경험과 취업에 필요한 다양한 교육,서비스를 동시에 제공해 사업 참여 후 민간일자리로의 취업을 돕는 공공 일자리 사업 정책- 월 최대 임금 235만원 지급( 서울형 생활임금 시급 : 10,702원)\\n- 최대 23개월간 안정적으로 근무가능(풀타임/파트타임 선택가능)\\n- 일하는 동안 관련 경력을 쌓아 민간일자리 취업(2019년 참여자 취업률 52.9%)\\n- 최대 130시간 취업교육,  자격증 응시비용 지원'"
      ]
     },
     "execution_count": 153,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "text_list = [input()]\n",
    "check_my_poilcy(text_list)"
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
