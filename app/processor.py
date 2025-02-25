import os

from tqdm import tqdm


class Processor:
    def __init__(self, train, train_dataloader, optimizer, model, device, tokenizer):
        """
        init 메소드
        """
        root_dir = os.path.abspath(os.curdir)
        # 학습 루프
        num_epochs = 10
        if train:
            for epoch in range(num_epochs):
                model.train()
                loop = tqdm(train_dataloader, leave=True)
                for batch in loop:
                    optimizer.zero_grad()

                    input_ids = batch["input_ids"].to(device)
                    attention_mask = batch["attention_mask"].to(device)

                    # 모델 실행
                    outputs = model(
                        input_ids=input_ids,
                        attention_mask=attention_mask,
                        labels=input_ids,
                    )
                    loss = outputs.loss

                    # 역전파 & 최적화
                    loss.backward()
                    optimizer.step()

                    # 진행률 표시
                    loop.set_description(f"Epoch {epoch}")
                    loop.set_postfix(loss=loss.item())

            model.save_pretrained(root_dir + "\\data\\kogpt2-finetuned")
