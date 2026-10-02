#include <stdio.h>
#include <stdlib.h>
 
#define MAX_W 256       /* 画像の幅の最大 */
#define MAX_H 256       /* 画像の高さの最大 */
#define BUF 256         /* バッファサイズ */
 
/* 画像の幅，高さ，画素値を格納する外部変数 */
int w, h, i_img[MAX_W * MAX_H], o_img[MAX_W * MAX_H];
 
int read();
void write();
void superpose();
 
int main(){
	superpose();
	write();
	return 0;
}
 
/*
 * 入力されたファイル名の Plain PBM 形式画像ファイルを読み込み，
 * その幅，高さ，画素値をそれぞれ外部変数 w, h, i_img に格納する
 */
int read(){
	FILE *fp;
	char filename[BUF];
	int r;
	
	/* 必要に応じて変数宣言を追加 */
	
	printf("ファイル名を入力してください: ");
	
	if((r = scanf("%s", filename)) == EOF)
		return EOF;
		
	if((fp = fopen(filename, "r")) == NULL){
		fprintf(stderr, "ファイル %s を開けません！\n", filename);
		exit(1);
	}
	
	/* 仕様にしたがって関数を作成しなさい */
 
}
 
/*
 * 外部変数 w(幅)，h(高さ)，o_img(画素値) で与えられる画像を，
 * Plain PBM 形式でファイル out.pbm に書き出す
 */
void write(){
	/* 仕様にしたがって関数を作成しなさい */
}
 
/*
 * 画像ファイルを read 関数を用いて読み込み，
 * それらを重ね合わせてできる画像の画素値を
 * 外部変数 o_img に格納する
 */
void superpose(){
	/* 仕様にしたがって関数を作成しなさい */
}