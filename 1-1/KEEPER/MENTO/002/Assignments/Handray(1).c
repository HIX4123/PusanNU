int main(void) {
    int var1 = 3, var2 = 15, var3 = var2;
    var3 = var1;
    var2 = var1 - 1;
    var2 += 3;
    char *var6 = "hello world", *var8 = var6;
    var8 = "hihi";
    int var9 = 0xdeadbeef;
    var9 = 0x10000000;
    return 0;
}