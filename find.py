#!/Bio/Software/Python/anaconda3/bin/python3.6
# -*- coding:utf-8 -*-
# @author:zhoutong
'''
 This script can
 Input:
 Output:
'''
import sys,argparse,os
from itertools import islice
import pandas as pd
#############################################################
## Argument Parser
parser = argparse.ArgumentParser(description='',add_help=True)
# add arguments
parser.add_argument('-in','--in_file',nargs="?",type=str,required=True,help='input annot file')
parser.add_argument('-out','--out_file',type=str,required=True,default="new.annot",help='output new annot file')
parser.add_argument('-ic','--in_change',type=str,required=True,default=None,help="like '1,' or '2,5,6',not '1' ")
parser.add_argument('-oc','--out_change',type=str,required=True,default=None,help=' ')

args = parser.parse_args()
#################################################################################
## 接收参数，获取绝对路径 
file_in = args.in_file
file_in_abpath = os.path.abspath(file_in)

file_out = args.out_file
file_out_abpath = os.path.abspath(file_out)

ic = args.in_change; oc = args.out_change
#################################################
#判断文件是否存在
if os.path.exists(file_in_abpath) is False:
	print("\nWarning: The file " + file_in_abpath + " is not exist, please check again.")
	exit()
##########################################
# 参数拆分整理
ic_list = ic.split(','); oc_list = oc.split(',')
len_ic = len(ic_list); len_oc = len(oc_list)
############################################
#参数有效性判断
print(ic)
print(type(ic))
print(ic_list)

'''
if len_ic != len_oc:
	print("\nWarning:The number of ic parameters "+len_ic +" is not equal to the number of oc parameters "+len_oc +",please check again.")
	exit()
print(ic_list)
for i in list(ic_list):
	if str(i).isdigit() is False:
		print("\nWarning:The ic parameters should be entered into a positive integer,please check again.")
		exit()
	else:
		pass
for i in list(oc_list):
	if str(i).isdigit() is False:
		print("\nWarning:The oc parameters should be entered into a positive integer,please check again.")
		exit()
	else:
		pass
#################################################################
df_file_in = pd.read_table(file_in,sep='\t')
print(df_file_in.head())

#读取存储file_in
indexfile_dict = {}
Not_mapped = []
mapped = []

with open(file_map,'r') as fm:            #file_map中第二列是唯一索引，无重复，可做键
	lines = fm.readlines()
	first_line = lines[0].strip('\n')
	mk_column_name = first_line.split('\t')[mk-1]
	mv_column_name = first_line.split('\t')[mv-1]
	for line in lines[head:]:
		line0 = line.strip('\n')
		line_list = []
		line_list = line0.split('\t')
		for i in range(0,len(line_list)):
			if not line_list[i]:
				line_list[i] = '-'
		line1 = '\t'.join(line_list)
		index_id = line1.split('\t')[mk-1]
		indexfile_dict[index_id] = line1.split('\t')[mv-1]

index_id_list = list(indexfile_dict.keys())

with open(file_in,'r') as fi:
	lines = fi.readlines()
	first_line = lines[0].strip('\n')
	k_column_name = first_line.split('\t')[k-1]
	v_column_name = first_line.split('\t')[v-1]

	title = mv_column_name + '\t' + v_column_name

	for line in lines[head:]:
		file_id = line.split('\t')[k-1]
		file_value = line.split('\t')[v-1]
        
		if file_id in index_id_list:
#			result_line = file_id +'\t'+ indexfile_dict[file_id] + '\t' + file_value
			result_line = indexfile_dict[file_id] + '\t' + file_value
			mapped.append(result_line)
		else:
			Not_mapped.append(file_id)
Not_mapped = sorted(list(set(Not_mapped)))
with open(file_out,'wt') as fo:
	for i in sorted(mapped):
		fo.write(i)
if head > 0:
	with open(file_out,'r+') as f:
		content = f.read()
		f.seek(0,0)
		f.write(title+'\n'+content)

with open(file_nom,'wt') as out:
	for i in Not_mapped:
		out.write(i+'\n')
#################################################################
'''

