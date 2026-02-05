#!/usr/bin/env python
# coding: utf-8

# In[ ]:


text=input("Insert text: ")
print(text)  
# 일단 소규모로 먼저 진행해보자. 


# In[ ]:


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
            max_values=max(max_list) # 리스트에서 최대값을 추출한다
        find_list.append(max_values) # 넣어주시죠 
# 이상하다... 왜 제시한거랑 결과가 다르지? 


# In[ ]:


find_text=''.join(map(str,find_list))
# 출력할 문자열을 붙여준다. (데이터 저장 형태가 리스트였음)
print(find_text)


# In[ ]:


with open ('Result.txt','w',encoding='utf-8') as result_write:
    result_write.write('Input sequence: ')
    result_write.write(text)
    result_write.write('\nOutput: ')
    result_write.write(find_text)  
# reference: https://smart-factory-lee-joon-ho.tistory.com/200


# In[ ]:




