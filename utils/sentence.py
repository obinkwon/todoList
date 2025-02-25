import os

from transformers import AutoModelForCausalLM, PreTrainedTokenizerFast

root_dir = os.path.abspath(os.curdir)

model = AutoModelForCausalLM.from_pretrained(root_dir + "\\data\\kogpt2-finetuned")
tokenizer = PreTrainedTokenizerFast.from_pretrained(
    "skt/kogpt2-base-v2",
    bos_token="</s>",
    eos_token="</s>",
    unk_token="<unk>",
    pad_token="<pad>",
    mask_token="<mask>",
)


def create_sentence(list):
    """
    문장 생성

    :param list: 단어 리스트
    """
    print(list)

    input_text = f"입력: {', '.join(list)}"
    input_ids = tokenizer.encode(input_text, return_tensors="pt")
    output = model.generate(
        input_ids,
        max_length=len(", ".join(list)) * 5,
        num_return_sequences=1,
        eos_token_id=tokenizer.eos_token_id,
    )
    sentence = tokenizer.decode(output[0], skip_special_tokens=True)
    sentence = sentence.split("출력:")[1]
    return sentence


def tokenize_sentence(examples):
    """
    토큰화

    :param examples: 단어 리스트
    """
    return tokenizer(
        examples["text"], truncation=True, padding="max_length", max_length=64
    )
