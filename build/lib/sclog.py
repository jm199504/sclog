import os
import subprocess
import time
import zipfile
from datetime import datetime

def get_desktop_path():
    if os.name == "posix":  # For macOS and Linux
        return os.path.join(os.path.join(os.environ["HOME"]), "Desktop")
    elif os.name == "nt":  # For Windows
        return os.path.join(os.path.join(os.environ["USERPROFILE"]), "Desktop")
    else:
        raise OSError("Unsupported operating system.")

def record_screen(logcat_filename, output_filename):
    # 启动录屏和日志抓取，添加 --record-audio 参数捕获系统音频
    screen_recording_process = subprocess.Popen(["scrcpy", "--record", "--record-audio", "/sdcard/screen.mp4"])
    logcat_process = subprocess.Popen(["adb", "logcat", "-v", "threadtime", "-f", "/sdcard/{}".format(logcat_filename)])

    print("录屏和日志抓取已开始，请进行您的调试操作。按 Enter 键停止录制和抓取...")

    # 等待用户按下Enter键，录制和抓取将停止
    input()

    # 停止录屏和日志抓取
    screen_recording_process.terminate()
    logcat_process.terminate()

    # 等待一段时间确保进程完全停止
    time.sleep(1)

    # 将录制好的视频和日志文件拉取到本地
    desktop_path = get_desktop_path()
    output_folder = os.path.join(desktop_path, "output")
    os.makedirs(output_folder, exist_ok=True)
    subprocess.run(["adb", "pull", "/sdcard/screen.mp4", os.path.join(output_folder, output_filename)])
    subprocess.run(["adb", "pull", "/sdcard/{}".format(logcat_filename), os.path.join(output_folder, logcat_filename)])
    print("录屏和日志抓取已完成，生成的文件位于桌面的output文件夹中。")


def create_zip(logcat_filename, output_filename, zip_filename):
    desktop_path = get_desktop_path()
    zip_file_path = os.path.join(desktop_path, zip_filename)

    # 创建一个zip文件并将录屏视频和日志文件添加进去
    with zipfile.ZipFile(zip_file_path, "w") as zip_file:
        zip_file.write(os.path.join(desktop_path, "output", output_filename), arcname=output_filename)
        zip_file.write(os.path.join(desktop_path, "output", logcat_filename), arcname=logcat_filename)

    print("文件已成功压缩为：{}".format(zip_file_path))

def main():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    logcat_filename = "logcat_{}.log".format(timestamp)
    output_filename = "video_{}.mp4".format(timestamp)
    zip_filename = "logs_and_screen_{}.zip".format(timestamp)

    record_screen(logcat_filename, output_filename)
    create_zip(logcat_filename, output_filename, zip_filename)

if __name__ == "__main__":
    main()