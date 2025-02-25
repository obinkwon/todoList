from torch.utils.data import DataLoader as DL


class DataLoader:
    def __init__(self, tokenized_datasets):
        """
        init 메소드
        """
        # 데이터셋 토큰화
        tokenized_datasets.set_format(
            type="torch", columns=["input_ids", "attention_mask"]
        )
        self.dataloader = DL(tokenized_datasets, batch_size=8, shuffle=True)
