from win10toast import ToastNotifier

toaster = ToastNotifier()

def sayReconnect():
    toaster.show_toast("校园网自动重连", "网络不稳定，正在自动重连……")

def sayCheck():
    toaster.show_toast("校园网自动重连", "多次重连仍然不稳定，请手动检查")

def sayConnectSuccess():
    toaster.show_toast("校园网自动重连", "重连成功！")