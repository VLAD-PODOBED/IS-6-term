from alphabet import *
import warnings
warnings.filterwarnings("ignore")

latEntropy = 0
kirEntropy = 0
binEntropy = 0
# а) рассчитать энтропию алфавитовна латинице и кириллице входной параметр провизвольный электронный документ
print("Рассчитать энтропию алфавитов: один – на латинице, другой – на кириллице \n")
latEntropy = entropy(text_reader("D://крипта//LABA1.1//LABA1//latin.txt"))
print("Энтропия латиницы: ", latEntropy)
kirEntropy = entropy(text_reader("D://крипта//LABA1.1//LABA1//kirilitsa.txt"))
print("Энтропия кириллицы: ", kirEntropy)
# частоты появления символов алфавитов оформить в виде гистограмм
serialize("D://крипта//LABA1.1//LABA1//probs_lat.xml", probs(text_reader("D://крипта//LABA1.1//LABA1//latin.txt")))
serialize("D://крипта//LABA1.1//LABA1//probs_kir.xml", probs(text_reader("D://крипта//LABA1.1//LABA1//kirilitsa.txt")))

serialize("D://крипта//LABA1.1//LABA1//probs_lat1.xml", count_chars_in_text(text_reader("D://крипта//LABA1.1//LABA1//latin.txt")))
serialize("D://крипта//LABA1.1//LABA1//probs_kir1.xml", count_chars_in_text(text_reader("D://крипта//LABA1.1//LABA1//kirilitsa.txt")))

# б) определить энтропию бинарного алфавита
print("\nДля входных документов, представленных в бинарных кодах, определить энтропию бинарного алфавита \n")
binEntropy = entropy(convert_to_ascii(text_reader("D://крипта//LABA1.1//LABA1//latin.txt")))
print("Энтропия бинарного для документа на латинице: ", binEntropy)
print("Энтропия бинарного для документа на кириллице: ", entropy(convert_to_ascii("D://крипта//LABA1.1//LABA1//kirilitsa.txt")))

# в) подсчитать кол - во информации в ФИО на исх.алфавите и кодах ASCII
print("\nПодсчитать количество информации в сообщении, состоящем из собственных фамилии, имени и отчества\n")
print("Количество информации на латинице: ", quantity_of_information(latEntropy,"Podobed Vladislav Heorhovytsj"))
print("Количество информации на кириллице: ", quantity_of_information(kirEntropy,"Подобед Владислав Георгійович"))
print("Количество информации в ASCII: ", quantity_of_information(binEntropy,convert_to_ascii("Podobed Vladislav Heorhovytsj")))

# г) вероятность 0,1
print("\nПри условии, что вероятность ошибочной передачи единичного бита сообщения составляет\n")
print("Количество информации на латинице с вероятностью 0,1: ", mistake_quantity(0.1,"Podobed Vladislav Heorhovytsj",latEntropy))
print("Количество информации на кириллице с вероятностью 0,1: ", mistake_quantity(0.1,"Подобед Владислав Георгійович",kirEntropy))
print("Количество информации в ASCII с вероятностью 0,1: " , mistake_quantity(0.1,convert_to_ascii("Podobed Vladislav Heorhovytsj"),binEntropy))
# вероятность 0,5
print("\nКоличество информации на латинице с вероятностью 0,5: ",mistake_quantity(0.5,"Podobed Vladislav Heorhovytsj", 1))
print("Количество информации на кириллице с вероятностью 0,5: ",mistake_quantity(0.5,"Подобед Владислав Георгійович",1))
print("Количество информации в ASCII с вероятностью 0,5: ",mistake_quantity(0.5,convert_to_ascii("Podobed Vladislav Heorhovytsj"),1))
# вероятность 1,0
print("\nКоличество информации на латинице с вероятностью 1,0: ",0.0)
print("Количество информации на кириллице с вероятностью 1,0: ",0.0)
print("Количество информации в ASCII с вероятностью 1,0: " ,mistake_quantity(0.999,convert_to_ascii("Podobed Vladislav Heorhovytsj"),binEntropy))
