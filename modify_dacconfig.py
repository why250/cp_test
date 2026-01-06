
import time

def modify_dac_config(current_dac_index):
    file_path = "DACCONFIG.txt"

    try:
        with open(file_path, "r", encoding='utf-8') as f:
            lines = f.readlines()
        
        new_lines = []
        modified_any = False # Track if any changes were actually made

        for line_idx, line in enumerate(lines):
            # Check if this line corresponds to a DAC from 1 to 7
            is_dac_line = False
            for i in range(1, 8):
                target_string_prefix = f"DAC{i} 5 "
                if target_string_prefix in line:
                    is_dac_line = True
                    # Set all DACs 1-7 to -2.5V initially
                    if i != current_dac_index:
                        if f"DAC{i} 5 -2.5" not in line:
                            new_lines.append(line.replace(f"DAC{i} 5 -4.5", f"DAC{i} 5 -2.5"))
                            modified_any = True
                            print(f"将 DAC{i} 设置为 -2.5V")
                        else:
                            new_lines.append(line)
                    else: # This is the current_dac_index
                        if f"DAC{i} 5 -4.5" not in line:
                            new_lines.append(line.replace(f"DAC{i} 5 -2.5", f"DAC{i} 5 -4.5"))
                            modified_any = True
                            print(f"将 DAC{i} 设置为 -4.5V")
                        else:
                            new_lines.append(line)
                    break # Move to next line once DAC is processed
            if not is_dac_line:
                new_lines.append(line) # Keep non-DAC lines as is

        with open(file_path, "w", encoding='utf-8') as f:
            f.writelines(new_lines)

        if not modified_any:
            print("文件内容未发生改变 (可能已是目标状态)。")

    except FileNotFoundError:
        print(f"错误: 文件 '{file_path}' 未找到。")
    except Exception as e:
        print(f"发生错误: {e}")


if __name__ == "__main__":
    # 示例运行，你可以手动调用 modify_dac_config(i) 来测试
    for i in range(1, 8):
        print(f"\n--- 处理 DAC{i} ---")
        modify_dac_config(i)
        time.sleep(5) # 等待5秒
