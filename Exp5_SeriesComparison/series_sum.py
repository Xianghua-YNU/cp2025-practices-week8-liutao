import numpy as np
import matplotlib.pyplot as plt

def sum_S1(N):
    """计算第一种形式的级数和：交错级数"""
    s = 0.0
    for n in range(1, 2*N +1):
        term = (-1)**n * n / (n + 1)
        s += term
    return s

def sum_S2(N):
    """计算第二种形式的级数和：两项求和相减"""
    sum1 = 0.0
    sum2 = 0.0
    for n in range(1, N+1):
        sum1 += (2*n -1) / (2*n)
        sum2 += (2*n) / (2*n +1)
    return sum2 - sum1

def sum_S3(N):
    """计算第三种形式的级数和：直接求和"""
    s = 0.0
    for n in range(1, N+1):
        s += 1 / (2*n * (2*n +1))
    return s

def calculate_relative_errors(N_values):
    """计算相对误差"""
    err1, err2 = [], []
    for N in N_values:
        # 计算三个级数的和
        s1 = sum_S1(N)
        s2 = sum_S2(N)
        s3 = sum_S3(N)
        
        # 计算相对误差（避免除以零）
        if s3 == 0:
            e1 = e2 = float('inf')
        else:
            e1 = abs((s1 - s3) / s3)
            e2 = abs((s2 - s3) / s3)
        
        err1.append(e1)
        err2.append(e2)
    return (err1, err2)
    
def plot_errors(N_values, err1, err2):
    """绘制误差分析图"""
    plt.figure(figsize=(10, 6))
    plt.loglog(N_values, err1, 'b-', label='Error of S1')
    plt.loglog(N_values, err2, 'r--', label='Error of S2')
    
    plt.xlabel('N', fontsize=12)
    plt.ylabel('Relative Error', fontsize=12)
    plt.title('Relative Error Comparison (Log-Log Plot)', fontsize=14)
    plt.grid(True, which='both', linestyle='--', alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.show()
    

def print_results():
    """打印典型N值的计算结果"""
    test_N = [10, 100, 1000, 10_000]
    print(f"{'N':<8} | {'S1':<15} | {'S2':<15} | {'S3 (Ref)':<15} | {'Err1':<10} | {'Err2':<10}")
    print("-" * 85)
    for N in test_N:
        s1 = sum_S1(N)
        s2 = sum_S2(N)
        s3 = sum_S3(N)
        err1 = abs((s1 - s3) / s3 if s3 != 0 else float('inf'))
        err2 = abs((s2 - s3) / s3 if s3 != 0 else float('inf'))
        
        # 格式化输出
        print(
            f"{N:<8} | {s1:<15.6e} | {s2:<15.6e} | {s3:<15.6e} | "
            f"{err1:<10.2e} | {err2:<10.2e}"
        )

def main():
    """主函数"""
    # 生成N值序列
    N_values = np.logspace(0, 4, 50, dtype=int)
    
    # 计算误差
    err1, err2 = calculate_relative_errors(N_values)
    
    # 打印结果
    print_results()
    
    # 绘制误差图
    plot_errors(N_values, err1, err2)

if __name__ == "__main__":
    main()
