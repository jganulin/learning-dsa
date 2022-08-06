package SearchingAlgorithms;

import java.util.Arrays;

public class BinarySearch {

    // Searches 'input' for 'target' using binary search. Returns index if found, -1 if not
    // O(log2 n) time worst case
    public static int binarySearch(int[] input, int target) {
        int low = 0;
        int high = input.length - 1;

        while (low <= high) {
            int mid = (low + high) / 2;
            if (input[mid] == target) {
                return target;
            } else if (input[mid] > target) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }

        return -1;
    }

    public static void main(String[] args) {
        int[] test = {5, 7, 9, 444, -66, 0, 1, 12};

    }
}
