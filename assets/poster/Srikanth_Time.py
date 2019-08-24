if __name__ == "__main__":
    n=int(input())
    while(n>=1):
        t1=input()
        t2=input()
        h1,m1=[int(o) for o in t1.split(':')]
        h2,m2=[int(o) for o in t2.split(':')]
        if(h1>=24 or m1>=60 or h2>=24 or m2>=60):
            print("Invalid Input")
        else:
            if(h1*60 + m1 < h2*60 + m2):
                h1,h2=h2,h1
                m1,m2=m2,m1
            res_hour = h1-h2
            res_min = m1-m2
            if(res_min<0):
                res_hour-=1
                res_min+=60
            hour=str(res_hour)
            minute=str(res_min)
            if(res_hour<10):
                hour='0'+hour
            if(res_min<10):
                minute='0'+minute
            print(hour+":"+minute)
        n=n-1
