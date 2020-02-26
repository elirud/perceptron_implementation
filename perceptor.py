import numpy as np
import matplotlib.pyplot as plt

# x = [[x0, x1, x2, ref to learn against]]
x = [[1, 0.4650374, 0.417356930, 0],
 [1, 0.5541088, 0.51976657, 0],
 [1, 0.19761486, 0.18637048, 0],
 [1, 0.46005865, 0.42808735, 0],
 [1, 0.38840013, 0.35109187, 0],
 [1, 0.52466601, 0.49058735, 0],
 [1, 0.9714174, 0.90455572, 0],
 [1, 0.48828935, 0.45105422, 0],
 [1, 0.40443141, 0.37518825, 0],
 [1, 0.32379277, 0.30628765, 0],
 [1, 0.47144998, 0.4471009, 0],
 [1, 0.51550342, 0.48192771, 0],
 [1, 0.94551971, 0.8653991, 0],
 [1, 0.98210492, 0.91698042, 0],
 [1, 0.23500815, 0.21065512, 0],
 [1, 0.48173346, 0.47119729, 1],
 [1, 0.56853698, 0.56325301, 1],
 [1, 0.20454871, 0.19615964, 1],
 [1, 0.47221896, 0.46818524, 1],
 [1, 0.39029, 0.37914157, 1],
 [1, 0.52900619, 0.5280497, 1],
 [1, 0.98084066, 0.95293675, 1],
 [1, 0.49148257, 0.49755271, 1],
 [1, 0.40272401, 0.4002259, 1],
 [1, 0.33217335, 0.33584337, 1],
 [1, 0.48871945, 0.4971762, 1],
 [1, 0.52652981, 0.52070783, 1],
 [1, 0.96585207, 0.95011295, 1],
 [1, 1, 1, 1],
 [1, 0.23873574, 0.22872741, 1]]
w = [0, 1, 1]

# line -> y = (-w[1]-w[2]x)/w[3]

def predict(x, w):
    right = 0
    wrong = 0
    predictions = []
    for x1 in x:
        pred = 0
        sum = 0
        sum = w[0] + w[1] * x1[1] + w[2] * x1[2]
        if sum > 0:
            pred = 1
        else:
            pred = 0
        if pred == x1[3]:
            right += 1
        else:
            wrong += 1
        predictions.append(pred)
    return right, wrong, predictions

def update(predictions, x, w, rate):
    for pred, x1 in zip(predictions, x):
        if not pred == x1[3]:
            d = 1 if x1[3] == 1 else -1
            for i in range(len(w)):
                w[i] = w[i] + rate * d * x1[i]
    return w

right, wrong, predictions = predict(x, w)

while right < 30:
    print(f'{right} / {wrong} = {(right / wrong):.3f} ---- {w}')
    w = update(predictions, x, w, 0.0024)
    right, wrong, predictions = predict(x, w)

print(w)
x_eng = np.array([x for x in filter(lambda x: x[3] == 0, x)])
x_fr = np.array([x for x in filter(lambda x: x[3] == 1, x)])
x_axis = np.array(x)[:,1]
y_axis = []
plt.plot(x_axis, abs(w[1]) * x_axis + w[0], '-')
plt.scatter(x_eng[:,1], x_eng[:,2], marker='o', label='English')
plt.scatter(x_fr[:,1], x_fr[:,2], marker='x', label='French')
plt.xlabel('Letters')
plt.ylabel('A\'s')
plt.legend()
plt.show()