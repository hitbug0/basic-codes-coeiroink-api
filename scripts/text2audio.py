import json
import requests
from pydub import AudioSegment, playback

# やり取りするローカルサーバ
URL = "http://localhost:50032/"

# 音声モデルの情報
SPEAKER_INFO = {
    "kanae": ['d41bcbd9-f4a9-4e10-b000-7a431568dd01', '100'], # AI声優-金苗
    "ayaka": ['d1143ac1-c486-4273-92ef-a30938d01b91', '50' ], # AI声優-朱花
}

def make_wav(text, speed_scale, speaker_info):
    # 音声モデルを使ってtextからwavを生成する関数
    speaker_uuid, style_id = speaker_info
    response = requests.post(
        URL+"v1/predict",
        json={
            "speakerUuid": speaker_uuid,
            "styleId": style_id,
            "text": text,
            "speedScale": speed_scale
            }
        )
    
    if response.content==b'Internal Server Error':
        print('Internal Server Error')
    
    return response.content

def play_wav(wav):
    # wavを再生する関数
    playback.play(
        AudioSegment(
            wav,
            sample_width=2, 
            frame_rate=44100, 
            channels=1
            )
        )
    return 0

def write_wav_file(file_path, audio_data, sample_width=2, sample_rate=44100, channels=1):
    # wavを書き出す関数
    # file_path: 書き出すファイルのパス
    # audio_data: 書き出す音声データ（バイナリ形式の文字列）
    # sample_width: サンプルのビット幅（バイト数）デフォルトは2（16bit）
    # sample_rate: サンプルレート デフォルトは44100Hz
    # channels: チャンネル数 デフォルトは1（ステレオ）
    audio_segment = AudioSegment(audio_data, sample_width=sample_width, frame_rate=sample_rate, channels=channels)
    # wavファイルとして保存
    audio_segment.export(file_path, format="wav")

# メイン処理
def text2audio():
    # テキストファイルの読み込み
    with open("input.txt", "r", encoding='utf-8') as file:
        # ファイルの各行をリストとして読み込む
        lines = file.readlines()

    speed_scale = 1.0 # 発話速度
    
    # 音声合成
    audio_data = b''
    for line in lines:
        speaker, text = line.split(":")
        w0 = make_wav(text, speed_scale, SPEAKER_INFO[speaker])
        # _ = play_wav(w0) # 一つずつ再生する場合は使う
        audio_data += w0

    # 連結した音声の出力
    play_wav(audio_data) # 再生
    write_wav_file("output.wav", audio_data) # 保存

text2audio()
