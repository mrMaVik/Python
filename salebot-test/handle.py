import json


def handle(params):
    data = json.loads(params)
    q = data['q']
    w = data['w']
    q = {"result": q*w}
    return json.dumps(q)


#s = '{"q":18,"w":3}'
#print(handle(s))
