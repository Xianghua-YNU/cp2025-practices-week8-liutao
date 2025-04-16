import numpy as np
import matplotlib.pyplot as plt
import time

def f(x):
    return np.sqrt(1 - x**2)

def rectangle_method(f, a, b, N):
    h = (b - a) / N
    total = 0.0
    for i in range(N):
        x = a + i * h
        total += f(x)
    return total * h
    # 学生在此实现矩形法
    # 提示:
    # 1. 计算步长 h = (b - a)/N
    # 2. 使用循环计算每个矩形的面积并累加

def trapezoid_method(f, a, b, N):
    h = (b - a) / N
    total = (f(a) + f(b)) / 2.0
    for i in range(1, N):
        x = a + i * h
        total += f(x)
    return total * h
    # 学生在此实现梯形法
    # 提示:
    # 1. 计算步长 h = (b - a)/N
    # 2. 使用循环计算每个梯形的面积并累加

def calculate_errors(a, b, exact_value):
    N_values = [10, 100, 1000, 10000, 100000]
    h_values = [(b - a)/N for N in N_values]
    rect_errors = []
    trap_errors = []
    for N in N_values:
        rect = rectangle_method(f, a, b, N)
        trap = trapezoid_method(f, a, b, N)
        rect_errors.append(abs(rect - exact_value) / abs(exact_value))
        trap_errors.append(abs(trap - exact_value) / abs(exact_value))
    return (N_values, h_values, rect_errors, trap_errors)
    # 学生在此实现误差计算
    # 提示:
    # 1. 定义不同的N值列表
    # 2. 对每个N值计算两种方法的积分近似值
    # 3. 计算相对误差 = |近似值 - 精确值| / |精确值|

def plot_errors(h_values, rect_errors, trap_errors):
    plt.figure()
    plt.loglog(h_values, rect_errors, 'o-', label='Rectangle Method')
    plt.loglog(h_values, trap_errors, 's-', label='Trapezoid Method')
    h_array = np.array(h_values)
    plt.loglog(h_array, h_array, '--', label='Slope 1 (O(h))')
    plt.loglog(h_array, h_array**2, '--', label='Slope 2 (O(h²))')
    plt.xlabel('Step Size (h)')
    plt.ylabel('Relative Error')
    plt.title('Error vs. Step Size')
    plt.legend()
    plt.grid(True)
    plt.show()
    # 学生在此实现绘图功能
    # 提示:
    # 1. 使用plt.loglog绘制双对数坐标图
    # 2. 添加参考线表示理论收敛阶数
    # 3. 添加图例、标题和坐标轴标签

def print_results(N_values, rect_results, trap_results, exact_value):
    print("N\tRectangle Result\tTrapezoid Result\tRect Error\tTrap Error")
    for N, rect, trap in zip(N_values, rect_results, trap_results):
        rect_err = abs(rect - exact_value) / abs(exact_value)
        trap_err = abs(trap - exact_value) / abs(exact_value)
        print(f"{N}\t{rect:.10f}\t{trap:.10f}\t{rect_err:.4e}\t{trap_err:.4e}")
    # 学生在此实现结果打印
    # 提示: 格式化输出N值和对应积分结果

def time_performance_test(a, b, max_time=1.0):
    exact_value = 0.5 * np.pi

    def test_method(method):
        N = 10
        best_error = float('inf')
        best_N = 0
        start_time = time.time()
        while True:
            t0 = time.time()
            approx = method(f, a, b, N)
            elapsed = time.time() - t0
            if (time.time() - start_time) + elapsed > max_time:
                break
            error = abs(approx - exact_value) / exact_value
            if error < best_error:
                best_error = error
                best_N = N
            N *= 2
        return best_error, best_N

    rect_error, rect_N = test_method(rectangle_method)
    trap_error, trap_N = test_method(trapezoid_method)

    print("\nTime Performance Test (Max Time: {:.1f}s):".format(max_time))
    print(f"Rectangle Method: N={rect_N}, Error={rect_error:.2e}")
    print(f"Trapezoid Method: N={trap_N}, Error={trap_error:.2e}")
    # 学生在此实现性能测试
    # 提示:
    # 1. 从小的N值开始测试
    # 2. 逐步增加N值直到计算时间接近max_time
    # 3. 记录每种方法能达到的最高精度

def calculate_convergence_rate(h_values, errors):
    log_h = np.log(np.array(h_values))
    log_e = np.log(np.array(errors))
    coeffs = np.polyfit(log_h, log_e, 1)
    return coeffs[0]
    # 学生在此实现收敛阶数计算
    # 提示: 使用最小二乘法拟合log(h)和log(error)的关系

def main():
    """主函数"""
    a, b = -1.0, 1.0  # 积分区间
    exact_value = 0.5 * np.pi  # 精确值
    
    print(f"计算积分 ∫_{a}^{b} √(1-x²) dx")
    print(f"精确值: {exact_value:.10f}")
    
    # 计算不同N值下的结果
    N_values = [10, 100, 1000, 10000]
    rect_results = []
    trap_results = []
    
    for N in N_values:
        rect_results.append(rectangle_method(f, a, b, N))
        trap_results.append(trapezoid_method(f, a, b, N))
    
    # 打印结果
    print_results(N_values, rect_results, trap_results, exact_value)
    
    # 计算误差
    _, h_values, rect_errors, trap_errors = calculate_errors(a, b, exact_value)
    
    # 绘制误差图
    plot_errors(h_values, rect_errors, trap_errors)
    
    # 计算收敛阶数
    rect_rate = calculate_convergence_rate(h_values, rect_errors)
    trap_rate = calculate_convergence_rate(h_values, trap_errors)
    
    print("\n收敛阶数分析:")
    print(f"矩形法: {rect_rate:.2f}")
    print(f"梯形法: {trap_rate:.2f}")
    
    # 时间性能测试
    time_performance_test(a, b)

if __name__ == "__main__":
    main()
