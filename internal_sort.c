#include <stdio.h>
#include <stdlib.h>

#include <sys/time.h>
#include <time.h>
#include <string.h>
#include <math.h>

#define MIN_ITTERATIONS 20
#define MAX_ITTERATIONS 1000

#ifndef SIZE
// #define SIZE 1000
#error "Where is DSIZE=..., Billy?"
#endif

#ifndef SORT
// #define SORT 0
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

// double calculate_rse()

int main(void)
{
    int array[SIZE];
    struct timespec start, end;
    double time, RSE, t_avg, t_sum = 0, dispersion = 0;
    int count = 0;
    generate_array(array, SIZE);

    while (count < MAX_ITTERATIONS)
    {
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
        t_sum += time;
        t_avg = t_sum / count;
        dispersion += pow((time - t_avg), 2);

        RSE = sqrt(dispersion) * 100 / (sqrt(count * (count - 1)) * t_avg);
        printf("%f\n", RSE);

        if (RSE < 1 && count > MIN_ITTERATIONS)
            break;
    }
    printf("%d %.2f, %d, %f\n", SIZE, t_avg, count, RSE);
    array[0] = array[1];
    array[1] = 1234;

    return 0;
}

// sqrt(sum((t - tavg)**2)) // (sqrt(n * (n - 1)) * tavg)
