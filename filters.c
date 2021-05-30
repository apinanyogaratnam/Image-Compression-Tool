#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

// dark lines
void increase_shade_filter(size_t size_of_image, unsigned char *image) {
    for (long i=0; i<size_of_image; i+=9) {
        image[i] = 0;
    }

    return;
}

// red filter
void red_filter(size_t size_of_image, unsigned char *image) {
    for (long i=0; i<size_of_image; i+=3) {
        image[i] = 0;
    }

    return;
}

// empty filter
void empty_filter(size_t size_of_image, unsigned char *image) {
    for (long i=0; i<size_of_image; i++) {
        image[i] = 0;
    }

    return;
}

// green filter
void green_filter(size_t size_of_image, unsigned char *image) {
    for (long i=0; i<size_of_image; i+=2) {
        image[i] = 0;
    }

    return;
}

// blue/turquise filter
void blue_turquise_filter(size_t size_of_image, unsigned char *image) {
    for (long i=0; i<size_of_image; i+=4) {
        image[i] = 0;
    }

    return;
}

// broken screen filter
void broken_screen_filter(size_t size_of_image, unsigned char *image) {
    for (long i=0; i<size_of_image; i+=5) {
        image[i] = 0;
    }

    return;
}

// reduced opacity filter
void reduced_opacity_filter(size_t size_of_image, unsigned char *image, int opacity_level) {
    if (1 > opacity_level || opacity_level > 255) {
        printf("opacity level out of range of [1, 255]");
        return;
    }

    for (long i=0; i<size_of_image; i++) {
        image[i] = image[i] / opacity_level;
    }

    return;
}

// brighter_filter
void brighter_filter(size_t size_of_image, unsigned char *image) {
    for (long i=0; i<size_of_image; i++) {
        image[i] = image[i] * 3;
        if (image[i] >255) image[i] = 255;
    }
}

// grayscale filter
void greyscale_filter(size_t size_of_image, int width, int height, int channels, unsigned char *image) {
    unsigned char image_test[width*2][height*2];

    long count = 0;
    for (long i=0; i<width*2; i++) {
        for (long j=0; j<height*2; j++) {
            image_test[i][j] = image[count];
            count++;
        }
    }


    stbi_write_png("output.png", width, height, channels, image_test, width * channels);
}

// works well
void increase_shade_filter(size_t size_of_image, unsigned char *image);

// doesnt work well
void red_filter(size_t size_of_image, unsigned char *image);
void empty_filter(size_t size_of_image, unsigned char *image);
void green_filter(size_t size_of_image, unsigned char *image);
void blue_turquise_filter(size_t size_of_image, unsigned char *image);
void broken_screen_filter(size_t size_of_image, unsigned char *image);

// opacity level range: 1 <= opacity_level <= 255
void reduced_opacity_filter(size_t size_of_image, unsigned char *image, int opacity_level);
void brighter_filter(size_t size_of_image, unsigned char *image);
