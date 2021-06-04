#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <locale.h> /* Without this library Turkish chars can not be comparable, doesn't work */

#define SIZE 255
int find(char word[SIZE]);
int main(int argc, char const *argv[])
{
	setlocale(LC_ALL, "Turkish"); /* doesn't work */

	char word[SIZE];
	int i;
	strcpy(word,"zeliha");
	find(word); 
	strcpy(word,"telefon");
	find(word);  
	strcpy(word,"krem");
	find(word);
	strcpy(word,"silgi");
	find(word);
	
	return 0;
}
int find(char word[SIZE]){
	const char deep_vowels[5]={'a', 'ı', 'o', 'u'};
	const char acute_vowels[5]={'e', 'i', 'ö', 'ü'};
	int i,j,flag1=0,flag2=0;
	if (word[0]=='\0')
	{
		return -1; /* word length is zero, there is no word to test */
	}
	for (i = 0; word[i] != '\0'; ++i)
	{
		if((word[i]>=65 && word[i]<=90) || (word[i]>=97 && word[i]<=122) || (word[i]== 'ü') || (word[i]=='ğ') || (word[i]=='Ü') || (word[i]=='Ğ')){
			for (j = 0; j < strlen(deep_vowels); ++j)
			{
				if (word[i]==deep_vowels[j])
				{
					flag1=1;
				}
				if (word[i]==acute_vowels[j])
				{
					flag2=1;
				}
			}
			if (flag1 && flag2)
			{
				printf("%s -> Buyuk unlu uyumuna uymaz.\n",word);
				return -1;
			}
		}
	}
	printf("%s -> Buyuk unlu uyumuna uyar.\n",word);
	return 1;
}