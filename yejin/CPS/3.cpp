// �ڿ��� N�� �־����� �ڿ��� N�� ������� ���� ���İ� �Բ� ����ϴ� ���α׷��� �ۼ��ϼ���.
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
