import json

def http_headers_to_json(http, save_json):
    dict = {}
    get_answ = {
	    "HTTP/": ['protocol', 'status_code', 'status_message'],
		"GET": ['method', 'uri', 'protocol'],
		"HTTP/2": ['protocol', 'status_code']
	}
    with open(http) as f:
        for i, line in enumerate(f):
            line = line.replace("\n","")
            if(i == 0):
                first_line = line.split(" ", 2)
                answ = get_answ.get("GET") if not get_answ.get(first_line[0][:5]) else get_answ.get(first_line[0][:5])
                if first_line[0] == "HTTP/2":
                    answ = get_answ.get(first_line[0])
                for i, head in enumerate(answ):
                    dict[head] = first_line[i]
            else:
                if line:
                    list = line.split(': ', 1)
                    dict[list[0]] = list[1]
					
    with open(save_json, 'w') as f:
        json.dump(dict, f, indent=4)
        
