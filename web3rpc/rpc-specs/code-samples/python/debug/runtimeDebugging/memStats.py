from opensdk.sdk import OpenSDK

host = "https://api.baobab.klaytn.net:8651"

sdk = OpenSDK(host)
debug_response = sdk.debug.mem_stats()

print(debug_response)