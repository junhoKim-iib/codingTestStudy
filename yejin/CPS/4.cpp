/* N���� ���̰� �Էµ˴ϴ�.
�� N ���� ��� �� ���� �������̰� ���� ���� ���� �� ���ϱ��?
�ִ� ���� ���̸� ����ϴ� ���α׷��� �ۼ��ϼ���. 
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
