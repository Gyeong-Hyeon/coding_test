## Question 1. Cut them all
 
 막대기를 부분으로 자르는 자동 절단기가 있습니다. 이 절단기는 minLength길이 이상의 막대기만 잡을 수 있습니다. 

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
