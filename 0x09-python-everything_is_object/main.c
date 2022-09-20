#include <stdio.h>
#include <stdlib.h>

/*file input */

int main()
{
	FILE *ptr = NULL;
	char str[10] = "type";
	ptr = fopen("0-answer.txt", "w");

	if (ptr == NULL)
	{
		printf("cant write into file\n");
		exit(1);
	}
	else
	{
		fprintf(ptr, "%s", str);
		fclose(ptr);
	}
	return 0;
}

