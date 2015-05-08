#include <stdio.h>
#include <time.h>

int main(void){
	clock_t begin, end;
	float time_spent;
	long x;
	begin = clock();
	for(long i=0; i<100000000; i++){
		x = i * i;
	}
	end = clock();
	time_spent = ((float) (end - begin)) / CLOCKS_PER_SEC;
	printf("Program execution time:\n");
	printf("--- %f seconds ---\n", time_spent);
}
