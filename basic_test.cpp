#include "lsm9ds0.h"
#include <math.h>
#include <iostream>
#include <unistd.h>
#include <cstdlib>

#define LSM9DS0_XM  0x1D // Would be 0x1E if SDO_XM is LOW
#define LSM9DS0_G   0x6B // Would be 0x6A if SDO_G is LOW
#define PI 3.1415926

using namespace std;

LSM9DS0 dof(1, LSM9DS0_G, LSM9DS0_XM);

// Here's a fun function to calculate your heading, using Earth's
// magnetic field.
// It only works if the sensor is flat (z-axis normal to Earth).
// Additionally, you may need to add or subtract a declination
// angle to get the heading normalized to your location.
// See: http://www.ngdc.noaa.gov/geomag/declination.shtml
void printHeading(float hx, float hy)
{
  float heading;

  if (hy > 0)
  {
    heading = 90 - (atan(hx / hy) * (180 / PI));
  }
  else if (hy < 0)
  {
    heading = - (atan(hx / hy) * (180 / PI));
  }
  else // hy = 0
  {
    if (hx < 0) heading = 180;
    else heading = 0;
  }

  cout << "Heading: " << heading << endl;
  //Serial.println(heading, 2);
}

// Another fun function that does calculations based on the
// acclerometer data. This function will print your LSM9DS0's
// orientation -- it's roll and pitch angles.
void printOrientation(float x, float y, float z)
{
  float pitch, roll;

  pitch = atan2(x, sqrt(y * y) + (z * z));
  roll = atan2(y, sqrt(x * x) + (z * z));
  pitch *= 180.0 / PI;
  roll *= 180.0 / PI;

  cout << "Pitch, Roll: " << pitch << ", "<< roll << endl;
/*
  Serial.print("Pitch, Roll: ");
  Serial.print(pitch, 2);
  Serial.print(", ");
  Serial.println(roll, 2);
  */
}

int main() {
  int status = dof.begin();
  cout << "Status: " << status << endl;
	while (1) {
		// To read from the accelerometer, you must first call the
		// readAccel() function. When this exits, it'll update the
		// ax, ay, and az variables with the most current data.
		float ax, ay, az, gx, gy, gz, mx, my, mz;
		dof.readAccel();

		// Now we can use the ax, ay, and az variables as we please.
		// Either print them as raw ADC values, or calculated in g's.
		
		// If you want to print calculated values, you can use the
		// calcAccel helper function to convert a raw ADC value to
		// g's. Give the function the value that you want to convert.
		ax = dof.calcAccel(dof.ax);
		ay = dof.calcAccel(dof.ay);
		az = dof.calcAccel(dof.az);

		cout << "A: " << ax << ", " << ay << ", " << az << endl;
		
		dof.readGyro();

		// Now we can use the gx, gy, and gz variables as we please.
		// Either print them as raw ADC values, or calculated in DPS.
		gx = dof.calcGyro(dof.gx);
		gy = dof.calcGyro(dof.gy);
		gz = dof.calcGyro(dof.gz);

		cout << "G: " << gx << ", " << gy << ", " << gz <<endl;

		dof.readMag();
		
		// Now we can use the mx, my, and mz variables as we please.
		// Either print them as raw ADC values, or calculated in Gauss.
		mx = dof.calcMag(dof.mx);
		my = dof.calcMag(dof.my);
		mz = dof.calcMag(dof.mz);

		cout << "M: " << mx << ", " << my << ", " << mz <<endl;

		// If you want to print calculated values, you can use the
		// calcMag helper function to convert a raw ADC value to
		// Gauss. Give the function the value that you want to convert.
		printOrientation(ax, ay, az);
		//dof.readTemp();
		//cout << "T: " << (21.0 + (float)dof.temperature/8.) << endl;
		sleep(0.5);
		system("clear");
	}
}
