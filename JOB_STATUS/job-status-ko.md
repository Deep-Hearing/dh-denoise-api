# 파일 상태 확인

[한국어](https://github.com/Deep-Hearing/dh-denoise-api/blob/main/JOB_STATUS/job-status-ko.md) | [Eng](https://github.com/Deep-Hearing/dh-denoise-api/blob/main/JOB_STATUS/job-status-en.md)

해당 문서는 DeepHearing API에 관한 문서입니다.

모든 요청에 대해서 유저의 키를 필요로 하기 때문에 [스튜디오](https://dashboard.deephearing.com)에서 회원가입을 진행해 키를 발급받으시길 바랍니다.

## HTTP Request

### 파일 상태 확인

|Method|URL|
|:--:|:-:|
|**POST**|```https://api.deephearing.com/stat/jobs/<Job ID>```|

먼저 파일 업로드 단계에서 `Job ID`를 응답받은 후 요청을 진행할 수 있습니다.

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
|model|String|`model_16k`|모델명|`model_16k`|
|app_id|Number|1 (only)|DeepHearing 제품 번호|`1`|
|billed_time|Number|-|총 파일 길이(초 단위, 모든 채널 길이 합산 값)|-|
|mod_time|Number|-|딥히어링 서버에서 마지막으로 수정된 시간|-|
|timestamp|Number|-|작업이 시작된 시간|-|
|result|String|-|처리된 파일 주소|`job_status`가 `complete`가 아닌 경우, 해당 값은 반환되지 않음|
|file_name|String|-|파일 이름|-|
|job_id|String|-|`/enhance` 로 요청 시 반환되는 Job ID|-|
|uid|Number|-|유저 고유 번호|-|
|file_key|String|-|파일 고유 번호|-|
|job_status|String|-|현재 파일 처리 상태|`pending`, `pre-processing`, `processing`, `post-processing`, `completed`|

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