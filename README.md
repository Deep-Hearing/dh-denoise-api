# DeepHearing Denoise API

## HTTP Request
```POST https://32c0w7t15f.execute-api.ap-northeast-2.amazonaws.com/Stage/enhance```

## Request body
### JSON representation
```json
{
  "config": {
    "filename": "source file name"
  },
  "audio": {
    "content": "(base64 encoded file data)"
  }
}
```

## Response body
### JSON representation
```json
{
  "result": "(base64 encoded file data)",
  "totalBilledTime": "string"
}
```

## Supported Format
|Property|Value|
|-----|-------|
|Samplerate|```16000Hz```|
|Maximum Length|```1 minute```|
|Maximum Channel|```1 CH ```|
