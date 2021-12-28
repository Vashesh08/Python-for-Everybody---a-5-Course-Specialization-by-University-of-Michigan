import xml.etree.ElementTree as ET

# data = '''<person>
# <name>Vashesh</name>
# <phone type='intl'>
# +1 786 958 3468
# </phone>
# <email hide='yes'/>
# </person>
# '''
#
# tree = ET.fromstring(data)
# print("Name: ", tree.find('name').text)
# print("Attr: ", tree.find('email').get('hide'))

input_xml = '''<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>'''

stuff = ET.fromstring(input_xml)
st = stuff.findall('users/user')
print('User Count: ', len(st))
for item in st:
    print('Name: ',item.find('name').text)
    print('Id: ',item.find('id').text)
    print('Attribute: ',item.get('x'))
