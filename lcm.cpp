#include<iostream>
#include<string.h>
#include<algorithm>
using namespace std;
int main()
{
    string t,p,qw;
    char a,b;
    int i=0,j=0,k,count=0,max=0,z=0,temp,m;
    cin>>t;
    k=t.length();
    while(i<k){
        a=t[i];
        z=i;
        while(t[z]==t[i])
            z++;
        b=t[z];
        count=0;
        j=i;
        while((t[j]==a||t[j]==b) && j<k){
            count++;
            cout<<t[j];
            j++;
        }
        m=j-count;
        if(max<=count)
        {
          max=count;
          temp=m;
        }
        cout<<temp<<"\n";
        i++;
        
    }
    cout<<temp;
    qw=t.substr(temp,max);
    cout<<max<<"\n"<<temp;
    cout<<qw;
}
