import os
import sys
from PySide2.QtWidgets import QApplication, QFileDialog

def select_directory():
    app = QApplication(sys.argv)
    folder_path = QFileDialog.getExistingDirectory(None, "폴더 선택")
    return folder_path

if __name__ == "__main__":
    # path = select_directory()
    path = "/Users/jdu/Desktop/E"
    print(f"선택된 폴더 경로: {path}")
    result_path = "/Users/jdu/Desktop/errors"
    error_root = os.listdir(path)

    # result path 초기화
    if os.path.exists(result_path):
        os.system(f"rm -rf {result_path}")
    os.mkdir(result_path)

    for dir in error_root:
        if dir == ".DS_Store":
            continue
        error_dir = os.listdir(os.path.join(path, dir))
        for file in error_dir:
            if file == ".DS_Store":
                continue
            file_name = f"E-{dir}-{file}"
            print(f"{os.path.join(result_path, file_name)}")
            os.system(f"cp {os.path.join(path, dir, file)} {os.path.join(result_path, file_name)}")
            