#ifndef SORTS
#define SORTS
#define SUCCESS_OUTPUT 0

#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#include <time.h>
#include <string.h>
#include <math.h>
#include <x86gprintrin.h>

void generate_array(int array[], size_t len);
void bubble_sort_1(int array[], size_t len);
void bubble_sort_2(int *array, size_t len);
void bubble_sort_3(int *array, size_t len);
double sum_time(double time_array[], size_t count);
int calc_rse(double time_array[], size_t count, double *rse);
#endif
