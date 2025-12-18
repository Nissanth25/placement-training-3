class Solution {
    public int[] frequencySort(int[] nums) {
        int mini = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;
        for (int n: nums){
            mini = Math.min(mini, n);
            max  = Math.max(max, n);
        }

        int range = max - mini + 1;
        int[] freq = new int[range];
        for (int n:nums){
            freq[n - mini]+=1;
        }
        List<List<Integer>> numsInAFreq = new ArrayList<>();
        for(int i = 0 ; i <= nums.length; i++){
            numsInAFreq.add(new ArrayList<>());
        }
        for (int i = max; i >=mini; i--){
            if (freq[i-mini]> 0) numsInAFreq.get(freq[i-mini]).add(i);
        }
        int[] ans = new int[nums.length];
        int k = 0;
        for (int f = 1; f <= nums.length; f++){
            for(int n: numsInAFreq.get(f)){
                for (int i = 0; i < f; i++) ans[k++] = n;
            }
        }
        return ans;
    }
}
