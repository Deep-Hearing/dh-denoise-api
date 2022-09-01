# File Upload

[한국어](https://github.com/Deep-Hearing/dh-denoise-api/blob/main/FILE_UPLOAD/file-upload-ko.md) | [Eng](https://github.com/Deep-Hearing/dh-denoise-api/blob/main/FILE_UPLOAD/file-upload-en.md)

This document is about the DeepHearing API.

A user's key needs to be issued for all requests, so please sign up at Studio to receive a key.

## HTTP Request

### Enhance File

|Method|URL|
|:--:|:-:|
|**POST**|```https://api.deephearing.com/enhance```|

When a request is sent to the Enhance Endpoint to process a file, a Base64-encoded `UUID` value is returned.

You can check the progress of the current file through the corresponding `Job ID`.

#### Job ID Example

```jsonc
ACtYB187SXiv9___FlpPig
```

## Request body

### Javascript
```javascript
// You can send multiple files at the same time.
var formdata = new FormData();
formdata.append('file_key', fileInput.files[0]);\n
await fetch('https://api.deephearing.com/enhance',
    {
      method: 'POST',
      headers: {'Authorization', 'User Key'},
      body: formdata,
      redirect: 'follow'
    }
  )
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
 ```
 
### Python
 ```python
  import requests
  response = requests.request(
    'POST',
    'https://api.deephearing.com/enhance',
    headers={
      'Authorization': 'User Key',
    },
    # You can send multiple files at the same time.
    files={
      'file_key': open('your-file-path','rb')
    }
  )
  
  print(response.text)
```

## Response body

### Response

The key of the return value is returned to the value set when sending the file.

```
{
  "file_key\": <Job ID>
}
```


### Error

#### If the file does not exist or there is something wrong with the file
```
{
    "error": {
        "code": "INVALID_FILE",
        "msg": "Invalid file type from input"
    }
}
```

#### If the key does not exist or the key is invalid
```
{
    "error": {
        "code": "API_KEY_NOT_FOUND",
        "msg": "Unregistered API Key"
    }
}
```