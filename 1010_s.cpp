#include <iostream>
#include <vector>

using namespace std;

int main() {
    int testcase;
    cin >> testcase;

    for(int i = 0; i < testcase; i++) {
        int n, m;
        cin >> n >> m;

        vector<vector<unsigned long long int>> 
            dp(n + 1, vector<unsigned long long int>(m + 1));
        
        for(int i = 0; i <= n; i++) {
            for(int j = 0; j <= m; j++) {
                if(i == j || i == 0 || j == 0) dp[i][j] = 1;
                else dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1];
            }
        }

        cout << dp[n][m] << endl;
    }
}