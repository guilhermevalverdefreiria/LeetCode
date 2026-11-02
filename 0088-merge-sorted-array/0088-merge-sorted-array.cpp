class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {

        for (int i = 0; i<n; i++){
            int a  = nums2[i];
            for (int j = 0; j<m+i; j++){
                int b = nums1[j];

                if (a<b){
                    nums1[j] = a;
                    a = b;
                }
            }
            nums1[m + i] = a;
        }       
    }
};