#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(const vector<int>& a, const vector<int>& b, int columnIndex){
    return a[columnIndex] < b[columnIndex];
}

int str_to_idx(string str){ // ext 와 sort_by 를 정수 인덱스로 변환 
    if(str == "code"){
        return 0;
    }
    else if(str == "date"){
        return 1;
    }
    else if(str == "maximum"){
        return 2;
    }
    else if(str == "remain"){
        return 3;
    }
    return -1;
}

vector<vector<int>> solution(vector<vector<int>> data, string ext, int val_ext, string sort_by) {
    vector<vector<int>> answer;
    
    int idx = str_to_idx(ext);
    int sort_idx = str_to_idx(sort_by);

    for(int i = 0; i < data.size(); i++){
        if(data[i][idx] < val_ext){
            answer.push_back(data[i]);
        }
    }
    sort(answer.begin(), answer.end(), [sort_idx](const vector<int>& a, const vector<int>& b) {
        return compare(a, b, sort_idx);
    });
    
    
    return answer;
}