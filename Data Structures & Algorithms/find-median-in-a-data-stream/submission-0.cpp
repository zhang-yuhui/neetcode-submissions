#include <queue>
#include <iostream>
using namespace std;
class MedianFinder {
public:
    priority_queue<int> left_half;
    priority_queue<int, vector<int>, greater<int> > right_half;
    MedianFinder() {

    }
    
    void addNum(int num) {
        if (left_half.empty() or num <= left_half.top()) {
            left_half.push(num);
        } else {
            right_half.push(num);
        }
        
        // Balance the heaps
        if (left_half.size() > right_half.size() + 1) {
            right_half.push(left_half.top());
            left_half.pop();
        }
        if (right_half.size() > left_half.size()) {
            left_half.push(right_half.top());
            right_half.pop();
        }
    }
    
    double findMedian() {
        int diff = left_half.size() - right_half.size();
        if(diff == 0){
            return (left_half.top() + right_half.top()) / 2.0;
        } else {
            return (double)left_half.top();
        }
    }

};






