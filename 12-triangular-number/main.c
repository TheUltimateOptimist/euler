#include "math.h"
#include "stdio.h"
#include "time.h"

long long firstNum(int moreThan) {
    long long number = 0;
    long long delta = 1;
    while (1) {
        number = number + delta;
        double num_sqrt = sqrt(number);
        delta++;
        int count = 0;
        for (long long i = 1; i < num_sqrt; i++) {
            if (number % i == 0) {
                count++;
            }
        }
        count = 2*count;
        if (number == num_sqrt / 1) {
            count++;
        }
        if (count > moreThan) {
            return number;
        }
    }
}

int main() {
    clock_t start = clock();
    long long result = firstNum(500);
    clock_t end = clock();
    printf("time taken: %f\n", ((double) (end - start)) / CLOCKS_PER_SEC);
}