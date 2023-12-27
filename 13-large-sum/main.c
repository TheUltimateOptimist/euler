#include "stdio.h"
#include "stdlib.h"
#include "string.h"

void addLargeNumbers(char *a, char *b, char *result) {
    int aLength = strlen(a);
    int bLength = strlen(b);
    int maxLength = aLength;
    if (bLength > maxLength) {
        maxLength = bLength;
    }
    int carry = 0;
    int index = 0;
    for (int i = maxLength - 1; i >= 0; i--) {
        int aDigit = 0;
        int bDigit = 0;
        int aAt = i - maxLength + aLength;
        int bAt = i - maxLength + bLength;
        if (aAt >= 0) {
            aDigit = a[aAt] - 48;
        }
        if (bAt >= 0) {
            bDigit = b[bAt] - 48;
        }
        int sum = aDigit + bDigit + carry;
        int newDigit = sum % 10;
        carry = sum / 10;
        result[index] = newDigit + 48;
        index++;
    }
    while (carry > 0) {
        result[index] = carry % 10 + 48;
        index++;
        carry = carry / 10;
    }
    result[index] = '\0';
    for (int i = 0; i < index / 2; i++) {
        char front = result[i];
        result[i] = result[index - i - 1];
        result[index - i - 1] = front;
    }
}

int main() {
    FILE *fp;
    fp = fopen("number.txt", "r");
    if (fp == NULL) {
        printf("opening the file failed!\n");
        exit(1);
    }
    char numbers[100][52];
    for (int i = 0; i < 100; i++) {
        fgets(numbers[i], 52, fp);
        numbers[i][50] = '\0';
    }
    char sum[200];
    for (int i = 0; i < 100; i++) {
        char container[200];
        addLargeNumbers(numbers[i], sum, container);
        strcpy(sum, container);
    }
    printf("%s\n", sum);
}