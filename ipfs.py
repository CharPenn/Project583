import requests
import json

def pin_to_ipfs(data):
	assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
	headers = {
		"pinata_api_key": "9fb100470475cde82ed4",
		"pinata_secret_api_key": "91b89ec37bff29af7623291ac3ddec561f1159fe86abc538cd10b4e500f25ffe"
	}
	url = "https://api.pinata.cloud/pinning/pinJSONToIPFS"
	response = requests.post(url, headers=headers, json={"pinataContent": data})
	if response.status_code == 200:
		cid = response.json()["IpfsHash"]
	else:
		raise Exception(f"Error pinning to IPFS: {response.text}")

	return cid

def get_from_ipfs(cid,content_type="json"):
	assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
	#YOUR CODE HERE	
	url = f"https://gateway.pinata.cloud/ipfs/{cid}"
	response = requests.get(url)
	if response.status_code != 200:
		raise Exception(f"Error retrieving from IPFS: {response.text}")
	if content_type == "json":
		data = response.json()
	else:
		data = response.content
	assert isinstance(data,dict), f"get_from_ipfs should return a dict"
	return data
