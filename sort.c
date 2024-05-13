#include <stdio.h>


#ifndef SIZE
#error "Where is DSIZE=..., Billy?"
#endif

#ifndef SORT
#error "Where is DSORT=..., Billy?"
#endif


int main(void)
{
    printf("%d %d", SIZE, SORT);
    return 0;
}