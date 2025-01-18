# Möllendorff-Traditional-Manchu-Conversion

用于将传统满文（如：ᠮᠠᠨᠵᡠ）和穆麟德（Möllendorff）转写式满文（如：manju）进行自动转换。

参考：
- [Latin-Manchu-Transliteration-Tool](https://github.com/foxal/Latin-Manchu-Transliteration-Tool.git)
- [满文转写方案](https://zh.wikipedia.org/wiki/满文转写方案)

## 使用方法

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

