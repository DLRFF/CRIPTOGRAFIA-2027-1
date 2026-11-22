/*
 * Función f(R,K) de DES
 *
 *   (6)  B1 B2 ... B8 = K xor E(R)        (bloques de 6 bits)
 *   (7)  f(R,K) = P( S1(B1) S2(B2) ... S8(B8) )
 *
 * Convención: el bit 1 es el más significativo (MSB), igual que en el estándar.
 *
 * Compilar:  gcc -Wall -O2 des_f.c -o des_f
 */
#include <stdio.h>
#include <stdint.h>

/* Permutación P (32 -> 32): la de la diapositiva */
static const uint8_t P[32] = {
    16,  7, 20, 21,
    29, 12, 28, 17,
     1, 15, 23, 26,
     5, 18, 31, 10,
     2,  8, 24, 14,
    32, 27,  3,  9,
    19, 13, 30,  6,
    22, 11,  4, 25
};

/* Expansión E (32 -> 48) */
static const uint8_t E[48] = {
    32,  1,  2,  3,  4,  5,
     4,  5,  6,  7,  8,  9,
     8,  9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32,  1
};

/* Las 8 cajas S: 4 filas x 16 columnas cada una */
static const uint8_t S[8][4][16] = {
  { /* S1 */
    {14, 4,13, 1, 2,15,11, 8, 3,10, 6,12, 5, 9, 0, 7},
    { 0,15, 7, 4,14, 2,13, 1,10, 6,12,11, 9, 5, 3, 8},
    { 4, 1,14, 8,13, 6, 2,11,15,12, 9, 7, 3,10, 5, 0},
    {15,12, 8, 2, 4, 9, 1, 7, 5,11, 3,14,10, 0, 6,13}},
  { /* S2 */
    {15, 1, 8,14, 6,11, 3, 4, 9, 7, 2,13,12, 0, 5,10},
    { 3,13, 4, 7,15, 2, 8,14,12, 0, 1,10, 6, 9,11, 5},
    { 0,14, 7,11,10, 4,13, 1, 5, 8,12, 6, 9, 3, 2,15},
    {13, 8,10, 1, 3,15, 4, 2,11, 6, 7,12, 0, 5,14, 9}},
  { /* S3 */
    {10, 0, 9,14, 6, 3,15, 5, 1,13,12, 7,11, 4, 2, 8},
    {13, 7, 0, 9, 3, 4, 6,10, 2, 8, 5,14,12,11,15, 1},
    {13, 6, 4, 9, 8,15, 3, 0,11, 1, 2,12, 5,10,14, 7},
    { 1,10,13, 0, 6, 9, 8, 7, 4,15,14, 3,11, 5, 2,12}},
  { /* S4 */
    { 7,13,14, 3, 0, 6, 9,10, 1, 2, 8, 5,11,12, 4,15},
    {13, 8,11, 5, 6,15, 0, 3, 4, 7, 2,12, 1,10,14, 9},
    {10, 6, 9, 0,12,11, 7,13,15, 1, 3,14, 5, 2, 8, 4},
    { 3,15, 0, 6,10, 1,13, 8, 9, 4, 5,11,12, 7, 2,14}},
  { /* S5 */
    { 2,12, 4, 1, 7,10,11, 6, 8, 5, 3,15,13, 0,14, 9},
    {14,11, 2,12, 4, 7,13, 1, 5, 0,15,10, 3, 9, 8, 6},
    { 4, 2, 1,11,10,13, 7, 8,15, 9,12, 5, 6, 3, 0,14},
    {11, 8,12, 7, 1,14, 2,13, 6,15, 0, 9,10, 4, 5, 3}},
  { /* S6 */
    {12, 1,10,15, 9, 2, 6, 8, 0,13, 3, 4,14, 7, 5,11},
    {10,15, 4, 2, 7,12, 9, 5, 6, 1,13,14, 0,11, 3, 8},
    { 9,14,15, 5, 2, 8,12, 3, 7, 0, 4,10, 1,13,11, 6},
    { 4, 3, 2,12, 9, 5,15,10,11,14, 1, 7, 6, 0, 8,13}},
  { /* S7 */
    { 4,11, 2,14,15, 0, 8,13, 3,12, 9, 7, 5,10, 6, 1},
    {13, 0,11, 7, 4, 9, 1,10,14, 3, 5,12, 2,15, 8, 6},
    { 1, 4,11,13,12, 3, 7,14,10,15, 6, 8, 0, 5, 9, 2},
    { 6,11,13, 8, 1, 4,10, 7, 9, 5, 0,15,14, 2, 3,12}},
  { /* S8 */
    {13, 2, 8, 4, 6,15,11, 1,10, 9, 3,14, 5, 0,12, 7},
    { 1,15,13, 8,10, 3, 7, 4,12, 5, 6,11, 0,14, 9, 2},
    { 7,11, 4, 1, 9,12,14, 2, 0, 6,10,13,15, 3, 5, 8},
    { 2, 1,14, 7, 4,10, 8,13,15,12, 9, 0, 3, 5, 6,11}}
};

/*
 * Permuta bits: el bit i de la salida (i = 1..n_out, desde el MSB) es el bit
 * table[i-1] de la entrada (de n_in bits, también numerado desde el MSB).
 * Ej.: con P, el bit 16 de L pasa a ser el bit 1 de P(L).
 */
static uint64_t permute(uint64_t in, int n_in, const uint8_t *table, int n_out)
{
    uint64_t out = 0;
    for (int i = 0; i < n_out; i++) {
        uint64_t bit = (in >> (n_in - table[i])) & 1u;
        out = (out << 1) | bit;
    }
    return out;
}

/* P(L): permutación de 32 bits */
uint32_t des_P(uint32_t L)
{
    return (uint32_t)permute(L, 32, P, 32);
}

/* f(R,K): R de 32 bits, K de 48 bits (en los 48 bits bajos de un uint64_t) */
uint32_t des_f(uint32_t R, uint64_t K)
{
    /* (6) B1..B8 = K xor E(R) */
    uint64_t B = K ^ permute(R, 32, E, 48);

    /* S1(B1)...S8(B8): 8 bloques de 6 bits -> 8 nibbles de 4 bits */
    uint32_t s_out = 0;
    for (int i = 0; i < 8; i++) {
        uint8_t six = (B >> (42 - 6 * i)) & 0x3F;          /* Bi */
        int row = ((six & 0x20) >> 4) | (six & 0x01);      /* bits 1 y 6 */
        int col = (six >> 1) & 0x0F;                       /* bits 2..5  */
        s_out = (s_out << 4) | S[i][row][col];
    }

    /* (7) P(S1(B1)...S8(B8)) */
    return des_P(s_out);
}

/* Imprime n bits en grupos de 4 */
static void print_bits(const char *label, uint64_t v, int n)
{
    printf("%-10s ", label);
    for (int i = n - 1; i >= 0; i--) {
        putchar(((v >> i) & 1) ? '1' : '0');
        if (i % 4 == 0 && i) putchar(' ');
    }
    putchar('\n');
}

int main(void)
{
    /* Vector de prueba (ejemplo clásico "DES Algorithm Illustrated"):
     * R0 = 1111 0000 1010 1010 1111 0000 1010 1010
     * K1 = 000110 110000 001011 101111 111111 000111 000001 110010
     * f(R0,K1) esperado = 0010 0011 0100 1010 1010 1001 1011 1011
     */
    uint32_t R = 0xF0AAF0AA;
    uint64_t K = 0x1B02EFFC7072ULL;
    uint32_t esperado = 0x234AA9BB;

    uint32_t r = des_f(R, K);

    print_bits("R",        R, 32);
    print_bits("K",        K, 48);
    print_bits("E(R)",     permute(R, 32, E, 48), 48);
    print_bits("f(R,K)",   r, 32);
    print_bits("esperado", esperado, 32);
    printf("%s\n", r == esperado ? "OK: coincide" : "ERROR: no coincide");

    /* Prueba de P: el bit 16 de L debe ser el bit 1 de P(L) */
    uint32_t L = 1u << (32 - 16);               /* solo el bit 16 encendido */
    printf("P(bit16) = 0x%08X (esperado 0x80000000)\n", des_P(L));

    return r == esperado ? 0 : 1;
}
