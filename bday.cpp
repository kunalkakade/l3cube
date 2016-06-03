#include<bits/stdc++.h>
#include<math.h>
#include<iostream>
using namespace std;
int main()
{
int n;
int nfp;
cout<<"enter number";
cin>>n;
nfp=(n*(n-1))/2;

cout<<nfp<<endl;
float p1=(float)364/365;

cout<<p1<<endl;
double mul=1;
for(int i=0;i<nfp;i++)
{
mul=mul*p1;
}

cout<<mul<<endl;
double p3=1-mul;

cout<<p3<<endl;
int nofdays[365]={0};
int bday[n];
for(int i=0;i<n;i++)
{
bday[i] = rand() % 365 + 1;
cout<<bday[i]<<endl;
nofdays[bday[i]-1]+=1;
}
cout<<"************************************************************************************************************************";
for(int i=0;i<365;i++)
{
if(nofdays[i]>1)
{
cout<<i+1<<"\t"<<nofdays[i]<<endl;
}
}
return 0;
}
