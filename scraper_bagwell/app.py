from flask import Flask, request, make_response
import requests
import json

app = Flask(__name__)

def load_counters():
    f=open('tblArray.json')
    tblArray=json.load(f)
    return tblArray

def save_counters(tblArray):
    jsonobject=json.dumps(tblArray)
    with open('tblArray.json', 'w') as outfile:
        outfile.write(jsonobject)
    return

@app.route('/version')
def hello_world():  # put application's code here
    return '1.0'

@app.route('/', methods=['POST'])
def scrape_me():  
    print ("here I am")
    # Uncomment to load saved counters
    try:
        # Restore counters from last time
        tblArray=load_counters()
    except:
        # If no such counters file exists, then create one
        tblArray={}
        save_counters(tblArray)

    payload=request.get_json()
    if 'url' not in payload:
        return({
            'result': "error, expected URL in JSON payload"
        })
    else:
        # Try and hit the URL
        tryme=payload['url']
        try:
            page = requests.get(tryme, allow_redirects=False)
            status_code=page.status_code
        except:
            # Save status 999 for weird non-HTTP things, like DNS errors and the like
            status_code="999"

        # Now, see if we can find an entry in the tblArray
        for item in tblArray:
            if item['url'] == tryme and item['code'] == status_code:
                item['count'] = item['count'] + 1
                save_counters(tblArray)
                return tblArray

        # If you get here, the item exists, but is not in the array
        newitem={
            'url': tryme,
            'code': status_code,
            'count': 1
        }
        tblArray.append(newitem)
        save_counters(tblArray)
        return tblArray

@app.route('/metrics', methods=['GET'])
def metrics():  # put application's code here
    try:
        # Restore counters from last time
        tblArray=load_counters()
    except:
        # If no such counters file exists, then create one
        tblArray={}
        save_counters(tblArray)
        return {}

    outputString = ""
    for item in tblArray:
        outputString = outputString + 'http_get{\"url\"=\"' + item['url'] + '\",\"code\"=\"' + str(item['code']) + '\"} ' + str(item['count']) + "\n"
    return outputString

if __name__ == '__main__':
    app.run()
