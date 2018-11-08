# Autogenerated with SMOP 
import numpy as np
# sub_basic_info.m

class basic_info_class:
  def __init__(self):
    self.cmd_num_read = []
    self.cmd_num_write = []
    self.max_time = 1
    self.eff_time = 1
    self.iops_read = 0
    self.iops_write = 0
    self.total_size_read = []
    self.total_size_write = []
    self.ave_size_read = []
    self.ave_size_write = []
    self.ave_tp_read = []
    self.ave_tp_write = []
    
def sub_basic_info(lists_action,lists_cmd,options=None):


    a=np.shape(lists_action)[0]
    idx_read=np.nonzero(lists_cmd[:,2] == 1)
    idx_write=np.nonzero(lists_cmd[:,2] == 0)
    basic_info=basic_info_class()
                               
    basic_info.cmd_num_read = (np.shape(idx_read)[1])
    basic_info.cmd_num_write = (np.shape(idx_write)[1])
    basic_info.max_time = (lists_action[a-1,0])
    basic_info.eff_time = (lists_action[a-1,0] - lists_action[0,0])
    basic_info.iops_read = (basic_info.cmd_num_read / basic_info.eff_time)
    basic_info.iops_write = (basic_info.cmd_num_write / basic_info.eff_time)
    basic_info.total_size_read = np.sum(lists_cmd[idx_read,1])
    basic_info.total_size_write = np.sum(lists_cmd[idx_write,1])
    basic_info.ave_size_read = 1.0*(basic_info.total_size_read / basic_info.cmd_num_read)
    basic_info.ave_size_write =1.0* (basic_info.total_size_write / basic_info.cmd_num_write)
    basic_info.ave_tp_read = (np.dot(basic_info.total_size_read / basic_info.eff_time,512) / 1024 ** 2)
    basic_info.ave_tp_write = (np.dot(basic_info.total_size_write / basic_info.eff_time,512) / 1024 ** 2)
    
    return basic_info