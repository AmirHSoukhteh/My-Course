"""

در یک نظرسنجی از افراد علاقه‌­مند به تماشای فیلم، درخواست شد تا 3 تا از ژانرهای مورد علاقه‌­ی خود را بنویسند. 6 ژانر مختلف برای انتخاب به آن­‌ها داده شده است که شامل:

Horror, Romance, Comedy, History , Adventure , Action

برنامه‎ای بنویسید که تعداد افراد را بگیرد سپس اسم هر فرد را با ژانرهای مورد علاقش بگیرد و اسم هر ژانر و تعداد افراد علاقه‌مند به آن ژانر را به ترتیب از بیشترین علاقه‌مندی در خروجی چاپ کند. ( در صورتی که میزان علاقه‌مندی در ژانرهای مختلف یکسان شد، به ترتیب الفبای انگلیسی در خروجی چاپ کنید.) در صورتی که ژانری انتخاب نشد، مقدار آن را صفر در نظر بگیرید و در خروجی اسم و عدد 0 را چاپ کنید.

4
hossein Horror Romance Comedy
mohsen Horror Action Comedy
mina Adventure Action History
sajjad Romance History Action
نمونه خروجی:

Action : 3
Comedy : 2
History : 2
Horror : 2
Romance : 2
Adventure : 1
توجه: چنانچه قصد دارید از دیکشنری در حل مسائل خود استفاده کنید، به این نکته توجه کنید که دیکشنری ترتیب را حفظ نمی‌کند.
"""




#popular genre

genres =dict(Action=0, Comedy=0, History=0,
            Horror=0, Romance=0, Adventure=0)   


num = int(input())

def pg():
    #pg = Popular Genre

    name = str(input()).split(' ')
    for i in name[1:]:
        genres[i]=genres[i]+1


for i in range(num):
    pg()

genres = dict(sorted(genres.items(), key=lambda item: (-item[1],item[0])))

for k in genres:
    print(k,":",genres[k])
