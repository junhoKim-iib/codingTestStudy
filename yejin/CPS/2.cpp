// �ڿ��� A, B�� �־����� A���� B������ ���� ���İ� �Բ� ����ϼ���.

#include <iostream>
int main() {
	int A, B, sum = 0;
	std::cin >> A >> B;
	
	for(int i = A; i <= B; i++) {
		sum += i;
		std::cout << i << " ";
		if(i == B) {
			std::cout << "=" << " " << sum;
		}
		else {
			std::cout << "+" << " ";
		}
	}
	return 0;
} 
