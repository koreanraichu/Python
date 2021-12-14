text=input("Insert text: ")
# 전체 텍스트를 slicing하는 for문. 이 안에는 찾을 영역과 찾아야 할 영역이 포함되어 있다.
# 한 글자일때는 찾을 영역이 존재하지만 찾아야 하는 글자가 없으므로 첫 글자는 0이다.
find_list=[]
length=len(text)
for i in range(1,length+1):
    if len(text[0:i]) == 1:
        find_list.append(0)
    else:
        text_sub=text[0:i] # 전체 텍스트
        find=text_sub[0:i-1]# 찾을 범위
        max_list=[]
        for j in range(1,len(find)+1):
            subset=text_sub[j:] # 찾을 텍스트
            find_values=0
            if subset in find:
                max_list.append(len(subset))
            else:
                max_list.append(0)
            max_list=set(max_list)
            max_list=list(max_list)
            max_values=max(max_list) # 리스트에서 최대값을 추출
        find_list.append(max_values) # 했으면 넣어주세요
# 리스트 출력이 뭔가 이상하다.
# set을 적용하게 되면 각 iteration별로 고유값이 나오는 게 아니라 엉뚱한 값이 나오게 된다.
# append의 대상이 되는 리스트는 밖에 있지만, append는 안에 있어서 또 애매하고... append를 밖으로 뺄 수도 없다.
find_text=''.join(map(str,find_list))
# 리스트 형태로 처리한 것을 문자열로 붙여서 출력
print(find_text)