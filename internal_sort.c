#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#include <time.h>
#include <string.h>
#include <math.h>
#define SUCCESS_OUTPUT 0
#define MIN_ITERATIONS 20
#define MAX_ITERATIONS 2000

#ifndef SIZE
#error "Where is DSIZE=..., Billy?"
#endif

#ifndef SORT
#error "Where is DSORT=..., Billy?"
#endif

void generate_array(int array[], size_t len)
{
    srand(time(0));
    for (size_t i = 0; i < len; i++)
    {
        array[i] = rand() % 100;
    }
}

void bubble_sort_1(int array[], size_t len)
{
    for (size_t i = 0; i < len - 1; i++)
    {
        for (size_t j = 0; j < len - i - 1; j++)
        {
            if (array[j] > array[j + 1])
            {
                int temp = array[j];
                array[j] = array[j + 1];
                array[j + 1] = temp;
            }
        }
    }
}

void bubble_sort_2(int *array, size_t len)
{
    for (size_t i = 0; i < len - 1; i++)
    {
        for (size_t j = 0; j < len - i - 1; j++)
        {
            if (*(array + j) > *(array + j + 1))
            {
                int temp = *(array + j);
                *(array + j) = *(array + j + 1);
                *(array + j + 1) = temp;
            }
        }
    }
}

void bubble_sort_3(int *array, size_t len)
{
    int *ptr;
    int temp;
    for (size_t i = 0; i < len - 1; i++)
    {
        ptr = array;
        for (size_t j = 0; j < len - i - 1; j++)
        {
            if (*ptr > *(ptr + 1))
            {
                // Обмен значений, используя указатели
                temp = *ptr;
                *ptr = *(ptr + 1);
                *(ptr + 1) = temp;
            }
            ptr++;
        }
    }
}

double sum_time(double time_array[], size_t count)
{
    double sum = 0;
    for (size_t i = 0; i < count; i++)
    {
        sum += time_array[i];
    }
    return sum;
}

int calc_rse(double time_array[], size_t count, double *rse)
{
    double t_avg, dispersion = 0;
    if (count <= 1)
        return -1;
    t_avg = sum_time(time_array, count) / count;

    for (size_t i = 0; i < count; i++)
    {
        dispersion += pow((time_array[i] - t_avg), 2);
    }
    dispersion /= (count - 1);
    double standard_deviation = sqrt(dispersion);
    double std_error = standard_deviation / sqrt(count);
    *rse = std_error * 100 / t_avg;
    return SUCCESS_OUTPUT;
}

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
        if (SORT == 0)
        {
            clock_gettime(CLOCK_REALTIME, &start);
            bubble_sort_1(array, SIZE);
            clock_gettime(CLOCK_REALTIME, &end);
        }
        else if (SORT == 1)
        {
            clock_gettime(CLOCK_REALTIME, &start);
            bubble_sort_2(array, SIZE);
            clock_gettime(CLOCK_REALTIME, &end);
        }
        else if (SORT == 2)
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
