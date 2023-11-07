with open("output.txt", "r", encoding="utf-8") as file:
    data = file.readlines()

    # for data in file:
    #     if isinstance(eval(data), tuple):
    #         # print("转换成功:", data)
    #         pass
    #     else:
    #         print("转换失败：不是一个元组",data)
    # print(type(eval(data)))

    tuples = [eval(x) for x in data]

    ls = list(filter(lambda x: x[0] != "回复", tuples))
    all = sorted(ls, key=lambda x: int(x[0].replace(",", "")), reverse=True)
    with open("./output2.txt", "w", encoding="utf-8") as f:
        print(*all, file=f, sep="\n")
