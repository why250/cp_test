
import serial
import serial.tools.list_ports

class SerialController:
    """负责所有串口通信逻辑的类"""
    def __init__(self):
        self.ser = None

    def scan_ports(self):
        """扫描并返回可用的串口列表"""
        return [port.device for port in serial.tools.list_ports.comports()]

    def connect(self, port, baudrate=9600):
        """
        连接到指定的串口。
        :param port: 串口号 (e.g., 'COM3')
        :param baudrate: 波特率
        :return: (bool, str) -> (连接是否成功, 错误信息或成功信息)
        """
        if self.ser and self.ser.is_open:
            return False, "已有串口连接，请先断开。"
        
        try:
            self.ser = serial.Serial(port, baudrate, timeout=1)
            return True, f"成功连接到 {port}"
        except serial.SerialException as e:
            self.ser = None
            return False, f"无法打开串口 {port}\n错误: {e}"

    def disconnect(self):
        """断开当前串口连接"""
        if self.ser and self.ser.is_open:
            self.ser.close()
            self.ser = None
            print("串口已断开")

    @property
    def is_connected(self):
        """检查串口是否连接"""
        return self.ser is not None and self.ser.is_open

    # 后续功能的占位符
    def send_command(self, command):
        if not self.is_connected:
            return "错误：串口未连接"
        # 串口命令需要是字节串，通常以换行符结尾
        self.ser.write(command.encode('utf-8') + b'\n')
        print(f"发送: {command}")
        # 这里可以添加读取返回值的逻辑
        return "发送成功"
