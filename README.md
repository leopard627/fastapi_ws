# fastapi_ws Example 
## Fast API WS + BroadCaster + Docker Example

### 1. install requirements.txt
```
pip install requirements/requirements.txt
```

### 2. install redis & run redis
```
85502:C 08 Dec 2022 23:10:08.164 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
85502:C 08 Dec 2022 23:10:08.164 # Redis version=7.0.5, bits=64, commit=00000000, modified=0, pid=85502, just started
85502:C 08 Dec 2022 23:10:08.164 # Warning: no config file specified, using the default config. In order to specify a config file use redis-server /path/to/redis.conf
85502:M 08 Dec 2022 23:10:08.164 * Increased maximum number of open files to 10032 (it was originally set to 256).
85502:M 08 Dec 2022 23:10:08.164 * monotonic clock: POSIX clock_gettime
                _._
           _.-``__ ''-._
      _.-``    `.  `_.  ''-._           Redis 7.0.5 (00000000/0) 64 bit
  .-`` .-```.  ```\/    _.,_ ''-._
 (    '      ,       .-`  | `,    )     Running in standalone mode
 |`-._`-...-` __...-.``-._|'` _.-'|     Port: 6379
 |    `-._   `._    /     _.-'    |     PID: 85502
  `-._    `-._  `-./  _.-'    _.-'
 |`-._`-._    `-.__.-'    _.-'_.-'|
 |    `-._`-._        _.-'_.-'    |           https://redis.io
  `-._    `-._`-.__.-'_.-'    _.-'
 |`-._`-._    `-.__.-'    _.-'_.-'|
 |    `-._`-._        _.-'_.-'    |
  `-._    `-._`-.__.-'_.-'    _.-'
      `-._    `-.__.-'    _.-'
          `-._        _.-'
              `-.__.-'

85502:M 08 Dec 2022 23:10:08.166 # WARNING: The TCP backlog setting of 511 cannot be enforced because kern.ipc.somaxconn is set to the lower value of 128.
85502:M 08 Dec 2022 23:10:08.166 # Server initialized
85502:M 08 Dec 2022 23:10:08.166 * Ready to accept connections


>> redis-server
```

### 3. runserver
```
export DATABASE_CONFIG=""
export REDIS_URL="redis://localhost:6379/1"
uvicorn fastapi_ws.main:app --port 8000 --ws-ping-interval 300 --timeout-keep-alive 300 --ws-ping-timeout 300
```


## Demo with chrome extensions (Simple Websocket Client)
### Simple WebSocket Client

![화면_기록_2023-01-02_오후_11_34_20_AdobeExpress (2)](https://user-images.githubusercontent.com/16227780/210246428-3617bf8a-85bf-4260-b70c-ca61502cc881.gif)
<img width="1216" alt="스크린샷 2023-01-02 오후 11 48 42" src="https://user-images.githubusercontent.com/16227780/210247022-a5ff0f14-2393-4cdf-a464-6aca8faaffa8.png">

<img width="1230" alt="스크린샷 2023-01-02 오후 11 42 48" src="https://user-images.githubusercontent.com/16227780/210246345-effd6916-da2c-47b4-bd2e-ff467f539bb1.png">
https://chrome.google.com/webstore/detail/simple-websocket-client/pfdhoblngboilpfeibdedpjgfnlcodoo
