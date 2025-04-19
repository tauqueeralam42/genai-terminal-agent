import tiktoken

enc_base = tiktoken.get_encoding("o200k_base")
enc_gpt = tiktoken.encoding_for_model("gpt-4o")

message = "Hello World . .. ... "

print(enc_base.encode(message))
print(enc_gpt.encode(message))
