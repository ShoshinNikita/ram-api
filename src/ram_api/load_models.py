import time
import torch

from ram.models import ram_plus
from ram import (inference_ram, get_transform)


def load_ram_plus(image_size):
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print("using device: ", device)

    transform = get_transform(image_size=image_size)

    model = ram_plus(pretrained="/data/pretrained/ram_plus_swin_large_14m.pth",
                     image_size=image_size,
                     vit='swin_l')

    model.eval()
    model = model.to(device)

    print("loaded ram_plus_swin_large_14m.pth")

    def inference(image):
        start_time = time.perf_counter()

        transformed = transform(image).unsqueeze(0).to(device)
        result = inference_ram(transformed, model)

        return {
            "english": result[0].split(" | "),
            "chinese": result[1].split(" | ")
        }

    return {
        "device": device,
        "model": model,
        "inference": inference,
        "transform": transform
    }
