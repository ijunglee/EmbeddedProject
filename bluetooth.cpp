#include <unistd.h>
#include <stdio.h>
using namespace std;

 int main()
 {
         FILE *export_file = NULL;        //declare pointers
         FILE *IO_direction = NULL;
         //char str1[] = "low";
         //char str2[] = "high";
         //char str[] = "60";                       //value to pass to export file
<<<<<<< HEAD
         char str[] = "Hello";
         export_file = fopen ("/dev/ttyO1", "w");
         fwrite (str, sizeof(char), sizeof(str), export_file);
=======
         char str[] = "BB-UART1";
         export_file = fopen ("/dev/ttyO1", "w");
         fwrite (str, 1, sizeof(str), export_file);
>>>>>>> 81a7a8945e95ad3f1f70e7caca8d31ff82178c65
         fclose (export_file);
 }
