def find_password(password_file, target_password):
    """
    查找密码是否存在于文件中
    :param password_file: 密码字典文件的路径
    :param target_password: 要查找的密码
    """
    try:
        with open(password_file, "r") as f:
            passwords = f.read().splitlines()  # 读取所有密码并去除换行符
        
        # 查找密码
        if target_password in passwords:
            print(f"密码 '{target_password}' 存在于文件中。")
        else:
            print(f"密码 '{target_password}' 不存在于文件中。")
    except FileNotFoundError:
        print(f"文件 {password_file} 未找到，请检查文件路径。")
    except Exception as e:
        print(f"发生错误：{e}")

def main():
    # 获取用户输入的密码字典文件路径
    password_file = input("请输入密码字典文件的路径（例如：passwords.txt）：").strip()
    if not password_file:
        print("未输入文件路径，程序退出。")
        return
    
    while True:
        # 获取用户输入的密码
        target_password = input("请输入要查找的密码（输入 'exit' 退出程序）：").strip()
        if target_password.lower() == 'exit':
            print("程序退出。")
            break
        
        # 查找密码
        find_password(password_file, target_password)

if __name__ == "__main__":
    main()
