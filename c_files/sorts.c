#include "sorts.h"

// Генерация массива случайных чисел
void generate_array(int array[], size_t len)
{
    srand(time(0));
    for (size_t i = 0; i < len; i++)
    {
        array[i] = rand() % 100;
    }
}

// Пузырьковая сортировка с использованием индексов
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

// Пузырьковая сортировка с использованием формальной замены индексов
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

// Пузырьковая сортировка с использованием указателей
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

// Получения суммы значений массива
double sum_time(double time_array[], size_t count)
{
    double sum = 0;
    for (size_t i = 0; i < count; i++)
    {
        sum += time_array[i];
    }
    return sum;
}

// Подсчет RSE
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
