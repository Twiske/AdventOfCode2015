#include <stdio.h>


int main()
{
  int floor = 0;
  int index = 0;
  while(1)
  {
    char paren = getchar();
    
    switch(paren)
    {
      case ')':
        index++;
        floor--;
        break;
      case '(':
        index++;
        floor++;
        break;
      case EOF:
        return;
    }
    if (floor < 0)
    {
      printf("%d\n", index);
      return;
    }
    //printf("%d\n", floor);
  }
}
