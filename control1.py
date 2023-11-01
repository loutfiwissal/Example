def soustableau(T,I1,I2):
    st=[]
    for i in range(I1,I2):
        st.append(T[i])
    return st
while True:
 T=[]
 for i in range(10):
  x=int(input("enter a number: "))
  T.append(x)
 print(T)
 I1=int(input("please type the first indice: "))
 I2=int(input("please type the second indice: "))
 a=soustableau(T,I1,I2)
 print("soustableau:",a)
 C=input("do you want to enter a new list: ")  
 if C!="YES":
   break