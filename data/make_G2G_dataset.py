
# from options.G2G_dataset_option import G2GDatasetOptions
import numpy as np
import pandas as pd
from pandas import DataFrame as df
import math
import os
from util import util
from util import dataframe_util
class G2GDataSetTransformer(object):

    def __init__(self):
        pass

    # def origindf_to_txtaligned_dataset_format(self,origin_df_a,origin_df_b,split_to_ab_format=False):
    #     pass

        # AB_path = self.AB_paths[index]
        # AB = np.loadtxt(AB_path, delimiter="\t") # dtype=np.double
        #  # split AB image into A and B
        # # w, h = AB.size
        # # w2 = int(w / 2)
        # # A = AB.crop((0, 0, w2, h))
        # # B = AB.crop((w2, 0, w, h))
        #
        # h, w = AB.shape
        # w2 = int(w / 2)
        # A = AB[0:h, 0:w2]
        # B = AB[0:h, w2:w]

    # 将Train需要的数据文件转化为原始数据文件
    def data_list_to_dataframe(self,datalist,m,n):
        recordlist = list()
        for j in range(0,n):
            infolist = list()
            for i in range(0,m):
                index= j*m + i
                infolist.append(datalist[index])
            recordlist.append(infolist)
        resultdf = df.from_records(recordlist)
        return resultdf
    # 将Train需要的数据文件转化为原始数据文件
    def data_frame_to_data_list(self,origindf):
        pass

        #df.f
    def G2G_dataframe_txtaligned_dataframe(self,origindf,m=None,n=None):

        resultdf_list = list()
        for column_name in origindf.columns:
            listInfo= origindf[column_name].to_list()

            if (m == None):
                length = len(listInfo)
                m = math.floor(math.sqrt(length))
                n = m
            resultdf = self.data_list_to_dataframe(listInfo,m,n)
            resultdf_list.append(resultdf)
        return resultdf_list



    def normalize_dataframe(self,origindf,normallize_method):
        if(normallize_method == "atan"):
            resultdf = origindf.applymap(lambda x: math.atan(x)*2/math.pi)


        elif(normallize_method=="origin"):
            resultdf = origindf
        elif(normallize_method=="tanh"):

            resultdf = origindf.applymap(lambda x: math.tanh(x))

        else:
            resultdf = origindf

        return resultdf

    def write_dataframe_list(self,result_df_list_a,result_df_list_b, write_file_path, split_to_ab_format):

        if(split_to_ab_format):
            dir_a = write_file_path+'A'
            dir_b = write_file_path+'B'
            self.write_dataframe_list_withPath(result_df_list_a,dir_a)
            self.write_dataframe_list_withPath(result_df_list_b,dir_b)
        else:
            result_df_list = dataframe_util.join_dataframe_list(result_df_list_a,result_df_list_b)
            self.write_dataframe_list_withPath(result_df_list,write_file_path)




    def write_dataframe_list_withPath(self,result_df_list,write_file_path):
        if (not os.path.exists(write_file_path)):
            os.makedirs(write_file_path)

        i = 1
        for result_df in result_df_list:
            file_name = os.path.join(write_file_path,f"{i}.txt")
            result_df.to_csv(file_name,sep="\t",index=False,header=None)

            i = i + 1



            #

    def G2G_format_to_txtaligned_dataset_format(self,G2G_file_path_a,G2G_file_path_b,txtaligned_file_path,normalize_method="tan0",split_to_ab_format=False):
        """Trans A pair G2G-data-file To txtaligned.

        Parameters:
            G2G_file_path_a (file_name)      -- a G2G_format_gene_file
            G2G_file_path_b (file_name)      -- a G2G_format_gene_file
            txtaligned_file_path(file_path)  -- txtaligned_file_path
            normalize_method                 -- a tranform_method_to_normalize_the_matrix
            split_to_ab_format(bool)         -- need_to_split_ab_format(default false)

        Returns a list that contains A,B file_name

            file_name_list_ab(list)             -- a list contains A,B file_name
            file_name_list_a(list)           -- a list contains A file_name
            file_name_list_b(list)           -- a list contains B file_name
        """
        origindf_a = pd.read_csv(G2G_file_path_a,sep="\t",index_col=0)
        origindf_b = pd.read_csv(G2G_file_path_b,sep="\t",index_col=0)
        operation_df_a = self.normalize_dataframe(origindf_a,normalize_method)
        operation_df_b = self.normalize_dataframe(origindf_b,normalize_method)


        result_df_list_a = self.G2G_dataframe_txtaligned_dataframe(operation_df_a)
        result_df_list_b = self.G2G_dataframe_txtaligned_dataframe(operation_df_b)

        self.write_dataframe_list(result_df_list_a,result_df_list_b, txtaligned_file_path, split_to_ab_format)



    #将原始的数据文件转换为Train需要的数据文件
    def txtaligned_dataset_format_to_G2G_format(self,file_path_a,file_path_b,file_path_ab,result_G2G_filename_a,result_G2G_filename_b,normalize_method):
        if (file_path_ab):
            pass
        else:
            resultdf = None
            resultdict = dict()
            for filename in os.listdir(file_path_a):
                file_path = file_path_a + "/" + filename
                key = "simple" + filename.split(".")[0]
                origindf = pd.read_csv(file_path,sep="\t",header=None)
                listinfo = origindf.values.tolist()
                print(listinfo)
                resultdict[key] = listinfo
            resultdf = df(resultdict)

            for filename in os.listdir(file_path_b):
                pass

        #

if __name__ == '__main__':
    testFilePath = "../../test_data/"
    resultFilePath = "../../result_data/"
    G2G_file_name_a = testFilePath + "pix2pix_user_data_format/paired_cpm_FF_count_mask.txt"
    G2G_file_name_b = testFilePath + "pix2pix_user_data_format/paired_cpm_FFPE_count_mask.txt"

    result_txtaligned_data_set = resultFilePath + "pix2pix_input_ready_to_use_1024gene/train"

    txtaligned_data_set = testFilePath+ "pix2pix_input_ready_to_use_1024gene/train"
    txtaligned_data_set_a = testFilePath + "cycleGAN_input_ready_to_use_1024gene/1024h0tanh/trainA"
    txtaligned_data_set_b = testFilePath + "cycleGAN_input_ready_to_use_1024gene/1024h0tanh/trainB"


    result_G2G_file_path = resultFilePath + "pix2pix_input_ready_to_use_1024gene/train"

    result_G2G_file_name_a = resultFilePath + "pix2pix_user_data_format/paired_cpm_FF_count_mask.txt"
    result_G2G_file_name_b = resultFilePath + "pix2pix_user_data_format/paired_cpm_FFPE_count_mask.txt"
    normalize_method = "tanh"
    #归一化 ->文件互相转换表
    transformer = G2GDataSetTransformer()
    #G2G数据转换成预训练数据
    transformer.G2G_format_to_txtaligned_dataset_format(G2G_file_name_a,
                                                                 G2G_file_name_b,
                                                                 result_txtaligned_data_set,
                                                                 normalize_method,
                                                                 False)

    # transformer.txtaligned_dataset_format_to_G2G_format(txtaligned_data_set_a,
    #                                                              txtaligned_data_set_b,
    #                                                             None,
    #                                                              result_G2G_file_name_a,
    #                                                             result_G2G_file_name_b,
    #                                                              normalize_method,
    #                                                              )


    # self.dir_AB = os.path.join(opt.dataroot, opt.phase)  # get the image directory
    #
    #     self.AB_paths = sorted(make_dataset(self.dir_AB, opt.max_dataset_size))  # get image paths
    #




    #
   # def __init__(self, opt):

