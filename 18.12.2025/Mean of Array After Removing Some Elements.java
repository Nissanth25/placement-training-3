class Solution {
    public double trimMean(int[] arr) {
        int len = arr.length;
        double sum = 0;
        Arrays.sort(arr);

        for (int i = len / 20; i < len - len / 20; i++) {
            sum += arr[i];
        }

        return sum / (len * 9 / 10);
    }
}
