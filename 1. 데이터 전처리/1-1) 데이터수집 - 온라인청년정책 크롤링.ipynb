{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "from selenium import webdriver # 시간이 좀 오래걸림\n",
    "from bs4 import BeautifulSoup\n",
    "\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "\n",
    "dir = 'C:/Users/juwan/Desktop/산학프로젝트/'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "# format으로 \n",
    "next_jeongchak = ['#srchFrm > div.sch-result-wrap.compare-result-list > div.result-list-box > ul > li:nth-child(1) > a',\n",
    "'#srchFrm > div.sch-result-wrap.compare-result-list > div.result-list-box > ul > li:nth-child(2) > a',\n",
    "'#srchFrm > div.sch-result-wrap.compare-result-list > div.result-list-box > ul > li:nth-child(3) > a', \n",
    "'#srchFrm > div.sch-result-wrap.compare-result-list > div.result-list-box > ul > li:nth-child(4) > a',\n",
    "'#srchFrm > div.sch-result-wrap.compare-result-list > div.result-list-box > ul > li:nth-child(5) > a',\n",
    "'#srchFrm > div.sch-result-wrap.compare-result-list > div.result-list-box > ul > li:nth-child(6) > a',\n",
    "'#srchFrm > div.sch-result-wrap.compare-result-list > div.result-list-box > ul > li:nth-child(7) > a',\n",
    "'#srchFrm > div.sch-result-wrap.compare-result-list > div.result-list-box > ul > li:nth-child(8) > a',\n",
    "'#srchFrm > div.sch-result-wrap.compare-result-list > div.result-list-box > ul > li:nth-child(9) > a',\n",
    "'#srchFrm > div.sch-result-wrap.compare-result-list > div.result-list-box > ul > li:nth-child(10) > a',\n",
    "'#srchFrm > div.sch-result-wrap.compare-result-list > div.result-list-box > ul > li:nth-child(11) > a',\n",
    "'#srchFrm > div.sch-result-wrap.compare-result-list > div.result-list-box > ul > li:nth-child(12) > a']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 205,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 최종코드 (한번에 하면 에러 - 20페이지씩 끊어서 수집)\n",
    "\n",
    "young_list = []\n",
    "young_name = []\n",
    "young_dec = []\n",
    "region = []\n",
    "\n",
    "chrome_loc = 'C:/Users/juwan/Desktop/chromedriver.exe'\n",
    "\n",
    "for i in range(1,20):\n",
    "    browser = webdriver.Chrome(chrome_loc)\n",
    "    \n",
    "    url_target = 'https://www.youthcenter.go.kr/youngPlcyUnif/youngPlcyUnifList.do?plcyTpOpenTy=list_004001&srchPlcyTp=004001&pageIndex={}&trgtJynEmp=&trgtJynEmp='.format(i)\n",
    "    browser.get(url_target)\n",
    "    \n",
    "    young_html = browser.page_source\n",
    "    soup = BeautifulSoup(young_html, 'html.parser')\n",
    "    region.extend([i.text.strip() for i in soup.select('.badge')])\n",
    "    \n",
    "    for i in next_jeongchak: # 정책하나씩넘기기\n",
    "        browser.find_element_by_css_selector(i).click() \n",
    "    \n",
    "        young_html = browser.page_source\n",
    "        soup = BeautifulSoup(young_html, 'html.parser')\n",
    "        young_list.append(soup.select('.list_cont'))\n",
    "        young_name.append(\"\".join([i.text.strip() for i in soup.select('.plcy-left')]))\n",
    "        young_dec.append(\"\".join([i.text.strip() for i in soup.select('.bullet-arrow1')]))\n",
    "        \n",
    "        browser.find_element_by_css_selector('#content > div.btn_wrap.view-btn.green_type > a').click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 215,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_example = pd.DataFrame()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 216,
   "metadata": {},
   "outputs": [],
   "source": [
    "type = []\n",
    "for i in young_list:\n",
    "    type.append(i[0].text.strip())\n",
    "    \n",
    "content = []\n",
    "for i in young_list:\n",
    "    content.append(i[1].text.strip())\n",
    "    \n",
    "age = []\n",
    "for i in young_list:\n",
    "    age.append(i[5].text.strip())\n",
    "    \n",
    "region_income = []\n",
    "for i in young_list:\n",
    "    region_income.append(i[6].text.strip())\n",
    "    \n",
    "edu = []\n",
    "for i in young_list:\n",
    "    edu.append(i[7].text.strip())\n",
    "    \n",
    "major = []\n",
    "for i in young_list:\n",
    "    major.append(i[8].text.strip())\n",
    "\n",
    "job = []\n",
    "for i in young_list:\n",
    "    job.append(i[9].text.strip())\n",
    "    \n",
    "special = []\n",
    "for i in young_list:\n",
    "    special.append(i[10].text.strip())\n",
    "    \n",
    "plus = []\n",
    "for i in young_list:\n",
    "    plus.append(i[11].text.strip())\n",
    "    \n",
    "limit = []\n",
    "for i in young_list:\n",
    "    limit.append(i[12].text.strip())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 217,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_example['name'] = young_name    # 정책명\n",
    "df_example['description'] = young_dec    # 정책 내용\n",
    "\n",
    "df_example['type'] = type    # 정책 유형\n",
    "df_example['content'] = content    # 지원 내용\n",
    "\n",
    "df_example['age'] = age    # 연령\n",
    "df_example['region_income'] = region_income    # 거주지 및 소득\n",
    "df_example['edu'] = edu    # 학력\n",
    "df_example['major'] = major    # 전공\n",
    "df_example['job'] = job    # 취업 상태\n",
    "df_example['special'] = special    # 특화 분야\n",
    "df_example['plus'] = plus    # 추가 단서 사항\n",
    "df_example['limit'] = limit    # 참여 제한 대상\n",
    "\n",
    "df_example['region'] = region    # 정책 지자체\n",
    "df_example['URL']  = 'https://www.youthcenter.go.kr/youngPlcyUnif/youngPlcyUnifList.do'    # 온라인 청년센터 URL"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 219,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_example = df_example.reset_index()    # index 설정"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 224,
   "metadata": {},
   "outputs": [],
   "source": [
    "dir = 'C:/Users/juwan/Desktop/산학프로젝트/'\n",
    "\n",
    "# csv로 저장\n",
    "# df_example.to_csv(dir + 'online_jeongchaek.csv', encoding = 'utf-8', index = False) # online_jeongchaek.csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# pickle로 저장\n",
    "\n",
    "import pickle\n",
    " \n",
    "# Save pickle \n",
    "# with open(\"online_jeongchaek.pickle\",\"wb\") as fw:\n",
    "#     pickle.dump(df_example, fw)\n",
    " \n",
    " #  Load pickle|\n",
    "with open(\"online_jeongchaek.pickle\",\"rb\") as fr:\n",
    "    df_example = pickle.load(fr)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 온라인청년센터 데이터에 age -> min_age/max_age로 나눔\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_csv(dir + 'online_jeongchaek.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "#최소나이, 최대나이 col 생성\n",
    "\n",
    "a = df['age'].str\n",
    "df['max_age'] = a[-4:-1]\n",
    "df['min_age'] = a[1:4]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "replace_zero = df['min_age'].replace(' 0세', \"0\")\n",
    "df['min_age'] = replace_zero"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 인덱스 붙임\n",
    "df = df.reset_index()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "# df.to_csv('age.csv', header=True, index=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### csv 파일 안에서 세, 이상, 이하 등 수정 -> age_fix.csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_csv('online_jeongchaek_fix.csv', encoding='cp949')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['15', '18', '0', '제한없음', '19', '21', '20', '16', '1', '25', '9',\n",
       "       '8'], dtype=object)"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['min_age'].unique()"
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
       "array(['69', '34', '75', '제한없음', '39', '100', '35', '99', '40', '29',\n",
       "       '49', '60', '55', '64', '33', '30', '24', '45', '26', '19', '50',\n",
       "       '25', '20', '44', '65'], dtype=object)"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['max_age'].unique()"
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
