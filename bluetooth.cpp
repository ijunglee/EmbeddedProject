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
         char str[] = "BB-UART1"
         export_file = fopen ("/sys/devices/bone_capemgr.*/slots", "w");
         fwrite (str, 1, sizeof(str), export_file);
         fclose (export_file);
 }
