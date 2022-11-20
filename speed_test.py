import speedtest

test = speedtest.Speedtest(secure=True)

down_speed = test.download()
up_speed = test.upload()
ping = test.results.ping

download = down_speed/1024/1024
upload = up_speed/1024/1024

print(f"Ping: {ping} ms")
print(f"Download speed: {round(download, 3)} Mb/s")
print(f"Upload speed: {round(upload, 3)} Mb/s")

#print(f"Download speed: {download} Mb/s")
#print(f"Upload speed: {upload} Mb/s")

#import speedtest
#
#speed = speedtest.Speedtest(secure=True)
#
#def main():
#        print(f"Download speed: {'{:.2f}'.format(speed.download()/1024/1024)} Mb/s")
#        print(f"Upload speed: {'{:.2f}'.format(speed.upload()/1024/1024)} Mb/s")
#        servernames = []
#        speed.get_servers(servernames)
#        print(f"Ping: {speed.results.ping}")
#        root.after(500, main)
#root.after(500, main)