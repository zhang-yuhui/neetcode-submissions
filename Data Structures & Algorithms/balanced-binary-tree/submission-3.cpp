/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    bool ans = true;
    bool isBalanced(TreeNode* root) {
        if (root == nullptr) {
            return true;
        }
        auto v = dfs(root);
        return ans;
    }

    int dfs(TreeNode* root) {
        if(not ans){
            return -1;
        }
        int l = 0, r = 0;
        if (root->right != nullptr){
            r = dfs(root->right);
        }
        if (root->left != nullptr){
            l = dfs(root->left);
        }
        if(not ans){
            return -1;
        }
        if (l - r < -1 or l - r > 1) { 
            ans = false;
            return -1;
        }
        return max(l, r) + 1;
    }
};
