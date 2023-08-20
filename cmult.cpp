#include <stdlib.h>
#include <iostream>


extern "C"
float cmult(int int_param, float float_param){
    float return_value = int_param * float_param;
    std::cout << "In cmult: int " << int_param << " float " << float_param << " returning " << return_value<< std::endl; 
    return return_value;
}

// int main(){
//     return 0;
// }