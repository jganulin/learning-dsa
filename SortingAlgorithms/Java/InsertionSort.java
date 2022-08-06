package SortingAlgorithms;

import java.util.Arrays;

public class InsertionSort {
	public static int[] insertionSort(int[] array) {
		for (int i = 1; i < array.length; i++) {
			int key = array[i], position = i;
			while (position > 0 && array[position - 1] > key) {
				array[position] = array[position - 1];
				position--;
			}
			array[position] = key;
		}
		return array;
	}

    public static void main(String[] args) {
        int[] in = {7, 9, 2, 5, 1, 8, 0, 3};
        System.out.println(Arrays.toString(in));
        in = insertionSort(in);
        System.out.println("\n" + Arrays.toString(in));
    }
}