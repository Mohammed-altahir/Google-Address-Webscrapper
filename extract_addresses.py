def extract_addresses():
    import fitz,re
    name = input('enter the name of your pdf:\n')
    textCollection = []
    name_pattren = r''   
    address_pattern = r't .[0-9]+'
    file = fitz.open(f'{name}.pdf')
    for pageNum ,page in enumerate(file.pages(),start=1):
        extracted_text = page.get_text()
        names = re.findall(name_pattren,extracted_text)
        results = re.findall(address_pattern,extracted_text)
        for result in range(len(results)):
            person = {"name":names[result],"address":results[result],"google_maps_address":""}
            textCollection.append(person)
    return textCollection
    # this is for checking the results were extracted correctly
    # with open('result.txt','a') as result:
    #     result.write(f'{textCollection}')