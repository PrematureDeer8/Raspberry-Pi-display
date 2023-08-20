#include <iostream>

class Geek{
    public:
        void myFunction(){
            std::cout << "Hello Geek" << std::endl;
        }
};
extern "C" {
    Geek* geek = new Geek();
    void Geek_myfunction(Geek* geek){
        geek->myFunction();
    }
}