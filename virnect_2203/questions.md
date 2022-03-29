## Question 1. Cut them all
 
 막대기를 부분으로 자르는 자동 절단기가 있습니다. 이 절단기는 minLength길이 이상의 막대기만 잡을 수 있습니다. 막대기는 잘라야하는 길이만큼 표시되어 있고, 해당 길이는 표시되어 있는 순서대로 array로 주어집니다. minLength길이를 기준으로 마지막 절단이 가능한지를 판단하여 이 절단 계획이 가능한 계획인지 아닌지를 확인하세요.

</br>

### 예시 1.

</br>

 ```
 n = 3
 lengths = [4,3,2]
 minLength = 7
 ```

</br>

 처음 막대기의 길이는 `4+3+2=9`unit입니다. 첫번째 절단은 `4+3=7`unit을 잘라서 `9-7=2`길이를 남김으로써 가능합니다. 두 번째 절단은 처음으로 절단한 7unit을 절단기가 잡을 수 있는지 확인함으로써 가능한지 아닌지 판단합니다. 7unit은 절단기가 잡을 수 있는 최소 길이인 `minLength=7`길이와 같으므로 최종 절단이 가능합니다. 따라서 Return 값은 "Possible"입니다.

</br>

### 예시 2.

</br>

 ```
 n = 3
 lengths = [4,2,3]
 minLength = 7
 ```

</br>

 처음 막대기의 길이는 `4+3+2=9`unit입니다. 첫번째 절단은 `4`unit또는 `4+2=6`unit이 가능합니다. 둘 중 어떤 길이로 절단하든 남은 길이가 `5`또는 `6`으로 절단기가 잡을 수 있는 최소 길이인 `minLength=7`길이보다 짧습니다. n-1인 2회의 절단이 이루어질 수 없으므로 Return 값은 "Impossible"입니다.

</br>

### 함수 설명
 Complete the function `cutThemAll` in the editor below.

 </br>

**Parameter**
- list `legnths`: array of int(the lengths of the segments, in order)
- int `minLength`: the minimum length the machine can accept

**Returns**:
- string: 절단 횟수인 n을 기준으로 n-1회의 절단이 모두 가능하면 "Possible"을, 아니면 "Impossible"을 반환하세요.

</br>

### 제한사항
- lengths의 길이는 2이상 100000이하입니다.
- t의 길이는 1이상 1000000000이하입니다 (t가 뭐임..?)
- 절단 길이인 lengths[i]의 길이는 1이상 1000000000이하입니다.
- lengths의 모든 요소의 합은 잘리지않은 막대기의 길이와 같습니다.

</br>

### 입출력 예

|n|minLength|result|
|:---:|:---:|:---:|
|[3,5,4,3]|9|"Possible"|
|[5,6,2]|12|"Impossible"|
|[4,3,2]|3|"Possible"|
|[4,2,3]|3|"Impossible"|

</br>

## Question 2. SQL Problems
 
 다음 문제에 알맞는 쿼리를 작성하세요.

</br>

### Table 1. Meber Table

</br>

|Field|Type|Null|Key|Default|Extra|
|:---:|:---:|:---:|:---:|:---:|:---:|
|id|int|No|Primary|Null|Auto increment|
|name|varchar(32)|No||Null||

</br>

### Table 1. Meber Table

</br>

|Field|Type|Null|Key|Default|Extra|
|:---:|:---:|:---:|:---:|:---:|:---:|
|order_id|int|No|Primary|Null|Auto increment|
|status|varchar(32)|No||Null||
|create_at|date|No||Null||
|member_id|int|No||Null||

</br>

 order_status 필드는 다음 여섯 개의 값으로 구성되어 있습니다.
 - "Completed", "Failure", "In Processing", "Canceled", "Refunded", "Pending"
 - 각 값은 주문이 완료되었는지, 주문이 실패했는지, 주문이 진행중인지, 주문이 취소되었는지, 환불이 완료되었는지, 또는 주문이 보류 중인지를 나타냅니다.

### 문제
 지난 달 동안 하루에 다섯 번 이상 주문을 완료한 고객의 리스트를 출력하는 쿼리를 짜세요.
