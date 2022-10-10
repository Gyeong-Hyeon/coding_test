def checkInclusion(s1: str, s2: str) -> bool:
        for i in range(len(s2)-len(s1)):
            if s2[i] in s1:
                st=s1
                cnt=0
                for j in range(len(s1)):                    
                    if s2[i+j] not in st:
                        break
                    st=st.replace(s2[i+j],"",1)
                    cnt+=1
                if cnt == len(s1):
                    return True
        return False