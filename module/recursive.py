allList = []
templist = []
json_key_list = []

def createTestCase(currentarray, singlearray, indexNum):

    indexNum = indexNum -1
    if (indexNum < 0):
        array_a = []

        for x in singlearray:
            array_a.append(x)

        allList.append(array_a)
    else:
        for i in range (0 , len(currentarray[indexNum]), 1):
            array = currentarray[indexNum]
            if len(singlearray) > len(currentarray)-indexNum-1 or len(singlearray) == len(currentarray):

                singlearray[len(currentarray)-indexNum-1] = array[i]

            else:
                singlearray.append(array[i])
            createTestCase(currentarray, singlearray, indexNum)

    return allList

def json_key(data, url1):
    if type(data) == dict:
        for first in data:
            end_url = url1+"."+first
            if data[first]:
                json_key(data[first], end_url)
            else:
                json_key_list.append(end_url[2:])
    elif type(data) == list:
        n = len(data)
        for i in range(0 , n , 1):
            end_url = url1+"."+ "["+str(i)+"]"
            if data[i]:
                json_key(data[i], end_url)
            else:
                json_key_list.append(end_url[2:])
    else:
        end_url = url1
        json_key_list.append(end_url[2:])
    return json_key_list