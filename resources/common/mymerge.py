import json
import copy
#from example_json import j1,j2

type_error = -1

def merge_array(base, head):

	if type(base) != list or type(head) != list:
		return type_error

	result = copy.deepcopy(base)
	for item in head:
		if item in base:
			continue
		else:
			if type(item) not in [list, dict]:
				result.append(item)
			else:
				index = None
				for new_base in base:
					if type(new_base) == type(item):
						index = base.index(new_base)
						break
				if index is None:
					result.append(item)
					continue
				if type(new_base) is list:
					result[index] = merge_array(new_base, item)
				elif type(new_base) is dict:
					result[index] = merger(new_base, item)

	return sorted(result)


def merger(base, head):

	if not isinstance(base, dict) or not isinstance(head, dict):
		return type_error

	result = copy.deepcopy(base)
	for key in head:
		if key not in base:
			result[key] = head[key]
		elif type(head[key]) not in [list, dict]:
			result[key] = head[key]
		elif type(head[key]) is list:
			result[key] = merge_array(result[key], head[key])
		elif type(head[key]) is dict:
			result[key] = merger(result[key], head[key])

	return result




def new_merger(base, head):

    if isinstance(base, str):
        base = json.loads(base)
    if isinstance(head, str):
        head = json.loads(head)

    print base
    print head

    if (not isinstance(base, dict)) or (not isinstance(head, dict)):
        return type_error

    result = copy.deepcopy(base)
    print result
    print type(result)
    for head_key in head:

        mergeTag = False
        # This tag is set to indicate whether head[head_key] needs to
        # be merged with an entry in the base.
        # If this tag is false, head[head_key] only needs to be added
        # into the base.

        for base_key in result:
            resourceTag = head[head_key]['Policy_ResourceType'] == result[base_key]['Policy_ResourceType']
            scopeTag    = head[head_key]['Scope'] == result[base_key]['Scope']
            if resourceTag is True and scopeTag is True:
                merged_privacy = merger(head[head_key]['Policy'], result[base_key]['Policy'])
                result[base_key]['Policy'] = merged_privacy
                mergeTag = True
                break

        if mergeTag == False:
            result[head_key] = head[head_key]

    return result


if __name__ == '__main__':
    print json.dumps(new_merger(j1, j2), indent=2)
