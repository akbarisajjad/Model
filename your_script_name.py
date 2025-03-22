from huggingface_hub import InferenceClient

# استفاده از متغیر محیطی برای API Key (امن‌تر)
import os
api_key = os.getenv("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")  # API Key را در محیط Codespace تنظیم کنید

# ایجاد کلاینت
client = InferenceClient(
    provider="together",
    api_key=api_key,  # استفاده از متغیر محیطی
)

# درخواست چت
completion = client.chat.completions.create(
    model="Qwen/Qwen2.5-Coder-32B-Instruct",
    messages=[
        {
            "role": "user",
            "content": "What is the capital of France?"
        }
    ],
    max_tokens=500,
)

# نمایش نتیجه
print(completion.choices[0].message.content)
