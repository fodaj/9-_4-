welcome='''
┌────────────────────┐
  상명대 최고의 맛집!!
  안다미로에 오신 것을 환영합니다!!
  먼저 인원수를 선택해주세요!    
└────────────────────┘
　   ᕱ  ᕱ  ||
　 (♡ω♡)||
　 /  つΦ
'''

menu='''
┌───────────────┐
┊    　<안다미로 메뉴판>　     ┊　　
┊                              ┊
┊-단품-                        ┊
┊1.순대국.................5,500┊
┊                              ┊
┊2.안다가츠동.............6,000┊　
┊3.김치가츠동.............6,500┊　　
┊4.고기우동...............5,500┊　　
┊5.새우튀김우동...........6,500┊
┊                              ┊
┊6.계란라면...............3,000┊　　
┊7.치즈라면...............3,500┊　　
┊8.김가루주먹밥...........2,000┊
┊9.국물떡볶이.............3,000┊
┊10.로제떡볶이(신메뉴♥)..3,000┊
┊                              ┊
┊-세트-                        ┊
┊11.김가루주먹밥+국떡.....4,500┊
┊12.계란라면+공기밥.......3,400┊
└───────────────┘
┊     ┊       ┊   ┊    ┊
┊     ┊       ┊   ┊    ┊    
┊     ┊       ┊   ┊   ˚➶ ｡˚
┊     ┊       ┊
┊     ┊        ☪.
┊     ✱ 
✧ ⋆         
'''

remainder='''
┌──────────────────────────────────┐
┊　나머지 값 추첨하기!                       　　　　　　[－][口][×]┊
┊￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣┊
┊　나머지 값을 어떻게 할까요? 랜덤 추첨을 원하시면 >1<을 입력하고,　 ┊
┊　랜덤 추첨을 원하지 않으시면 >2<를 입력해주세요!　　　　　　 　    ┊
┊　           　　　　　　　　　　　　　　　　　　　　　　　　 　    ┊
┊　　　        ┌────────┐　　┌────────┐　　　　  ┊
┊ 　　         ｜  1 > 추첨 시작 |　　 | 2 > 추첨 안함   |　         ┊
┊　　　        └────────┘　　└────────┘　　　    ┊
└──────────────────────────────────┘
'''

total_1='''
♡ ∧＿∧
 (*　･ω･)♡
┏∪∪━━━━━━━━━━━┓
'''

total_2='''
┗━━━━━━━━━━━━━┛
'''

Lotto_1='''
♡ ∩_∩
（„• ֊ •„)♡
┏∪∪━━━━━━━━━┓
┃나머지 값을 낼 사람은 ┃
'''

Lotto_2='''                
┃님 입니다!            ┃
┗━━━━━━━━━━━┛
'''

end='''
。　♡ 。　　♡。　　♡
♡。　＼　　｜　　／。　♡
 。 계산이 끝났습니다. ♡。
。─주문서를 꼭 챙겨가세요─。
   ♡ 맛있게 드세요!    .
♡。　／　　｜　　＼。　♡
。　♡。 　　。　　♡。

'''

print(welcome)
number=int(input('인원수를 입력해주세요:'))

print(menu)
print('메뉴 번호와 수량을 선택해주세요!!')
print('메뉴선택이 끝났다면 > 0 <을 입력해주세요.')
print()

total=0
while True :
    menu_type=int(input('메뉴 번호를 입력해주세요.:'))
    if menu_type==0:
        break
    else:
        amount=int(input('수량을 입력해주세요:'))
    if menu_type==1 or menu_type==4:
        total=total+(amount*5500)
    elif menu_type==2:
        total=total+(amount*6000)
    elif menu_type==3 or menu_type==5:
        total=total+(amount*6500)
    elif menu_type==6 or menu_type==9 or menu_type==10:
        total=total+(amount*3000)
    elif menu_type==7:
        total=total+(amount*3500)
    elif menu_type==8:
        total=total+(amount*2000)
    elif menu_type==11:
        total=total+(amount*4500)
    else:
        total=total+(amount*3400)
print('--------------------------------')
print(total_1, end='')
print('┃총 금액은 ', total, ' 원 입니다!┃', end='')
print(total_2)

dutch = total//number
remain = total%number

name=[]
if total%number==0:
   print("각자 내야 할 금액은", dutch,"원 입니다.")
   print()
elif total%number!=0:
       print("각자 내야 할 금액은", dutch,"원 이고,나머지는 ", remain,"원 입니다.")
       print()
       print(remainder)
       ran=int(input("1 or 2? :"))
       if ran==1:
          import random
          name = input("참가자들의 이름을 입력해주세요. 구분은 띄어쓰기(스페이스)로 합니다:").split()
          prize=random.choice(name)
         
          print(Lotto_1, end='')
          print('┃         ', prize, '♡     ┃', end='')
          print(Lotto_2)
       else:
          print()
          
print(end)



