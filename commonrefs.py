
import json
import re
import requests

LIBRARY = 'library_test.bib'
REF_URL = 'https://api.elsevier.com/content/abstract/DOI:{}?apiKey={}&view=REF'
DOI_URL = 'https://api.elsevier.com/content/search/scopus?query=SCOPUS-ID({})&field=prism:doi'

with open('api_key.txt','r') as f:
    KEY = f.readline()


def get_references(DOI):
    url = REF_URL.format(DOI, KEY)
    data = requests.get(url, headers={'Accept': 'application/json'})
    data_dict = json.loads(data.text)
    try:
        references = data_dict['abstracts-retrieval-response']['references']['reference']
    except:
        references = []
    return references


def get_doi(SID):
    url = DOI_URL.format(SID)
    data = requests.get(url, headers={'Accept': 'application/json', 'X-ELS-APIKey': KEY})
    data_dict = json.loads(data.text)
    try:
        return data_dict['search-results']['entry'][0]['prism:doi']
    except:
        return []


def count_references(DOI_list):
    title_dict = {}
    sid_list = []
    title_by_sid = {}
    not_found = []
    for d, DOI in enumerate(DOI_list):
        print('{:>5} / {:<5}'.format(d+1, len(DOI_list)), end='\r')

        references = get_references(DOI)
        if not references:
            not_found.append(DOI)

        for ref in references:
            title, sid = ref['title'], int(ref['scopus-id'])
            if title:
                if title in title_dict:
                    title_dict[title] += 1
                else:
                    title_dict[title] = 1
                title_by_sid[sid] = title
            else:
                sid_list.append(sid)

    for sid in sid_list:
        if sid in title_by_sid:
            title_dict[title_by_sid[sid]] += 1

    sid_by_title = {title: sid for sid, title in title_by_sid.items()}

    return title_dict, sid_by_title, not_found


def simplify_title(title):
    return re.sub('[^a-z0-9 ]+', '', title.lower())


if __name__ == "__main__":
    DOI_list = []
    title_list = []
    with open(LIBRARY,'r') as f:
        for line in f:
            words = line.strip().split(' = ')
            if words and words[0] == "doi":
                DOI_list.append(words[1].strip('{},').lower())
            if words and words[0] == "title":
                title_list.append(simplify_title(words[1]))
    print('Document Object Identifier (DOI) found for {} publications'.format(len(DOI_list)))

    title_dict, sid_by_title, not_found = count_references(DOI_list)

    print('No references found for {} publications (see not_found.txt file)'.format(len(not_found)))
    with open('not_found.txt','w') as f:
        f.write('\n'.join(not_found))

    print('\nResults:')
    with open('results_title.txt','w') as f:
        for i, title in enumerate(sorted(title_dict, key=title_dict.get, reverse=True)):
            line = '{} x {}'.format(title_dict[title], title)
            if simplify_title(title) not in title_list:
                DOI = get_doi(sid_by_title[title])
                if not DOI:
                    line += '    ?'
                elif DOI.lower() not in DOI_list:
                    line += '    x'
            f.write(line+'\n')
            print(line)
            if title_dict[title] < 2:
                break
