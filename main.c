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

    stbi_write_png("sky2.png", width, height, channels, image, width * channels);
    stbi_write_png("sky.jpg", width, height, channels, image, width * channels);
    stbi_write_png("sky2.jpg", width, height, channels, image, width * channels);

    size_t image_size = width * height * channels;
    for (long i=0; i<image_size; i++) {
        if (image[i] != 254 && image[i] != 255) {
            printf("%d\n", image[i]);
        }
    }

    stbi_image_free(image);
    return 0;
}
