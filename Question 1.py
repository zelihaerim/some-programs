# -*- coding: utf-8 -*-
import sys
"""
Created on Sat Jun  5 16:46:30 2021

@author: Zeliha
"""
def checkSpecialTurkishChar(i):
    if((i=='ü') or (i=='Ü') or (i=='ö') or (i=='Ö') or (i=='ç') or (i=='Ç') or (i=='ğ') or (i=='Ğ') or (i=='ş') or (i=='Ş')):
        return 1
    else:
        return 0
    
def find(word):
    deep_vowels=['a', 'ı','o', 'u','A','I','O', 'U']
    acute_vowels=['e', 'i','ö','ü','E', 'İ','Ö','Ü']
    flag1=0
    flag2=0
    if len(word)==0:
        return -1
    for i in word:
        if((i.isalpha()==True) or (checkSpecialTurkishChar(i)==1)):
            for j in deep_vowels:
                if i==j:
                    flag1=1
            for j in acute_vowels:
                if i==j:
                    flag2=1
            if (flag1==1 and flag2==1):
                print("{} -> Buyuk unlu uyumuna uymaz.".format(word))
                return 0
        else:
            print("{} -> Contains special charachter".format(word))
            return -2
    print("{} -> Buyuk unlu uyumuna uyar.".format(word))
    return 1        


# driver code
if __name__ == "__main__":
    word=['Ü','r','d','ü','n']
    find(word)
    word=['K','ı','r','ı','m']
    find(word)
    word=['D','ü','ğ','Ü','m']
    find(word)
    word=['Z','e','l','i','h','a']
    find(word)
    word=['A','r','d','i','c']
    find(word)
    word=['Ç','a','ğ','r','ı']
    find(word)
    word=['I','ş','ı','l']
    find(word)
    

