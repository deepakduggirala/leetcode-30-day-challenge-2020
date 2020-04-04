#include<stdio.h>

void moveZeroes(int* nums, int numsSize){
    int i, numZeros;
    numZeros = 0;
    for(i=0; i<numsSize; i++) {
      if(nums[i] != 0) {
        nums[i - numZeros] = nums[i];
      } else {
        numZeros = numZeros + 1;
      }
    }
    for(i=(numsSize - numZeros);i<numsSize; i++) {
      nums[i] = 0;
    }
}

int main() {
  int nums[] = {1,0};
  int numsSize = 2;
  moveZeroes(nums, numsSize);
  int i;
  for(i=0;i<numsSize; i++) {
    printf("%d, ", nums[i]);
  }
}