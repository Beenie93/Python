import pandas as pd
import numpy as np
from selenium import webdriver
import matplotlib as mpl
import matplotlib.pyplot as plt

%matplotlib inline 
# jupyter에서 바로 그리게 설정
mpl.rcParams['font.family'] = 'Malgun Gothic' # 맑은 고딕체로 한글 폰트 지정
mpl.rcParams['axes.unicode_minus'] = False #그래프에서 마이너스(-)폰트가 깨지는 문제 해결

driver = webdriver.Chrome(executable_path='./chromedriver')
#'./chromedriver' 이곳에 파일 다운받은 경로명 입력하여 driver 설정

league_year = [] # 2009~2018년 각 연도 넣을 리스트
team_name = [] #각 팀들의 이름 넣을 리스트
team_point = [] # 각 팀들의 승점 넣을 리스트
team_rank = [] # 각 팀들의 순위 넣을 리스트
years = pd.date_range('2009',periods=10,freq="Y") # 2009년부터 1년 단위로 10개 생성

for year in years: # 각 연도 대입
    html = "https://sports.news.naver.com/wfootball/record/index.nhn?category=epl&year={this_year}"
    year = year.strftime('%Y') # 위 주소의 {this_year} 이 "2009" 형식으로 들어가므로 %Y로 연도 재대입
    convert_html = html.format(this_year=year) # html의 this_year에 재대입한 year를 넣어줌
    driver.get(convert_html) # 웹 브라우저를 열어 해당 html객체 불러옴 
    
    last_rank_num = 20 # 팀 순위가 20위가 최하위임으로 20을 대입

    season = year + '/' + str(int(year)-2000+1) # league_year에 넣을 각 연도를 2009/10 이런식으로 표시
    league_year.extend([season for n in range(last_rank_num)]) # 시즌당 20개의 팀이 표시되므로 팀에 맞춰 20개를 넣어줌

    team_selector = 'tr > td.align_l > div > span' # 팀 이름 검색을 위한 소스 태그 위치
    team_name.extend([driver.find_elements_by_css_selector(team_selector)[rank_num].text for rank_num in range(last_rank_num)])
    # selector로 parsing한 각 팀의 이름을 .text로 추출하여 20개의 팀 이름을 리스트에 추가
    
    point_selector = 'tr > td.selected > div > span' # 팀 승점 검색을 위한 소스 태그 위치
    team_point.extend([int(driver.find_elements_by_css_selector(point_selector)[rank_num].text) for rank_num in range(last_rank_num)])
    # selector로 parsing한 각 팀의 승점을 .text로 추출하여 추출한 20개의 팀에 대응되는 승점을 리스트에 추가 
    
    team_rank.extend([rank for rank in range(1,last_rank_num+1)])
    # 시즌별 20개의 팀의 순위가 있으므로 range(1~21)을 통해 1부터 20까지의 순위 리스트에 추가
    
team_record = pd.DataFrame({'year':league_year,'rank':team_rank,'team':team_name,'point':team_point})
# DataFrame형태로 연도,순위,이름,승점 데이터 저장
team_record

# 2009/10 ~ 2018/19년도별로 보기 좋게 재정렬한 데이터
team_record_pd = pd.pivot_table(team_record,index=['year','rank','team'],values=['point'], aggfunc=np.sum)
team_record_pd

# 2009/10 ~ 2018/19 동안 가장 많은 승점을 얻은 팀
team_record_pd = pd.pivot_table(team_record,index=['team'] ,values=['point'], aggfunc=np.sum)
team_best_point = team_record_pd.sort_values(by='point', ascending=False)
team_best_point.head()

# 특정 팀의 순위 및 승점 변화 확인
tmp = team_record.query('team==["스토크 시티 FC"]') # 해당 팀을 검색

plt.figure(figsize=(12,8)) # 그려지는 사이즈를 정의
plt.plot(tmp['year'],tmp['rank'],'m-o') # 연도별 순위를 보라색 실선 원모양으로 선 표시
#plt.plot(tmp['year'],tmp['point']) # 시즌별 승점을 표현 시 사용
plt.xlabel('Season') # x축 정의
plt.ylabel('순위') # y축 정의
#ply.ylabel('승점') $ 시즌별 승점 표현 시 사용
plt.legend(loc='best') # 그려지는 선에 대한 정보를 자동으로 적합한 곳에 표시
plt.grid() # 격자 무늬 생성
plt.show() # 그려짐


#전체 팀의 시즌별 순위(또는 승점) 변화 확인
team_total = pd.pivot_table(team_record,index=['year'],columns=['team'],values=['rank']) # values=['point'] 할 시에는 승점으로 확인 가능
team_total.columns = team_total.columns.droplevel() # team column위에 추가되어 있는 rank 삭제하여 테이블 보기 좋게 만듬
team_total

team_total.plot(y=['첼시 FC','리버풀 FC','맨체스터 유나이티드 FC','토트넘 핫스퍼 FC','맨체스터 시티 FC','아스널 FC'],figsize=(12,6))
#해당 팀들의 시즌별 순위 변화를 그려주기 위한 설정
plt.legend(loc='best') # 그려지는 선에 대한 정보를 자동으로 적합한 곳에 표시
plt.xlabel('Season') # x축 정의
plt.ylabel('순위') # y축 정의
plt.grid() # 격자 무늬 생성
plt.show() # 그려짐