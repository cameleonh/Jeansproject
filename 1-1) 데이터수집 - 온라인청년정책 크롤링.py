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
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- 크롬드라이버 위치  \n",
    "chrome_loc = 'C:/Users/juwan/Desktop/chromedriver.exe' \n",
    "   \n",
    "- 브라우저 열기  \n",
    "browser = webdriver.Chrome(chrome_loc)  \n",
    "    \n",
    "- 띄울 URL  \n",
    "url_target = 'https://www.youthcenter.go.kr/youngPlcyUnif/youngPlcyUnifList.do?pageIndex=2&trgtJynEmp=&trgtJynEmp='\n",
    "\n",
    "- 가져오기  \n",
    "browser.get(url_target)"
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
   "execution_count": 206,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 최종코드\n",
    "\n",
    "for i in range(20,40):\n",
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
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 최종코드\n",
    "\n",
    "for i in range(40,67):\n",
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
   "execution_count": 214,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "789\n",
      "789\n",
      "789\n",
      "789\n"
     ]
    }
   ],
   "source": [
    "print(len(young_list))\n",
    "print(len(young_name))\n",
    "print(len(young_dec))\n",
    "print(len(region))"
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
   "execution_count": 220,
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
       "      <th>index</th>\n",
       "      <th>name</th>\n",
       "      <th>description</th>\n",
       "      <th>type</th>\n",
       "      <th>content</th>\n",
       "      <th>age</th>\n",
       "      <th>region_income</th>\n",
       "      <th>edu</th>\n",
       "      <th>major</th>\n",
       "      <th>job</th>\n",
       "      <th>special</th>\n",
       "      <th>plus</th>\n",
       "      <th>limit</th>\n",
       "      <th>region</th>\n",
       "      <th>URL</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>국민취업지원제도</td>\n",
       "      <td>한국형 실업부조로 고용안전망 사각지대에 있는 취업취약계층에게 취업지원서비스 및 생활...</td>\n",
       "      <td>취업지원, 교육훈련·체험·인턴</td>\n",
       "      <td>1. 취업취약계층에 취업지원\\n- 취업지원서비스를 종합적으로 제공하고, 저소득 구직...</td>\n",
       "      <td>만 15세 ~ 69세</td>\n",
       "      <td>Ⅰ유형 요건심사형 (구직촉진수당(50만원*6개월)과 취업지원서비스 함께 지원)\\n-...</td>\n",
       "      <td>제한없음</td>\n",
       "      <td>제한없음</td>\n",
       "      <td>미취업자</td>\n",
       "      <td>제한없음</td>\n",
       "      <td>2020년에 취업성공패키지, 청년구직활동지원금 등 사업에 참여하였다가 2021년 1...</td>\n",
       "      <td>국민취업지원제도에 참여할 수 없는 대상(Ⅰ유형)\\n\\n-학업/군복무 등으로 즉시 취...</td>\n",
       "      <td>고용노동부</td>\n",
       "      <td>https://www.youthcenter.go.kr/youngPlcyUnif/yo...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>청년추가고용장려금 지원사업</td>\n",
       "      <td>청년을 정규직으로 추가로 고용한 중소?중견기업에 인건비를 지원함으로써, 양질의 청년...</td>\n",
       "      <td>취업지원, 중소(중견)기업 취업지원</td>\n",
       "      <td>1. 청년 추가채용 1명당 연 최대 900만원을 3년간 지원2. 고용위기 지역 지정...</td>\n",
       "      <td>만 15세 ~ 34세</td>\n",
       "      <td>1. 신청대상 : 고용보험 피보험자 수 5인 이상을 고용하고, 기업 및 신규채용 청...</td>\n",
       "      <td>제한없으나 재학중인자는 불가</td>\n",
       "      <td>제한없음</td>\n",
       "      <td>해당기업 신규취업자</td>\n",
       "      <td>제한없음</td>\n",
       "      <td>-</td>\n",
       "      <td>기업에서 채용한 청년이 아래에 해당하는 경우는 지원대상에서 제외 1) 근로계약 기간...</td>\n",
       "      <td>고용노동부</td>\n",
       "      <td>https://www.youthcenter.go.kr/youngPlcyUnif/yo...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>청년 구직활동 수당 지원</td>\n",
       "      <td>도내 미취업 청년들에게 취업에 필요한 최소한의 경비를 지원하여 취업의욕 고취 및 노...</td>\n",
       "      <td>취업지원, 교육훈련·체험·인턴</td>\n",
       "      <td>월 50만원×6개월 총 300만원 지원, 지원금 수급 중 취업 시 50만원 지원최대...</td>\n",
       "      <td>만 18세 ~ 34세</td>\n",
       "      <td>신청일 기준 도내 거주, 졸업·중퇴 후 2년경과, 중위소득 150프로 미만인 자</td>\n",
       "      <td>제한없음</td>\n",
       "      <td>제한없음</td>\n",
       "      <td>미취업자</td>\n",
       "      <td>제한없음</td>\n",
       "      <td>지원금 수급 중 취업하고, 취업 후 3개월 근속 시 취업성공금 50만원 지급단 전남...</td>\n",
       "      <td>취업성공패키지, 청년구직활동지원금 등 정부사업 참여자</td>\n",
       "      <td>전남</td>\n",
       "      <td>https://www.youthcenter.go.kr/youngPlcyUnif/yo...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>3</td>\n",
       "      <td>3</td>\n",
       "      <td>국민내일배움카드</td>\n",
       "      <td>국민 누구나 일자리에 도움이 되는 훈련을 받을 수 있는 평생능력개발 기반 마련을 위...</td>\n",
       "      <td>취업지원, 교육훈련·체험·인턴</td>\n",
       "      <td>1. 국민 누구나 국민내일배움카드 신청 가능\\n- 분리 운영되었던 실업자/재직자 내...</td>\n",
       "      <td>만 0세 ~ 75세</td>\n",
       "      <td>1. 지원대상: 실업자, 근로자, 특수형태근로종사자, 자영업자\\n2. 거주지 제한 ...</td>\n",
       "      <td>제한없음</td>\n",
       "      <td>제한없음</td>\n",
       "      <td>제한없음</td>\n",
       "      <td>제한없음</td>\n",
       "      <td></td>\n",
       "      <td>국민내일배움카드 운영규정 제 4조(지원 및 지원제외)\\n-공무원, 사립학교 교직원,...</td>\n",
       "      <td>고용노동부</td>\n",
       "      <td>https://www.youthcenter.go.kr/youngPlcyUnif/yo...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>4</td>\n",
       "      <td>4</td>\n",
       "      <td>청년내일채움공제</td>\n",
       "      <td>중소·중견기업 청년 근로자의 장기근속과 자산형성을 지원하기 위해 청년, 기업, 정부...</td>\n",
       "      <td>취업지원, 중소(중견)기업 취업지원</td>\n",
       "      <td>1. 청년 지원내용\\n - 청년 본인이 2년간 300만원(매월 12만 5천원)을 적...</td>\n",
       "      <td>만 15세 ~ 34세</td>\n",
       "      <td>1. 청년 참여요건(2년형)\\n 1) 연령 : 만 15세 이상 34세 이하(※ 군필...</td>\n",
       "      <td>제한없음</td>\n",
       "      <td>제한없음</td>\n",
       "      <td>재직자</td>\n",
       "      <td>중소기업 취업</td>\n",
       "      <td>1. 계약취소\\n - 청약신청 후 청약 승인이 되면 계약이 성립하며, 계약 성립 후...</td>\n",
       "      <td>1. 가입 제외 청년\\n 1) 청년공제에 가입했던 자\\n 2) 중기부의 청년재직자 ...</td>\n",
       "      <td>고용노동부</td>\n",
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
       "2      2   청년 구직활동 수당 지원  도내 미취업 청년들에게 취업에 필요한 최소한의 경비를 지원하여 취업의욕 고취 및 노...   \n",
       "3      3        국민내일배움카드  국민 누구나 일자리에 도움이 되는 훈련을 받을 수 있는 평생능력개발 기반 마련을 위...   \n",
       "4      4        청년내일채움공제  중소·중견기업 청년 근로자의 장기근속과 자산형성을 지원하기 위해 청년, 기업, 정부...   \n",
       "\n",
       "                  type                                            content  \\\n",
       "0     취업지원, 교육훈련·체험·인턴  1. 취업취약계층에 취업지원\\n- 취업지원서비스를 종합적으로 제공하고, 저소득 구직...   \n",
       "1  취업지원, 중소(중견)기업 취업지원  1. 청년 추가채용 1명당 연 최대 900만원을 3년간 지원2. 고용위기 지역 지정...   \n",
       "2     취업지원, 교육훈련·체험·인턴  월 50만원×6개월 총 300만원 지원, 지원금 수급 중 취업 시 50만원 지원최대...   \n",
       "3     취업지원, 교육훈련·체험·인턴  1. 국민 누구나 국민내일배움카드 신청 가능\\n- 분리 운영되었던 실업자/재직자 내...   \n",
       "4  취업지원, 중소(중견)기업 취업지원  1. 청년 지원내용\\n - 청년 본인이 2년간 300만원(매월 12만 5천원)을 적...   \n",
       "\n",
       "           age                                      region_income  \\\n",
       "0  만 15세 ~ 69세  Ⅰ유형 요건심사형 (구직촉진수당(50만원*6개월)과 취업지원서비스 함께 지원)\\n-...   \n",
       "1  만 15세 ~ 34세  1. 신청대상 : 고용보험 피보험자 수 5인 이상을 고용하고, 기업 및 신규채용 청...   \n",
       "2  만 18세 ~ 34세       신청일 기준 도내 거주, 졸업·중퇴 후 2년경과, 중위소득 150프로 미만인 자   \n",
       "3   만 0세 ~ 75세  1. 지원대상: 실업자, 근로자, 특수형태근로종사자, 자영업자\\n2. 거주지 제한 ...   \n",
       "4  만 15세 ~ 34세  1. 청년 참여요건(2년형)\\n 1) 연령 : 만 15세 이상 34세 이하(※ 군필...   \n",
       "\n",
       "               edu major         job  special  \\\n",
       "0             제한없음  제한없음        미취업자     제한없음   \n",
       "1  제한없으나 재학중인자는 불가  제한없음  해당기업 신규취업자     제한없음   \n",
       "2             제한없음  제한없음        미취업자     제한없음   \n",
       "3             제한없음  제한없음        제한없음     제한없음   \n",
       "4             제한없음  제한없음         재직자  중소기업 취업   \n",
       "\n",
       "                                                plus  \\\n",
       "0  2020년에 취업성공패키지, 청년구직활동지원금 등 사업에 참여하였다가 2021년 1...   \n",
       "1                                                  -   \n",
       "2  지원금 수급 중 취업하고, 취업 후 3개월 근속 시 취업성공금 50만원 지급단 전남...   \n",
       "3                                                      \n",
       "4  1. 계약취소\\n - 청약신청 후 청약 승인이 되면 계약이 성립하며, 계약 성립 후...   \n",
       "\n",
       "                                               limit region  \\\n",
       "0  국민취업지원제도에 참여할 수 없는 대상(Ⅰ유형)\\n\\n-학업/군복무 등으로 즉시 취...  고용노동부   \n",
       "1  기업에서 채용한 청년이 아래에 해당하는 경우는 지원대상에서 제외 1) 근로계약 기간...  고용노동부   \n",
       "2                      취업성공패키지, 청년구직활동지원금 등 정부사업 참여자     전남   \n",
       "3  국민내일배움카드 운영규정 제 4조(지원 및 지원제외)\\n-공무원, 사립학교 교직원,...  고용노동부   \n",
       "4  1. 가입 제외 청년\\n 1) 청년공제에 가입했던 자\\n 2) 중기부의 청년재직자 ...  고용노동부   \n",
       "\n",
       "                                                 URL  \n",
       "0  https://www.youthcenter.go.kr/youngPlcyUnif/yo...  \n",
       "1  https://www.youthcenter.go.kr/youngPlcyUnif/yo...  \n",
       "2  https://www.youthcenter.go.kr/youngPlcyUnif/yo...  \n",
       "3  https://www.youthcenter.go.kr/youngPlcyUnif/yo...  \n",
       "4  https://www.youthcenter.go.kr/youngPlcyUnif/yo...  "
      ]
     },
     "execution_count": 220,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_example.head() ######"
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
   "execution_count": 3,
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
       "      <th>type</th>\n",
       "      <th>content</th>\n",
       "      <th>age</th>\n",
       "      <th>region_income</th>\n",
       "      <th>edu</th>\n",
       "      <th>major</th>\n",
       "      <th>job</th>\n",
       "      <th>special</th>\n",
       "      <th>plus</th>\n",
       "      <th>limit</th>\n",
       "      <th>region</th>\n",
       "      <th>URL</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>국민취업지원제도</td>\n",
       "      <td>한국형 실업부조로 고용안전망 사각지대에 있는 취업취약계층에게 취업지원서비스 및 생활...</td>\n",
       "      <td>취업지원, 교육훈련·체험·인턴</td>\n",
       "      <td>1. 취업취약계층에 취업지원\\n- 취업지원서비스를 종합적으로 제공하고, 저소득 구직...</td>\n",
       "      <td>만 15세 ~ 69세</td>\n",
       "      <td>Ⅰ유형 요건심사형 (구직촉진수당(50만원*6개월)과 취업지원서비스 함께 지원)\\n-...</td>\n",
       "      <td>제한없음</td>\n",
       "      <td>제한없음</td>\n",
       "      <td>미취업자</td>\n",
       "      <td>제한없음</td>\n",
       "      <td>2020년에 취업성공패키지, 청년구직활동지원금 등 사업에 참여하였다가 2021년 1...</td>\n",
       "      <td>국민취업지원제도에 참여할 수 없는 대상(Ⅰ유형)\\n\\n-학업/군복무 등으로 즉시 취...</td>\n",
       "      <td>고용노동부</td>\n",
       "      <td>https://www.youthcenter.go.kr/youngPlcyUnif/yo...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   index      name                                        description  \\\n",
       "0      0  국민취업지원제도  한국형 실업부조로 고용안전망 사각지대에 있는 취업취약계층에게 취업지원서비스 및 생활...   \n",
       "\n",
       "               type                                            content  \\\n",
       "0  취업지원, 교육훈련·체험·인턴  1. 취업취약계층에 취업지원\\n- 취업지원서비스를 종합적으로 제공하고, 저소득 구직...   \n",
       "\n",
       "           age                                      region_income   edu major  \\\n",
       "0  만 15세 ~ 69세  Ⅰ유형 요건심사형 (구직촉진수당(50만원*6개월)과 취업지원서비스 함께 지원)\\n-...  제한없음  제한없음   \n",
       "\n",
       "    job special                                               plus  \\\n",
       "0  미취업자    제한없음  2020년에 취업성공패키지, 청년구직활동지원금 등 사업에 참여하였다가 2021년 1...   \n",
       "\n",
       "                                               limit region  \\\n",
       "0  국민취업지원제도에 참여할 수 없는 대상(Ⅰ유형)\\n\\n-학업/군복무 등으로 즉시 취...  고용노동부   \n",
       "\n",
       "                                                 URL  \n",
       "0  https://www.youthcenter.go.kr/youngPlcyUnif/yo...  "
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
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
    "    df_example = pickle.load(fr)\n",
    "\n",
    "df_example.head(1)"
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
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['만 15세 ~ 69세', '만 15세 ~ 34세', '만 18세 ~ 34세', '만 0세 ~ 75세', '제한없음',\n",
       "       '만 18세 ~ 39세', '만 0세 ~ 39세', '만 19세 ~ 34세', '만 18세 이상',\n",
       "       '만 19세 ~ 39세', '만 0세 ~ 34세', '만 15세 ~ 39세', '만 18세 ~ 35세',\n",
       "       '만 18세 ~ 99세', '만 21세 ~ 39세', '만 34세 이하', '만 39세 이하',\n",
       "       '만 15세 ~ 99세', '만 20세 ~ 40세', '만 19세 이상', '만 19세 ~ 99세',\n",
       "       '만 18세 ~ 29세', '만 세 ~ 세', '만 29세 이하', '만 20세 ~ 39세', '만 35세 이하',\n",
       "       '만 19세 ~ 49세', '만 16세 ~ 39세', '만 19세 ~ 35세', '만 18세 ~ 40세',\n",
       "       '만 19세 ~ 60세', '만 20세 ~ 99세', '만 15세 이상', '만 1세 ~ 34세',\n",
       "       '만 18세 ~ 55세', '만 15세 ~ 64세', '만 20세 이상', '만 0세 ~ 33세',\n",
       "       '만 25세 ~ 39세', '만 19세 ~ 29세', '만 19세 ~ 30세', '만 19세 ~ 100세',\n",
       "       '만 9세 ~ 24세', '만 16세 ~ 30세', '만 18세 ~ 45세', '만 19세 ~ 26세',\n",
       "       '만 18세 ~ 60세', '만 18세 ~ 19세', '만 18세 ~ 50세', '만 16세 ~ 25세',\n",
       "       '만 16세 ~ 24세', '만 18세 ~ 25세', '만 45세 이하', '만 0세 ~ 30세', '만 20세 이하',\n",
       "       '만 18세 ~ 44세', '만 20세 ~ 26세', '만 8세 이상', '만 18세 ~ 65세',\n",
       "       '만 18세 ~ 49세', '만 20세 ~ 25세', '만 18세 ~ 24세', '만 18세 ~ 75세',\n",
       "       '만 19세 ~ 40세', '만 0세 ~ 45세', '만 15세 ~ 19세'], dtype=object)"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['age'].unique()"
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
   "execution_count": 7,
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
       "      <th>type</th>\n",
       "      <th>content</th>\n",
       "      <th>age</th>\n",
       "      <th>region_income</th>\n",
       "      <th>edu</th>\n",
       "      <th>major</th>\n",
       "      <th>job</th>\n",
       "      <th>special</th>\n",
       "      <th>plus</th>\n",
       "      <th>limit</th>\n",
       "      <th>region</th>\n",
       "      <th>URL</th>\n",
       "      <th>max_age</th>\n",
       "      <th>min_age</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>국민취업지원제도</td>\n",
       "      <td>한국형 실업부조로 고용안전망 사각지대에 있는 취업취약계층에게 취업지원서비스 및 생활...</td>\n",
       "      <td>취업지원, 교육훈련·체험·인턴</td>\n",
       "      <td>1. 취업취약계층에 취업지원\\n- 취업지원서비스를 종합적으로 제공하고, 저소득 구직...</td>\n",
       "      <td>만 15세 ~ 69세</td>\n",
       "      <td>Ⅰ유형 요건심사형 (구직촉진수당(50만원*6개월)과 취업지원서비스 함께 지원)\\n-...</td>\n",
       "      <td>제한없음</td>\n",
       "      <td>제한없음</td>\n",
       "      <td>미취업자</td>\n",
       "      <td>제한없음</td>\n",
       "      <td>2020년에 취업성공패키지, 청년구직활동지원금 등 사업에 참여하였다가 2021년 1...</td>\n",
       "      <td>국민취업지원제도에 참여할 수 없는 대상(Ⅰ유형)\\n\\n-학업/군복무 등으로 즉시 취...</td>\n",
       "      <td>고용노동부</td>\n",
       "      <td>https://www.youthcenter.go.kr/youngPlcyUnif/yo...</td>\n",
       "      <td>69</td>\n",
       "      <td>15</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   index      name                                        description  \\\n",
       "0      0  국민취업지원제도  한국형 실업부조로 고용안전망 사각지대에 있는 취업취약계층에게 취업지원서비스 및 생활...   \n",
       "\n",
       "               type                                            content  \\\n",
       "0  취업지원, 교육훈련·체험·인턴  1. 취업취약계층에 취업지원\\n- 취업지원서비스를 종합적으로 제공하고, 저소득 구직...   \n",
       "\n",
       "           age                                      region_income   edu major  \\\n",
       "0  만 15세 ~ 69세  Ⅰ유형 요건심사형 (구직촉진수당(50만원*6개월)과 취업지원서비스 함께 지원)\\n-...  제한없음  제한없음   \n",
       "\n",
       "    job special                                               plus  \\\n",
       "0  미취업자    제한없음  2020년에 취업성공패키지, 청년구직활동지원금 등 사업에 참여하였다가 2021년 1...   \n",
       "\n",
       "                                               limit region  \\\n",
       "0  국민취업지원제도에 참여할 수 없는 대상(Ⅰ유형)\\n\\n-학업/군복무 등으로 즉시 취...  고용노동부   \n",
       "\n",
       "                                                 URL max_age min_age  \n",
       "0  https://www.youthcenter.go.kr/youngPlcyUnif/yo...      69      15  "
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head(1)"
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
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['15', '18', '0', '제한없음', '19', '21', '20', '16', '1', '25', '9',\n",
       "       '8'], dtype=object)"
      ]
     },
     "execution_count": 16,
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
    "### csv 파일 안에서 세, 이상, 이하 등 수정 -> age_fix.csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 확인작업\n",
    "\n",
    "df = pd.read_csv('online_jeongchaek_fix.csv', encoding='cp949')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
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
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
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
