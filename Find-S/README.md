# Find-S Algorithm

<b>Output of algorithm:
<img src="https://github.com/rishav-karanjit/Machine-Learning-Algorithms/raw/master/Find-S/Find-S%20Scr%20Shot.png"></img>

<b>Algorithm:</b>
1. Initialize h to the most specific hypothesis in H
2. For each positive training instance x<br>
   &nbsp;&nbsp;&nbsp;&nbsp;For each attribute constraint a, in h<br>
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;If the constraint a, is satisfied by x<br>
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Then do nothing<br>
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Else replace a, in h by the next more general constraint that is satisfied by x<br>
3. Output hypothesis h 
