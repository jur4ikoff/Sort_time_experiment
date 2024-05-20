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

// Внутренний подсчет для тиков
int main(void)
{
    int array[SIZE];
    double time_array[SIZE];
    struct timespec start, end;
    double time, rse = 100;
    int count = 0;
    generate_array(array, SIZE);

    while ((count < MAX_ITERATIONS) && (rse > 1 || count < MIN_ITERATIONS))
    {
        generate_array(array, SIZE);
        if (SORT == 1)
        {
            clock_gettime(CLOCK_REALTIME, &start);
            bubble_sort_1(array, SIZE);
            clock_gettime(CLOCK_REALTIME, &end);
        }
        else if (SORT == 2)
        {
            clock_gettime(CLOCK_REALTIME, &start);
            bubble_sort_2(array, SIZE);
            clock_gettime(CLOCK_REALTIME, &end);
        }
        else if (SORT == 3)
        {
            clock_gettime(CLOCK_REALTIME, &start);
            bubble_sort_3(array, SIZE);
            clock_gettime(CLOCK_REALTIME, &end);
        }
        count++;
        time = (double)((end.tv_sec - start.tv_sec) * 1e9 + (end.tv_nsec - start.tv_nsec));
        time_array[count] = time;
        calc_rse(time_array, count, &rse);
        printf("%f\n", time);
    }

    return SUCCESS_OUTPUT;
}
