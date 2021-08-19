#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

#define COLOR_NUM (4)
#define COLOR_NAME (0x20)
#define COLOR_COMPONENT (0x4d8)

struct palette {
    char color[COLOR_NAME];
    char ingredient[COLOR_COMPONENT];
}*your_palette[COLOR_NUM];

long secret_button = 0;

void welcome()
{
    puts("    ____              __           __     __        ");
    puts("   / __ \\   ____ _   / /  ___     / /_   / /_   ___ ");
    puts("  / /_/ /  / __ `/  / /  / _ \\   / __/  / __/  / _ \\");
    puts(" / ____/  / /_/ /  / /  /  __/  / /_   / /_   /  __/");
    puts("/_/       \\__,_/  /_/   \\___/   \\__/   \\__/   \\___/ ");
    puts("\n");
}

void prepare()
{
    welcome();
    setvbuf(stdin, 0LL, 2, 0LL);
    setvbuf(stdout, 0LL, 2, 0LL);
    memset(your_palette, 0, (COLOR_NUM * sizeof(struct palette*)));
}



void choose_action(int *choice)
{
    puts("Now you can take on one of the following actions:");
    puts("1 : squeeze some pigment to the palette");
    puts("2 : wash one color out of the palette");
    puts("3 : display one color");
    puts("4 : change one color's component");
    puts("5 : inspect the palette");
    puts("Now give me your chocie:");
    scanf("%d", choice);
}

void make_component(char* ptr, int len)
{
    if (0 == len) {
        return;
    }
    char c;
    int i = 0;
    while ( i < len ) {
        read(0, &c, 1);
        if ( c == '\n' ) {
            ptr[i] = 0;
            return;
        }
        ptr[i++] = c;
    }
    ptr[i] = 0;
}

void squeeze()
{
    int i;
    struct palette* tmp;
    for(i = 0; i < COLOR_NUM; i++) {
        if (!your_palette[i]) {
            puts("Found some free space for you!");
            break;
        }
    }
    if (i == COLOR_NUM) {
        puts("Your palette is full :(");
        exit(0);
    }
    tmp = malloc(sizeof(struct palette));
    if (!tmp) {
        puts("Sorry but something wrong with your palette :(");
        exit(0);
    }
    puts("Now you are squeezing some pigment into the palette...");
    puts("Please name youe color:");
    make_component(tmp->color, COLOR_NAME);
    puts("Please add some ingredients:");
    make_component(tmp->ingredient, COLOR_COMPONENT);
    printf("Finished! You've squeezed something into %d slot",i);
    your_palette[i] = tmp;
}

void wash()
{
    int index;
    puts("Now input the color index:");
    scanf("%d", &index);
    index--;

    if (0 <= index && index < COLOR_NUM) {
        if (your_palette[index]) {
            free(your_palette[index]);
            your_palette[index] = NULL;
            puts("Finish!");
            return;
        } else {
            puts("Maybe you are willing to wash the palette...");
            puts("But it is clean!");
            exit(0);
        }
    }  else {
        puts("Your palette is not as large as you imagine...");
        exit(0);
    }
}

void display()
{
    int index;
    puts("Now input the color index:");
    scanf("%d", &index);
    index--;

    if (0 <= index && COLOR_NUM > index) {
        if (your_palette[index]) {
            printf("Color name: %s\n", your_palette[index]->color);
            printf("Color ingredients: %s\n", your_palette[index]->ingredient);
            puts("Finished!");
            return;
        } else {
            puts("Maybe you are willing to display your work...");
            puts("But you should squeeze first!");
            exit(0);
        }
    } else {
        puts("Your palette is not as large as you imagine...");
        exit(0);
    }
}

void mix()
{
    int index;
    puts("Now input the color index:");
    scanf("%d", &index);
    index--;

    if (0 <= index && index < COLOR_NUM) {
        if (your_palette[index]) {
            struct palette* ddl_ptr = your_palette[index];
            puts("Please name youe color:");
            make_component(ddl_ptr->color, COLOR_NAME);
            puts("Please add some ingredients:");
            make_component(ddl_ptr->ingredient, COLOR_COMPONENT);
            puts("Finished!");
            return;
        } else {
            puts("Maybe you are willing to mix some color...");
            puts("But you should squeeze first!");
            exit(0);
        }
    } else {
        puts("Your palette is not as large as you imagine...");
        exit(0);
    }
}

void insepct()
{
    if (secret_button) {
        puts("You've successfully broken the palette >_< ");
        system("/bin/sh");
    }
    else {
        puts("You can explore your palette futher more :) ");
    }
    exit(0);
}

int main()
{
    int choice = 0;
    prepare();

    while(1) {
        choose_action(&choice);
        switch (choice) {
            case 1:
                squeeze();
                break;
            case 2:
                wash();
                break;
            case 3:
                display();
                break;
            case 4:
                mix();
                break;
            case 5:
                insepct();
                break;
            default:
                puts("Nah... You just cannot do this :( ");
                exit(0);
        }
    }
    return 0;
}