print("Starting program")
import csv
import json
import hashlib
import os

k = []

def create_dir():	
	print("Creating directory for files......")
	if not os.path.exists('Json-for-each-entry'):
		os.mkdir('Json-for-each-entry')
	if not os.path.exists('Hashed-csv'):
		os.mkdir('Hashed-csv')


def to_hash():
		for file in os.listdir('Json-for-each-entry'):
			sha256_hash = hashlib.sha256()
			with open(f'Json-for-each-entry/{file}', "rb") as f:
			    for byte_block in iter(lambda: f.read(4096),b""):
			        sha256_hash.update(byte_block)
			        k.append(sha256_hash.hexdigest())
	
def append_hash_to_csv():
	print(f"{len(k)} + files created")
	file =  'HNGi9_nft1.csv'
	new_f = "Hashed-csv/HNGi9_nft(updated).csv"
	with open(file, 'r') as origin_csv:
		data = [line.strip().split(',') for line in origin_csv.readlines()]
		header = data[0]
		data = data[1:]
		header.append('Hash-value')
		data = [line + [k[idx]] for idx, line in enumerate(data[1::])]
		data = [','.join(line) for line in [header]+data]
		with open(new_f, 'w') as newFile:
			newFile.writelines('\n'.join(data))
		print("Program completed successfully !!!")


def to_json():
    print("Creating files.......")
    with open('HNGi9_nft2.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        Active_team = ''
        
    
        for line,row in enumerate(csv_reader):
            team, sn, filename, name, description, gender, attributes, _ = row[:8]
            
            if line== 0:
            	continue 
            else:
                if team:
                    active_team = team
                    
                ch_format = {
                            "format": "CHIP-0007",
                            "name": name,
                            "description": description,
                            "minting_tool": active_team,
                            "sensitive_content": False,
                            "series_number": sn,
                            "series_total": 420,
                            "attributes": [
                                {
                                    "trait_type": "gender",
                                    "value": gender,
                                },
                                
                            ],
                            "collection": {
                                "name": "Zuri NFT Tickets for Free Lunch",
                                "id": "b774f676-c1d5-422e-beed-00ef5510c64d",
                                "attributes": [
                                    {
                                        "type": "description",
                                        "value": "Rewards for accomplishments during HNGi9.",
                                    }
                                ],
                            },
                        }
                json_attr = [x.split(':') for x in attributes.split(';') if x]                
                i =0
                for items in json_attr:
                    ch_format['attributes'].append({'trait_type': items[i].strip(), 'value':items[i +1].strip()})
                
                with open(f'Json-for-each-entry/{filename}.json', 'w') as f:
                    f.write(json.dumps(ch_format, indent=4))
                    
           
                    
    print('Done')


create_dir()
to_json()
to_hash()
append_hash_to_csv()	




