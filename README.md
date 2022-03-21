# DeepHearing Denoise API

## HTTP Request
|Method|URL|
|:--:|:-:|
|**POST**|```https://32c0w7t15f.execute-api.ap-northeast-2.amazonaws.com/Stage/enhance```|

### Test Code for Performance
<a href="https://colab.research.google.com/drive/1aRHoHbmyzDOSWL589AarI2rm5O8oqJfx?usp=sharing">
  <img alt="Google Colab" src="https://img.shields.io/badge/Google Colab-F9AB00.svg?&style=for-the-badge&logo=Google Colab&logoColor=white">
</a><br><br>

## Request body
### JSON representation
```jsonc
{
  "config": {
    "filename": "your audio file name" //ex. audio.wav
  },
  "audio": {
    "content": "file data encoded base64"
  }
}
```
Audio data is binary data. however, JSON is used when making a request. JSON is a text format that does **not directly support binary data**, so you will **need to convert such binary data into text using Base64 encoding**.<br>

|Supported Format|
|-|
|```.wav```, ```.flac```, ```.aiff```, ```.w64``` and Click on <a href="https://libsndfile.github.io/libsndfile/formats.html">the this link</a> for more details.|

## Response body
### JSON representation
```jsonc
{
  "result": "file data encoded base64",
  "totalBilledTime": "String"
}
```
<br>

## Supported Format
|Property       |Value         |
|---------------|:------------:|
|Samplerate     |```16000Hz``` |
|Maximum Length |```1 minute```|
|Maximum Channel|```1 CH ```   |
