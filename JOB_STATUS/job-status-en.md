# Check File State

[한국어](https://github.com/Deep-Hearing/dh-denoise-api/blob/main/JOB_STATUS/job-status-ko.md) | [Eng](https://github.com/Deep-Hearing/dh-denoise-api/blob/main/JOB_STATUS/job-status-en.md)

This document is about the DeepHearing API.

A user's key needs to be issued for all requests, so please sign up at Studio to receive a key.

## HTTP Request

### Check File State

|Method|URL|
|:--:|:-:|
|**POST**|```https://api.deephearing.com/stat/jobs/<Job ID>```|

First, you can proceed with the request after receiving the `Job ID` response in the file upload stage.

#### Job ID Example

```jsonc
ACtYB187SXiv9___FlpPig
```

## Request body
### Javascript
```javascript
await fetch('https://api.deephearing.com/stat/jobs/<Job ID>',
    {
      method: 'GET',
      headers: {
        'Authorization': '<User Key>',
      }
      redirect: 'follow'
    }
  )
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

## Response body

### Response
|Key|Type|Default|Description|Value|
|:-:|:-:|:-:|:-:|:-:|
|model|String|`model_16k`|Model Name|`model_16k`|
|app_id|Number|1 (only)|DeepHearing Product Number|`1`|
|billed_time|Number|-|Total file length (in seconds, Sum of all channel lengths)|-|
|mod_time|Number|-|Last modified time on the DeepHearing server|-|
|timestamp|Number|-|Time the job started|-|
|result|String|-|	Processed file url|If `job_status` is not `complete`, no value is returned.|
|file_name|String|-|File Name|-|
|job_id|String|-|Job ID returned when requested with `/enhance`|-|
|uid|Number|-|User Unique Number|-|
|file_key|String|-|File Unique Number|-|
|job_status|String|-|Current File Processing Status|`pending`, `pre-processing`, `processing`, `post-processing`, `completed`|

#### Sample
```json
{
  "model": <Model Type>,
  "app_id": 1,
  "billed_time": 4,
  "mod_time": 1661754618,
  "timestamp": 1661754616,
  "result": <URL>,
  "file_name": <File Name>,
  "job_id": "83N36k6vTLmmGG-w-XjTZA",
  "uid": 1,
  "file_key": "1-1-A9DA6504-FACE-49F9-9D39-8BE8E1F395E9",
  "job_status": "completed"
}
```