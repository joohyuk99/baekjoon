#include <iostream>
#include <vector>

using namespace std;

int main() {
    int L, C;
    cin >> L >> C;

    vector<pair<char, bool>> l;  // true when char is gather
    for(int i = 0; i < C; i++) {
        char t;
        cin >> t;
        if(t == 'a' || t == 'e' || t == 'i' || t == 'o' || t == 'u')
            l.push_back(make_pair(t, 1));
    }
}