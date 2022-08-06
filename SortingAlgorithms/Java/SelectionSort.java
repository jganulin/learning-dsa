package SortingAlgorithms;

public class SelectionSort {

    // Sorts an int array 'input' in ascending order using selection sort.
    // O(n^2) worst case time
    public static void selectionSort(int[] input) {
        for (int i = 0; i < input.length - 1; i++) {
            int min = i;
            for (int j = i + 1; j < input.length; j++) {
                if (input[j] < input[min]) {
                    min = j;
                }
            }
            // Swap input[i] with input[min]
            int temp = input[min];
            input[min] = input[i];
            input[i] = temp;
        }
    }

    public static void main(String[] args) {
        int[] test1 = {10, 99, 2, 5, 8, 7, -1, 1000};
        for (int i : test1) {
            System.out.print(i + " ");
        }
        System.out.println("\nSorted:");
        selectionSort(test1);
        for (int i : test1) {
            System.out.print(i + " ");
        }
    }

}
