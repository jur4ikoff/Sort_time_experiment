#include "sorts.h"

#define SUCCESS_OUTPUT 0
#define MIN_ITERATIONS 15
#define MAX_ITERATIONS 2000

#ifndef SIZE
#error "ERORR. Input DSIZE"
#endif

#ifndef SORT
#error "ERORR. Input DSORT"
#endif

// Внутренний подсчет времени выполнения программы
int main(void)
{
    int array[SIZE];
    double ticks_array[SIZE];
    double ticks, rse = 100, start, end;
    int count = 0;
    generate_array(array, SIZE);

    while ((count < MAX_ITERATIONS) && (rse > 1 || count < MIN_ITERATIONS))
    {
        generate_array(array, SIZE);
        if (SORT == 1)
        {
            start = __rdtsc();
            bubble_sort_1(array, SIZE);
            end = __rdtsc();
        }
        else if (SORT == 2)
        {
            start = __rdtsc();
            bubble_sort_2(array, SIZE);
            end = __rdtsc();
        }
        else if (SORT == 3)
        {
            start = __rdtsc();
            bubble_sort_3(array, SIZE);
            end = __rdtsc();
        }
        count++;
        ticks = end - start;
        ticks_array[count] = ticks;
        calc_rse(ticks_array, count, &rse);
        printf("%.0f\n", ticks);
    }

    return SUCCESS_OUTPUT;
}
