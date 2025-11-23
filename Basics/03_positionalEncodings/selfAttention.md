# Self-Attention

## Purpose
Allows each token to attend to all other tokens in the sequence, capturing contextual relationships regardless of distance.

## How It Works
1. **Create Q, K, V matrices**: Transform input embeddings using learned weight matrices
   - Query (Q): What I'm looking for
   - Key (K): What I have to offer
   - Value (V): What I'll output if matched

2. **Calculate attention scores**: `Attention(Q, K, V) = softmax(QK^T / √d_k) V`
   - Dot product between queries and keys
   - Scale by √d_k to prevent large values
   - Softmax to get attention weights
   - Multiply by values to get output

3. **Output**: Weighted sum of values based on attention scores

## Key Features
- **Parallel computation**: All tokens processed simultaneously
- **Dynamic relationships**: Attention weights change based on context
- **Long-range dependencies**: Can connect distant tokens directly

## Multi-Head Attention
- Run multiple attention mechanisms in parallel
- Each head learns different relationships
- Concatenate outputs and project back
- Formula: `MultiHead(Q,K,V) = Concat(head_1,...,head_h)W^O`
- Allows model to focus on different aspects simultaneously

## Complexity
- Time: O(n²·d) where n = sequence length, d = dimension
- Main bottleneck for long sequences

## Example
🍎 Super Simple Analogy

Imagine you're watching a movie, and 8 people are in the room:

One pays attention to the storyline

One watches the background details

One notices the music

One analyzes character emotions

One checks for plot holes

All together → you get a richer understanding.

Multi-head attention works exactly like that. Each "head" focuses on different parts of the input, allowing the model to capture various aspects of the data simultaneously.