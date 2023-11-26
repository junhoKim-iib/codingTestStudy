/* N명의 나이가 입력됩니다.
이 N 명의 사람 중 가장 나이차이가 많이 나는 경우는 몇 살일까요?
최대 나이 차이를 출력하는 프로그램을 작성하세요. 
*/
#include <iostream>
int main() {
	int n, min, max;
	std::cin >> n;
	int age[n];
	for(int i = 0; i < n; i++) {
		std::cin >> age[i];
	}
	min = age[0];
	max = age[0];
	
	for(int i = 1; i < n; i++) {
		if(age[i] > max) {
			max = age[i];
		}
		if(age[i] < min) {
			min = age[i];
		} 
	}
	std::cout <<  max - min;
	return 0;
}
