在寻找当前所能到达的几个位置里面，选择下一步跳的最远的位置，然后就跳到这个位置，即在选择当前步跳跃的时候，为下一步留下了最好的结果。
​
current表示当前所能跳到的最远的位置
previous表示上一步能达到的最远的位置
所以应该在遍历上一步的覆盖范围内，当前所能跳到最远位置来更新current
position为当前所检查的位置，这样每次检查的范围为position-previous