#include <bits/stdc++.h>
using namespace std;
int main()
{
    string str = "Mewa wa mey twsam iepjoys gt mey ipbya. Pa xgn iph ayy, meysy wa hgmewhr gt whmysyam wh mey iepjoys.Agjy gt mey kpmys iepjoysa vwkk oy jgsy whmysyamwhr meph mewa ghy !Mey iguy nayu tgs mewa jyaapry wa p awjfky anoamwmnmwgh iwfeys wh vewie uwrwma epby oyyh aewtmyu ox 8 fkpiya.Mey fpaavgsu wa \"mxSrN03uwdd\" vwmegnm mey dngmya.";
    char c = 'a', C = 'A';
    int ct;
    for (int j = 0; j < 26; j++)
    {
        ct = 0;
        for (int i = 0; str[i] != '\0'; i++)
        {
            if (str[i] == c + j || str[i] == C + j)
            {
                ct++;
            }
        }
        cout << char(c + j) << ":" << ct << endl;
    }
    char a, A;
    vector<int> k(str.size());
    while (true)
    {
        cout << "letter to be substituted:" << endl;
        cin >> a;
        A = a - 'a' + 'A';
        char s;
        cout << "letter substituted by:" << endl;
        cin >> s;
        for (int i = 0; str[i] != '\0'; i++)
        {
            if (str[i] == a && k[i] == 0)
            {
                str[i] = s;
                k[i] = 1;
            }
            if (str[i] == A && k[i] == 0)
            {
                str[i] = s - 'a' + 'A';
                k[i] = 1;
            }
            cout << str[i];
        }
        cout << endl;
    }
    return 0;
}
