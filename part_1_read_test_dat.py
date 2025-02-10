import cc_dat_utils

#Part 1
input_dat_file = "data/pfgd_test.dat"
load_files = cc_dat_utils.make_cc_level_pack_from_dat(input_dat_file)
string_representation = str(load_files)

file = open("data/pfgd_test.txt","w")
file.write(string_representation)
file.close()

#Use cc_dat_utils.make_cc_level_pack_from_dat() to load the file specified by input_dat_file
#print the resulting data
