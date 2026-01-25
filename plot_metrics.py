import matplotlib.pyplot as plt

# Epochs completed
epochs = list(range(1, 19))

# Validation IoU values (update if you have exact logs)
val_iou = [
    0.2172, 0.2441, 0.2628, 0.2715, 0.2760,
    0.2818, 0.2850, 0.2920, 0.2921, 0.2929,
    0.2960, 0.2980, 0.3000, 0.3010, 0.3030,
    0.3050, 0.3060, 0.3070
]

plt.figure()
plt.plot(epochs, val_iou, marker='o')
plt.xlabel("Epoch")
plt.ylabel("Validation IoU")
plt.title("Validation IoU vs Epochs")
plt.grid(True)

# Save graph
plt.savefig("outputs/val_iou_18_epochs.png")
plt.show()
