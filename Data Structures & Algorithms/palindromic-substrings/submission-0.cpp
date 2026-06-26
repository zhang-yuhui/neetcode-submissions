#include <vector>
#include <iostream>
using namespace std;
class Solution {
public:
    int countSubstrings(string s) {
        int n = s.size();
        auto dp = vector<vector<int>>(n, vector<int>(n, 0));
        int ans = 0;
        for(int len = 1; len <= n; len++){
            for(int i = 0; i + len <= n; i++){
                int j = i + len - 1;
                if (len == 1){
                    dp[i][j] = 1;
                    ans ++;
                } else if (len == 2 and s[i] == s[j]) {
                    dp[i][j] =1;
                    ans ++;
                } else if (s[i] == s[j] and dp[i+1][j-1] == 1){
                    dp[i][j] = 1;
                    ans ++;
                }
            }
        }
        return ans;
    }
};
