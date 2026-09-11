class Solution {
public:
    bool isPalindrome(string s) {
        string a = "";
        for (char c : s) {
            if (isalnum(c)) {
                a += tolower(c);
            }
        }
        string b = a;
        reverse(b.begin(), b.end());
        return a == b;
    }
};