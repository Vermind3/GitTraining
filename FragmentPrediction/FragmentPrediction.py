import pandas as pd

elementDict = {
    'C' : 12,
    'O' : 16,
    'N' : 14,
    'H' : 1,
    'Cl' : 35,
    'F' : 19,
    'Br' : 80,
    'I' : 127

}

def refineDict(user_input, dictionary):
    new_dict = {char: dictionary.get(char, None) for char in user_input}
    return new_dict
### 简化字典，通过user_input把我们所需要的元素筛选出来形成一个新的字典

def findCombinations(dictionary, target):

    values = sorted(dictionary.values())
    
    def backtrack(remain, combo, index, result):
        if remain == 0:
            result.append(list(combo))
            return
        
        for i in range(index, len(values)):
            if remain - values[i] < 0:
                break
            combo.append(values[i])
    
            backtrack(remain - values[i], combo, i, result)  
            combo.pop()
    results = []
    backtrack(target, [], 0, results)
    return results
### 给一个字典和一个数字，找到这个字典里各个key的和等于这个数字的各种组合,并转化成字符类型
 
def revertToFormula(list_of_lists , dictionary):
    
    reverse_dict = {value: key for key, value in elementDict.items()}
    
    converted_list_of_lists = [[reverse_dict.get(value, '未知值') for value in sublist] for sublist in list_of_lists]
    

    return converted_list_of_lists
#把数字变成字符类型

def refineFormulas(formulas):


    newFormulas = list()
    for sublist in formulas:
        temp = dict()
        for char in sublist:
            temp[char] = temp.get(char,0) + 1
        
        if temp.get('C', 0) != 0 and (int(temp.get('H', 0))/int(temp.get('C', 1))) <= 3:
            newFormulas.append(sublist)
    
    return "no combination for this number" if newFormulas is None else newFormulas
###把formula根据规则精简，去掉那些不可能出现的规则

def count_elements(list_of_lists):


    # 初始化结果列表
    result_list = []
    
    # 遍历每个子列表
    for sublist in list_of_lists:
        # 计算子列表中每个元素的出现次数
        element_counts = {}
        for element in sublist:
            if element in element_counts:
                element_counts[element] += 1
            else:
                element_counts[element] = 1
        
        # 构建计数字符串
        count_str = ''.join([f"{element}{count}" if count > 1 else f"{element}" for element, count in element_counts.items()])
        
        # 添加到结果列表
        result_list.append(count_str)
    
    return result_list
###把formula变成字符+数字的形式

def peak2Formulas(peak : int, elementDict: dict) -> list:
    if peak == 18:
        return ['H2)']
    formulas = findCombinations(elementDict, peak)
    formulas = revertToFormula(formulas, elementDict)
    formulas = refineFormulas(formulas)
    formulas = count_elements(formulas)
    return formulas
##集大成

###def selectThePeak(df)

###file_path = 'your_file.csv' 
###df = pd.read_csv(file_path)

###test
peakList = [15, 18, 56, 31, 29, 30]
fragmentList = []

for peak in peakList:
    temp = peak2Formulas(peak, elementDict)
    fragmentList.append(temp)

print(fragmentList)