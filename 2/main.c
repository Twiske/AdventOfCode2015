#include <stdio.h>


int main()
{
  int totalArea = 0;
  int totalLength = 0;
  while(1)
  {
   int width, length, height;

   if (3 != scanf("%dx%dx%d\n", &width, &length, &height))
   {
     break;
   }

   int area1 = width*length;
   int area2 = width*height;
   int area3 = length*height;

   int minArea = area1;
   if (area2 < minArea) minArea = area2;
   if (area3 < minArea) minArea = area3;

   totalArea += 2*(area1 + area2 + area3) + minArea;


   int perimeter1 = 2*(width+length);
   int perimeter2 = 2*(width+height);
   int perimeter3 = 2*(length+height);
   int minPerimeter = perimeter1;
   if (perimeter2 < minPerimeter) minPerimeter = perimeter2;
   if (perimeter3 < minPerimeter) minPerimeter = perimeter3;

   totalLength += minPerimeter + width * length * height;

  }

  printf("%d, %d\n", totalArea, totalLength);
}
