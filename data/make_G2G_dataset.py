
from options.G2G_dataset_option import G2GDatasetOptions
import numpy as np

class G2GDataSetTranformer(object):

    def __init__(self):
        pass

    def origindf_to_txtaligned_dataset_format(self,origin_df_a,origin_df_b,split_to_ab_format=False):
        pass


    # 将Train需要的数据文件转化为原始数据文件

    def G2G_format_to_txtaligned_dataset_format(self,G2G_file_path_a,G2G_file_path_b,txtaligned_file_path,split_to_ab_format=False):
        """Trans A pair G2G-data-file To txtaligned.

        Parameters:
            G2G_file_path_a (file_name)      -- a G2G_format_gene_file
            G2G_file_path_b (file_name)      -- a G2G_format_gene_file
            txtaligned_file_path(file_path)  -- txtaligned_file_path
            split_to_ab_format(bool)         -- need_to_split_ab_format(default false)

        Returns a list that contains A,B file_name

            file_name_list_ab(list)             -- a list contains A,B file_name
            file_name_list_a(list)           -- a list contains A file_name
            file_name_list_b(list)           -- a list contains B file_name
        """
        pass
    #将原始的数据文件转换为Train需要的数据文件
    def txtaligned_dataset_format_to_G2G_format(self,file_path_a,file_path_b,file_path_ab):
        pass

if __name__ == '__main__':
    G2G_file_name_a = "../test_data/pix2pix_user_data_format/paired_cpm_FF_count_mask.txt"
    G2G_file_name_b = "../test_data/pix2pix_user_data_format/paired_cpm_FFPE_count_mask.txt"

    result_txtaligned_data_set = "../result_data/pix2pix_input_ready_to_use_1024gene/train"

    txtaligned_data_set = "../test_data/pix2pix_input_ready_to_use_1024gene/train"

    result_G2G_file_path = "../result_data/pix2pix_input_ready_to_use_1024gene/train"

    pass
    # self.dir_AB = os.path.join(opt.dataroot, opt.phase)  # get the image directory
    #
    #     self.AB_paths = sorted(make_dataset(self.dir_AB, opt.max_dataset_size))  # get image paths
    #




    #
   # def __init__(self, opt):

