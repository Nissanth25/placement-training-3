class Solution {
    public boolean canFormArray(int[] arr, int[][] pieces) {
        int[] map = new int[101];
        for (int i = 0; i < arr.length; i++) {
            map[arr[i]] = i+1;
        }
        for (int[] piece: pieces) {
            for (int j = 0; j < piece.length; j++) {
                if (map[piece[j]] == 0 || map[piece[j]] - map[piece[0]] != j) {
                    return false;
                }
            }
        }
        return true;
    }
}
