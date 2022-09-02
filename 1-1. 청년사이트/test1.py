import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'youngPlcyUnifR2022011101082=youngPlcyUnifR2022011101082; youngPlcyUnifR2022031100661=youngPlcyUnifR2022031100661; youngPlcyUnifR2020123102722=youngPlcyUnifR2020123102722; youngPlcyUnifR2022042202601=youngPlcyUnifR2022042202601; youngPlcyUnifR2022032000330=youngPlcyUnifR2022032000330; WMONID=--frPsu5wES; PCID=16607228926917109832086; RC_COLOR=24; RC_RESOLUTION=2560*1440; YOUTHCENTERSESSIONID=K1-wpqW1BiHiAyUxxwfLRCjIh1rpsfIt8T_XcMIft6Xq5nk14fW6!-624621045!-194101071',
    'Referer': 'https://www.youthcenter.go.kr/youngPlcyUnif/youngPlcyUnifList.do?srchPlcyTp=004001&plcyTpOpenTy=list_004001',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.87 Whale/3.16.138.22 Safari/537.36',
    'sec-ch-ua': '"Whale";v="3", " Not;A Brand";v="99", "Chromium";v="104"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'pageUnit' : 100
    # 3000까지 된다.
}

r = requests.get('https://www.youthcenter.go.kr/youngPlcyUnif/youngPlcyUnifList.do', headers=headers, params=params)
r = BeautifulSoup(r.text, "lxml")
# print(r)
main_= r.select('div.result-list-box')[0]
# . class   # id
# print(main_)

# input 태그의 value 값을 가져온다.
input_value = main_.select('input.checkbox')

get_df = pd.DataFrame(columns=['정책명','설명','정책 유형','지원 내용','사업운영기간','사업신청기간','지원규모(명)','비고','연령',
    '거주지 및 소득','학력','전공','취업상태','특화분야','추가단서사항','참여제한대상','신청절차','심사및발표','신청사이트',
    '제출서류','기타유익정보','주관기관','운영기관','사업관련참고사이트1','사업관련참고사이트2','첨부파일','링크'])

for i in range(len(input_value)):
    code = input_value[i]['value']
    print(i)
    r = requests.get(f'https://www.youthcenter.go.kr/youngPlcyUnif/youngPlcyUnifDtl.do?bizId={code}', headers=headers)
    r = BeautifulSoup(r.text, "lxml")

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
    get_df.loc[y,"링크"]              = f"https://www.youthcenter.go.kr/youngPlcyUnif/youngPlcyUnifDtl.do?bizId={code}"

get_df.to_excel(f"youthcenter1.xlsx",encoding="utf-8-sig",index=False)




# print(code)
# .select 는 소스에 있는 전부를 가져온다. 숫자 012345
# list 배열 필수적으로 반복문 
# 우리가지금해야할게 가져온 여러개의 R값을 순서대로 상세페이지에 접속해서 자료를 가져온다.

# https://www.youthcenter.go.kr/youngPlcyUnif/youngPlcyUnifDtl.do?bizId=




# r = requests.get(f'https://www.youthcenter.go.kr/youngPlcyUnif/youngPlcyUnifDtl.do?bizId={code}', headers=headers)
# r = BeautifulSoup(r.text, "lxml")


# get_df = pd.DataFrame(columns=['정책명','설명','정책 유형','지원 내용','사업운영기간','사업신청기간','지원규모(명)','비고','연령',
#     '거주지 및 소득','학력','전공','취업상태','특화분야','추가단서사항','참여제한대상','신청절차','심사및발표','신청사이트',
#     '제출서류','기타유익정보','주관기관','운영기관','사업관련참고사이트1','사업관련참고사이트2','첨부파일','링크'])

# y = len(get_df)
# get_df.loc[y,"정책명"]       = r.select_one('h3.doc_tit02.green.plcy-pc > div:nth-child(1)').text.strip()
# get_df.loc[y,"설명"]         = r.select_one('div.ply-view-section.green > div.tit-box > h4').text.strip()
# get_df.loc[y,"정책 유형"]    = r.select_one('ul > li:nth-child(1) > div.list_cont').text.strip()
# get_df.loc[y,"지원 내용"]    = r.select_one('ul > li:nth-child(2) > div.list_cont').text.strip()
# get_df.loc[y,"사업운영기간"]  = r.select_one('ul > li:nth-child(3) > div.list_cont').text.strip()
# get_df.loc[y,"사업신청기간"]  = r.select_one('ul > li:nth-child(4) > div.list_cont').text.strip()
# get_df.loc[y,"지원규모(명)"]  = r.select_one('ul > li:nth-child(5) > div.list_cont').text.strip()
# get_df.loc[y,"비고"]          = r.select_one('ul > li:nth-child(6) > div.list_cont').text.strip()
# # 신청자격
# get_df.loc[y,"연령"]          = r.select_one('div:nth-child(4) > ul > li:nth-child(1) > div.list_cont').text.strip()
# get_df.loc[y,"거주지 및 소득"] = r.select_one('div:nth-child(4) > ul > li:nth-child(2) > div.list_cont').text.strip()
# get_df.loc[y,"학력"]          = r.select_one('div:nth-child(4) > ul > li:nth-child(3) > div.list_cont').text.strip()
# get_df.loc[y,"전공"]          = r.select_one('div:nth-child(4) > ul > li:nth-child(4) > div.list_cont').text.strip()
# get_df.loc[y,"취업상태"]       = r.select_one('div:nth-child(4) > ul > li:nth-child(5) > div.list_cont').text.strip()
# get_df.loc[y,"특화분야"]       = r.select_one('div:nth-child(4) > ul > li:nth-child(6) > div.list_cont').text.strip()
# get_df.loc[y,"추가단서사항"]   = r.select_one('div:nth-child(4) > ul > li:nth-child(7) > div.list_cont').text.strip()
# get_df.loc[y,"참여제한대상"]   = r.select_one('div:nth-child(4) > ul > li:nth-child(8) > div.list_cont').text.strip()
# # 신청방법
# get_df.loc[y,"신청절차"]       = r.select_one('div:nth-child(6) > ul > li:nth-child(1) > div.list_cont').text.strip()
# get_df.loc[y,"심사및발표"]     = r.select_one('div:nth-child(6) > ul > li:nth-child(2) > div.list_cont').text.strip()
# get_df.loc[y,"신청사이트"]     = r.select_one('div:nth-child(6) > ul > li:nth-child(3) > div.list_cont').text.strip()
# get_df.loc[y,"제출서류"]       = r.select_one('div:nth-child(6) > ul > li:nth-child(4) > div.list_cont').text.strip()
# # 기타
# get_df.loc[y,"기타유익정보"]       = r.select_one('div:nth-child(8) > ul > li:nth-child(1) > div.list_cont').text.strip()
# get_df.loc[y,"주관기관"]           = r.select_one('div:nth-child(8) > ul > li:nth-child(2) > div.list_cont').text.strip()
# get_df.loc[y,"운영기관"]           = r.select_one('div:nth-child(8) > ul > li:nth-child(3) > div.list_cont').text.strip()
# get_df.loc[y,"사업관련참고사이트1"] = r.select_one('div:nth-child(8) > ul > li:nth-child(4) > div.list_cont').text.strip()
# get_df.loc[y,"사업관련참고사이트1"] = r.select_one('div:nth-child(8) > ul > li:nth-child(5) > div.list_cont').text.strip()
# get_df.loc[y,"첨부파일"]           = r.select_one('div:nth-child(8) > ul > li:nth-child(6) > div.list_cont').text.strip()
# get_df.loc[y,"링크"]              = f"https://www.youthcenter.go.kr/youngPlcyUnif/youngPlcyUnifDtl.do?bizId={code}"

# get_df.to_excel(f"youthcenter1.xlsx",encoding="utf-8-sig",index=False)