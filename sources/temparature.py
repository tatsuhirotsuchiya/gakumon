# セルシウス度->ファーレンハイト度
print("温度を入力してください")
x = input()
x = float(x)
print("セルシウス度:", x)
if x >= -273.15:
    y = 1.8*x + 32
    print("ファーレンハイト度:", y)
else:
    print("温度が低すぎます")
