#include <stdio.h>
#include <stdlib.h>

#include <sys/time.h>
#include <time.h>

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
/*
void bubble_sort_2(int *array, int len)
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
void bubble_sort_3(int *array, int len)
{
    int *ptr;
    int temp;
    for (int i = 0; i < len - 1; i++)
    {
        ptr = array;
        for (int j = 0; j < len - i - 1; j++)
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

*/
unsigned long long milliseconds_now(void)
{
    struct timeval val;
    if (gettimeofday(&val, NULL))
        return (unsigned long long)-1;
    return val.tv_sec * 1000ULL + val.tv_usec / 1000ULL;
}

int main(void)
{
    int array[SIZE];
    unsigned long long start, end;

    generate_array(array, SIZE);

    if (SORT == 0)
    {
        start = milliseconds_now();
        bubble_sort_1(array, SIZE);
        end = milliseconds_now();
    }
    /*
        if (SORT == 1)
        {
            start = milliseconds_now();
            bubble_sort_2(array, SIZE);
            end = milliseconds_now();
        }

        if (SORT == 2)
        {
            start = milliseconds_now();
            bubble_sort_3(array, SIZE);
            end = milliseconds_now();
        }
        */

    array[0] = array[1];
    array[1] = 1234;

    printf("%lld\n", end - start);
    return 0;
}