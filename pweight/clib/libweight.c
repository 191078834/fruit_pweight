#include <stdio.h>
#include <unistd.h>
#include <wiringPi.h>

int SCK=15;
int SDA=16;

float coefficient = 109.28726;
unsigned long calibration;

void init_pin(int SDA_PORT, int SCK_PORT)
{
    SCK=SCK_PORT;
    SDA=SDA_PORT;
    pinMode(SCK,OUTPUT);
    pinMode(SDA,INPUT);
    pullUpDnControl(SDA,PUD_UP);
}
int get_SDAPORT(void)
{
    return SDA;
}
int get_SCKPORT(void)
{
    return SCK;
}
int get_coefficient(void)
{
    return coefficient;
}
int set_coefficient(int new)
{
    return coefficient=new;
}
int get_calibration(void)
{
    return calibration;
}
int set_calibration(int new)
{
    return calibration=new;
}
unsigned long get_hx711_value(void)
{
    int i;
    unsigned long value;
    digitalWrite(SCK,LOW);        //使能AD
    while(digitalRead(SCK));
    value = 0;                    //数值
    while(digitalRead(SDA));        //AD转换未结束则等待。
    usleep(1);
    for(i=0;i<24;i++){
        digitalWrite(SCK,HIGH);
        while(0 == digitalRead(SCK))usleep(1);
        value<<=1;
        digitalWrite(SCK,LOW);
        while(digitalRead(SCK));
        if(digitalRead(SDA))
            value++;
    }
    digitalWrite(SCK,HIGH);
    value=value^0x800000;
    digitalWrite(SCK,LOW);

    return value;
}

unsigned long get_average_value(unsigned int count)
{
    unsigned int i;
    unsigned long value=0;
    for(i=0;i<count;i++){
        value += get_hx711_value();
        usleep(200000);
    }
    return value/count;
}
int init_weight(int SDA_PORT, int SCK_PORT)
{
    if(wiringPiSetup()==-1)
        return 1;
    printf("wiring setup finished.\n");
    init_pin(SDA_PORT, SCK_PORT);
    printf("init pin finished\n");
    usleep(200000);
    calibration=get_average_value(5);
    printf("calibration:%8lx \n", calibration);
    usleep(200000);
    return 0;
}
unsigned int get_weight(void)
{
    long weight;
    unsigned long value;
    value = get_hx711_value();
    weight = ((float)value-calibration)/coefficient;
    //printf("value:%8lx, 重量为：%d g\n", value, weight);
    return weight;
}

