## Worldlm 使用教程

Worldlm 是一个可国内直连的前端镜像！只需要使用您购买的 API 秘钥，即可无限制的访问各个不同版本的模型！

以下是使用步骤：

1. 请访问 [chat.worldlm.me](https://chat.worldlm.me/)，并注册账号

   <img src="https://github.com/WorldLM/worldlm-ecosystem-docs/blob/xy-docs/docs/materials/image-20241118184901167.png" alt="注册账号" width="30%" />

2. 访问 [chat.worldlm.me](https://chat.worldlm.me/)，并登录，在顶部找到模型菜单

   <img src="https://github.com/WorldLM/worldlm-ecosystem-docs/blob/xy-docs/docs/materials/image-20241118183700668.png" alt="模型菜单" width="70%" />

3. 选择您购买的对应模型，点击“设置API 秘钥”并输入您购买的 API 秘钥

   <img src="https://github.com/WorldLM/worldlm-ecosystem-docs/blob/xy-docs/docs/materials/image-20241118183821365.png" alt="设置API秘钥" width="50%" />

4. 提交后，即可正常使用！

5. 您也可以直接将秘钥应用在您自己的代码中

   <img src="https://github.com/WorldLM/worldlm-ecosystem-docs/blob/xy-docs/docs/materials/image-20241118184118273.png" alt="代码示例" width="50%" />

6. 示例代码：
```python
from openai import OpenAI

client = OpenAI(
    base_url="https://api.pplm.ai",
        api_key="sk-xxxxxx",  # 您购买的API Key
    )

completion = client.chat.completions.create(
    model="gemini-1-5-pro",  # 对应的大模型名称
    messages=[
         {
            "role": "user",
            "content": "What is xxxxx?"
         }
    ]
)
print(completion.choices[0].message.content)
