#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

# define STB_IMAGE_IMPLEMENTATION
#include "stb_image/stb_image.h"
#define STB_IMAGE_WRITE_IMPLEMENTATION
#include "stb_image/stb_image_write.h"

#include "filters.c"
#include "edge_detection.c"

#include <math.h>
#include <stdio.h>
#include <stdlib.h>

void writePGM(const char *filename, unsigned char *data, int SIZEX, int SIZEY) {
  /**
   * Output a PGM image given the pixel data at the given filename. If the file
   * already exists it will be overwritten. The image array should be of size
   * SIZEY x SIZEX
   */

  FILE *f = fopen(filename, "wb");
  if (f != NULL) {
    // Write the header for the PGM file
    fprintf(f, "P5\n%d %d\n255\n", SIZEX, SIZEY);
    // Write the pixel data to the file
    fwrite(data, SIZEX * SIZEY * sizeof(unsigned char), 1, f);
    fclose(f);
  }
}

void readPGM(const char *filename, unsigned char *data, int SIZEX, int SIZEY) {
  /**
   * Read in a PGM file with a given file name, and return the pixel data
   * array (data) only if the input image size matches sx and sy.
   */

  char buffer[1024];
  int sx, sy;

  FILE *f = fopen(filename, "rb+");
  if (f == NULL) {
    printf("Unable to open %s. Make sure the path is correct\n", filename);
    exit(1);
  }
  fgets(buffer, 1024, f);
  if (strcmp(buffer, "P5\n")) {
    printf("%s is not a valid input PGM file.\n", filename);
    fclose(f);
    exit(1);
  }
  // Skip over comments
  do {
    fgets(buffer, 1024, f);
  } while (buffer[0] == '#');
  // Read the file size from the image into sx and sy
  sscanf(buffer, "%d %d\n", &sx, &sy);
  if (sx != SIZEX || sy != SIZEY) {
    printf("PGM image does not match expected size.\n");
    fclose(f);
    exit(1);
  }
  // Read the remaining header line
  fgets(buffer, 1024, f); 
  // Read the image data into the given array.
  fread(data, sx * sy * sizeof(unsigned char), 1, f);
  fclose(f);
  return;
}

int main() {
    unsigned char data[3024][4032];
    unsigned char edge[3024][4032];

    readPGM("apishan.jpg", &data[0][0], 3024, 4032);
    writePGM("output.png", &data[0][0], 3024, 4032);
}
