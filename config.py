
arg_config = {
    'path_stopword': './file/stopword',
    
    # math23k相关数据
    'path_math23k_train': './comment/datasets/math23k_data/train_23k.json',
    'path_math23k_valid': './comment/datasets/math23k_data/test_23k.json',

    # momery module(检索模型路径)
    'path_w2v_model': './preprocess/save_trained_model/w2v_model.md',
    'path_math23k_w2v_model': './preprocess/save_trained_model/math23k_w2v_model.md',
    'path_math23k_test1k_w2v_model': './preprocess/save_trained_model/math23k_test1k_w2v_model.md',
    'path_w2v_sim_question_train': './preprocess/sim_result/sim_question_by_w2v_train.pkl',
    'path_w2v_sim_question_valid': './preprocess/sim_result/sim_question_by_w2v_valid.pkl',
    'path_w2v_sim_question_test': './preprocess/sim_result/sim_question_by_w2v_test.pkl',

    
    # math23k包含所有训练集和1000个测试集的数据路径；
    'path_math23k_all_train': './comment/datasets/math23k_data/math23k_train.json', # math23k test1k数据划分，用于官方验证集测试
    'path_math23k_test_1000': './comment/datasets/math23k_data/math23k_test.json',  # math23k test1k数据划分，用于官方验证集测试
    'path_math23k_dataset': './comment/datasets/math23k_data/Math_23K.json',  # math23k全量数据，用于五折交叉验证

    
    # end2end方案相关数据的存储地址
    'raw_math23k_data_dict_path': './preprocess/raw_sim_dict/raw_math23k_data_dict.pkl',
    'math23k_train_sim_id_path': './preprocess/raw_sim_dict/math23k_train_sim_id.pkl',
    'math23k_valid_sim_id_path': './preprocess/raw_sim_dict/math23k_valid_sim_id.pkl',

    'raw_math23k_test1k_data_dict_path': './preprocess/raw_sim_dict/raw_math23k_test1k_data_dict.pkl',
    'math23k_test1k_train_sim_id_path': './preprocess/raw_sim_dict/math23k_test1k_train_sim_id.pkl',
    'math23k_test1k_valid_sim_id_path': './preprocess/raw_sim_dict/math23k_test1k_valid_sim_id.pkl',

}


