import os
import glob
import operator
word_list =[]
word_dict = {}
txt_list = glob.glob('./보이스피싱/'+ '*.txt')
#print(txt_list)
for i in range(len(txt_list)):
    f = open(txt_list[i], 'rt', encoding='UTF8')
    while True:
        line = f.readline()
        
        if not line: break
        elif line[0:3] =='사기범':
            line = line.split(':')[-1]
            line = line.split(' ')
            for word in line:
                if len(word) >=2 and len(word)<=5:
                    
                    if len(word) > 2 and word[0:2] in word_list:
                        word_dict[word[0:2]]+=1
                    if len(word) > 3 and word[0:3] in word_list:
                        word_dict[word[0:3]] +=1
                       
                    if word not in word_list: #단어 리스트에 없는 단어인 경우 단어 리스트에 단어를 추가함
                        word_list.append(word) 
                        word_dict[word] =1 #단어 사전에 1값으로 추가함   
                    else:
                        word_dict[word]+=1    
            #print(line)
            
word_dict_sorted = sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True)
   
print(dict(word_dict_sorted))