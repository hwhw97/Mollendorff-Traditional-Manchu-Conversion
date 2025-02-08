# Möllendorff-Traditional-Manchu-Conversion

用于将传统满文（如：ᠮᠠᠨᠵᡠ）和穆麟德（Möllendorff）转写式满文（如：manju）进行自动转换。

**参考：**
- [Latin-Manchu-Transliteration-Tool](https://github.com/foxal/Latin-Manchu-Transliteration-Tool.git)
- [满文转写方案](https://zh.wikipedia.org/wiki/满文转写方案)

**相关：**
- [manchu_input_transliteration](https://github.com/jungyitsai/manchu_input_transliteration)
- [Wiktionary: Manchu transliteration](https://en.m.wiktionary.org/wiki/Wiktionary:Manchu_transliteration)

## 使用方法
```text
穆麟德转写中的特殊字符（ž、š、ū）可以直接在文本框输入，也可以基于如下规则输入：
    输入 zv 将自动替换为 ž
    输入 sv 将自动替换为 š
    输入 uv 将自动替换为 ū
例如，可以直接输入 “hūwang wei.” 也可以输入 “huvwang wei.”。
```

### 在线使用 Demo
点击使用在线版 [Demo](https://hwhw97.github.io/Mollendorff-Traditional-Manchu-Conversion)


Demo 更新记录
- 2025-02-08 | v2.0.0
  > 处理穆麟德转写特殊字符输入：
    输入 zv 将自动替换为 ž，输入 sv 将自动替换为 š，输入 zv 将自动替换为 ž
- 2025-02-04 | v1.1.0
  > 优化 t、d 的转写
- 2025-02-01 | v1.0.0
  > 初始版本

### 在 python 中调用
```bash
git clone https://github.com/hwhw97/Mollendorff-Traditional-Manchu-Conversion.git
cd Mollendorff-Traditional-Manchu-Conversion
```

- 自动识别输入的文本是传统满文还是穆麟德转写式满文，并互相转换
```python
from convert_manscript import convert_manscript

text1 = "ᠮᠠᠨᠵᡠ"
text2 = "manju"

print(convert_manscript(text1))  # output: manju
print(convert_manscript(text2))  # output: ᠮᠠᠨᠵᡠ
```

- 如果需要的方向已经确定，也可以不使用自动转换
```python
# 传统满文转穆麟德
from convert_manscript import manscript2mulinde
text1 = "ᠮᠠᠨᠵᡠ"
print(manscript2mulinde(text1)) # output: manju

# 穆麟德转传统满文
from convert_manscript import mulinde2manscript
text2 = "manju"
print(mulinde2manscript(text2)) # output: ᠮᠠᠨᠵᡠ
```

