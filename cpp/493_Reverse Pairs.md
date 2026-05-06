# Reverse Pairs

Given an integer array nums, return the number of reverse pairs in the array.

A reverse pair is a pair (i, j) where:

    0 <= i < j < nums.length and
    nums[i] > 2 * nums[j].

Example 1:

Input: nums = [1,3,2,3,1]
Output: 2
Explanation: The reverse pairs are:
(1, 4) --> nums[1] = 3, nums[4] = 1, 3 > 2 *1
(3, 4) --> nums[3] = 3, nums[4] = 1, 3 > 2* 1

Example 2:

Input: nums = [2,4,3,5,1]
Output: 3
Explanation: The reverse pairs are:
(1, 4) --> nums[1] = 4, nums[4] = 1, 4 > 2 *1
(2, 4) --> nums[2] = 3, nums[4] = 1, 3 > 2* 1
(3, 4) --> nums[3] = 5, nums[4] = 1, 5 > 2 * 1

Constraints:

    1 <= nums.length <= 5 * 10^4
    -2^31 <= nums[i] <= 2^31 - 1

merge sort:

```cpp
class Solution {
public:
    int reversePairs(vector<int>& nums) {
        return mergeSort(nums, 0, nums.size() - 1);
    }
    int mergeSort(vector<int>& nums, int left, int right) {
        if (left >= right) return 0;
        int mid = left + (right - left) / 2;
        int res = mergeSort(nums, left, mid) + mergeSort(nums, mid + 1, right);
        for (int i = left, j = mid + 1; i <= mid; ++i) {
            while (j <= right && nums[i] / 2.0 > nums[j]) ++j;
            res += j - (mid + 1);
        }
        sort(nums.begin() + left, nums.begin() + right + 1);
        return res;
    }
};
```

红黑树:

```cpp
namespace tree{
    enum Color : char
    {
        Black,
        Red,
    };
    template<typename T>
    struct RedBlackTreeNode{
        T val;
        int count;
        int sums;
        Color color;
        
        
        RedBlackTreeNode *left;
        RedBlackTreeNode *right;

        RedBlackTreeNode(T _val):val(_val),count(0),sums(0),color(Color::Red),left(nullptr),right(nullptr){}
    };
    template<typename T>
    class RedBlackTree{
    private:
        RedBlackTreeNode<T> *root=nullptr;
        void _left_rotate(RedBlackTreeNode<T>* &node);
        void _right_rotate(RedBlackTreeNode<T>* &node);
        void _insert(RedBlackTreeNode<T>* &grand,RedBlackTreeNode<T>* &parent,RedBlackTreeNode<T>* &node,T value);
        int _uppersums(T value,RedBlackTreeNode<T>* node);
    public:
        void insert(T value);
        int uppersums(T value);
        int size();
    };
    template<typename T>
    void RedBlackTree<T>::_left_rotate(RedBlackTreeNode<T>* &node){
        RedBlackTreeNode<T>* right = node->right;
        node->right = right->left;
        right->left = node;

        right->sums = node->sums;
        if(node!=nullptr){
            node->sums = node->count;
            if(node->left!=nullptr){
                node->sums += node->left->sums;
            }
            if(node->right!=nullptr){
                node->sums += node->right->sums;
            }
        }
        node = right;
    }
    template<typename T>
    void RedBlackTree<T>::_right_rotate(RedBlackTreeNode<T>* &node){
        RedBlackTreeNode<T>* left = node->left;
        node->left = left->right;
        left->right = node;

        left->sums = node->sums;
        if(node!=nullptr){
            node->sums = node->count;
            if(node->left!=nullptr){
                node->sums += node->left->sums;
            }
            if(node->right!=nullptr){
                node->sums += node->right->sums;
            }
        }

        node = left;
    }
    template<typename T>
    void RedBlackTree<T>::_insert(RedBlackTreeNode<T>* &grand,RedBlackTreeNode<T>* &parent,RedBlackTreeNode<T>* &node,T value){
        if(node==nullptr){
            node = new RedBlackTreeNode<T>(value);
            node->count=1;
            node->sums = 1;
            return;
        }
        else if(node->val>value){
            _insert(parent,node,node->left,value);
        }
        else if(node->val<value){
            _insert(parent,node,node->right,value);
        }
        else{
            node->count ++;
            node->sums ++;
            return;
        }

        if(node!=nullptr){
            node->sums = node->count;
            if(node->left!=nullptr){
                node->sums += node->left->sums;
            }
            if(node->right!=nullptr){
                node->sums += node->right->sums;
            }
        }
        
        if(parent == nullptr){
            node->color = Color::Black;
        }        
        else if(parent->color==Color::Black){
            
        }
        else if(parent->color!=node->color){
            
        }
        else if(parent == node){

        }
        else{
            RedBlackTreeNode<T>* uncle;
            if(grand->left == parent){
                uncle = grand->right;
                if(uncle != nullptr && uncle->color == Color::Red){
                    parent->color = Color::Black;
                    uncle->color = Color::Black;
                    grand->color = Color::Red;
                }
                else{
                    if(parent->left == node){
                        _right_rotate(grand);
                        grand->color=Color::Black;
                        grand->right->color=Color::Red;
                    }
                    else{
                        _left_rotate(parent);
                        _right_rotate(grand);
                        grand->color=Color::Black;
                        grand->right->color = Color::Red;
                    }
                }
            }
            else{
                uncle = grand->left;
                if(uncle != nullptr && uncle->color == Color::Red){
                    parent->color = Color::Black;
                    uncle->color = Color::Black;
                    grand->color = Color::Red;
                }
                else{
                    if(parent->right == node){
                        _left_rotate(grand);
                        grand->color=Color::Black;
                        grand->left->color=Color::Red;
                    }
                    else{
                        _right_rotate(parent);
                        _left_rotate(grand);
                        grand->color=Color::Black;
                        grand->left->color = Color::Red;
                    }
                }
            }
        }

    }
    template<typename T>
    void RedBlackTree<T>::insert(T value){
        RedBlackTreeNode<T>* grand = nullptr;
        RedBlackTreeNode<T>* parent = nullptr;
        _insert(grand,parent,root,value);
    }

    template<typename T>
    int RedBlackTree<T>::_uppersums(T value,RedBlackTreeNode<T>* node){
        int sums = 0;
        if(node==nullptr){
            return sums;
        }
        if(node->val <= value){
            sums = _uppersums(value,node->right);
        }
        else{
            sums = _uppersums(value,node->left);
            sums += node->count;
            if(node->right != nullptr){
                sums += node->right->sums;
            }
        }
        return sums;
    }
    template<typename T>
    int RedBlackTree<T>::uppersums(T value){
        return _uppersums(value,root);
    }    
    template<typename T>
    int RedBlackTree<T>::size(){
        if(root == nullptr){
            return 0;
        }
        return root->sums;
    }    
}
using namespace tree;
class Solution {
public:
    int reversePairs(vector<int>& nums) {
        int n = nums.size();
        if(n==0){
            return 0;
        }
        int ans = 0;
        RedBlackTree<int> rbtree;
        long long d;
        for(int i = 0; i < n; i ++){
            d = (long long)nums[i];
            d = d*2;
            if(d>=INT_MAX){
                
            }
            else if(d<INT_MIN){
                ans += rbtree.size();
            }
            else{
                ans += rbtree.uppersums((int)d);
            }
            rbtree.insert(nums[i]);
        }
        return ans;
    }
};
```
