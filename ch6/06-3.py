"""6-3"""
b1 = {'그룹명':'방탄소년단', '인원수':7, '리더': '김님준'}
b1['소속사'] = '빅히트 엔터테인먼트'
print(b1)
b2 = dict([['그룹명', '방탄소년단'], ['인원수', 7]])
print(b2)
b3 = dict((('리더','김님준'),('소속사','빅히트 엔터테인먼트')))
print(b3)

bts = dict(그룹명='방탄소년단', 인원수 =7, 리더 ='김님준', 소속사='빅히트 엔터테인먼트')
#구성원 추가
bts['구성원'] = ['RM','진','슈가','제이홉','지민','뷔','정국']

print(bts) #전체 출력
print(bts['구성원']) #구성원 출력
