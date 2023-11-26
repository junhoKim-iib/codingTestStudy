// 자연수 N이 주어지면 자연수 N의 진약수의 합을 수식과 함께 출력하는 프로그램을 작성하세요.
#include <iostream>
int main() {
	int  i, n, sum = 0, last;
	std::cin >> n;
	for(i = 2; i <= n; i++) {
		if(n % i == 0) {
			break;
		}
	}
	last = n / i;
	for(int j = 1; j < last; j++) {
		if(n % j == 0) {
			std::cout << j << " + ";
			sum += j;
		}
	}
	std::cout << last << " = " << sum + last;
	return 0;
} 
