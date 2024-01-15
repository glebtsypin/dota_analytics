


from dota_client import DotaClient



client = DotaClient()


try:
    u = client.run(1)
    print(u)
except BaseException as ex:
    print("error")
    print(ex)