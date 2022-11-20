import speedtest

test = speedtest.Speedtest(secure=True)

down_speed = test.download()
up_speed = test.upload()
ping = test.results.ping
test.get_servers()
best = test.get_best_server()

download = down_speed/1024/1024
upload = up_speed/1024/1024

print(f"Ping: {ping} ms")
print(f"Found: {best['host']} located in {best['country']}")
print(f"Download speed: {round(download, 3)} Mb/s")
print(f"Upload speed: {round(upload, 3)} Mb/s")
