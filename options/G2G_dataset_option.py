from .base_options import BaseOptions


class G2GDatasetOptions(BaseOptions):
    """This class includes G2G-data pre-training options.

    It also includes shared options defined in BaseOptions.
    """

    def initialize(self, parser):
        parser = BaseOptions.initialize(self, parser)
        #预处理
        parser.add_argument('--normalization_method', type=str, default="tan0h", help='Normalization method 归一化方法,tan0h,tan4h,log,etc')

        parser.add_argument('--system', type=int, default=4, help='if positive, display all images in a single visdom web panel with certain number of images per row.')

        # parser.add_argument('--display_ncols', type=int, default=4, help='if positive, display all images in a single visdom web panel with certain number of images per row.')
        # parser.add_argument('--display_id', type=int, default=1, help='window id of the web display')

        self.isTrain = False
        return parser
