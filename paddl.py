import paddlehub as hub
import paddle
import glob


# 模型列表
pretrained_models = [
    'animegan_v1_hayao_60', 
    'animegan_v2_hayao_64', 
    'animegan_v2_hayao_99',  
    'animegan_v2_paprika_74', 
    'animegan_v2_paprika_97', 
    'animegan_v2_paprika_98', 
    'animegan_v2_shinkai_33',
    'animegan_v2_shinkai_53'
]


def main(num,input_img_path):
    model = hub.Module(name=pretrained_models[num], use_gpu=False)

    # 模型预测
    result = model.style_transfer(
        images=None,
        paths=[input_img_path],
        batch_size=1,
        output_dir='output',
        visualization=True,
        min_size=32,
        max_size=512
    )
    file = glob.glob(r"./output/*.jpg")
    for i in file:
        path = i
    return path 