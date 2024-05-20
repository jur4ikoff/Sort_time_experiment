#include "sorts.h"
#ifndef SIZE
#error "ERORR. Input DSIZE"
#endif

#ifndef SORT
#error "ERORR. Input DSORT"
#endif

int main(void)
{
    int array[SIZE];
    struct timespec start, end;
    double time;

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

    time = (end.tv_sec - start.tv_sec) * 1e9 + (end.tv_nsec - start.tv_nsec);
    printf("%f\n", time);
    return SUCCESS_OUTPUT;
}
