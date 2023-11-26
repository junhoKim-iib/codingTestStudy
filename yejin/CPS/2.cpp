// 자연수 A, B가 주어지면 A부터 B까지의 합을 수식과 함께 출력하세요.

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
