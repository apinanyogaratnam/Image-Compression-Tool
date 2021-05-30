#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

# define STB_IMAGE_IMPLEMENTATION
#include "stb_image/stb_image.h"
#define STB_IMAGE_WRITE_IMPLEMENTATION
#include "stb_image/stb_image_write.h"

#include "filters.c"

int main() {
    int width, height, channels;
    unsigned char *image = stbi_load("sky.png", &width, &height, &channels, 0);
    if (!image) {
        printf("Image failed to load.\n");
        return 1;
    }

    printf("Loaded Image with a width of %dpx, a height of %dpx and %d channels.\n", width, height, channels);
    size_t size_of_image = width * height * channels;



    unsigned char image_test[width*2][height*2];

    long count = 0;
    for (long i=0; i<width*2; i++) {
        for (long j=0; j<height*2; j++) {
            image_test[i][j] = image[count];
            count++;
        }
    }
    
    stbi_write_png("output.png", width, height, channels, image_test, width * channels);




    // stbi_write_png("sky.jpg", width, height, channels, image, width * channels);
    // stbi_write_png("sky2.jpg", width, height, channels, image, width * channels);

    stbi_image_free(image);
    return 0;
}
