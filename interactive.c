#include <stdio.h>
#include <stdlib.h>
#include <string.h>

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
           "Select a number: ");
    scanf("%d", &choice);

    printf("selected: %d\n", choice);

    stbi_image_free(image);
    return 0;
}