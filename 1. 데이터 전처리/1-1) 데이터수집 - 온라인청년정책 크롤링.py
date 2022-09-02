# https://www.youthcenter.go.kr/youngPlcyUnif/youngPlcyUnifDtl.do?bizId=R2022010701021
# https://youth.seoul.go.kr/site/main/customSupp/list?targetMulti=&ageMulti=#n
import requests
from bs4 import BeautifulSoup  
import re
import pandas as pd
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Origin': 'https://www.youthcenter.go.kr',
    'Referer': 'https://www.youthcenter.go.kr/youngPlcyUnif/youngPlcyUnifList.do',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.87 Whale/3.16.138.22 Safari/537.36',
}
params = {
    'pageIndex': '1',
    'srchSortOrder': '2', #2 조회순 , 1 추천순
    'pageUnit': '1',
    # 'pageUnit': '3000', 
}
r = requests.get('https://www.youthcenter.go.kr/youngPlcyUnif/youngPlcyUnifList.do',headers=headers, params=params)

r = BeautifulSoup(r.text, "lxml")

main_= r.select('div.result-list-box')[0]

# 1 replace
def replace_list(main_):
	detailCode_replace_list = []
	detailCode_replace = main_.select('li a')
	for i in range(len(detailCode_replace)):
		code = detailCode_replace[i]['onclick'].replace("f_Detail('","").replace("');","")
		detailCode_replace_list.append(code)
	# print(detailCode_replace_list)
	print(len(detailCode_replace_list))
	return detailCode_replace_list
detailCode_list = replace_list(main_)

# 2 정규식사용
def re_list(main_):
	detailCode_re_list = []
	detailCode_re = main_.select('li a')
	for i in range(len(detailCode_re)):
		code = detailCode_re[i]['onclick']
		code = re.search(r"R\d*", code)
		detailCode_re_list.append(code.group())
	print(detailCode_re_list)
	return detailCode_re_list
# detailCode_list = re_list(main_)

# 3 value값 따기
def value_list(main_):
	detailCode_input_list = []
	detailCode_input = main_.select('input.checkbox')
	for i in range(len(detailCode_input)):
		detailCode_input_list.append(detailCode_input[i]['value'])
	print(detailCode_input_list)
	return detailCode_input_list
# detailCode_list = value_list(main_)


# ---------------------------상세페이지---------------------------
get_df = pd.DataFrame(columns=['정책명','설명','정책 유형','지원 내용','사업운영기간','사업신청기간','지원규모(명)','비고','연령',
    '거주지 및 소득','학력','전공','취업상태','특화분야','추가단서사항','참여제한대상','신청절차','심사및발표','신청사이트',
    '제출서류','기타유익정보','주관기관','운영기관','사업관련참고사이트1','사업관련참고사이트2','첨부파일','링크'])


def page2(detailCode_list):
    for i in detailCode_list:
        try :
            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'Cookie': 'youngPlcyUnifR2022010701021=youngPlcyUnifR2022010701021; youngPlcyUnifR2022032202066=youngPlcyUnifR2022032202066; youngPlcyUnifR2022032000435=youngPlcyUnifR2022032000435; youngPlcyUnifR2022011101102=youngPlcyUnifR2022011101102; youngPlcyUnifR2022011101082=youngPlcyUnifR2022011101082; WMONID=--frPsu5wES; PCID=16607228926917109832086; RC_COLOR=24; RC_RESOLUTION=2560*1440; YOUTHCENTERSESSIONID=xpmrv2xrhVd2q-EVuJEfV94_c_gKFsaL6wsWDhMIIDcVJTKfYYdR!-127131465!-1863065322',
                'Origin': 'https://www.youthcenter.go.kr',
                'Referer': 'https://www.youthcenter.go.kr/youngPlcyUnif/youngPlcyUnifList.do?pageUnit=3000',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.87 Whale/3.16.138.22 Safari/537.36',
            }

            data = {
                '_csrf': '140b3e4b-1934-4dc2-ab62-5ade468502ee',
                'bizId': i,
            }
            r = requests.post('https://www.youthcenter.go.kr/youngPlcyUnif/youngPlcyUnifDtl.do', headers=headers, data=data)
            r = BeautifulSoup(r.text, "lxml")
            # print(r.select_one('div:nth-child(4) > ul > li:nth-child(1) > div.list_cont').text.strip())

            y = len(get_df)
            get_df.loc[y,"정책명"]       = r.select_one('h3.doc_tit02.green.plcy-pc > div:nth-child(1)').text.strip()
            get_df.loc[y,"설명"]         = r.select_one('div.ply-view-section.green > div.tit-box > h4').text.strip()
            get_df.loc[y,"정책 유형"]    = r.select_one('ul > li:nth-child(1) > div.list_cont').text.strip()
            get_df.loc[y,"지원 내용"]    = r.select_one('ul > li:nth-child(2) > div.list_cont').text.strip()
            get_df.loc[y,"사업운영기간"]  = r.select_one('ul > li:nth-child(3) > div.list_cont').text.strip()
            get_df.loc[y,"사업신청기간"]  = r.select_one('ul > li:nth-child(4) > div.list_cont').text.strip()
            get_df.loc[y,"지원규모(명)"]  = r.select_one('ul > li:nth-child(5) > div.list_cont').text.strip()
            get_df.loc[y,"비고"]          = r.select_one('ul > li:nth-child(6) > div.list_cont').text.strip()
            # 신청자격
            get_df.loc[y,"연령"]          = r.select_one('div:nth-child(4) > ul > li:nth-child(1) > div.list_cont').text.strip()
            get_df.loc[y,"거주지 및 소득"] = r.select_one('div:nth-child(4) > ul > li:nth-child(2) > div.list_cont').text.strip()
            get_df.loc[y,"학력"]          = r.select_one('div:nth-child(4) > ul > li:nth-child(3) > div.list_cont').text.strip()
            get_df.loc[y,"전공"]          = r.select_one('div:nth-child(4) > ul > li:nth-child(4) > div.list_cont').text.strip()
            get_df.loc[y,"취업상태"]       = r.select_one('div:nth-child(4) > ul > li:nth-child(5) > div.list_cont').text.strip()
            get_df.loc[y,"특화분야"]       = r.select_one('div:nth-child(4) > ul > li:nth-child(6) > div.list_cont').text.strip()
            get_df.loc[y,"추가단서사항"]   = r.select_one('div:nth-child(4) > ul > li:nth-child(7) > div.list_cont').text.strip()
            get_df.loc[y,"참여제한대상"]   = r.select_one('div:nth-child(4) > ul > li:nth-child(8) > div.list_cont').text.strip()
            # 신청방법
            get_df.loc[y,"신청절차"]       = r.select_one('div:nth-child(6) > ul > li:nth-child(1) > div.list_cont').text.strip()
            get_df.loc[y,"심사및발표"]     = r.select_one('div:nth-child(6) > ul > li:nth-child(2) > div.list_cont').text.strip()
            get_df.loc[y,"신청사이트"]     = r.select_one('div:nth-child(6) > ul > li:nth-child(3) > div.list_cont').text.strip()
            get_df.loc[y,"제출서류"]       = r.select_one('div:nth-child(6) > ul > li:nth-child(4) > div.list_cont').text.strip()
            # 기타
            get_df.loc[y,"기타유익정보"]       = r.select_one('div:nth-child(8) > ul > li:nth-child(1) > div.list_cont').text.strip()
            get_df.loc[y,"주관기관"]           = r.select_one('div:nth-child(8) > ul > li:nth-child(2) > div.list_cont').text.strip()
            get_df.loc[y,"운영기관"]           = r.select_one('div:nth-child(8) > ul > li:nth-child(3) > div.list_cont').text.strip()
            get_df.loc[y,"사업관련참고사이트1"] = r.select_one('div:nth-child(8) > ul > li:nth-child(4) > div.list_cont').text.strip()
            get_df.loc[y,"사업관련참고사이트1"] = r.select_one('div:nth-child(8) > ul > li:nth-child(5) > div.list_cont').text.strip()
            get_df.loc[y,"첨부파일"]           = r.select_one('div:nth-child(8) > ul > li:nth-child(6) > div.list_cont').text.strip()
            get_df.loc[y,"링크"]              = f"https://www.youthcenter.go.kr/youngPlcyUnif/youngPlcyUnifDtl.do?bizId={i}"

        except:
            continue
    # print(get_df)
    get_df.to_excel(f"youthcenter.xlsx",encoding="utf-8-sig",index=False)

page2(detailCode_list)