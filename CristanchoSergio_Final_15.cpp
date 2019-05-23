#include <fstream>
#include <iostream>

float Ex (float t){
    return 0;
}

float Ey (float t){
    if (t<3){
        return 0;
    }
    else if ((3<t)&&(t<7)){
        return 3;
    }
    else{
        return 0;
    }
}

int main(){
    float q = 2;
    float m = 7294.29;
    float dt = 0.1;
    float x = 1;
    float y = 0;
    float vx = 0;
    float vy = 1;
    std::ofstream outfile;
    outfile.open("Datos15.dat");
    outfile<<0<<","<<x<<","<<y<<std::endl;
    
    for(int i=1; i< 100; i++){
        vxh = vx + (dt/2)*(q/m)*Ex(i*dt);
        vyh = vy + (dt/2)*(q/m)*Ey(i*dt);
        x = x + dt*vxh;
        y = y + dt*vyh;
        vx = vxh + (dt/2)*(q/m)*Ex((i+1)*dt);
        vy = vyh + (dt/2)*(q/m)*Ey((i+1)*dt);
        outfile<<i*dt<<","<<x<<","<<y<<std::endl;
    }
    return 0;
}
        
        
        
        
    
    