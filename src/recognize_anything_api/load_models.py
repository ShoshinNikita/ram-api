import time
import torch

from recognize_anything.ram.models import ram_plus
from recognize_anything.ram import inference_ram
from recognize_anything.ram import get_transform


def load_ram_plus(image_size):
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print("Using device: ", device)

    transform = get_transform(image_size=image_size)

    model = ram_plus(pretrained="/data/pretrained/ram_plus_swin_large_14m.pth",
                     image_size=image_size,
                     vit='swin_l')

    model.eval()
    model = model.to(device)

    print("Loaded ram_plus_swin_large_14m.pth")

    def inference(image):
        start_time = time.perf_counter()

        transformed = transform(image).unsqueeze(0).to(device)
        result = inference_ram(transformed, model)

        print(f"processed image in {time.perf_counter() - start_time:0.4f}s")

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
