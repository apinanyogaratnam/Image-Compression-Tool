#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

# define STB_IMAGE_IMPLEMENTATION
#include "stb_image/stb_image.h"
#define STB_IMAGE_WRITE_IMPLEMENTATION
#include "stb_image/stb_image_write.h"

int main() {
    int width, height, channels;
    unsigned char *image = stbi_load("sky.png", &width, &height, &channels, 0);
    if (!image) {
        printf("Image failed to load.\n");
        return 1;
    }

    printf("Loaded Image with a width of %dpx, a height of %dpx and %d channels.\n", width, height, channels);

    size_t image_size = width * height * channels;
    for (long i=0; i<image_size-9; i+=9) {
        int one = image[i];
        int two = image[i+1];
        int three = image[i+2];
        int four = image[i+2];
        int five = image[i+2];
        int six = image[i+2];
        int seven = image[i+2];
        int eight = image[i+2];
        int nine = image[i+2];
        int ten = image[i+2];
        int average = (one + two + three + four + five + six + seven + eight + nine + ten) / 10;
        image[i] = 0;
    }

    stbi_write_png("sky2.png", width, height, channels, image, width * channels);
    // stbi_write_png("sky.jpg", width, height, channels, image, width * channels);
    // stbi_write_png("sky2.jpg", width, height, channels, image, width * channels);

    stbi_image_free(image);
    return 0;
}
