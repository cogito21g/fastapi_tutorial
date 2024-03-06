# FastAPI

## Tutorial
1. [Main Page](./01_main_page/)
2. [Templates](./02_templates/)
3. [Database(Sqlalchemy)](./03_database/)
4. [Single File Upload](./04_single_file_upload/)
5. [Multi File Upload](./05_multi_file_upload/)
6. [Single File Download](./06_single_file_download/)
7. [Multi File Download](./07_multi_file_download/)
8. [Video Streaming(HTTP)](./08_video_streaming_http/)
9. [Video Streaming(WebSocket)](./09_video_streaming_websocket/)
10. [Realtime Data Streaming](./10_realtime_data_streaming/)
11. [WebRTC](./11_webrtc/)

## Setting

- 가상환경설정
```bash
conda create -n fastapi python=3.10
conda activate fastapi
```

- 패키지 설치
```bash
pip install fastapi
pip install uvicorn
pip install jinja2
pip install python-multipart
pip install sqlalchemy
pip install email-validator
```

- 실행
```bash
python app.py
```