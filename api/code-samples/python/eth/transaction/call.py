import json

from eth.opensdk_python_eth import ApiClient, Configuration
from eth.opensdk_python_eth.apis.tags.eth_api import Call

host = "https://api.baobab.klaytn.net:8651"

call_object = {
    "from": "0xca7a99380131e6c76cfa622396347107aeedca2d",
    "to": "0xbE3892d33620bE5aca8c75D39e7401871194d290",
    "input": "0x2e64cec1"
}
block_tag = 'latest'
state_override_set = {
    "0xbE3892d33620bE5aca8c75D39e7401871194d290":
        {
            "code": "0x6080604052600436106049576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff1680632e64cec114604e5780636057361d146076575b600080fd5b348015605957600080fd5b50606060a0565b6040518082815260200191505060405180910390f35b348015608157600080fd5b50609e6004803603810190808035906020019092919050505060a9565b005b60008054905090565b80600081905550505600a165627a7a723058207783dba41884f73679e167576362b7277f88458815141651f48ca38c25b498f80029"
        }
}

eth = Call(ApiClient(configuration=Configuration(host=host)))
eth_response = eth.call(call_object, block_tag, state_override_set)

print(json.loads(eth_response.response.data))
