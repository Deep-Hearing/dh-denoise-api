# 파일 업로드

[한국어](https://github.com/Deep-Hearing/dh-denoise-api/blob/main/FILE_UPLOAD/file-upload-ko.md) | [Eng](https://github.com/Deep-Hearing/dh-denoise-api/blob/main/FILE_UPLOAD/file-upload-en.md)

해당 문서는 DeepHearing API에 관한 문서입니다.

모든 요청에 대해서 유저의 키가 발급될 필요가 있으므로 [스튜디오](https://dashboard.deephearing.com)에서 회원가입을 진행해 키를 발급받으시길 바랍니다.

## HTTP Request

### Enhance File

|Method|URL|
|:--:|:-:|
|**POST**|```https://api.deephearing.com/enhance```|

파일을 처리하기 위해 Enhance Endpoint로 요청을 보내게 되면 Base64로 인코딩된 `UUID` 값이 반환됩니다.

해당 `Job ID` 를 통해 현재 파일의 진행상태를 확인하실 수 있습니다.

#### Job ID Example

```jsonc
ACtYB187SXiv9___FlpPig
```

## Request body

### Javascript
```javascript
// 파일을 동시에 여러개 보낼 수 있습니다.
var formdata = new FormData();
formdata.append('file_key', fileInput.files[0]);\n
await fetch('https://api.deephearing.com/enhance',
    {
      method: 'POST',
      headers: {'Authorization', '<User Key>'},
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
      'Authorization': '<User Key>',
    },
    # 파일을 동시에 여러개 보낼 수 있습니다.
    files={
      'file_key': open('your-file-path','rb')
    }
  )
  
  print(response.text)
```

## Response body

### Response

반환값의 키는 파일을 보낼 때 설정한 값으로 돌아오게 됩니다.

```
{
  "file_key\": <Job ID>
}
```


### Error

#### 파일이 없거나 파일에 이상이 있는 경우
```
{
    "error": {
        "code": "INVALID_FILE",
        "msg": "Invalid file type from input"
    }
}
```

#### 키가 없거나 키가 잘못된 경우
```
{
    "error": {
        "code": "API_KEY_NOT_FOUND",
        "msg": "Unregistered API Key"
    }
}
```