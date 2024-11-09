from openai import OpenAI
import json

# 非流式调用
def internlm_gen(prompt,client):
    '''
    LLM生成函数
    Param prompt: prompt string
    Param client: OpenAI client 
    '''
    response = client.chat.completions.create(
        model="internlm2.5-latest",
        messages=[
            {"role": "user", "content": prompt},
      ],
        stream=False
    )
    return response.choices[0].message.content

api_key = 'eyJ0eXBlIjoiSldUIiwiYWxnIjoiSFM1MTIifQ.eyJqdGkiOiI1MDE3MzAzOSIsInJvbCI6IlJPTEVfUkVHSVNURVIiLCJpc3MiOiJPcGVuWExhYiIsImlhdCI6MTczMTE1MTYwMywiY2xpZW50SWQiOiJlYm1ydm9kNnlvMG5semFlazF5cCIsInBob25lIjoiMTgzMzYzMDM4ODIiLCJ1dWlkIjoiOTBmNWYzYWYtNDA5Zi00NGJkLTg4OTQtNDYwZmQ5MTcyZmIxIiwiZW1haWwiOiIiLCJleHAiOjE3NDY3MDM2MDN9.Qk4rPKp7wnxSOlJllonkxaa22Dx8c2eEwH3w4f9_si1eAxv5GIVSM8hJySeh0WQ5HKiLffuxmvhEbLhVElygSQ'
client = OpenAI(base_url="https://internlm-chat.intern-ai.org.cn/puyu/api/v1/",api_key=api_key)

content = """
书生浦语InternLM2.5是上海人工智能实验室于2024年7月推出的新一代大语言模型，提供1.8B、7B和20B三种参数版本，以适应不同需求。
该模型在复杂场景下的推理能力得到全面增强，支持1M超长上下文，能自主进行互联网搜索并整合信息。
"""
prompt = f"""
请帮我从以下``内的这段模型介绍文字中提取关于该模型的信息，要求包含模型名字、开发机构、提供参数版本、上下文长度四个内容，以json格式返回。
`{content}`
"""
res = internlm_gen(prompt,client)
res = res.strip("```json\n").strip("```\n")
res_json = json.loads(res)
print(res_json)