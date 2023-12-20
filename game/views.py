from django.shortcuts import render
# code='a' n=0 q=0 cors=-1
def main(request):
    return render(request,"main.html") 

def game(request):
    if request.method=="POST":
        with open('data.txt', 'r') as file:
            code = file.readline().strip()
            n = int(file.readline().strip())
            q = int(file.readline().strip())
            cors = int(file.readline().strip())
        
        if code=='a':
            n=int(request.POST["input"])

            code="0".zfill(n)

            with open('data.txt', 'w') as file:
                file.write(f"{code}\n")
                file.write(f"{n}\n")
                file.write(f"{q}\n")
                file.write(f"{cors}\n")
                
            return render(request,"game.html",{'code':code})

        elif cors==-1:
            cors=int(request.POST["input"])
            if cors== n:
                with open('data.txt', 'w') as file:
                    file.write(f"a\n")
                    file.write(f"0\n")
                    file.write(f"0\n")
                    file.write(f"-1\n")
                return render(request,'final.html',{'code':code})
            
            if cors==0:
                with open('data.txt', 'w') as file:
                    file.write(f"a\n")
                    file.write(f"0\n")
                    file.write(f"0\n")
                    file.write(f"-1\n")
                return render(request,'final.html',{'code':"1"*n})

            code = code[:q] + '1' + code[q + 1:]

            with open('data.txt', 'w') as file:
                file.write(f"{code}\n")
                file.write(f"{n}\n")
                file.write(f"{q}\n")
                file.write(f"{cors}\n")              
            return render(request,"game.html",{'code':code})
        

        ans=int(request.POST["input"])

        if ans==n:
            with open('data.txt', 'w') as file:
                file.write(f"a\n")
                file.write(f"0\n")
                file.write(f"0\n")
                file.write(f"-1\n")            
            return render(request,'final.html',{'code':code})

        if ans < cors:
            code = code[:q] + '0' + code[q + 1:]
            q+=1
            if q==n-1:
                code = code[:q] + '1' + code[q + 1:]    
                with open('data.txt', 'w') as file:
                    file.write(f"a\n")
                    file.write(f"0\n")
                    file.write(f"0\n")
                    file.write(f"-1\n")            
                return render(request,'final.html',{'code':code})
            
            code = code[:q] + '1' + code[q + 1:]
            with open('data.txt', 'w') as file:
                file.write(f"{code}\n")
                file.write(f"{n}\n")
                file.write(f"{q}\n")
                file.write(f"{cors}\n")
            return render(request,"game.html",{'code':code})
        
        if ans > cors:
            cors=ans
            q+=1
            if q==n-1:
                code = code[:q] + '1' + code[q + 1:]    
                with open('data.txt', 'w') as file:
                    file.write(f"a\n")
                    file.write(f"0\n")
                    file.write(f"0\n")
                    file.write(f"-1\n")
                return render(request,'final.html',{'code':code})
            
            code = code[:q] + '1' + code[q + 1:]
            with open('data.txt', 'w') as file:
                file.write(f"{code}\n")
                file.write(f"{n}\n")
                file.write(f"{q}\n")
                file.write(f"{cors}\n")
            return render(request,"game.html",{'code':code})


    return render(request,"game.html") 

def guide(request):
    return render(request,'guide.html')