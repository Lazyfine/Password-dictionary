import itertools
from tqdm import tqdm  # 用于显示进度条

def generate_passwords(keywords, output_file):
    """
    生成密码字典并保存到文件中
    :param keywords: 包含关键信息的列表
    :param output_file: 输出文件的名称（无需输入后缀名）
    """
    # 定义一些常见的密码组合规则
    common_suffixes = ["", "123", "!", "@", "#", "123456", "123456789","1234567890","520","1314","666","888","999","8888","6","8","9","5201314" ]
    common_prefixes = ["", "!", "@", "#"]
    separators = ["", ".", "-", "_", ""]
    
    # 生成所有可能的组合
    passwords = set()  # 使用集合避免重复
    
    # 计算总任务量（用于进度条）
    total_tasks = (
        len(keywords) * 3  # 单个关键信息重复 2 到 4 遍
        + sum(len(list(itertools.permutations(keywords, i))) for i in range(2, min(len(keywords) + 1, 5)))  # 多组关键信息组合
        + sum(len(list(itertools.product(keywords, repeat=i))) for i in range(2, 5))  # 多个关键信息重复组合
    )
    
    # 初始化进度条
    with tqdm(total=total_tasks, desc="生成密码字典") as pbar:
        # 单个关键信息重复 2 到 4 遍
        for keyword in keywords:
            for repeat in range(2, 5):
                passwords.add(keyword * repeat)
                pbar.update(1)  # 更新进度条
        
        # 多组关键信息相互组合（最多 4 个关键信息）
        for combo_length in range(2, min(len(keywords) + 1, 5)):
            for combo in itertools.permutations(keywords, combo_length):
                # 将关键信息与常见的前缀、后缀和分隔符组合
                for prefix in common_prefixes:
                    for suffix in common_suffixes:
                        for sep in separators:
                            # 生成密码
                            password = prefix + sep.join(combo) + suffix
                            passwords.add(password)
                            
                            # 添加大小写变化的组合
                            passwords.add(password.lower())
                            passwords.add(password.upper())
                            passwords.add(password.capitalize())
                pbar.update(1)  # 更新进度条
        
        # 多个关键信息重复组合（如 722722722mimi）
        for repeat in range(2, 5):
            for combo in itertools.product(keywords, repeat=repeat):
                # 将关键信息与常见的前缀、后缀和分隔符组合
                for prefix in common_prefixes:
                    for suffix in common_suffixes:
                        for sep in separators:
                            # 生成密码
                            password = prefix + sep.join(combo) + suffix
                            passwords.add(password)
                            
                            # 添加大小写变化的组合
                            passwords.add(password.lower())
                            passwords.add(password.upper())
                            passwords.add(password.capitalize())
                pbar.update(1)  # 更新进度条
    
    # 将生成的密码写入文件
    print("将密码写入文件...")
    with open(f"{output_file}.txt", "w") as f:
        for password in tqdm(passwords, desc="写入文件"):
            f.write(password + "\n")
    
    print(f"密码字典已生成，保存到 {output_file}.txt 中，共生成 {len(passwords)} 个密码。")

def main():
    # 定义关键信息类别
    categories = {
        "姓名": "请输入姓名（如 zhangsan）：",
        "姓名首字母": "请输入姓名首字母（如 z）：",
        "昵称": "请输入昵称网名（如 xiaoming）：",
        "生日": "请输入生日（如 19901212）：",
        "手机号": "请输入手机号（如 13812345678）：",
        "父姓名": "请输入父亲姓名（如 lisi）：",
        "母姓名": "请输入母亲姓名（如 wangwu）：",
        "兄弟姐妹姓名": "请输入兄弟姐妹姓名（如 wangwu）：",
        "对象姓名": "请输入对象姓名（如 lisi）：",
        "身份证号": "请输入身份证号（如 123456199001011234）：",
        "家乡": "请输入家乡名称（如 beijing）：",
        "幸运数字": "请输入幸运数字（如 888）：",
        "特殊日期": "请输入特殊日期（如 20200202）：",
        "其他信息": "请输入其他关键信息："
    }
    
    keywords = []
    print("请输入关键信息（若无则直接回车跳过）：")
    for category, prompt in categories.items():
        keyword = input(prompt).strip()
        if keyword:
            keywords.append(keyword)
    
    if not keywords:
        print("未输入任何关键信息，程序退出。")
        return
    
    # 获取输出文件名
    output_file = input("请输入输出文件的名称（无需输入后缀名，例如 passwords）：").strip()
    if not output_file:
        output_file = "password_dictionary"  # 默认文件名
    
    # 生成密码字典
    generate_passwords(keywords, output_file)

if __name__ == "__main__":
    main()