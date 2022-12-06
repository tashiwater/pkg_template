###
# pip install moviepy
# githubのissueは10MBまでしか乗らないので、それ用にファイルを減らすこと
###
from moviepy.editor import VideoFileClip
import os
import glob


width = 900
fps = 30
start_t = 0
end_t = 6

dirname = os.path.dirname(__file__)

input_dir = dirname + "/input/*.mp4"
output_dir = dirname + "/output/"

input_files = glob.glob(input_dir)
for i, input_file in enumerate(input_files):
    # 動画読み込み
    clip = VideoFileClip(input_file)
    # ビデオのカット開始
    clip = clip.subclip(start_t, end_t)

    # 動画のサイズ変更
    clip = clip.resize(width=width)
    # 動画をGIFアニメに変換
    basename_without_ext = os.path.splitext(os.path.basename(input_file))[0]
    output_file = output_dir + basename_without_ext + ".gif"
    clip.write_gif(output_file, fps=fps)
    # 閉じる
    clip.close()
