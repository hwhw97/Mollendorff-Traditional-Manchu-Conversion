import re

def deal_special_Latin(word):
    """
    初步处理 拉丁转写 便于后续转为传统满文
    适用于 穆麟德 转写
    在 mulinde2manscript 中调用，不单独调用
    """
    # 使用正则表达式删除 ' 符号前后的空格
    word = re.sub(r'\s*\'\s*', "'", word)
    vowel = ["a", "e", "i", "o", "u", "ū"]
    i = 0
    while i < len(word):
        if word[i] == "g": ##case of "ng+consonant" or final "ng".
                if i < len(word) - 1: ##not final "g"
                    if word[i+1] not in vowel and word[i-1] == "n": #letter "g" in "ng+consonant" case
                        word = word[:i-1] + "N" + word[i+1:]
                elif i == len(word) - 1 and word[i-1] == "n": ##final "g", i.e. "ng" at the final part of a word.
                    word = word[:i-1] + "N"
        i += 1
    return word

def mulinde2manscript(latinword):
    '''
    定义 穆麟德 转 传统满文 函数
    '''
    ManchuScript_Latin_map = {
        "a":"ᠠ", "e":"ᡝ", "i":"ᡳ",
        "o":"ᠣ", "u":"ᡠ", "ū":"ᡡ", "n":"ᠨ",
        "N":"ᠩ", 
        "k":"ᡴ", "g":"ᡤ", "h":"ᡥ",
        "b":"ᠪ", "p":"ᡦ", "s":"ᠰ", "š":"ᡧ",
        "t":"ᡨ᠋", "d":"ᡩ", "l":"ᠯ", "m":"ᠮ",
        "c":"ᠴ", "j":"ᠵ", "y":"ᠶ", "r":"ᡵ",
        "f":"ᡶ", "w":"ᠸ", "k'":"ᠺ", "g'":"ᡬ",
        "h'":"ᡭ", "ts'":"ᡮ", "ts":"ᡮᡟ", "dz":"ᡯ",
        "dzi":"ᡯᡳ", "ž":"ᡰ", "sy":"ᠰᡟ", "c'y":"ᡱᡳ","jy":"ᡷᡳ",
        ",":"᠈", "<":"︽", ".":"᠉", ">":"︾", 
        "?":"︖", "!":"︕", ";":"︔", ":":"᠄", "[":"﹇", "]":"﹈", 
        "{":"︿", "}":"﹀", "\\":"᠁", "|":"︱", "-":" ", 
    }
    # 调用上面定义的函数 deal_special_Latin
    latinword = deal_special_Latin(latinword)
    i = 0
    manjuword = ""
    while i < len(latinword):
        found = False
        # 优先匹配更长的子串（长度为 3 到 1）
        for length in range(3, 0, -1):
            substring = latinword[i:i + length]
            if substring in ManchuScript_Latin_map:
                manjuword += ManchuScript_Latin_map[substring]
                i += length  # 跳过匹配的子串长度
                found = True
                break
        if not found:  # 如果没有匹配到，直接保留原字符
            manjuword += latinword[i]
            i += 1
        # 使用正则表达式，在 `᠈` 或 `᠉` 前添加空格（如果没有空格）
        manjuword = re.sub(r"(?<!\s)([᠈᠉])", r" \1", manjuword)

    return manjuword

def manscript2mulinde(manjuword):
    '''
    定义 传统满文 转 穆麟德 函数
    '''
    ManchuScript_Latin_map = {
        "a":"ᠠ", "e":"ᡝ", "i":"ᡳ",
        "o":"ᠣ", "u":"ᡠ", "ū":"ᡡ", "n":"ᠨ",
        "N":"ᠩ", 
        "k":"ᡴ", "g":"ᡤ", "h":"ᡥ",
        "b":"ᠪ", "p":"ᡦ", "s":"ᠰ", "š":"ᡧ",
        "t":"ᡨ᠋", "d":"ᡩ", "l":"ᠯ", "m":"ᠮ",
        "c":"ᠴ", "j":"ᠵ", "y":"ᠶ", "r":"ᡵ",
        "f":"ᡶ", "w":"ᠸ", "k'":"ᠺ", "g'":"ᡬ",
        "h'":"ᡭ", "ts'":"ᡮ", "ts":"ᡮᡟ", "dz":"ᡯ",
        "dzi":"ᡯᡳ", "ž":"ᡰ", "sy":"ᠰᡟ", "c'y":"ᡱᡳ","jy":"ᡷᡳ",
        ",":"᠈", "<":"︽", ".":"᠉", ">":"︾", 
        "?":"︖", "!":"︕", ";":"︔", ":":"᠄", "[":"﹇", "]":"﹈", 
        "{":"︿", "}":"﹀", "\\":"᠁", "|":"︱", "-":" ", 
    }
    # 创建反向映射字典
    reversed_dict = {v: k for k, v in ManchuScript_Latin_map.items()}
    i = 0
    latinword = ''
    while i < len(manjuword):
        found = False
        # 尝试匹配最长的 Manchu 字符串
        for length in range(2, 0, -1):  # 尝试匹配长度为2或1的子字符串
            substring = manjuword[i:i+length]
            if substring in reversed_dict:
                latinword += reversed_dict[substring]
                i += length
                found = True
                break
        if not found:  # 如果当前字符不在字典中，直接保留
            latinword += manjuword[i]
            i += 1
    latinword = latinword.replace("N","ng")

    return latinword

def detect_script(input_text):
    """
    判断输入是传统满文（manscript）还是拉丁文（mulinde）。
    如果前 5 个字符不包含英文字母，则认为是传统满文，否则是拉丁文。
    返回输入类型：'manscript' 或 'mulinde'。
    """
    # 定义英文26个字母
    english_letters = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    # 检查前5个字符
    for char in input_text[:5]:
        if char in english_letters:
            return "mulinde"  # 输入为拉丁文

    return "manscript"  # 输入为传统满文

def convert_manscript(text):
    """
    根据输入的文本类型调用相应的转换函数。
    """
    script_type = detect_script(text)
    if script_type == "manscript":
        return manscript2mulinde(text)
    elif script_type == "mulinde":
        return mulinde2manscript(text)
    else:
        raise ValueError("Unknown script type.")

def convert_manscript2(text):
    """
    根据输入的文本类型调用相应的转换函数。
    如果输入的是穆麟德，则不转，如果输入的是传统满文，则转为穆麟德
    """
    script_type = detect_script(text)
    if script_type == "manscript":
        return manscript2mulinde(text)
    elif script_type == "mulinde":
        return text
    else:
        raise ValueError("Unknown script type.")