class_name = [
    '00', 'S13_gho_CC', 'S34_so_CC', 'Sign 19_to', 'S12_go_CC', 'Sign 17_DO',
    'S8_O_CC', 'Sign 15_To', 'Sign 20_tho', 'Sign 36_bishorgo', 'S28_dho_CC',
    'S31_bo_CC', 'S7_Oi_CC', '4', '000', 'S30_fo_CC', '6', 'S19_Io_CC',
    'S24_no_CC', 'S3_i_CC', 'Sign 9_go', 'S17_jo_CC', '9', 'Sign 10_ Gho',
    'Sign 31_so', 'Sign 27_mo', 'S20_To_CC', 'S4_u_CC', 'Sign 25_bo',
    'S33_lo_CC', 'Sign 12_cho', 'Sign 21_do', 'Sign 1_o', 'Sign 14_Jho',
    'S38_Chandrabindu_CC', 'S11_Kho_CC', 'Sign 34_RHo', 'Sign 6_I',
    'S23_Dho_CC', '5', 'Sign 11_co', 'Sign 18_DHO', 'Sign 35_onosshar',
    'S16_Cho_CC', 'S10_ko_CC', 'S15_co_CC', 'Sign 2_a', 'Sign 5_e',
    'S36_onnosar_CC', 'Sign 33_RO', 'S35_ho_CC', 'Sign 16_THo', 'S26_tho_CC',
    'Counting', 'Sign 23_po', 'Sign 7_ko', 'S32_mo_CC', 'Sign 4_U',
    'Sign 32_ho', 'S9_OU_CC', 'S25_to_CC', '0', 'Sign 3_O', 'S22_Do_CC',
    'Sign 24_fo', 'Sign 22_dho', 'S14_Umo_CC', 'S6_e_CC', '1', '7',
    'Sign 26_bho', 'S18_jho_CC', '2', 'S37_bissorgo_CC', 'S1_o_CC', '8',
    'Sign 29_ro', 'S5_ro_CC', 'Sign 13_jo', 'Sign 30_lo', 'Sign 8_kho', '3',
    'S27_do_CC', 'S21_THo_CC', 'S2_a_CC', 'Sign 28_yo', 'S29_po_CC'
]

for i in range(len(class_name)):
    with open('class_name.csv', 'a') as f:
        f.write(f"{i},{class_name[i]}\n")

# convert class_name list to dictionary
class_name_dict = {}
for i in range(len(class_name)):
    class_name_dict[i] = class_name[i]


def get_id_from_class_name(class_name):
    for key, value in class_name_dict.items():
        if value == class_name:
            return key
