drinkMenu={}
drinkMenu["coffee"]=75
drinkMenu["blacktea"]=30
drinkMenu["juice"]=75
drinkMenu["Greentea"]=40
drinkSheet={}
drinkSheet["coffee"]=2
drinkSheet["blacktea"]=1
drinkSheet["juice"]=1
drinkSheet["milk"]=2
sum=0
for name,number in drinkSheet.items():
    if name in drinkMenu:
        price=number*drinkMenu[name]
        print("計算商品:"+name)
        print("商品乘上數量的價格:"+str(price))
        sum+=price
    else:
        print("不存在商品:" + name)
print("購買飲料的總金額: "+str(sum))
