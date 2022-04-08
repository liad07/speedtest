import speedtest
wifi=speedtest.Speedtest()
print("download is:",wifi.download()/1024/1024)
print("upload is:",wifi.upload()/1024/1024)