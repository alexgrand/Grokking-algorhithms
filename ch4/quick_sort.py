import random

def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr.pop(random.randrange(0, len(arr)))
        less = [i for i in arr[:] if i <= pivot]
        greater = [i for i in arr[:] if i > pivot]

        # less = []
        # greater = []

        # for i in arr[:]:
        #     if i <= pivot: less.append(i)
        #     else: greater.append(i) 

        return quick_sort(less) + [pivot] + quick_sort(greater)

arr = [5406, 7098, 1650, 7584, 5686, 7619, 6715, 8718, 8359, 8295, 8490, 1637, 815, 1369, 5415, 8254, 6893, 6473, 1150, 1463, 3332, 2780, 6821, 4643, 4136, 4699, 2382, 4513, 7257, 984, 4285, 3796, 8420, 6182, 870, 333, 6284, 5866, 2734, 8055, 9043, 8323, 9308, 915, 611, 9733, 1774, 8131, 2622, 6317, 9249, 6358, 4890, 1458, 2494, 4543, 8307, 3577, 9272, 4040, 8815, 773, 3087, 4581, 5775, 7334, 4881, 2883, 7109, 2403, 7681, 6384, 2623, 6968, 7444, 4849, 95, 756, 7456, 6733, 8026, 6246, 8947, 6992, 6410, 9928, 4907, 8247, 379, 8383, 3451, 9877, 4827, 7754, 2502, 7842, 6793, 8467, 267, 5049, 8617, 2969, 7865, 3023, 3298, 1948, 6483, 7910, 2121, 2732, 1545, 6265, 8481, 1569, 4925, 5561, 9409, 917, 9368, 1619, 4357, 1146, 4610, 7907, 6943, 5664, 7723, 5508, 4786, 5182, 4778, 3974, 9304, 9959, 299, 7743, 7521, 1772, 9411, 7085, 4130, 203, 6228, 9701, 1965, 4254, 412, 1730, 8564, 2497, 511, 7293, 1610, 9381, 16, 6279, 7112, 5875, 3998, 5914, 9631, 1249, 4377, 7672, 1405, 1125, 6967, 2485, 9035, 766, 3961, 614, 2909, 4373, 4478, 4793, 356, 4687, 7824, 6287, 253, 1032, 603, 5620, 1961, 5907, 6184, 4609, 1661, 9059, 383, 5475, 610, 9863, 8016, 3759, 2572, 3667, 2594, 8980, 8366, 4085, 3795, 1000, 4579, 3073, 5004, 5165, 4137, 3331, 5544, 5309, 206, 696, 723, 3186, 5102, 8091, 4506, 9713, 1887, 4882, 2345, 4289, 3704, 9996, 3, 7320, 3252, 8498, 8414, 5905, 5403, 9910, 2851, 9273, 6238, 9288, 1977, 4193, 3355, 2678, 122, 2783, 2556, 9636, 916, 3387, 8945, 5995, 8128, 1578, 4932, 3847, 4983, 3260, 9258, 1257, 5598, 5363, 49, 2050, 3291, 3749, 4830, 7066, 8186, 7366, 2317, 9145, 7369, 4770, 4462, 5348, 2084, 231, 6897, 1496, 2239, 3619, 5993, 2247, 7355, 8285, 9794, 1707, 3718, 5485, 7123, 2253, 7269, 7158, 1412, 6966, 9534, 4648, 476, 3837, 758, 6971, 7323, 6863, 9576, 8641, 2205, 6016, 5112, 400, 9033, 1226, 5616, 5153, 6947, 2920, 682, 7397, 5651, 7416, 8642, 8509, 2042, 185, 6877, 2970, 3241, 3803, 2386, 4389, 6197, 269, 4571, 5942, 4293, 2101, 1872, 9297, 4262, 445, 6572, 1459, 4177, 5824, 3711, 7306, 1838, 1168, 8045, 2666, 3177, 3458, 2131, 28, 3123, 6625, 6056, 8288, 1055, 3429, 3568, 9461, 7626, 3984, 3892, 2789, 160, 5744, 1166, 6723, 127, 334, 61, 6827, 6010, 1992, 1573, 4548, 194, 9363, 855, 4279, 6822, 6855, 4955, 977, 7846, 9446, 9058, 4670, 1250, 2881, 3598, 7598, 1924, 5075, 6965, 972, 8435, 7975, 9718, 6350, 4364, 9643, 7055, 5236, 9393, 2544, 9419, 1410, 8035, 7800, 3248, 8638, 3752, 3913, 1665, 5224, 2901, 7918, 2581, 6908, 5665, 3936, 7133, 5966, 4174, 841, 8580, 488, 1039, 6713, 241, 4444, 8513, 6067, 359, 6437, 5595, 4446, 6970, 1381, 9524, 3792, 4090, 4189, 8909, 2053, 7088, 4453, 6193, 9710, 505, 9053, 8130, 8076, 7205, 3546, 2114, 3349, 2639, 4573, 1008, 7389, 1973, 5622, 7957, 9903, 3151, 4999, 3222, 1679, 4892, 1072, 9861, 589, 8150, 8479, 4514, 1727, 4499, 6773, 1031, 7068, 5605, 716, 8152, 6708, 8143, 6762, 8349, 6844, 2910, 3754, 7229, 8455, 8672, 7187, 1220, 2779, 2492, 1739, 9294, 2583, 2377, 8750, 2640, 2399, 9414, 8769, 6545, 6037, 7030, 8612, 1216, 6906, 6632, 622, 9661, 6315, 52, 1528, 5746, 9855, 2968, 1183, 9299, 2872, 4566, 9348, 7494, 3775, 7504, 7016, 5335, 8656, 1983, 557, 5603, 168, 3481, 633, 1639, 4233, 9444, 7531, 2156, 9502, 1862, 2132, 3939, 2612, 1430, 7385, 828, 5427, 3994, 9044, 4302, 1981, 5927, 3554, 8154, 2688, 9003, 8378, 3159, 3437, 7292, 2518, 6057, 8602, 9100, 8163, 5644, 2304, 3945, 9738, 2079, 7116, 8842, 8707, 2237, 9606, 7138, 1306, 8476, 3191, 5094, 1914, 4666, 478, 5016, 8796, 1318, 161, 5103, 204, 9086, 4646, 9157, 4239, 6890, 4914, 9237, 3915, 9543, 4823, 2318, 3692, 2515, 7146, 4037, 9824, 7353, 5789, 5985, 8257, 6909, 147, 8607, 9117, 4230, 1291, 6392, 7194, 1764, 5970, 2854, 9999, 704, 7173, 7548, 5934, 5023, 2381, 5379, 9506, 4985, 9189, 4064, 2589, 8377, 2177, 1959, 6650, 6324, 3652, 1810, 6597, 4016, 5924, 4022, 5395, 133, 3556, 1503, 9494, 5755, 7688, 2958, 6709, 6166, 6610, 9062, 5606, 9037, 73, 7053, 2684, 1171, 8115, 4023, 362, 474, 2106, 729, 391, 23, 7084, 5788, 7311, 8708, 3680, 9371, 856, 8096, 7510, 30, 4409, 1787, 4049, 6090, 5734, 7727, 144, 8759, 1575, 8554, 4635, 1548, 9912, 5633, 4025, 1710, 9604, 7993, 12, 3083, 3849, 142, 920, 6574, 1598, 218, 3612, 2002, 8679, 4889, 4105, 6618, 5629, 8976, 4012, 9741, 8687, 2660, 8132, 9550, 180, 9066, 8820, 1601, 5208, 8466, 275, 9870, 953, 1616, 7333, 3509, 44, 8576, 8703, 8487, 8484, 4165, 5009, 3463, 4686, 9674, 5718, 8870, 4110, 1734, 78, 5354, 3238, 7945, 3207, 8592, 2891, 6935, 8676, 2149, 3263, 3914, 8889, 6509, 6224, 4851, 4202, 3399, 1285, 6640, 625, 1455, 4576, 949, 1507, 9324, 2354, 111, 4471, 2746, 7056, 3560, 4745, 5506, 6794, 8345, 432, 8242, 3142, 2578, 7348, 9533, 3194, 6460, 112, 5280, 353, 4248, 6099, 2187, 2884, 7120, 7432, 7307, 4988, 2775, 7999, 80, 1967, 8822, 4934, 5424, 137, 1400, 4718, 2641, 3089, 6946, 6502, 2924, 3859, 4131, 2196, 6949, 5831, 3606, 5880, 2657, 396, 5933, 7384, 5294, 6270, 182, 3900, 2035, 2995, 1109, 2981, 7382, 5709, 8451, 9740, 5211, 8631, 361, 243, 8813, 4734, 4119, 8415, 6330, 9691, 573, 772, 9993, 8530, 25, 8878, 7215, 4370, 939, 5154, 1332, 4148, 555, 271, 8100, 4916, 7906, 5183, 7448, 9329, 1310, 2962, 343, 6898, 5433, 1999, 9447, 9476, 3844, 5795, 3258, 4852, 7673, 3779, 3821, 342, 1243, 930, 884, 8776, 324, 1693, 4263, 954, 8274, 6085, 371, 7595, 5756, 8463, 9547, 1741, 4926, 9022, 2325, 6419, 5643, 8098, 804, 735, 5503, 7014, 964, 6032, 368, 7105, 4542, 1275, 795, 1235, 2118, 7268, 2467, 2781, 2524, 6825, 8868, 426, 491, 7642, 7288, 1537, 742, 9287, 1087, 3255, 3566, 9426, 2299, 4322, 4565, 8292, 4634, 4728, 7965, 4965, 7049, 4351, 8927, 5051, 6255, 2597, 260, 4355, 4187, 2554, 447, 77, 1863, 8538, 2676, 9608, 3724, 3017, 5017, 536, 879, 843, 6159, 9109, 4869, 5221, 3242, 9799, 5625, 9350, 8187, 9893, 7537, 7404, 4052, 3466, 9961, 6116, 2526, 470, 5623, 6403, 3659, 5867, 3296, 3920, 2630, 5054, 574, 2737, 5770, 2742, 3400, 701, 8936, 6273, 6001, 7388, 7781, 7237, 270, 8953, 9385, 648, 2625, 1687, 2201, 3669, 4787, 8449, 2593, 8112, 1826, 3501, 3352, 6178, 9875, 9234, 6530, 7556, 7585, 2495, 6171, 4266, 4141, 2472, 1813, 381, 9612, 3432, 70, 2420, 8147, 2871, 8999, 3778, 9111, 2919, 6548, 4860, 4590, 2686, 7751, 8036, 2482, 6730, 2422, 5490, 4708, 5095, 461, 8483, 314, 8289, 3826, 449, 9320, 4927, 1100, 9669, 6563, 3934, 1074, 4720, 6035, 2077, 5978, 3396, 698, 5172, 5144, 2227, 1013, 2134, 2615, 7470, 6226, 5330, 3604, 7689, 7386, 6775, 7471, 6452, 1015, 509, 5610, 522, 9471, 2753, 358, 9839, 5115, 9598, 1737, 5300, 6695, 6229, 7281, 1265, 7430, 1159, 136, 6060, 8362, 3313, 9916, 5496, 7151, 2982, 5060, 3289, 5583, 7024, 6234, 5778, 2334, 72, 7073, 1516, 9082, 5992, 4211, 1283, 2434, 9703, 2509, 3581, 9309, 3673, 3264, 8023, 3609, 1893, 3906, 5217, 3729, 7503, 1232, 6665, 3283, 1353, 1406, 1181, 8236, 5621, 1322, 5327, 5068, 7837, 5841, 4839, 5840, 6048, 5761, 7633, 494, 7236, 9341, 7583, 5566, 5219, 3621, 2170, 5307, 5281, 3919, 9307, 6303, 8799, 1656, 8606, 1828, 1997, 9667, 9182, 3790, 1206, 956, 1919, 8371, 6338, 4604, 1053, 3689, 4423, 1372, 923, 7434, 1037, 5235, 3809, 8237, 9834, 2067, 3239, 3295, 330, 4904, 5359, 6232, 6857, 3202, 373, 1023, 8165, 3854, 4680, 6939, 1123, 6230, 8978, 782, 4219, 9045, 8745, 2939, 6221, 6347, 4168, 2529, 2632, 1214, 5660, 9563, 4015, 7419, 6661, 8074, 8193, 6720, 1780, 8439, 8260, 7651, 5577, 1913, 4290, 4647, 9048, 2262, 1026, 9159, 3045, 5991, 5362, 1916, 9118, 1138, 3842, 6564, 5383, 48, 4554, 9177, 6426, 1668, 3165, 247, 1935, 765, 9918, 9402, 6231, 4733, 8832, 4653, 9652, 13, 8373, 7387, 336, 545, 3417, 9540, 9666, 5998, 4947, 8895, 6983, 1435, 3408, 1686, 9452, 4354, 1174, 6760, 623, 386, 6209, 3204, 9769, 4593, 3717, 4359, 6953, 1020, 3476, 747, 5168, 7347, 92, 409, 8268, 720, 2505, 8299, 8944, 1394, 4695, 2486, 6743, 7345, 2974, 248, 4191, 473, 7296, 2598, 3734, 9683, 5977, 8109, 8963, 6797, 9087, 3928, 4369, 5733, 821, 7923, 2774, 2506, 6134, 1014, 1910, 3288, 9364, 1151, 8300, 1204, 4880, 1726, 918, 2250, 3918, 4612, 7674, 1230, 3011, 2731, 3696, 6451, 8203, 9202, 152, 4789, 4754, 5680, 2185, 3773, 827, 9023, 4639, 8862, 9102, 7826, 6117, 8144, 8218, 1835, 4034, 4683, 6309, 9140, 7390, 4980, 9825, 7297, 926, 9628, 9649, 7128, 1319, 2940, 9212, 6581, 9509, 1161, 9784, 8581, 7244, 1532, 3538, 7742, 7383, 4962, 7276, 6525, 9642, 6700, 8311, 6199, 8024, 3630, 9954, 2312, 1173, 9197, 1523, 4216, 2654, 2957, 6683, 1493, 5104, 1119, 3136, 8917, 8764, 2491, 2681, 7131, 8111, 8786, 8108, 7143, 6955, 9688, 6240, 3158, 5471, 2811, 1224, 689, 5356, 5177, 9635, 5342, 922, 7656, 9478, 867, 5436, 5290, 7647, 4360, 3280, 4115, 7700, 8057, 762, 9922, 5311, 4966, 8857, 3435, 2148, 9230, 126, 96, 9169, 5586, 8858, 702, 7017, 3334, 2914, 787, 2352, 4588, 7318, 8771, 8849, 293, 7549, 7447, 3359, 8145, 7726, 2469, 5941, 8510, 1277, 251, 1383, 3820, 2460, 8876, 4704, 5381, 9141, 178, 9491, 7705, 1941, 307, 5077, 5594, 2933, 7592, 1393, 9629, 1312, 4715, 3145, 5917, 1139, 5816, 5434, 4657, 6353, 4755, 4390, 8417, 894, 209, 4527, 1213, 4066, 846, 9955, 1883, 4275, 6094, 229, 9538, 4994, 7018, 8851, 8093, 1514, 2087, 9378, 5111, 258, 7178, 2562, 186, 8067, 7301, 9871, 9734, 8548, 9219, 6675, 1731, 4414, 9847, 5061, 1804, 7641, 1492, 7522, 3491, 7060, 8860, 8620, 2988, 5870, 4475, 1307, 7676, 8983, 2700, 3409, 1269, 6765, 7207, 9727, 7578, 1544, 3051, 4362, 8078, 2219, 3091, 6589, 9763, 3493, 2645, 7823, 4014, 519, 8499, 7127, 8012, 4393, 7499, 9805, 3549, 3865, 8190, 4336, 2095, 8200, 8861, 1203, 3144, 6070, 3500, 836, 540, 529, 4507, 5344, 1951, 3681, 6124, 1338, 2410, 4160, 7441, 966, 4884, 3771, 9793, 8609, 8706, 5446, 1688, 6385, 1131, 9006, 7285, 771, 1001, 4677, 8261, 9170, 6740, 2841, 5317, 4172, 6143, 1498, 7708, 2906, 8309, 541, 2236, 6316, 3557, 609, 5657, 7022, 1054, 839, 8431, 9840, 6934, 6205, 7692, 105, 6587, 9945, 9886, 7964, 2913, 7757, 1776, 3973, 8774, 7039, 5074, 1425, 8871, 5830, 1303, 1374, 7813, 2356, 2136, 8686, 5125, 280, 8283, 3572, 4467, 7289, 88, 727, 1221, 2951, 3559, 4685, 4083, 3516, 7803, 882, 851, 5853, 792, 810, 1803, 799, 5822, 1600, 3693, 7981, 2575, 6109, 9572, 4084, 5758, 5627, 5951, 9160, 6259, 5100, 3515, 5902, 1111, 6023, 6631, 7582, 3322, 2587, 3907, 1672, 8586, 8155, 7417, 6456, 9072, 5690, 719, 5726, 158, 3037, 1708, 7883, 312, 108, 7602, 1474, 7741, 6902, 451, 3127, 4873, 1740, 6157, 5952, 191, 5953, 1295, 1402, 5810, 5319, 3528, 8657, 234, 7899, 6376, 6261, 7573, 385, 6329, 5500, 2892, 5815, 6959, 7118, 2973, 3887, 1335, 730, 1356, 7796, 991, 4531, 2859, 6081, 6688, 1884, 1247, 6084, 2006, 5339, 7299, 7897, 7744, 8072, 9281, 6026, 439, 5939, 411, 6431, 7490, 8477, 2202, 9051, 9618, 4537, 7174, 2119, 3647, 7858, 1038, 5796, 3879, 6285, 437, 6592, 7772, 4502, 1282, 7209, 6560, 7452, 7240, 2459, 7110, 7894, 1647, 2975, 5488, 3532, 1006, 1954, 1148, 7033, 2414, 8808, 5807, 6977, 4445, 6397, 9536, 2097, 7272, 2870, 7733, 6418, 1736, 508, 2322, 8951, 1572, 5407, 2827, 224, 8457, 8677, 9525, 4625, 6471, 6082, 1428, 5538, 2516, 2090, 4469, 3960, 9181, 9678, 6484, 7180, 6051, 415, 4350, 2441, 8170, 2698, 7925, 3188, 1248, 8587, 1712, 5797, 3804, 969, 1533, 6239, 5384, 8956, 4822, 1217, 4320, 8001, 3330, 751, 4627, 4919, 4503, 8210, 9422, 4557, 1742, 2926, 3440, 8346, 6655, 2098, 8852, 4615, 3183, 3300, 8308, 2546, 2801, 5554, 9776, 2252, 6635, 3798, 3702, 1454, 2577, 8105, 8002, 9298, 2393, 7854, 4846, 6761, 1822, 999, 8003, 1855, 7541, 9172, 372, 5198, 3551, 5425, 994, 3125, 9106, 2543, 5466, 1933, 8334, 1096, 4021, 5122, 2, 8892, 3534, 8802, 5110, 7974, 9619, 3468, 9883, 9176, 6441, 8195, 5315, 3550, 3285, 9679, 8662, 1714, 3665, 808, 318, 3840, 6622, 3618, 5585, 754, 8715, 7807, 2154, 9480, 705, 9760, 1505, 6805, 3876, 5772, 5673, 17, 1705, 2480, 8508, 82, 9722, 7695, 2626, 1102, 9407, 5575, 8, 3851, 4523, 7450, 9493, 6119, 2051, 284, 5491, 3327, 3924, 1238, 4420, 7392, 4813, 3972, 5454, 5299, 7977, 5825, 8825, 5987, 4386, 4732, 1814, 5039, 2959, 7529, 1010, 5884, 2268, 8405, 5428, 4592, 9526, 862, 2557, 3529, 5043, 2693, 6596, 9166, 1144, 3406, 2199, 5510, 791, 9695, 9398, 6211, 3005, 1847, 2019, 5520, 2786, 1952, 7806, 9848, 1732, 8392, 4614, 8882, 686, 9255, 2813, 1579, 9806, 2671, 7801, 1903, 9344, 3723, 1963, 4000, 9987, 3740, 6659, 2844, 5369, 2764, 2706, 7442, 5227, 6047, 413, 4515, 7480, 9638, 4169, 7524, 6489, 4005, 9487, 130, 2553, 4225, 456, 586, 2027, 8107, 2874, 1684, 216, 1471, 1649, 1817, 3716, 4785, 8785, 4429, 1411, 7000, 6192, 7982, 5440, 3774, 8275, 2288, 1557, 7152, 7786, 3062, 807, 3963, 840, 4008, 1944, 3543, 6569, 6951, 6528, 550, 6017, 58, 3379, 9133, 8791, 2164, 2820, 9253, 2264, 909, 1070, 7283, 7115, 6018, 4192, 6776, 7710, 196, 2624, 8681, 331, 3338, 9057, 1478, 4700, 9692, 3567, 6341, 783, 1728, 5762, 7769, 6144, 6266, 6223, 7933, 317, 2309, 9347, 6500, 6841, 697, 7857, 7555, 9345, 6912, 8424, 995, 9209, 4654, 1426, 9001, 2258, 9284, 9017, 2993, 8704, 3117, 5149, 7263, 4741, 6276, 7702, 3200, 3457, 9498, 3819, 4595, 2620, 9644, 7875, 2534, 3765, 2795, 7878, 1512, 6929, 2049, 2287, 1560, 2435, 1920, 2616, 4767, 7082, 9597, 5980, 8063, 4738, 959, 9648, 7640, 6008, 2394, 3889, 8702, 4441, 9665, 3641, 8442, 2839, 2290, 9217, 5158, 8101, 5310, 8789, 8403, 4971, 7967, 8337, 3995, 7893, 263, 5693, 2060, 2912, 8621, 2687, 3793, 3614, 9575, 7061, 2916, 6442, 3323, 4618, 2778, 6916, 2368, 8529, 2426, 5204, 8960, 8205, 891, 2302, 5736, 2963, 4458, 5012, 1922, 4044, 5968, 9991, 6275, 9532, 5266, 4665, 4264, 3685, 8994, 6198, 1384, 3615, 1323, 3565, 1842, 7094, 6671, 1840, 7890, 4209, 1770, 8537, 2065, 1771, 9331, 8846, 5106, 8637, 7372, 626, 1690, 5729, 1762, 7302, 9909, 8993, 6383, 7712, 8754, 8317, 5011, 2931, 8881, 7340, 5541, 3192, 6130, 4650, 9830, 6818, 1350, 8691, 1556, 5396, 8781, 6940, 7044, 1382, 8221, 2408, 7603, 3324, 7012, 6732, 8397, 4406, 3675, 9165, 4811, 3467, 3293, 2998, 8391, 7594, 5698, 5151, 3988, 2596, 928, 4679, 6160, 8355, 1011, 3780, 8828, 21, 9456, 5247, 2709, 8021, 5862, 7394, 2054, 7691, 3739, 4491, 7685, 6066, 1255, 2876, 9881, 4396, 4569, 2158, 1632, 9207, 5499, 3046, 5832, 3926, 4056, 515, 3818, 8948, 3132, 9814, 9735, 8080, 4403, 4197, 4380, 3035, 7810, 7825, 7934, 176, 2188, 8430, 7989, 1773, 2750, 5969, 1132, 5872, 5511, 5278, 7570, 6322, 1546, 1135, 8763, 5305, 2656, 4412, 477, 890, 9388, 2500, 9377, 778, 8921, 9000, 3412, 2921, 24, 1839, 5611, 354, 4309, 3510, 4970, 1268, 9548, 8632, 6829, 3407, 2782, 1256, 8244, 1190, 3929, 8893, 4834, 1678, 4215, 3426, 5423, 7776, 6938, 2305, 6831, 913, 5687, 6444, 9544, 6833, 2868, 2178, 3885, 4731, 5570, 8543, 5556, 7218, 310, 7291, 1891, 7519, 369, 3169, 1279, 7458, 9617, 5692, 1348, 858, 9767, 908, 2889, 2704, 4203, 4145, 3698, 8341, 5608, 924, 8280, 9154, 9585, 6787, 286, 6750, 124, 9195, 1192, 6524, 4078, 3247, 770, 6235, 8935, 5711, 2691, 989, 7183, 5896, 3786, 8019, 4348, 5502, 6873, 4693, 5479, 2416, 4391, 6034, 4407, 2980, 3383, 6799, 4792, 9933, 7787, 1327, 9515, 3342, 4218, 6465, 7611, 8788, 32, 4872, 8294, 9187, 2473, 6931, 6819, 183, 4030, 9483, 9243, 9535, 5550, 1095, 9068, 9334, 6449, 4782, 7006, 7193, 7696, 8184, 5044, 6540, 7379, 9810, 6519, 3823, 2353, 1018, 2360, 7859, 4933, 6371, 1133, 1988, 6215, 9450, 768, 3428, 462, 6777, 3908, 9301, 2056, 8409, 4138, 3944, 8623, 4807, 9697, 8157, 4242, 852, 3077, 6585, 4166, 273, 2525, 3703, 965, 9519, 4017, 5898, 1657, 7275, 3421, 5938, 3395, 3168, 8368, 714, 3705, 5429, 3211, 6748, 3639, 8151, 7277, 11, 7520, 6461, 5020, 6292, 4509, 8485, 5582, 638, 7313, 6577, 2894, 1060, 7867, 588, 3448, 4363, 4858, 6398, 1555, 5082, 7913, 9895, 4029, 8888, 3281, 8069, 4861, 3269, 2743, 7792, 5764, 7367, 7682, 7331, 1696, 8472, 4605, 9094, 5695, 8158, 724, 2020, 2432, 9858, 6680, 4656, 8905, 3845, 9685, 2279, 4504, 3518, 7420, 5277, 5129, 9395, 7260, 1987, 5218, 3208, 880, 7572, 6522, 2137, 145, 8812, 418, 9867, 6753, 6780, 9280, 9433, 6555, 9650, 8995, 7819, 2631, 6370, 5741, 43, 5766, 9322, 7352, 517, 6975, 9125, 5456, 4282, 646, 1175, 6059, 1446, 8194, 5155, 5855, 784, 2023, 3571, 8358, 1357, 2866, 6118, 6268, 8669, 5926, 8573, 6454, 5222, 3651, 9790, 6611, 2537, 6608, 5560, 1711, 4944, 1270, 1484, 4496, 9074, 139, 8119, 1846, 4326, 3305, 5545, 4456, 2045, 8031, 1101, 5990, 9352, 6112, 6052, 6964, 5126, 3679, 66, 8412, 5850, 1565, 9408, 5392, 5242, 285, 6836, 6074, 2427, 3890, 5548, 8532, 8056, 5251, 1143, 7711, 2263, 6187, 6321, 8541, 5377, 8110, 4794, 8282, 3940, 4963, 5542, 4908, 5414, 9808, 6207, 6734, 6218, 5273, 1800, 3453, 8413, 6477, 3579, 1149, 9340, 8930, 6699, 6495, 6123, 583, 4157, 4597, 1874, 3762, 7896, 3055, 4342, 8400, 3290, 1978, 9798, 1811, 5888, 5276, 8050, 2248, 4901, 4340, 4207, 7321, 4864, 9906, 7921, 8122, 1974, 5739, 6883, 8169, 2443, 4809, 1868, 4250, 4563, 547, 9820, 8731, 3808, 7431, 3745, 8741, 9994, 9351, 5435, 4195, 7106, 6790, 3801, 7969, 4159, 5587, 9774, 3100, 9857, 5900, 9382, 8478, 6296, 319, 2224, 7898, 4777, 5340, 4027, 3385, 1984, 5467, 911, 2010, 7606, 3634, 51, 3649, 3482, 6511, 7015, 2015, 1098, 37, 9093, 3533, 9653, 9923, 3474, 1084, 4465, 7137, 7374, 3101, 7063, 9700, 6241, 8688, 5385, 6381, 5212, 487, 2701, 2677, 2383, 8135, 5180, 568, 1447, 440, 9931, 4820, 3825, 1611, 6751, 9574, 3038, 3060, 6213, 9551, 5890, 4622, 4255, 6103, 2358, 7407, 7461, 8082, 2895, 5813, 9613, 8241, 5045, 1966, 9914, 790, 6919, 546, 7932, 5647, 3746, 9119, 6306, 9366, 9431, 8139, 8777, 6941, 6567, 7885, 6455, 734, 4842, 2365, 4329, 6667, 4094, 9460, 9986, 8762, 5206, 233, 3099, 7996, 8512, 9570, 7214, 9539, 3642, 2401, 7713, 4672, 341, 7059, 3278, 2375, 5116, 3866, 2614, 5225, 9454, 8535, 8209, 9399, 1841, 1613, 8175, 814, 4076, 325, 7614, 6446, 6638, 9283, 388, 2089, 4617, 1833, 6601, 8178, 5127, 9640, 1549, 5380, 6005, 5370, 3224, 2523, 2165, 9726, 7406, 7324, 125, 3102, 2477, 931, 4961, 4308, 1234, 1468, 1995, 4902, 4401, 4221, 5639, 1986, 4930, 6510, 6154, 9316, 874, 781, 2670, 579, 4847, 3512, 6505, 8198, 5925, 9416, 4845, 387, 4194, 3902, 4494, 5956, 3923, 5040, 4895, 7368, 320, 1580, 4897, 3190, 6771, 5426, 6000, 9639, 8624, 3930, 7371, 6813, 3479, 2651, 5006, 950, 1571, 1290, 2223, 8284, 3806, 3050, 7988, 6277, 8798, 3245, 1769, 3212, 755, 9663, 1583, 3227, 5791, 5975, 9085, 2212, 3315, 5190, 1136, 746, 5133, 9027, 9902, 4228, 5536, 4501, 7863, 7725, 700, 8296, 8518, 2406, 8709, 1909, 8675, 4004, 9081, 4986, 174, 8133, 9927, 2638, 1536, 7732, 6343, 8434, 5655, 9380, 5946, 7396, 8633, 2108, 7607, 6921, 5243, 3916, 1491, 5684, 4795, 7962, 532, 3138, 4522, 62, 8546, 1114, 7184, 8171, 8126, 6045, 5248, 2350, 4210, 4536, 2182, 3697, 1448, 6672, 2086, 6806, 3860, 8095, 6253, 7664, 9989, 2835, 5522, 925, 5748, 1525, 8406, 4562, 906, 8937, 3709, 7663, 6582, 957, 3489, 8008, 502, 3589, 6195, 8916, 8805, 6744, 1163, 9624, 1976, 5814, 5438, 5666, 3022, 6129, 9850, 3732, 4664, 6704, 2570, 7941, 4943, 9319, 3354, 7089, 6860, 5893, 6135, 2462, 9343, 832, 7349, 3953, 7958, 2173, 7937, 6283, 3401, 4843, 3054, 4452, 6400, 4840, 4552, 3982, 1912, 8227, 4298, 4723, 2564, 4440, 6843, 2235, 3178, 983, 5486, 2116, 1258, 4156, 4311, 2797, 7453, 327, 7046, 7464, 5670, 6151, 166, 9578, 8875, 4427, 9257, 5614, 9835, 4050, 817, 173, 1207, 8946, 5688, 6469, 2180, 5394, 2978, 7956, 6536, 5135, 5869, 2487, 8077, 5683, 8270, 1211, 1308, 8500, 7130, 7202, 4577, 8674, 9206, 495, 1184, 2016, 8790, 9841, 2333, 2724, 4526, 5185, 4118, 1744, 6252, 6038, 6758, 1768, 1457, 6882, 6249, 9786, 2927, 8877, 2470, 5763, 5961, 9046, 5376, 5231, 3596, 1648, 5079, 1538, 6645, 6357, 5915, 84, 9303, 2590, 871, 3175, 2380, 2838, 8018, 5464, 4519, 2855, 384, 3555, 2267, 2210, 2643, 8665, 6960, 8168, 9878, 2777, 4109, 5578, 6049, 8752, 8758, 4288, 3364, 1423, 7788, 5593, 1968, 9720, 4749, 355, 4178, 9425, 2001, 663, 888, 1643, 3133, 9310, 4696, 420, 4128, 4524, 5661, 5202, 9215, 6447, 7798, 5535, 7119, 5474, 7841, 8803, 8555, 5532, 9716, 1237, 6696, 3811, 6870, 6167, 4258, 523, 9689, 7698, 3389, 5174, 8146, 1597, 9785, 6407, 6351, 5259, 5337, 3539, 9947, 9647, 5321, 9029, 7658, 6837, 4371, 1453, 9553, 9587, 8885, 5887, 8497, 7724, 5501, 8250, 7413, 1623, 9024, 2144, 4967, 539, 5, 6735, 9132, 5780, 5553, 20, 8693, 1561, 9375, 2922, 2535, 4899, 2349, 9467, 4009, 4530, 6278, 3952, 7411, 1337, 3719, 1500, 141, 5178, 6840, 3155, 226, 298, 5836, 1325, 5589, 8246, 7983, 4485, 6141, 208, 3431, 1969, 2674, 2313, 8327, 7462, 4327, 9747, 5549, 4292, 2512, 9560, 7922, 2221, 617, 8929, 722, 4642, 9866, 4231, 6918, 1127, 1588, 2608, 3095, 2110, 8792, 5932, 6814, 3563, 1029, 2452, 9211, 340, 9588, 7991, 5949, 6264, 6887, 4810, 8865, 5048, 4637, 2259, 7947, 4259, 9637, 9495, 452, 649, 2278, 5727, 2193, 9937, 1314, 675, 7978, 6901, 8310, 6466, 7223, 9122, 9030, 9765, 9836, 8350, 7446, 9286, 8482, 1079, 2261, 8880, 6245, 503, 2488, 7659, 7870, 3173, 8188, 7832, 7953, 8348, 3284, 877, 5742, 2274, 4691, 8438, 914, 150, 6565, 9982, 2833, 2122, 7889, 7667, 4964, 9034, 7154, 3737, 7443, 5160, 3075, 7437, 3442, 8628, 3185, 7581, 1642, 9601, 4662, 6491, 4616, 2886, 306, 2373, 9469, 9979, 8795, 8342, 6028, 820, 7072, 5352, 6497, 7486, 3644, 8286, 1118, 4280, 4714, 4204, 6409, 4490, 7785, 5645, 6148, 1836, 2189, 3893, 9194, 986, 6219, 3365, 9296, 2712, 4374, 1530, 8504, 5885, 5654, 709, 5349, 3195, 7220, 9424, 1005, 5450, 613, 4544, 6251, 3444, 8164, 6995, 4428, 3958, 8810, 5714, 8755, 8090, 8222, 604, 490, 2857, 1692, 1477, 8528, 8103, 5579, 7400, 75, 1153, 9537, 7264, 9367, 9121, 9138, 5386, 1284, 1567, 8626, 937, 7599, 6990, 7410, 9890, 3006, 9200, 2314, 9817, 496, 5410, 9788, 9226, 7316, 7828, 7255, 6936, 7047, 6737, 3372, 4941, 8712, 4862, 4954, 6423, 3020, 9090, 2277, 1606, 64, 1562, 3301, 5920, 3473, 2510, 537, 4299, 7748, 8473, 7267, 8700, 4432, 2928, 1755, 7399, 5834, 7657, 3254, 2580, 6616, 68, 5482, 543, 5838, 1504, 566, 3275, 1881, 1293, 948, 8301, 4508, 6520, 6677, 4051, 9392, 3487, 3047, 9300, 5431, 8243, 4006, 246, 4183, 8501, 8588, 7212, 2216, 4430, 9687, 6007, 7747, 7402, 4358, 5874, 9921, 2043, 1301, 7534, 8804, 1779, 8007, 5008, 118, 7108, 6387, 3605, 2695, 6176, 5848, 2041, 4815, 7924, 8567, 1805, 1625, 9844, 7764, 4582, 5098, 4753, 2682, 5260, 4366, 423, 1287, 3237, 5119, 7455, 2115, 2445, 4517, 4960, 5820, 4443, 3221, 5374, 344, 7198, 2877, 6854, 5849, 7866, 2987, 6594, 7735, 2629, 3027, 8933, 1854, 154, 1703, 5472, 2195, 3682, 5973, 179, 1674, 7433, 1612, 5286, 1939, 3043, 4716, 967, 1860, 7050, 7944, 1117, 3519, 8534, 997, 5539, 8125, 3674, 4483, 3028, 3881, 3594, 7928, 3128, 5047, 498, 2634, 1077, 5706, 4162, 3007, 2138, 9739, 6088, 3741, 9038, 2389, 2018, 3783, 9134, 9901, 2817, 5540, 4651, 9789, 4973, 693, 7159, 6923, 7817, 4087, 5038, 2395, 1751, 8043, 3638, 7135, 3791, 134, 2559, 7616, 7591, 865, 1176, 1022, 6222, 1009, 9458, 6626, 6856, 3812, 947, 3033, 2762, 6480, 5678, 5895, 8730, 165, 5089, 5331, 5067, 9952, 4771, 5313, 6679, 3146, 6058, 6889, 3302, 4447, 7629, 3277, 8575, 5671, 3584, 7332, 8199, 3157, 3085, 811, 1915, 7600, 4392, 9978, 458, 3012, 3636, 4123, 4232, 4806, 3797, 7326, 2409, 6042, 3303, 3495, 1179, 9607, 4667, 4352, 1093, 4802, 7749, 3848, 5930, 9084, 3504, 1550, 5332, 1925, 1675, 3210, 4816, 4058, 5013, 4281, 9546, 2303, 8015, 2400, 5518, 8262, 1422, 8659, 3004, 6173, 1630, 5175, 8843, 9292, 8097, 8448, 2438, 7092, 2719, 597, 6920, 7948, 514, 6072, 2986, 3274, 6389, 4773, 1543, 9171, 5790, 7829, 4938, 4659, 752, 1904, 5019, 6314, 8172, 8847, 8859, 2943, 5767, 1857, 671, 9804, 6479, 933, 2140, 4875, 1980, 2996, 4692, 6323, 2907, 2366, 4799, 9749, 177, 2591, 1539, 838, 9829, 958, 4331, 7722, 1063, 8596, 9686, 4375, 7508, 7378, 3008, 1271, 9099, 3249, 4488, 1923, 3588, 7175, 1215, 3341, 3872, 339, 8321, 935, 9655, 7058, 1521, 2257, 89, 7075, 4729, 6532, 4154, 7615, 7445, 8979, 4466, 6634, 2306, 3721, 6534, 6716, 2713, 2169, 4945, 3813, 6111, 1246, 9415, 3733, 2689, 3875, 5879, 302, 3755, 69, 3592, 8361, 6866, 2971, 6666, 1837, 6746, 7423, 2341, 7408, 250, 9880, 425, 7513, 1409, 5069, 1280, 5809, 8743, 3545, 3067, 892, 9924, 6991, 1676, 7917, 1825, 2044, 5215, 2475, 3153, 2882, 6668, 6566, 6267, 5358, 5173, 4757, 2808, 7811, 619, 9803, 9240, 6299, 1202, 5997, 2652, 2179, 1819, 8608, 4214, 6932, 9520, 405, 4450, 7856, 2990, 9041, 6366, 309, 5572, 4011, 6373, 2600, 2944, 6043, 8845, 7650, 641, 1651, 3772, 4170, 1783, 582, 1172, 4482, 5240, 667, 4774, 2749, 8932, 6917, 4418, 6470, 360, 1263, 8728, 4701, 1879, 1547, 7648, 2269, 835, 5445, 1483, 8614, 3758, 6646, 5296, 951, 5730, 4946, 8838, 1702, 3993, 8934, 8514, 3477, 8102, 6756, 2423, 151, 554, 635, 8724, 1697, 9384, 5723, 2603, 8996, 5320, 376, 788, 3478, 2243, 6933, 7395, 5455, 6399, 2508, 872, 8232, 6795, 5350, 1931, 3465, 1706, 4096, 3542, 5187, 9970, 666, 1046, 4690, 3261, 4589, 1666, 6155, 7968, 9566, 5284, 1028, 1225, 9323, 9369, 86, 9148, 4495, 3267, 65, 3664, 7718, 7533, 8029, 3413, 4556, 6115, 4019, 7586, 138, 3134, 3570, 9152, 4283, 3416, 9107, 8698, 7261, 8468, 9672, 2648, 8114, 2849, 7512, 7593, 2220, 2046, 7096, 1241, 8864, 2823, 1094, 7649, 3443, 2348, 8304, 8066, 5906, 8465, 3954, 6915, 6644, 5389, 9190, 1519, 9151, 4661, 8663, 6741, 6295, 4829, 8474, 2292, 4042, 7161, 1080, 642, 9964, 9729, 1502, 2374, 3213, 9167, 9758, 9615, 6029, 5275, 1626, 8086, 3086, 5632, 1440, 5162, 8544, 8977, 9634, 6544, 7485, 680, 3064, 8756, 9474, 3350, 9282, 7861, 5916, 3388, 2772, 6989, 6798, 2128, 4269, 7129, 9750, 3225, 9753, 9736, 3843, 3470, 8428, 4870, 5792, 7492, 4535, 238, 3748, 3223, 9517, 10, 960, 3311, 3781, 6421, 1778, 657, 3656, 2387, 7091, 3233, 2449, 8914, 2129, 6624, 1761, 8883, 6257, 6812, 7377, 7338, 1404, 3712, 3266, 54, 4769, 7252, 1518, 6985, 6838, 8984, 5005, 9512, 6360, 2232, 8826, 9373, 4276, 6468, 9976, 4660, 6501, 1305, 1850, 1795, 7460, 9600, 7527, 3671, 9807, 8148, 8928, 8408, 4740, 3987, 2730, 7065, 5984, 4600, 7909, 3391, 2705, 7156, 2364, 3464, 5186, 9602, 5612, 471, 5960, 5361, 4675, 7279, 2093, 6434, 6217, 7864, 6712, 9389, 3997, 308, 2716, 9161, 5828, 4558, 1365, 8121, 6164, 1896, 4344, 3370, 2569, 8834, 5923, 2911, 7601, 2773, 8551, 5787, 7070, 895, 3507, 7176, 5323, 3485, 6952, 5289, 7210, 4489, 3942, 9879, 288, 2490, 793, 9549, 7995, 8634, 6098, 4175, 5134, 8041, 8136, 9974, 6978, 4587, 1107, 2792, 3339, 3251, 1316, 1618, 2672, 2343, 4103, 159, 8673, 5213, 5964, 7428, 2754, 9218, 2369, 5856, 6726, 6345, 3163, 7365, 5719, 942, 672, 3886, 6181, 9567, 7997, 785, 4318, 5351, 5216, 1108, 8196, 7843, 4124, 9437, 4434, 8117, 7391, 2768, 1638, 3358, 1746, 6328, 7300, 9236, 8515, 1859, 9849, 252, 6515, 7706, 7080, 5892, 9112, 8272, 562, 4306, 2133, 4236, 5341, 3314, 9846, 4580, 6576, 2392, 6848, 7589, 7704, 6248, 1510, 9168, 7631, 3367, 4074, 571, 1926, 3344, 9250, 7895, 4877, 7535, 467, 2501, 3287, 970, 9946, 5090, 8060, 4261, 9479, 1818, 223, 2390, 4413, 8506, 7425, 4167, 7090, 806, 9174, 1975, 2956, 629, 5118, 4013, 8338, 9521, 4102, 102, 4088, 6445, 4737, 1475, 2362, 6019, 9403, 4055, 8255, 577, 9777, 2181, 1299, 8256, 2905, 4710, 3162, 7057, 1154, 8010, 2465, 9725, 5303, 9015, 4324, 6225, 548, 526, 4798, 3196, 7767, 8734, 7887, 1331, 6853, 6040, 7850, 5345, 3957, 8736, 9448, 4991, 4717, 4464, 3980, 1313, 618, 4082, 1685, 2175, 3063, 5564, 7354, 2126, 2275, 9056, 6127, 567, 6779, 927, 1034, 2830, 9175, 2217, 9876, 2246, 5823, 7412, 1328, 8894, 2937, 2163, 4888, 779, 2991, 9244, 9795, 5063, 9645, 9127, 2791, 5854, 7489, 6414, 3530, 6073, 6189, 1856, 389, 8682, 9497, 7144, 9440, 5821, 3320, 4196, 7142, 1760, 3310, 4345, 7950, 1347, 2800, 4758, 1831, 658, 3318, 8088, 7720, 3271, 5521, 816, 3472, 8134, 9499, 8429, 7025, 2005, 3756, 584, 8039, 4984, 7622, 2976, 2112, 859, 3576, 5334, 6694, 6531, 2429, 5783, 8695, 887, 8462, 5668, 3286, 9889, 975, 8998, 6354, 3728, 9507, 2765, 9139, 5214, 3661, 2323, 7007, 8571, 9971, 5099, 332, 2547, 4127, 4081, 4594, 5234, 9400, 1254, 7990, 4674, 2265, 4975, 7163, 4053, 6706, 3653, 6851, 7206, 3480, 8639, 4367, 8517, 8536, 3425, 2471, 3325, 5565, 5963, 2200, 8684, 9026, 4628, 7635, 7467, 5596, 8427, 1689, 5159, 1442, 8207, 7755, 352, 5355, 5447, 113, 1876, 5712, 8779, 4383, 6537, 6573, 9256, 8153, 9098, 4760, 7804, 7558, 5373, 3678, 4387, 3730, 7350, 4722, 878, 8723, 3171, 71, 8692, 866, 1433, 8042, 1905, 6550, 3802, 5569, 6907, 9561, 2424, 7728, 3025, 5773, 5617, 7571, 2898, 8907, 6742, 1577, 6458, 8224, 4314, 3236, 6332, 266, 1419, 5745, 9511, 7357, 650, 6488, 753, 4033, 7188, 1788, 4246, 9633, 8973, 3910, 837, 4910, 3531, 8454, 1898, 3895, 3346, 845, 3034, 5817, 2710, 4923, 6050, 9396, 2703, 1177, 199, 5312, 8259, 7502, 9473, 640, 1620, 5448, 4411, 8761, 6815, 4108, 3445, 3270, 8841, 2143, 3216, 2760, 6648, 6974, 9594, 3608, 5451, 2582, 3635, 6003, 8697, 3084, 8931, 3578, 1401, 1274, 3981, 7035, 7026, 9809, 4253, 407, 988, 5195, 2183, 7525, 9421, 9856, 7518, 961, 3582, 454, 1646, 1733, 1298, 4878, 5318, 3384, 8694, 2718, 6203, 7245, 4818, 8192, 5808, 9173, 1193, 9391, 9208, 5287, 5839, 5052, 8231, 9031, 8471, 4835, 1236, 2739, 2890, 5143, 4310, 4706, 2447, 211, 9486, 645, 8727, 1791, 7197, 2208, 397, 6642, 6015, 3056, 5325, 2606, 1585, 6297, 9054, 5737, 2994, 3938, 1792, 8768, 6846, 3461, 627, 5191, 802, 3074, 2610, 6538, 2376, 8127, 7543, 2665, 9872, 1044, 2863, 5591, 2240, 5878, 464, 7491, 5083, 4800, 8899, 8967, 8910, 3090, 9386, 5241, 7243, 8908, 1723, 7495, 1735, 8160, 3855, 5105, 3427, 9730, 9453, 9913, 363, 8034, 5675, 3398, 7992, 2679, 4243, 6826, 3595, 6055, 8590, 1467, 9293, 6168, 1341, 3688, 8240, 3419, 8569, 4958, 3498, 8486, 6770, 5107, 7259, 8574, 6030, 4335, 4257, 1104, 8705, 2661, 1427, 5628, 239, 9822, 5042, 2707, 3736, 2166, 3925, 9390, 5314, 6607, 5858, 8266, 1677, 9837, 1749, 4442, 5283, 9852, 7111, 2771, 7816, 2955, 8939, 6145, 3366, 7258, 6288, 6429, 710, 869, 8258, 2551, 5681, 8542, 9383, 4903, 3540, 5169, 9821, 4163, 7731, 2370, 3201, 8874, 6258, 8619, 4493, 3328, 5619, 4630, 6552, 6697, 9737, 7361, 3297, 395, 8906, 7125, 8613, 3094, 2650, 93, 2552, 4062, 9582, 8495, 6620, 9333, 6766, 1339, 3989, 5131, 9869, 2566, 3390, 2847, 5576, 8725, 4698, 6817, 7141, 7790, 6670, 1380, 7181, 3831, 659, 4989, 3726, 587, 8726, 4473, 7036, 99, 3031, 8269, 1827, 3897, 155, 5552, 3817, 4601, 7011, 2539, 7930, 844, 1953, 2011, 8488, 5637, 4631, 5777, 3977, 2388, 7848, 8519, 6755, 9342, 5613, 2094, 8652, 2647, 1097, 7473, 4173, 1765, 8333, 8550, 5378, 3964, 8783, 2498, 7459, 255, 5372, 2339, 5226, 2867, 2740, 2226, 3695, 3257, 2479, 2329, 9370, 8185, 2888, 6653, 9500, 5150, 7662, 9778, 50, 3321, 6024, 3629, 5514, 8814, 7818, 8970, 2228, 8585, 2070, 2038, 1873, 7563, 6988, 7031, 3166, 834, 4868, 8385, 7660, 4915, 7646, 4570, 2440, 4856, 7775, 3206, 210, 1392, 9658, 9670, 875, 322, 4541, 2430, 2514, 2744, 6041, 2117, 681, 8748, 4931, 5184, 2033, 3527, 8059, 4621, 3088, 5050, 9007, 9338, 8083, 721, 3317, 7882, 1081, 1743, 7778, 170, 606, 4668, 3492, 1662, 2983, 2431, 8440, 8835, 9091, 5442, 5861, 3526, 7290, 4135, 6649, 3181, 5092, 3999, 337, 5954, 1645, 7538, 9070, 9721, 3486, 6411, 6065, 7500, 6674, 1724, 5805, 189, 9992, 6725, 9313, 8699, 7186, 3430, 1704, 2836, 2153, 1027, 6605, 3948, 3103, 7791, 2807, 2542, 1387, 283, 4492, 6394, 434, 3394, 9627, 4575, 7665, 4120, 5430, 2151, 1059, 8322, 1716, 7588, 2068, 1064, 3869, 4498, 1165, 4957, 6518, 6412, 9261, 1041, 7901, 9973, 3141, 4500, 5494, 9263, 3727, 8214, 1709, 7753, 7239, 9510, 6613, 5176, 2503, 6643, 4832, 6478, 3573, 6250, 3231, 575, 1194, 1464, 801, 9812, 1437, 6993, 6096, 9405, 7709, 2733, 8436, 2184, 4394, 2832, 1947, 4468, 8075, 654, 6783, 8923, 8572, 2493, 7770, 6121, 8229, 5944, 4457, 9671, 9346, 7675, 1892, 5751, 5724, 9146, 7248, 221, 6660, 1201, 1929, 9888, 4619, 3877, 6861, 4454, 896, 9213, 3857, 5078, 7286, 3040, 8823, 1345, 8562, 5818, 8886, 9681, 6769, 7575, 979, 8335, 6852, 6475, 9622, 9137, 6185, 4113, 3650, 3386, 1964, 2336, 8904, 6693, 9942, 7463, 5994, 9120, 4315, 6832, 2885, 6895, 3093, 8401, 4068, 9028, 4071, 7830, 53, 8411, 8811, 607, 850, 5037, 4304, 4384, 1870, 3524, 595, 7604, 9246, 585, 7637, 316, 6493, 6617, 163, 864, 1396, 3381, 8655, 5109, 5519, 4032, 6202, 5132, 3161, 3042, 6586, 9773, 1300, 533, 5108, 9260, 3882, 7880, 8565, 9404, 3361, 500, 5462, 5674, 265, 9925, 5919, 6170, 5441, 7780, 295, 4436, 4334, 7756, 9754, 6956, 1946, 3039, 9432, 853, 4020, 8773, 4026, 2538, 8604, 4891, 9064, 6331, 4583, 6183, 5704, 2436, 9269, 3180, 3600, 9262, 998, 8913, 6308, 4323, 76, 985, 9124, 9568, 3548, 5205, 6339, 8605, 455, 3333, 9577, 7140, 8492, 6080, 6175, 1067, 8290, 5207, 9956, 4638, 9939, 2934, 5034, 3753, 4759, 8618, 6925, 3878, 1321, 7287, 4198, 4368, 528, 5194, 4669, 4993, 9552, 7436, 2207, 8352, 8690, 8447, 7774, 3611, 2058, 305, 486, 7405, 6583, 9832, 2272, 2439, 6280, 4561, 7376, 3658, 9005, 6006, 2541, 8235, 4640, 8598, 7561, 9349, 4511, 5769, 3182, 9899, 7551, 9191, 4844, 3637, 94, 5779, 4347, 1942, 861, 6482, 521, 9142, 5634, 338, 2215, 9413, 1466, 7099, 7003, 9662, 4125, 3663, 4270, 148, 438, 5279, 513, 4739, 4405, 7955, 3536, 4572, 9069, 1875, 684, 4397, 6492, 599, 6, 3450, 2711, 7219, 6372, 6981, 9756, 9965, 2785, 7590, 9199, 4826, 3410, 9484, 8068, 5417, 6792, 3114, 5058, 5282, 823, 5863, 2229, 2763, 7278, 6774, 5696, 9654, 2586, 457, 8990, 8985, 4272, 9468, 3522, 893, 3053, 6165, 5437, 9783, 6036, 3955, 4247, 9968, 3701, 5891, 2815, 4313, 976, 7013, 4775, 6244, 7041, 2824, 708, 6512, 4400, 1563, 1882, 6161, 3048, 2599, 3121, 9988, 9312, 1631, 6778, 9898, 6724, 2346, 5136, 3415, 8038, 6546, 4274, 364, 5199, 1436, 8065, 6417, 3715, 6402, 9223, 6424, 6305, 9185, 4776, 2952, 6237, 9406, 9372, 1844, 1016, 9149, 5996, 6663, 2337, 6401, 8660, 4356, 9267, 5473, 3662, 2372, 2545, 4002, 2611, 7579, 7960, 1806, 9205, 1370, 2950, 8556, 9932, 6547, 5931, 2953, 4812, 244, 1490, 2310, 8683, 5679, 2331, 1624, 9238, 4874, 4300, 9445, 7542, 741, 739, 3256, 2588, 8896, 2633, 2805, 2474, 4913, 7122, 6506, 1485, 6557, 60, 5901, 4730, 8395, 1481, 9302, 1445, 215, 8070, 8622, 9732, 8390, 7942, 8064, 2715, 5463, 2214, 2347, 7330, 8444, 7329, 9482, 8423, 2242, 5897, 6342, 5147, 4724, 3520, 2105, 9556, 2549, 4713, 7358, 2192, 9513, 2419, 9668, 6476, 7943, 8048, 2293, 3835, 5903, 6374, 3363, 3668, 4854, 268, 9110, 8339, 5527, 3152, 6710, 6786, 9907, 8732, 8459, 5626, 6504, 8106, 7935, 8988, 683, 9831, 4151, 4567, 776, 9558, 9430, 9279, 8589, 6982, 4972, 3505, 8302, 4097, 201, 2826, 7931, 3115, 249, 5071, 8142, 8735, 7250, 2653, 326, 1763, 7694, 576, 401, 5648, 780, 9900, 5419, 5271, 3156, 9129, 1209, 8678, 4791, 2507, 3523, 1071, 6549, 3521, 4200, 7409, 7451, 3057, 9530, 1182, 3096, 2102, 9434, 6754, 757, 3971, 7077, 4303, 1416, 9951, 6348, 2669, 5469, 2276, 7216, 119, 707, 14, 2413, 1377, 4783, 6973, 687, 2548, 9232, 7177, 6623, 4780, 1413, 1376, 8840, 4070, 2697, 2295, 5835, 404, 8809, 8666, 3111, 1367, 1669, 4940, 4900, 1245, 2437, 483, 290, 2755, 9646, 6247, 4437, 1767, 945, 7153, 2822, 4244, 5641, 5819, 3613, 6204, 2696, 7809, 4265, 1488, 3475, 1943, 9192, 5480, 7639, 1242, 5909, 1103, 3956, 4339, 5452, 5753, 9518, 5393, 9103, 1178, 8566, 1617, 8421, 7429, 6872, 2878, 4382, 6633, 2646, 4603, 8202, 9060, 9693, 348, 8252, 5263, 4144, 9254, 1794, 8747, 1276, 7341, 5601, 9938, 7501, 4997, 7147, 6494, 9930, 2900, 7497, 941, 1700, 3852, 8248, 2412, 1757, 3174, 235, 5459, 4584, 9555, 8685, 5504, 8281, 2887, 8251, 1750, 5886, 8279, 6464, 7312, 1594, 5084, 4098, 800, 2925, 3645, 6606, 3660, 5721, 873, 8975, 2635, 4419, 3506, 6731, 8749, 1050, 6850, 1414, 1663, 3691, 3423, 9012, 6260, 651, 8991, 4825, 5512, 1752, 4950, 2751, 6702, 1397, 2842, 8751, 4841, 605, 90, 7952, 4727, 1352, 5662, 5140, 6957, 2197, 774, 5523, 9860, 107, 559, 5076, 8450, 5752, 6114, 616, 8046, 8087, 7182, 3418, 4349, 3149, 8720, 3986, 1223, 2540, 9, 3393, 6830, 5559, 7839, 1444, 8887, 1122, 3061, 3282, 1487, 8897, 98, 4229, 5254, 7168, 7403, 501, 9554, 2363, 7062, 1180, 6865, 9420, 5189, 740, 9252, 4114, 375, 9764, 2289, 9920, 5546, 2609, 1197, 6517, 3218, 9410, 7393, 4116, 7855, 5253, 5388, 7027, 4694, 6884, 9605, 2517, 3014, 1129, 2464, 7224, 2147, 662, 5250, 6627, 7653, 6044, 4402, 7102, 4260, 8658, 8711, 3949, 7222, 8386, 8044, 3459, 750, 2351, 8005, 7620, 9221, 2683, 561, 5604, 7336, 4459, 6025, 8780, 2617, 3010, 7514, 4879, 9374, 6703, 4186, 3941, 4176, 4361, 3587, 8511, 6020, 7265, 809, 9950, 8729, 7745, 2806, 7439, 6937, 9203, 9676, 5731, 9589, 7627, 2407, 8545, 2530, 7739, 8890, 9771, 4673, 5024, 9188, 6413, 6834, 6639, 676, 3602, 1629, 2761, 3105, 3164, 1602, 4744, 2758, 2520, 5113, 5367, 1164, 1866, 1694, 2904, 3203, 4185, 9717, 9791, 570, 8505, 6087, 1587, 4433, 7071, 8772, 9696, 5708, 987, 4623, 3403, 9984, 5114, 5530, 8062, 7254, 2964, 8757, 8643, 4937, 7737, 8584, 7872, 6961, 2194, 1878, 5615, 3991, 2003, 3620, 822, 9462, 1586, 9508, 5842, 9953, 114, 6337, 3643, 8433, 8568, 7051, 5574, 3626, 7045, 1170, 2568, 2699, 6657, 217, 5346, 9768, 8925, 187, 8716, 4607, 2260, 3738, 919, 6311, 4681, 2513, 7002, 525, 1834, 9755, 7961, 4750, 5093, 5922, 8445, 2204, 7721, 8552, 4234, 2340, 9359, 6496, 6174, 7609, 1121, 8316, 5732, 7124, 3616, 5091, 6382, 9571, 9796, 4410, 1189, 6595, 5845, 2028, 3021, 7625, 1667, 2300, 6304, 5409, 8374, 3374, 6526, 9318, 1529, 3763, 4449, 9311, 8559, 7284, 279, 7191, 7994, 4476, 3397, 901, 5669, 8740, 4415, 245, 4036, 5086, 6256, 4126, 2747, 8560, 1691, 549, 7881, 580, 4599, 6393, 4278]
print(quick_sort(arr))
