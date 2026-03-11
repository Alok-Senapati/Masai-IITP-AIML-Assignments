import numpy as np
import plotly.graph_objects as go

# ===============================
# PART 1 — Linear Regression GD
# ===============================

areas = np.array([500, 800, 1200, 1500, 2000]) / 1000
prices = np.array([20, 30, 45, 55, 75])

w = 0.0
b = 0.0

learning_rate = 0.01
num_iterations = 1000
n = len(areas)

# Initial loss
predictions = w * areas + b
initial_loss = (1/n) * np.sum((predictions - prices)**2)

for i in range(num_iterations):

    predictions = w * areas + b

    dw = (2/n) * np.sum((predictions - prices) * areas)
    db = (2/n) * np.sum(predictions - prices)

    w = w - learning_rate * dw
    b = b - learning_rate * db

final_loss = (1/n) * np.sum((w * areas + b - prices)**2)

predicted_price = w * (1800/1000) + b

print(f"Initial Loss: {initial_loss:.2f}")
print(f"Final Loss: {final_loss:.2f}")
print(f"Optimized Weight: {w:.4f}")
print(f"Optimized Bias: {b:.4f}")
print(f"Predicted Price for 1800 sq.ft: Rs. {predicted_price:.2f} lakhs")


# =====================================
# PART 2 — Gradient Descent Visualization
# =====================================

def loss(w):
    return (w - 5) ** 2

def gradient(w):
    return 2 * (w - 5)

learning_rate = 0.4
iterations = 10
w = 9

w_history = [w]
loss_history = [loss(w)]

for _ in range(iterations):
    w = w - learning_rate * gradient(w)
    w_history.append(w)
    loss_history.append(loss(w))

w_vals = np.linspace(0, 10, 200)
loss_vals = loss(w_vals)

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=w_vals,
    y=loss_vals,
    mode='lines',
    name='Loss Function L(w) = (w-5)^2'
))

fig.add_trace(go.Scatter(
    x=w_history,
    y=loss_history,
    mode='markers+lines',
    name='Gradient Descent Path'
))

fig.update_layout(
    title="Gradient Descent Optimization Visualization",
    xaxis_title="Weight (w)",
    yaxis_title="Loss",
    template="plotly_white"
)

fig.show()