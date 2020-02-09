#include <stdlib.h>
#include <stdio.h>
#include <string.h>
int activate(char *str) 
{
	char key[25];
	strcpy(key, str);
	if (key[30] == 7) 
	{
		printf("Congratulations!  The first flag is XXXXXXXXXXXXXXXXX\n");
		fflush( stdout );
	}
	return 1;
}	
void win() 
{
	printf("Congratulations!  The second flag is XXXXXXXXXXXXXXX\n");
	fflush( stdout );
}	
void main() 
{
	char key[100];
	printf("Enter product key: ");
        gets(key);
	if (activate(key)) 
		printf("\nOh no! You may be the victim of software piracy!\n");
	else 
		win();
}

