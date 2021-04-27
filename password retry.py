#密碼重試程式
#password = 0224
#讓使用者重複輸入密碼，最多輸入3次
#如果輸入正確就印出 登入成功
#反之 印出登入失敗，並告知剩餘機會

password = '0224'
x = 0 #輸入次數
while x<3 :

    pwd = str(input('請輸入密碼'))

    if pwd == password :
        print('登入成功')
        break  #逃出迴圈        
    else:
        x=x+1 #輸入次數+1
        print('登入失敗，你還剩',3-x,'次機會')
        