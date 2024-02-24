import uiautomator2 as u2

d = u2.connect('941c5f067ce4') # alias for u2.connect_usb('123456f')
# print(d.info)
# print(d.window_size())
# print(d.app_current())
# print(d.device_info)

d.set_clipboard('test pesan clipboard', 'label')
print(d.clipboard)

# d.press("home") # press the home key, with key name
# d.press("back") # press the back key, with key name
# d.press(0x07, 0x02) # press keycode 0x07('0') with META ALT(0x02)

# username = d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.EditText[1]')
# username.set_text('irfanykywz')

# password = d.xpath('//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[3]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.EditText[1]')
# password.set_text('asukoejancukmark')

# submit = d.xpath('//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.Button[1]')
# submit.click()

# {'currentPackageName': 'com.android.launcher3', 'displayHeight': 1280, 'displayRotation': 0, 'displaySizeDpX': 360, 'displaySizeDpY': 640, 'displayWidth': 720, 'productName': 'samsung Galaxy S7 Edge', 'screenOn': True, 'sdkInt': 25, 'naturalOrientation': True}

# d.start('com.android.chrome')


# package:com.facebook.katana
# d.app_list_running()

d.open_url("https://www.baidu.com")

# d.app_stop_all()

# d.push("ss.jpg", "/sdcard/")