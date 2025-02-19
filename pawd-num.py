import itertools
from tqdm import tqdm  # 用于显示进度条

def generate_numeric_passwords(output_file, min_length=6, max_length=9):
    """
    生成纯数字字典并保存到文件中
    :param output_file: 输出文件的名称（无需输入后缀名）
    :param min_length: 最小密码长度（默认 6 位）
    :param max_length: 最大密码长度（默认 9 位）
    """
    # 定义数字范围
    digits = "0123456789"
    
    # 生成所有可能的组合
    passwords = set()  # 使用集合避免重复
    
    # 计算总任务量（用于进度条）
    total_tasks = sum(len(digits) ** length for length in range(min_length, max_length + 1))
    
    # 初始化进度条
    with tqdm(total=total_tasks, desc="生成数字字典") as pbar:
        # 遍历密码长度
        for length in range(min_length, max_length + 1):
            # 生成所有可能的数字组合
            for combo in itertools.product(digits, repeat=length):
                password = "".join(combo)
                passwords.add(password)
                pbar.update(1)  # 更新进度条
    
    # 将生成的密码写入文件
    print("将密码写入文件...")
    with open(f"{output_file}.txt", "w") as f:
        for password in tqdm(passwords, desc="写入文件"):
            f.write(password + "\n")
    
    print(f"数字字典已生成，保存到 {output_file}.txt 中，共生成 {len(passwords)} 个密码。")

def main():
    # 获取用户输入的文件名
    output_file = input("请输入输出文件的名称（无需输入后缀名，例如 numeric_passwords）：").strip()
    if not output_file:
        output_file = "numeric_passwords"  # 默认文件名
    
    # 生成数字字典
    generate_numeric_passwords(output_file)

if __name__ == "__main__":
    main()