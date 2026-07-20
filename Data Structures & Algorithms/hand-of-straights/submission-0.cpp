#include <map>

class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int groupSize) {
        map<int, int>m = map<int, int>();
        for(auto h: hand){
            if(m.find(h) != m.end()){
                m[h] += 1;
            } else {
                m[h] = 1;
            }
        }
        int cur = m.begin()->first;
        while(!m.empty()){
            for(int i = 0;i < groupSize; i++){
                if(m.find(cur) == m.end()){
                    return false;
                }
                m[cur] -= 1;
                if(m[cur] == 0){
                    m.erase(cur);
                }
                cur ++;
            }
            cur = m.begin()->first;
        }
        return true;
    }
};
