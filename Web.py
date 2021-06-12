menu_list = ['아메리카']
int(input("주문할 제품을 선택하십시오:"))
waitCount = 0
while True:
     option = ['1. Hot(2000원)', '2. Iced(3000원)']
     print('1. Hot(2000원), 2. Iced(3000원)')
     kind = int(input('종류를 선택하십시오.'))
     plusoption1 = [ '1. 샷 추가 없음', '2. 샷 추가 1개', '3. 샷 추가 2개']
     print( '1. 샷 추가 없음, 2. 샷 추가 1개, 3. 샷 추가 2개')
     shot = int(input('선택하십시오.'))
     plusoption2 = [ '1. 시럽 추가 없음', '2. 시럽 추가 1개', '3. 시럽 추가 2개', '4.시럽 추가 3개']
     print( '1. 시럽 추가 없음, 2. 시럽 추가 1개, 3. 시럽 추가 2개, 4.시럽 추가 3개')
     syrup = int(input('선택하십시오.'))
     print('주문이 완료되었습니까?')
     ending = [ '1. 예', '2.아니오']
     print('1. 예, 2.아니오')
     ending = int(input('결제 하시겠습니까?'))
     if ending == 1:
        print('주문이 완료되었습니다.')
        print('주문한 내용입니다.' )
        print( option[kind] )
        print( plusoption1[shot] )
        print( plusoption2[syrup] )
        waitCount = waitCount + 1
        print( '대기자 ' + str(waitCount ) + ' 명입니다' )
     if ending == 2:
         print('주문을 취소하였습니다.')