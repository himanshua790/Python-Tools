'''
Download and Extract Zip file using Python.
can be used to download and extract any zip file directly to Google Drive.
'''

import requests, zipfile, io
r = requests.get(<Download_Link>)
with zipfile.ZipFile(io.BytesIO(r.content) as zf:
  for member in tqdm.tqdm(zf.infolist(), desc='Extracting'):
    try:
      zf.extract(member, <Destination>)
    except zipfile.error as e:
      pass
