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
    char filename[1024] = "";
    printf("Name of image you would like to open: ");
    fgets(filename, 1024, stdin);
    filename[strlen(filename)-1] = 0;

    int width, height, channels;
    unsigned char *image = stbi_load(filename, &width, &height, &channels, 0);
    size_t size_of_image = width * height * channels;
    
    if (!image) {
        printf("Invalid image name or unable to load image.\n");
        return 1;
    }

    int choice;
    printf("Filter options: \n" \
           "1. Dark lines filter\n" \
           "2. Red filter\n" \
           "3. Empty filter\n" \
           "4. Green filter\n" \
           "5. Blue turquise filter\n" \
           "6. Broken screen filter\n" \
           "7. Reduced opacity filter\n" \
           "8. Dark lines filter\n" \
           "9. Exit program\n"
           "10. Grey Filter\n"
           "Select a number: ");
    scanf("%d", &choice);
    getchar();

    printf("selected: %d\n", choice);

    int opacity_level;
    bool repeat = true;
    bool exit = false;
    while (repeat) {
        switch (choice) {
            case 1:
                increase_shade_filter(size_of_image, image);
                repeat = false;
                break;
            case 2:
                red_filter(size_of_image, image);
                repeat = false;
                break;
            case 3:
                empty_filter(size_of_image, image);
                repeat = false;
                break;
            case 4:
                green_filter(size_of_image, image);
                repeat = false;
                break;
            case 5:
                blue_turquise_filter(size_of_image, image);
                repeat = false;
                break;
            case 6:
                broken_screen_filter(size_of_image, image);
                repeat = false;
                break;
            case 7:
                printf("Enter opacity level: ");
                scanf("%d", &opacity_level);
                getchar();
                reduced_opacity_filter(size_of_image, image, opacity_level);
                repeat = false;
                break;
            case 8:
                brighter_filter(size_of_image, image);
                repeat = false;
                break;
            case 9:
                exit = true;
                repeat = false;
                break;
            case 10:
                repeat = false;
                exit = true;
                greyscale_filter(size_of_image, width, height, channels, image);
            default:
                printf("Incorrect input.\n");
                repeat = true;
                break;
        }
    }

    if (exit) return 1;
    stbi_write_png("output_file.png", width, height, channels, image, width * channels);
    stbi_image_free(image);
    return 0;
}