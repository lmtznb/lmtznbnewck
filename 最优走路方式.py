s=float(input('行走的距离（米）:'))
if s/1.2<s/3+50:
    print('步行更好一些walk')
elif s/1.2>s/3+50:
    print('骑车更好一些bike')
elif s/1.2==s/3+50:
    print('一样快all')