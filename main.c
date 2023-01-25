#include <stdlib.h>
#include <stdio.h>

void Swap(int* first, int* second) {
	int temp = *first;
	*first = *second;
	*second = temp;
}

void Heapify(int* ms, int size, int index) {
	int larges = index;
	int left = 2 * index + 1;
	int right = 2 * index + 2;
	if (left < size && ms[left] > ms[larges]) {
		larges = left;
	}
	if (right < size && ms[right] > ms[larges] ) {
		larges = right;
	}
	if (larges != index) {
		Swap(&ms[index], &ms[larges]);
		Heapify(ms, size, larges);
	}
}

void HeapSort(int* ms, int size) {
	for (int i = size / 2 - 1; i >= 0; --i) {
		Heapify(ms, size, i);
	}
	for (int i = size - 1; i >= 0; --i) {
		Swap(&ms[0], &ms[i]);
		Heapify(ms, i, 0);
	}
}

int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    int* nums2 = (int*)malloc(numsSize * sizeof(int));
    memcpy (nums2, nums, numsSize * sizeof(int));
    int firstNum, secondNum;
    HeapSort(nums, numsSize);
    int left = 0;
    int right = numsSize - 1;
    while (left < right){
        int sum = nums[left] + nums[right];
        if (sum == target){
            firstNum = nums[left];
            secondNum = nums[right];
            break;
        }
        else if(sum < target){
            left++;
        }
        else{
            right--;
        }
    }
    int firstIndex, secondIndex;
    for(int i = 0; i < numsSize; ++i ){
        if (nums2[i] == firstNum ){
            firstIndex = i;
            break;
        }
    }
    for(int i = 0; i < numsSize; ++i ){
        if (nums2[i] == secondNum && i != firstIndex){
            secondIndex = i;
            break;
        }
    }
    printf("[%d,%d]", firstIndex, secondIndex);
    return 0;
}