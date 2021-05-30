#include <math.h>
#include <stdio.h>
#include <stdlib.h>

// Kernel size
#define K_SIZE 3

// Declaration of the X and Y kernel matrices.
double GX[K_SIZE][K_SIZE] = {
    {1, 0, -1},
    {2, 0, -2},
    {1, 0, -1},
};

double GY[K_SIZE][K_SIZE] = {
    {1, 2, 1},
    {0, 0, 0},
    {-1, -2, -1},
};

int is_valid(int current_x, int current_y, int width, int height) {
    return current_x > -1 && current_x < width*2 && current_y > -1 && current_y < height*2;
}

double calculate_hyp(double a, double b) {
    return sqrt(a*a + b*b);
}

double convolve(unsigned char inp[1580*2][950*2], int px, int py,
                double kernel[K_SIZE][K_SIZE], int width, int height)
{
  int temp = px;
  px = py;
  py = temp;
  int current_x;
  int current_y;
  double sum = 0.0;
  // check up is_valid then multiply if so
  current_x = px-1;
  current_y = py;
  if (is_valid(current_x, current_y, width, height)) {
      sum += inp[current_x][current_y] * kernel[0][1];
  }
  // check down is_valid then multiply if so
  current_x = px+1;
  current_y = py;
  if (is_valid(current_x, current_y, width, height)) {
      sum += inp[current_x][current_y] * kernel[2][1];
  }
  // check left is_valid then multiply if so
  current_x = px;
  current_y = py-1;
  if (is_valid(current_x, current_y, width, height)) {
      sum += inp[current_x][current_y] * kernel[1][0];
  }
  // check right is_valid then multiply if so
  current_x = px;
  current_y = py+1;
  if (is_valid(current_x, current_y, width, height)) {
      sum += inp[current_x][current_y] * kernel[1][2];
  }
  // check left up is_valid then multiply if so
  current_x = px-1;
  current_y = py-1;
  if (is_valid(current_x, current_y, width, height)) {
      sum += inp[current_x][current_y] * kernel[0][0];
  }
  // check left down is_valid then multiply if so
  current_x = px+1;
  current_y = py-1;
  if (is_valid(current_x, current_y, width, height)) {
      sum += inp[current_x][current_y] * kernel[2][0];
  }
  // check right up is_valid then multiply if so
  current_x = px-1;
  current_y = py+1;
  if (is_valid(current_x, current_y, width, height)) {
      sum += inp[current_x][current_y] * kernel[0][2];
  }
  // check right down is_valid then multiply if so
  current_x = px+1;
  current_y = py+1;
  if (is_valid(current_x, current_y, width, height)) {
      sum += inp[current_x][current_y] * kernel[2][2];
  }
  // check center is_valid then multiply if so
  current_x = px;
  current_y = py;
  if (is_valid(current_x, current_y, width, height)) {
      sum += inp[current_x][current_y] * kernel[1][1];
  }
  return sum; // Return with the correct value
}

void sobel(unsigned char inp[1580*2][950*2], unsigned char out[1580*2][950*2], int width, int height)
{
//     printf("Here\n");
//   for (int i=0; i<width*2; i++) {
//       for (int j=0; j<height*2; j++) {
//           double g_x = convolve(inp, i, j, GX, width, height);
//           double g_y = convolve(inp, i, j, GY, width, height);
//           int colour = calculate_hyp(g_x, g_y);
//           if (colour > 255) colour = 255;
//           out[j][i] = colour;
//       }
//   }
  return; // Update `out` before returning
}
