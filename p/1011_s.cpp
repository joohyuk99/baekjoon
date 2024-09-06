#include <iostream>

using namespace std;

int main() {
    int tc;
    cin >> tc;
    for(int _tc = 0; _tc < tc; _tc++) {
        unsigned int x, y;
        cin >> x >> y;

        unsigned int l = y - x;
        unsigned int a = 1, n = 1;
        while(n < l) {
            n += a / 2 + 1;
            a++;
        }

        cout << a << endl;
    }
}