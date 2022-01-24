{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "b4937727",
   "metadata": {},
   "source": [
    "## 단어사전에 넣은 키워드 추출\n",
    "\n",
    "- 고유명사를 뽑기 위한 작업\n",
    "- ex) [나는 취업박람회에 가서 직업체험을 경험했다.] --> 취업박람회(취업+박람회), 직업체험(직업+체험)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "5ed6c088",
   "metadata": {},
   "outputs": [],
   "source": [
    "from konlpy.tag import Mecab\n",
    "\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import os"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "818ba3d9",
   "metadata": {},
   "outputs": [],
   "source": [
    "mecab = Mecab(dicpath=r\"C:\\mecab\\mecab-ko-dic\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "eb6421bb",
   "metadata": {},
   "outputs": [],
   "source": [
    "content = pd.read_csv('using_data/policy_content.csv', encoding='cp949')\n",
    "\n",
    "content['content_all'] = content['name'] + ' ' + content['description'] + ' ' + content['content'] # 이름,내용,지원내용 한번에 처리"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "a17e8218",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 문장 띄어쓰기로 나눠서 명사 추출 - (고유명사 뽑기 위해)\n",
    "\n",
    "def pos_function(text):\n",
    "    content_split = []\n",
    "\n",
    "    for i in text.split():\n",
    "        content_split.append(mecab.pos(i))\n",
    "\n",
    "    new_words_list = []\n",
    "    noun_pos = ['NNG','XSN','NNP']    # 일반명사, 명사 파생 접미사, 고유명사인 애들만 붙이기 \n",
    "     \n",
    "    for i in content_split:\n",
    "        word = ''\n",
    "        for j in i:\n",
    "            if j[1] in noun_pos:\n",
    "                word = word + j[0]\n",
    "            else:\n",
    "                break\n",
    "        new_words_list.append(word)\n",
    "    \n",
    "    # 비교용 nouns\n",
    "    n = mecab.nouns(text)\n",
    "    \n",
    "    # 이미 dictionary에 있는 단어 제외하기 \n",
    "    # 수정 필요 - 한번에 remove가 안돼서 4번 반복\n",
    "    for i in new_words_list:\n",
    "        if i in n:\n",
    "            new_words_list.remove(i)\n",
    "    for i in new_words_list:\n",
    "        if i in n:\n",
    "            new_words_list.remove(i)\n",
    "    for i in new_words_list:\n",
    "        if i in n:\n",
    "            new_words_list.remove(i)                \n",
    "    for i in new_words_list:\n",
    "        if i in n:\n",
    "            new_words_list.remove(i) \n",
    "    \n",
    "    # 공백인 단어 제거\n",
    "    while '' in new_words_list:            \n",
    "        if '' in new_words_list:\n",
    "            new_words_list.remove('')\n",
    "    \n",
    "    return new_words_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ffee6973",
   "metadata": {},
   "outputs": [],
   "source": [
    "#추출한 명사 list\n",
    "\n",
    "word_list = []\n",
    "\n",
    "for i in range(0,1000):\n",
    "    w = pos_function(content['content_all'][i])\n",
    "    word_list.extend(w)\n",
    "    \n",
    "word_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "26f46846",
   "metadata": {},
   "outputs": [],
   "source": [
    "#중복제거\n",
    "\n",
    "word_list\n",
    "word_unique = list(set(word_list))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "c0b70468",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 과 -> 제거, 의/들/이 -> 빼기\n",
    "\n",
    "##### 아예 제거\n",
    "\n",
    "search = \"과\"\n",
    "for word in word_unique:\n",
    "    if word[-1] == search:\n",
    "        word_unique.remove(word)\n",
    "        \n",
    "word_unique.append('관련학과')\n",
    "word_unique.append('특성화학과')\n",
    "word_unique.append('스마트제조융합학과')\n",
    "\n",
    "search = \"인\"\n",
    "for word in word_unique:\n",
    "    if word[-1] == search:\n",
    "        word_unique.remove(word)\n",
    "\n",
    "word_unique.extend(['통합적','핵심분야','유망산업','긍정적','심층적','점진적'])\n",
    "\n",
    "search = \"와\"\n",
    "for word in word_unique:\n",
    "    if word[-1] == search:\n",
    "        word_unique.remove(word)\n",
    "\n",
    "search = \"이\"\n",
    "for word in word_unique:\n",
    "    if word[-1] == search:\n",
    "        word_unique.remove(word)\n",
    "        \n",
    "word_unique.extend(['안전지킴이','매칭데이','공감페이','넥타이','자찬릴레이','멘토데이','면접관','일구데이','오디션데이','외톨이','과학기술일자리진흥원'])\n",
    "        \n",
    "##### 한 글자 빼기\n",
    "\n",
    "search = '의'\n",
    "for i, word in enumerate(word_unique):\n",
    "    if search in word: \n",
    "        word_unique[i] = word.rstrip(search)\n",
    "\n",
    "search = '들'\n",
    "for i, word in enumerate(word_unique):\n",
    "    if search in word: \n",
    "        word_unique[i] = word.rstrip(search)\n",
    "\n",
    "search = '별'\n",
    "for i, word in enumerate(word_unique):\n",
    "    if search in word: \n",
    "        word_unique[i] = word.rstrip(search)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "10a87adc",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 2글자 이하 단어 삭제\n",
    "\n",
    "results = []\n",
    "\n",
    "for i in word_unique:\n",
    "    if len(i) >= 3:\n",
    "        results.append(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "21c4e891",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 마지막 중복제거\n",
    "\n",
    "results = list(set(results))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "8e320a9d",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.DataFrame({'words': results})\n",
    "df.to_csv('word_dictionary_final.csv', encoding = 'euc-kr', index = False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8c2c9714",
   "metadata": {},
   "outputs": [],
   "source": [
    "df # 확인 후 필요없는 단어 삭제"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "acf131c5",
   "metadata": {},
   "source": [
    "## 단어사전 생성"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "aa474c9a",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 현재 디렉토리 확인\n",
    "\n",
    "os.getcwd()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "38134c98",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 사전에 넣기 위해 mecab으로 이동\n",
    "\n",
    "os.chdir('C:\\mecab')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c0df3a2f",
   "metadata": {},
   "outputs": [],
   "source": [
    "os.getcwd()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "010dd4dc",
   "metadata": {},
   "outputs": [],
   "source": [
    "ls"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bb881a79",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 단어사전 불러오기\n",
    "words = pd.read_csv('C:/Users/juwan/Desktop/산학프로젝트/using_data/word_dictionary_final.csv', encoding='euc-kr')\n",
    "words"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d73db9d1",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 명사 목록 list로 추출\n",
    "word_lst = words['words']\n",
    "word_lst"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "5a08282c",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 등록할 단어 목록 list\n",
    "word_list = word_lst"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "79e55264",
   "metadata": {
    "jupyter": {
     "outputs_hidden": true
    },
    "scrolled": true,
    "tags": []
   },
   "outputs": [],
   "source": [
    "# 종성여부를 판단하기 위한 라이브러리 설치와 판단하는 함수\n",
    "#jamo 라이브러리 설치\n",
    "# !pip install jamo"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "ecfa795e",
   "metadata": {},
   "outputs": [],
   "source": [
    "#종성 여부를 판단하는 함수\n",
    "from jamo import h2j, j2hcj\n",
    "\n",
    "\n",
    "def get_jongsung_TF(sample_text):\n",
    "    sample_text_list = list(sample_text)\n",
    "    last_word = sample_text_list[-1]\n",
    "    last_word_jamo_list = list(j2hcj(h2j(last_word)))\n",
    "    last_jamo = last_word_jamo_list[-1]\n",
    "\n",
    "    jongsung_TF = \"T\"\n",
    "\n",
    "    if last_jamo in ['ㅏ', 'ㅑ', 'ㅓ', 'ㅕ', 'ㅗ', 'ㅛ', 'ㅜ', 'ㅠ', 'ㅡ', 'ㅣ', 'ㅘ', 'ㅚ', 'ㅙ', 'ㅝ', 'ㅞ', 'ㅢ', 'ㅐ,ㅔ', 'ㅟ', 'ㅖ', 'ㅒ']:\n",
    "        jongsung_TF = \"F\"\n",
    "\n",
    "    return jongsung_TF"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "fdce4467",
   "metadata": {},
   "outputs": [],
   "source": [
    "# nnp.csv에 단어 추가\n",
    "\n",
    "with open(\"C:/Mecab/user-dic/nnp.csv\", 'r', encoding='euc-kr') as f:\n",
    "    file_data = f.readlines()\n",
    "\n",
    "word_list = word_lst\n",
    "\n",
    "for word in word_list:\n",
    "    jongsung_TF = get_jongsung_TF(word)\n",
    "\n",
    "    line = '{},,,,NNP,*,{},{},*,*,*,*,*\\n'.format(word, jongsung_TF, word)\n",
    "\n",
    "    file_data.append(line)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "327f1df6",
   "metadata": {},
   "outputs": [],
   "source": [
    "with open(\"./user-dic/nnp.csv\", 'w', encoding='utf-8') as f: \n",
    "    for line in file_data: \n",
    "        f.write(line)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "312bb16f",
   "metadata": {},
   "outputs": [],
   "source": [
    "with open(\"./user-dic/nnp.csv\", 'r', encoding='utf-8') as f: \n",
    "    file_new = f.readlines() \n",
    "file_new\n",
    "\n",
    "# 여기서 주피터 끄고 확인"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cd8a07d7",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 컴파일 후 확인 (tools\\add-userdic-win.ps1)\n",
    "\n",
    "content = pd.read_csv('using_data/policy_content.csv', encoding='cp949')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "c4661a8c",
   "metadata": {},
   "outputs": [],
   "source": [
    "from konlpy.tag import Mecab"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ce685a07",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 잘 등록되었나 확인\n",
    "\n",
    "text = content['description'][36]\n",
    "\n",
    "print(text)\n",
    "print()\n",
    "print(mecab.nouns(text))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e55307e8",
   "metadata": {},
   "outputs": [],
   "source": [
    "mecab.nouns('플랫폼')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a64f7975",
   "metadata": {},
   "outputs": [],
   "source": [
    "mecab.nouns('나는 청춘센터에 가서 일한다.')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b19fcf4d",
   "metadata": {},
   "source": [
    "## 단어사전 우선순위 변경"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "b7d1544b",
   "metadata": {},
   "outputs": [],
   "source": [
    "with open('C:/Mecab/mecab-ko-dic/user-nnp.csv', 'r', encoding = 'utf-8') as f:\n",
    "    user_nnp = f.readlines()\n",
    "\n",
    "temp = []\n",
    "for i in user_nnp:\n",
    "    temp.append(i.split(','))\n",
    "\n",
    "# 4번째 열의 숫자가 단어의 가중치 - 낮을수록 우선순위가 높음(반비례)\n",
    "user_nnp = []    \n",
    "for i in temp:\n",
    "    i[3] = '0'\n",
    "    user_nnp.append(','.join(i))\n",
    "\n",
    "with open('C:/Mecab/mecab-ko-dic/user-nnp.csv', 'w', encoding = 'utf-8') as f:\n",
    "    for line in user_nnp: \n",
    "        f.write(line)\n",
    "\n",
    "# 주피터 끄고 컴파일 진행 (tools\\compile-win.ps1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "d249b7af",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['취업준비생', '일자리', '중소기업']\n",
      "['취준생', '일자리', '중소기업']\n",
      "['취준', '중', '일자리', '중소기업']\n"
     ]
    }
   ],
   "source": [
    "print(mecab.nouns('취업준비생인데 일자리가 급해서요. 괜찮은 중소기업이라도 있을까요?'))\n",
    "print(mecab.nouns('취준생인데 일자리가 급해서요. 괜찮은 중소기업이라도 있을까요?'))\n",
    "print(mecab.nouns('취준중인데요. 일자리가 급해서요. 괜찮은 중소기업이라도 있을까요?'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "2b561682",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['자기소개서']\n",
      "['취업성공패키지', '신청']\n"
     ]
    }
   ],
   "source": [
    "print(mecab.nouns('자기소개서 어떻게 쓰나요'))\n",
    "print(mecab.nouns('취업성공패키지 신청하고 싶어요'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9507084e",
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
 "nbformat_minor": 5
}
