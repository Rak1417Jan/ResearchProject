import os
from proactiveFunction import proactive_approach
from reactiveFunction import reactive_approach
def main(video_path, approach):
    if approach == 'proactive':
        proactive_approach(video_path)
    elif approach == 'reactive':
        reactive_approach(video_path)
    else:
        print("Invalid approach selected. Please choose either 'proactive' or 'reactive'.")

if __name__ == "__main__":
    video_path = '/content/mydir/Inputs/testa_real.mp4'
    approach = input("Choose approach (proactive/reactive): ").strip().lower()
    main(video_path, approach)