from os import urandom
import os, tempfile
import binascii


# 翻转字节的任意一位
def flipBit(x, kth):
    x = ord(x)
    if (x & 1 << kth) != 0:
        return chr(x & ~(1 << kth))
    else:
        return chr(x | (1 << kth))


# 十六进制字符串转二进制字符串
def byte_to_binary(n):
    return ''.join(str((n & (1 << i)) and 1) for i in reversed(range(8)))


def hex_to_binary(h):
    return ''.join(byte_to_binary(ord(b)) for b in binascii.unhexlify(h))


origin_text = "hello, shiyanlou"  # 源字符串
changed_text = list(origin_text)
changed_text[1] = flipBit(changed_text[1], 4)
changed_text = ''.join(changed_text)  # 修改后的字符串

with tempfile.NamedTemporaryFile() as fa:
    with tempfile.NamedTemporaryFile() as fb:
        # 通过系统命令行命令获取 hash 值
        def get_hash(fp, text):
            fp.write(text)
            fp.seek(0)
            result = os.popen("openssl dgst -sha1 {}".format(fp.name)).read().split('=')[1].strip()
            print(result)
            return result


        origin_hash = hex_to_binary(get_hash(fa, origin_text))
        changed_hash = hex_to_binary(get_hash(fb, changed_text))

        print(origin_text + ":")
        print(origin_hash)
        print(changed_text + ":")
        print(changed_hash)
        # 计算不同的位数
        print("diff count:",
              reduce(lambda x, y: x + y, [origin_hash[i] == changed_hash[i] for i in range(len(origin_hash))]))
