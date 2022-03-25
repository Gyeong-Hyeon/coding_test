## Question 1. Find substrings
 
 주어진 문자열 s에서 반복되지 않는 문자를 포함하는 substring의 최대 개수를 구하세요. 문자열 s에서의 인덱스가 다른 Substring은 각각 다른 것으로 취급합니다.

</br>

### 예시

</br>

 **`s = "abac"`**

</br>

 예시 s에서 반복되지 않는 substring은 "a", "b", "a", "c", "ab", "ba", "ac", "bac"입니다. "aba"와 "abac"는 'a'를 중복으로 포함하므로 substring으로 간주할 수 없습니다. 또한 "a"와 "a"는 문자열 s에서 인덱스 0과 2 두 개로 나눠질 수 있으므로 각각 다른 substring으로 취급할 수 있습니다. 따라서 위의 예시 s에서는 총 8개의 중복 문자를 포함하지 않는 substring이 존재합니다.

</br>

### 함수 설명
 Complete the function `findSubstrings` in the editor below.

 </br>

 **Parameter**
 `findSubstrings` has the following parameter:
    - string `s`: the given string
 **Returns**:
    - int: the number of substrings in `s` that have no repeating characters
    (s에 존재하는 중복 문자를 포함하지 않는 substring의 개수)

</br>

### 제한사항
- s의 길이는 1이상 100000 이하
- s는 소문자로 된 아스키 영문자만 포함합니다. ['a'-'z']

</br>

### 입출력 예

|s|result|
|:---:|:---:|
|"bcada"|12|
|"abcd"|10|

</br>

## Question 2. Gap in Traffic
 
 n개의 위치가 있는 2차선 도로 위에 시작 위치에서 끝 위치까지 m대의 차들이 왼쪽에서 오른쪽으로 달리고 있습니다. 차선에 관계없이 모든 차량의 위치에서 가장 넓은 간격을 구하세요.

</br>

### 예시

</br>

 ```python
 n = 10
 start = [1,2,5,8]
 finish = [2,2,6,10]
 ```
 
</br>

 다음 그림은 예시로 주어진 도로 위의 자동차들을 그림으로 나타낸 것입니다. 시작과 끝은 각 차의 뒤와 앞의 표시합니다. 도로의 길이는 n입니다.
<p align='center'><img width="400" alt="vroong_q1" src="https://imgur.com/glWFS8O.png"></p>
 차가 포함되는 도로의 부분은 회색으로 표시가 되어있고, 그렇지 않은 부분은 초록색으로 표시되어 있습니다.
 위의 그림은 길이가 n=10단위이고 차량이 m=4대인 도로를 표시합니다.
 
 - 첫 번째 차량의 위치는 start[0]=1에서 finish[0]=2입니다 (총 2칸).
 - 두 번째 차량의 위치는 start[1]=2에서 finish[1]=2입니다 (총 1칸).
 - 세 번째 차량의 위치는 start[2]=5에서 finish[2]=6입니다 (총 2칸).
 - 네 번째 차량의 위치는 start[3]=8에서 finish[3]=10입니다 (총 3칸).
 - 위치 3~4,7에 간격이 있습니다. 차량 사이의 가장 넓은 간격은 2입니다 (3~4).
 
</br>

### 함수 설명
 Complete the function `widestGap` in the editor below.
 **Parameter**
 `widestGap` has the following parameter:

   - int `n`: the length of the road section (도로의 길이)

   - int start`[m]`: the position of the rears of each car (각 차의 시작점 - 정수 배열)
    
   - int finish`[m]`: the positions of the fronts of each car (각 차의 끝 점 - 정수 배열)

 **Returns**:
   
   - int: the length of the longest gap between cars
    (차 사이의 가장 넓은 간격)

</br>

### 제한사항
- 도로의 길이 n은 1이상 1000000000이하
- 시작점과 끝 점 m은 1이상 100000이하
- start[i]는 항상 1이상, finish[i]보다 작으며, finish[i]는 항상 도로의 길이 이하이다 (인덱스 i는 0이상 차랑의 대수 미만임).

</br>

### 입출력 예

|n|start|finish|result|
|:---:|:---:|:---:|:---:|
|10|[3,8]|[4,9]|3|
|10|[1,2,5,8]|[2,2,6,10]|2|
