#include <iostream>
#include <string>

int main(){
	int playerLife;//ライフの数
	std::string playerLifeColor;//ライフの色名
	
	std::cin >> playerLife;

	if(playerLife >= 3){
		playerLifeColor = "Blue";
	}else if(playerLife == 2){
		playerLifeColor = "Yellow";
	}else{
		playerLifeColor = "Red";
	}
	
	std::cout << playerLifeColor << std::endl;
	
	return 0;
}