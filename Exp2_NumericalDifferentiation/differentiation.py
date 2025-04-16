import numpy as np
import matplotlib.pyplot as plt

def f(x):
    """定义测试函数 f(x) = x(x-1)"""
    return x * (x - 1)
    
def forward_diff(f, x, delta):
    """前向差分法计算导数"""
    return (f(x + delta) - f(x)) / delta
   
def central_diff(f, x, delta):
    """中心差分法计算导数"""
    return (f(x + delta) - f(x - delta)) / (2 * delta)

def analytical_derivative(x):
    """解析导数 f'(x) = 2x - 1"""
    return 2 * x - 1

def calculate_errors(x_point=1.0):
    """计算不同步长下的误差"""
    deltas = np.logspace(-2, -14, 13, base=10)
    exact = analytical_derivative(x_point)
    forward_errors = []
    central_errors = []
    for delta in deltas:
        fd = forward_diff(f, x_point, delta)
        cd = central_diff(f, x_point, delta)
        forward_errors.append(abs(fd - exact) / abs(exact))
        central_errors.append(abs(cd - exact) / abs(exact))
    return deltas, forward_errors, central_errors

def plot_errors(deltas, forward_errors, central_errors):
    """绘制误差-步长关系图"""
    plt.figure(figsize=(10, 6))
    
    # 绘制误差曲线
    plt.loglog(deltas, forward_errors, 'o-', label='前向差分', color='orange')
    plt.loglog(deltas, central_errors, 's-', label='中心差分', color='blue')
    
    # 添加理论参考线（斜率为1和2）
    theoretical_deltas = np.array([1e-2, 1e-6])
    plt.loglog(theoretical_deltas, 1e-1 * theoretical_deltas, '--', label='O(δ)', color='gray')
    plt.loglog(theoretical_deltas, 1e-3 * (theoretical_deltas**2), '--', label='O(δ²)', color='black')
    
    # 图表装饰
    plt.xlabel('步长 δ（对数坐标）', fontsize=12)
    plt.ylabel('相对误差（对数坐标）', fontsize=12)
    plt.title('数值微分误差与步长关系', fontsize=14)
    plt.legend()
    plt.grid(True, which='both', linestyle='--', alpha=0.5)
    plt.show()

def print_results(deltas, forward_errors, central_errors):
    """打印计算结果表格"""
    print("\n步长 δ\t\t前向差分误差\t\t中心差分误差")
    print("------------------------------------------------------------")
    for delta, fe, ce in zip(deltas, forward_errors, central_errors):
        # 格式化输出为科学计数法，对齐列
        delta_str = "{:.2e}".format(delta)
        fe_str = "{:.6e}".format(fe)
        ce_str = "{:.6e}".format(ce)
        print(f"{delta_str}\t{fe_str}\t{ce_str}")

def main():
    """主函数"""
    # 学生可以修改测试点
    x_point = 1.0
    
    # 计算误差
    deltas, forward_errors, central_errors = calculate_errors(x_point)
    
    # 打印结果
    print(f"函数 f(x) = x(x-1) 在 x = {x_point} 处的解析导数值: {analytical_derivative(x_point)}")
    print_results(deltas, forward_errors, central_errors)
    
    # 绘制误差图
    plot_errors(deltas, forward_errors, central_errors)
    
    # 以下分析代码可以保留或修改
    forward_best_idx = np.argmin(forward_errors)
    central_best_idx = np.argmin(central_errors)
    
    print("\n最优步长分析:")
    print(f"前向差分最优步长: {deltas[forward_best_idx]:.2e}, 相对误差: {forward_errors[forward_best_idx]:.6e}")
    print(f"中心差分最优步长: {deltas[central_best_idx]:.2e}, 相对误差: {central_errors[central_best_idx]:.6e}")
    
    print("\n收敛阶数分析:")
    mid_idx = len(deltas) // 2
    forward_slope = np.log(forward_errors[mid_idx] / forward_errors[mid_idx-2]) / np.log(deltas[mid_idx] / deltas[mid_idx-2])
    central_slope = np.log(central_errors[mid_idx] / central_errors[mid_idx-2]) / np.log(deltas[mid_idx] / deltas[mid_idx-2])
    
    print(f"前向差分收敛阶数约为: {forward_slope:.2f}")
    print(f"中心差分收敛阶数约为: {central_slope:.2f}")

if __name__ == "__main__":
    main()
