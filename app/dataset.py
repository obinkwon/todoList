import os

import pandas as pd
from datasets import Dataset as Ds


class Dataset:
    def __init__(self):
        """
        init 메소드
        """
        # CSV 파일 로드
        root_dir = os.path.abspath(os.curdir)
        df = pd.read_csv(root_dir + "\\data\\train_data.csv")
        # 텍스트 변환
        df["text"] = df.apply(
            lambda row: f"입력: {row['input']} | 출력: {row['output']}",
            axis=1,
        )

        # Hugging Face Dataset 변환
        self.dataset = Ds.from_pandas(df[["text"]])
